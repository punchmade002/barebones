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


def discover_and_download(subject: str, headful: bool, include_irish: bool) -> list[dict]:
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

        years = relevant_years(subject)          # cutoff-aware: on-course + 1 reference year
        cutoff, verified = cutoff_for(subject)
        print(f"{label}: pulling {len(years)} year(s) back to syllabus cutoff {cutoff}"
              f"{'' if verified else ' (UNVERIFIED — set SYLLABUS_CUTOFF in config.py)'}\n")
        for vt_value, vt_tag in VIEW_TYPES.items():
            for yinfo in years:
                year, status = yinfo["year"], yinfo["status"]
                # navigate back to the archive form before each cascade (results page hides the selects)
                if not page.locator(SEL.format("ViewType")).count():
                    page.goto(ARCHIVE_URL, wait_until="domcontentloaded")
                    try:
                        with page.expect_navigation(wait_until="domcontentloaded", timeout=15000):
                            page.check(AGREE)
                    except Exception:
                        page.wait_for_load_state("domcontentloaded")
                # drive the full chain fresh each time (every select rebuilds the rest)
                if not _select(page, "ViewType", value=vt_value):       continue
                yr_loc = page.locator(SEL.format("YearSelect"))
                yr_opts = [o.inner_text() for o in yr_loc.locator("option").all()] if yr_loc.count() else []
                if str(year) not in yr_opts:
                    continue  # year not in archive for this view type
                if not _select(page, "YearSelect", label=str(year)):    continue
                if not _select(page, "ExaminationSelect", value="lc"):  continue
                # subject options share a prefix ("History" vs "History (Early Modern)") -> exact text
                subj_loc = page.locator(SEL.format("SubjectSelect"))
                opts = subj_loc.locator("option").all_inner_texts()
                exact = next((o for o in opts if o.strip().lower() == label.lower()), None)
                if not exact or not _select(page, "SubjectSelect", label=exact):
                    continue

                # harvest the results table: each row -> level + version + ?fp= link
                for a in page.locator("a", has_text="Click Here").all():
                    row_txt = a.evaluate("e => (e.closest('tr')?.cells[0]?.innerText)||''")
                    m = ROW_RE.search(row_txt or "")
                    if not m:
                        continue
                    level = m.group(1).lower()           # higher | ordinary
                    version = m.group(2).upper()         # EV | IV
                    if version == "IV" and not include_irish:
                        continue
                    href = a.get_attribute("href")
                    if not href:
                        continue
                    url = href if href.startswith("http") else urljoin(page.url, href)
                    ref = "-REF" if status == "reference" else ""
                    dest = out_dir / f"{year}-{level}-{version}-{vt_tag}{ref}.pdf"
                    if dest.exists() and dest.stat().st_size > 0:
                        ok = True                        # cached
                    else:
                        resp = page.request.get(url)     # reuse session cookies/token
                        ok = resp.ok and "pdf" in resp.headers.get("content-type", "")
                        if ok:
                            dest.write_bytes(resp.body())
                            page.wait_for_timeout(int(REQUEST_DELAY_S * 1000))
                    print(f"[{'ok ' if ok else '-- '}] {dest.name}")
                    rows.append({"subject": subject, "year": year, "level": level,
                                 "version": version, "kind": vt_tag, "status": status,
                                 "bytes": dest.stat().st_size if ok and dest.exists() else 0,
                                 "path": str(dest)})
        browser.close()
    return rows


def run(subject: str, headful: bool, include_irish: bool) -> None:
    rows = discover_and_download(subject, headful=headful, include_irish=include_irish)
    manifest = REPORTS / f"manifest-{subject}.csv"
    if rows:
        with manifest.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["subject", "year", "level", "version", "kind", "status", "bytes", "path"])
            w.writeheader(); w.writerows(rows)
    got = sum(1 for r in rows if r["bytes"] > 0)
    print(f"\n{got}/{len(rows)} PDFs in {RAW / subject}\nManifest: {manifest}")


if __name__ == "__main__":
    args = sys.argv[1:]
    subject = next((a for a in args if not a.startswith("-")), "history")
    run(subject, headful=("--headful" in args), include_irish=("--include-irish" in args))
