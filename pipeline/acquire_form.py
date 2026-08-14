"""Stage 1 — ACQUIRE via the SEC archive form.  (Playwright)

Verified against the live site on 2026-06-06 by driving it for History. You do NOT need
subject codes or filename patterns: the archive's cascading form produces a per-file
download link and this script harvests + downloads it through the browser session.

HOW THE REAL FORM WORKS (confirmed):
  1. Tick the terms checkbox  #MaterialArchive__noTable__cbv__AgreeCheck  -> page reloads.
  2. Four cascading <select>s, each id  #MaterialArchive__noTable__sbv__<Field>, where each
     change fires SubmitForm(...) -> a POST reload that reveals the next select:
        ViewType         values: exampapers | markingschemes | deferredexams | ...
        YearSelect       value : the year, e.g. "2023"
        ExaminationSelect values: lc (Leaving Cert) | jc (Junior) | lb (LCA)
        SubjectSelect    value : a numeric id; we match it by visible text ("History")
  3. A results table then lists, per row:
        "Higher Level (EV)" | "Higher Level (IV)" | "Ordinary Level (EV)" | "Ordinary Level (IV)"
     each with a "Click Here" link to  /exammaterialarchive/?fp=<~135-char token>.
  4. GET that link (same browser session) -> 200, application/pdf.  [verified: 2023 LC
     History HL EV = 972,945 bytes]

EV = English version, IV = Irish version. We take EV by default.

SETUP (your machine):
    pip install playwright --break-system-packages
    playwright install chromium
RUN:
    python acquire_form.py history                 # HL+OL papers + marking schemes, EV
    python acquire_form.py history --headful       # watch it drive the form
    python acquire_form.py history --include-irish # also grab IV versions
"""
from __future__ import annotations
import csv
import re
import sys
from pathlib import Path
from urllib.parse import urljoin

from config import RAW, REPORTS, SUBJECTS, REQUEST_DELAY_S, relevant_years, cutoff_for

ARCHIVE_URL = "https://www.examinations.ie/exammaterialarchive/"
SEL = "#MaterialArchive__noTable__sbv__{}"
AGREE = "#MaterialArchive__noTable__cbv__AgreeCheck"
VIEW_TYPES = {"exampapers": "papers", "markingschemes": "scheme"}   # -> short tag for filenames
ROW_RE = re.compile(r"(Higher|Ordinary)\s+Level\s+\((EV|IV)\)", re.I)
PAPER_RE = re.compile(r"Paper\s*(\d)", re.I)   # multi-paper subjects (Maths, English, Irish…)
SECTION_RE = re.compile(r"Section\s*(A|B\s*&\s*C)", re.I)  # split Home Economics papers
# Geography publishes "Part One and Answerbook" and "Part Two" as two separate rows for the SAME
# level. Neither matches PAPER_RE nor SECTION_RE, so both used to be tagged paper="" — which made
# them collide on one destination filename and let seen_destinations silently drop Part Two. That
# is 320 of the paper's 400 marks. Treat a Part label as a paper component like Paper 1/2.
PART_RE = re.compile(r"\bPart\s+(One|Two|Three|1|2|3)\b", re.I)
_PART_NUM = {"one": "1", "two": "2", "three": "3", "1": "1", "2": "2", "3": "3"}


def _select(page, field: str, *, value: str | None = None, label: str | None = None) -> bool:
    """Set a cascade <select> and wait for the postback that reveals the next one."""
    loc = page.locator(SEL.format(field))
    if not loc.count():
        return False
    try:
        with page.expect_navigation(wait_until="domcontentloaded", timeout=15000):
            loc.select_option(value=value, label=label)
    except Exception:
        page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(250)
    return True


def _subject_label(subject_key: str) -> str:
    return SUBJECTS.get(subject_key, {}).get("label", subject_key.capitalize())


def discover_and_download(subject: str, headful: bool, include_irish: bool,
                          only_years: set[int] | None = None, force: bool = False) -> list[dict]:
    from playwright.sync_api import sync_playwright

    label = _subject_label(subject)
    out_dir = RAW / subject
    out_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict] = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headful)
        page = browser.new_context().new_page()
        page.goto(ARCHIVE_URL, wait_until="domcontentloaded")

        # 1. accept terms (reloads the page, revealing the ViewType select)
        try:
            with page.expect_navigation(wait_until="domcontentloaded", timeout=15000):
                page.check(AGREE)
        except Exception:
            page.wait_for_load_state("domcontentloaded")

        years = relevant_years(subject)
        if only_years:
            years = [y for y in years if y["year"] in only_years]
        cutoff, verified = cutoff_for(subject)
        print(f"{label}: pulling {len(years)} year(s) back to syllabus cutoff {cutoff}"
              f"{'' if verified else ' (UNVERIFIED — set SYLLABUS_CUTOFF in config.py)'}\n")
        gaps = []
        for vt_value, vt_tag in VIEW_TYPES.items():
            for yinfo in years:
                year, status = yinfo["year"], yinfo["status"]
                outcome = None                       # 'done' | 'absent' | None(=retry)
                for attempt in range(3):             # the gov site is slow/flaky: retry the chain
                    # always start from a fresh form (the results page hides the selects)
                    page.goto(ARCHIVE_URL, wait_until="domcontentloaded")
                    try:
                        with page.expect_navigation(wait_until="domcontentloaded", timeout=15000):
                            page.check(AGREE)
                    except Exception:
                        page.wait_for_load_state("domcontentloaded")

                    if not _select(page, "ViewType", value=vt_value):       continue
                    yr_loc = page.locator(SEL.format("YearSelect"))
                    yr_opts = [o.strip() for o in yr_loc.locator("option").all_inner_texts()] if yr_loc.count() else []
                    if yr_opts and str(year) not in yr_opts:
                        outcome = "absent"; break    # year genuinely not in archive for this view
                    if not _select(page, "YearSelect", label=str(year)):    continue
                    if not _select(page, "ExaminationSelect", value="lc"):  continue
                    subj_loc = page.locator(SEL.format("SubjectSelect"))
                    opts = [o.strip() for o in subj_loc.locator("option").all_inner_texts()]
                    exact = next((o for o in opts if o.lower() == label.lower()), None)
                    if len(opts) > 1 and not exact:
                        outcome = "absent"; break    # subject genuinely not offered that year
                    if not exact or not _select(page, "SubjectSelect", label=exact):
                        continue
                    # wait for the results table to actually render (not just the footer link)
                    try:
                        page.wait_for_function(
                            "() => [...document.querySelectorAll('tr')].some(r => /(Higher|Ordinary) Level/.test(r.innerText))",
                            timeout=8000)
                    except Exception:
                        continue                     # didn't render — retry the chain

                    got_any = False
                    seen_destinations = set()
                    for a in page.locator("a", has_text="Click Here").all():
                        row_txt = a.evaluate("e => (e.closest('tr')?.cells[0]?.innerText)||''")
                        m = ROW_RE.search(row_txt or "")
                        if not m:
                            continue
                        # Home Economics exposes a separate "Practical Paper / Higher Level"
                        # scheme link. It is the coursework rubric, not answers for the written
                        # exam; sharing the same destination used to let it shadow the real link.
                        if vt_tag == "scheme" and re.search(r"\b(practical|coursework)\b", row_txt, re.I):
                            continue
                        level, version = m.group(1).lower(), m.group(2).upper()
                        if version == "IV" and not include_irish:
                            continue
                        pm = PAPER_RE.search(row_txt or "")   # "Paper 1"/"Paper 2" if present
                        sm = SECTION_RE.search(row_txt or "")
                        rm = PART_RE.search(row_txt or "")     # "Part One"/"Part Two" (Geography)
                        if pm:
                            paper = pm.group(1)
                        elif sm:
                            paper = "A" if sm.group(1).upper() == "A" else "BC"
                        elif rm:
                            paper = _PART_NUM[rm.group(1).lower()]
                        else:
                            paper = ""
                        href = a.get_attribute("href")
                        if not href:
                            continue
                        url = href if href.startswith("http") else urljoin(page.url, href)
                        ref = "-REF" if status == "reference" else ""
                        ptag = f"-P{paper}" if paper else ""
                        dest = out_dir / f"{year}-{level}{ptag}-{version}-{vt_tag}{ref}.pdf"
                        if dest in seen_destinations:
                            continue                    # archive sometimes repeats the same link
                        seen_destinations.add(dest)
                        if not force and dest.exists() and dest.stat().st_size > 0:
                            ok = True                # cached
                        else:
                            resp = page.request.get(url)
                            ok = resp.ok and "pdf" in resp.headers.get("content-type", "")
                            if ok:
                                dest.write_bytes(resp.body())
                                page.wait_for_timeout(int(REQUEST_DELAY_S * 1000))
                        print(f"[{'ok ' if ok else '-- '}] {dest.name}")
                        rows.append({"subject": subject, "year": year, "level": level,
                                     "paper": paper, "version": version, "kind": vt_tag,
                                     "status": status,
                                     "bytes": dest.stat().st_size if ok and dest.exists() else 0,
                                     "path": str(dest)})
                        got_any = got_any or ok
                    if got_any:
                        outcome = "done"; break
                if outcome is None:                  # exhausted retries without results
                    gaps.append(f"{year}-{vt_tag}")
                    print(f"[gap] {year} {vt_tag}: no results after 3 tries")
        if gaps:
            print(f"\n⚠ {len(gaps)} gap(s) — re-run to fill (idempotent): {', '.join(gaps)}")
        browser.close()
    return rows


def _merge_rows(existing: list[dict], fresh: list[dict]) -> list[dict]:
    """Deduplicate manifest rows and preserve prior successes during targeted gap retries."""
    by_key = {}
    for row in existing:
        key = tuple(str(row.get(k, "")) for k in
                    ("subject", "year", "level", "paper", "version", "kind", "status"))
        if key not in by_key or int(row.get("bytes", 0) or 0) >= int(by_key[key].get("bytes", 0) or 0):
            by_key[key] = row
    for row in fresh:
        key = tuple(str(row.get(k, "")) for k in
                    ("subject", "year", "level", "paper", "version", "kind", "status"))
        # A successful targeted/forced download is authoritative even when the correct file is
        # smaller than a wrong cached asset. Preserve an existing success only if this retry failed.
        if int(row.get("bytes", 0) or 0) > 0 or key not in by_key:
            by_key[key] = row
    rows = list(by_key.values())

    # The archive occasionally changes from a single-paper listing to separately named
    # components (for example Home Economics Section A and Section B&C).  A manifest from an
    # earlier run can therefore retain the old component-less alias alongside the new rows;
    # that alias points at Section A and would make the digest/segment stages process it twice.
    # Once two or more explicit components exist, the component-less paper is superseded.
    component_counts: dict[tuple[str, ...], set[str]] = {}
    for row in rows:
        if row.get("kind") != "papers" or not row.get("paper"):
            continue
        group = tuple(str(row.get(k, "")) for k in
                      ("subject", "year", "level", "version", "kind", "status"))
        component_counts.setdefault(group, set()).add(str(row["paper"]))
    rows = [row for row in rows if not (
        row.get("kind") == "papers" and not row.get("paper") and
        len(component_counts.get(tuple(str(row.get(k, "")) for k in
            ("subject", "year", "level", "version", "kind", "status")), set())) >= 2
    )]

    return sorted(rows, key=lambda r: (int(r["year"]), r["kind"], r["level"],
                                       r.get("paper", ""), r["version"]))


def run(subject: str, headful: bool, include_irish: bool,
        only_years: set[int] | None = None, force: bool = False) -> None:
    fresh = discover_and_download(subject, headful=headful, include_irish=include_irish,
                                  only_years=only_years, force=force)
    manifest = REPORTS / f"manifest-{subject}.csv"
    existing = []
    if manifest.exists():
        with manifest.open() as f:
            existing = list(csv.DictReader(f))
    rows = _merge_rows(existing, fresh)
    if rows:
        with manifest.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["subject", "year", "level", "paper", "version", "kind", "status", "bytes", "path"])
            w.writeheader(); w.writerows(rows)
    got = sum(1 for r in rows if int(r.get("bytes", 0) or 0) > 0)
    print(f"\n{got}/{len(rows)} PDFs in {RAW / subject}\nManifest: {manifest}")


if __name__ == "__main__":
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), "history")
    only_years = None
    if "--years" in args:
        only_years = {int(y) for y in args[args.index("--years") + 1].split(",") if y.strip()}
    run(subject, headful=("--headful" in args), include_irish=("--include-irish" in args),
        only_years=only_years, force=("--force" in args))
