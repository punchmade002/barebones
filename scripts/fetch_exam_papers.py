#!/usr/bin/env python3
"""Download every Leaving Cert exam paper and marking scheme the SEC archive lists for a subject.

The pipeline's downloader only fetches what the question pipeline needs, and it has gaps (a
missing year, a booklet it couldn't name, a subject listed under a new name). This script asks
the archive itself: for each year it walks the archive's form and saves every English-version
row it lists, then records what it found in a manifest that build_exam_papers.py reads. The
PDFs are never opened.

    python3 scripts/fetch_exam_papers.py maths
    python3 scripts/fetch_exam_papers.py all

Re-running is safe: files already downloaded are kept, and only missing ones are fetched. The
archive often doesn't answer; the manifest lists the years it couldn't read, and
    python3 scripts/fetch_exam_papers.py --gaps all
looks at just those again.
Needs Playwright with Chromium (examinations.ie blocks plain HTTP clients):
    pip install playwright && playwright install chromium
"""

from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_exam_papers import SUBJECTS, DOWNLOADS, variant_for  # noqa: E402

ARCHIVE_URL = "https://www.examinations.ie/exammaterialarchive/"
SEL = "#MaterialArchive__noTable__sbv__{}"
AGREE = "#MaterialArchive__noTable__cbv__AgreeCheck"
VIEWS = {"exampapers": "papers", "markingschemes": "scheme"}
ROW = re.compile(r"(Higher|Ordinary|Foundation|Common)\s+Level", re.I)
VERSION = re.compile(r"\((EV|IV)\)")
DELAY_S = 1.0
LATEST_YEAR = time.localtime().tm_year


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def _select(page, field: str, **option) -> bool:
    loc = page.locator(SEL.format(field))
    if not loc.count():
        return False
    try:
        with page.expect_navigation(wait_until="domcontentloaded", timeout=20000):
            loc.select_option(**option)
    except Exception:
        page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(300)
    return True


def _options(page, field: str) -> list[str]:
    loc = page.locator(SEL.format(field))
    if not loc.count():
        return []
    return [o.strip() for o in loc.locator("option").all_inner_texts() if not o.startswith("[")]


def _start(page) -> None:
    page.goto(ARCHIVE_URL, wait_until="domcontentloaded")
    try:
        with page.expect_navigation(wait_until="domcontentloaded", timeout=20000):
            page.check(AGREE)
    except Exception:
        page.wait_for_load_state("domcontentloaded")


def _open_year(page, view: str, year: int) -> list[str] | None:
    """Walk the form to one year's Leaving Cert subject list. [] if the archive has no such
    year for this view, None if the page didn't load."""
    _start(page)
    if not _select(page, "ViewType", value=view):
        return None
    if str(year) not in _options(page, "YearSelect"):
        return []
    if not _select(page, "YearSelect", label=str(year)) or not _select(page, "ExaminationSelect", value="lc"):
        return None
    # The postbacks can land out of order; only trust a subject list for the year and exam asked for
    try:
        if (page.locator(SEL.format("ViewType")).input_value() != view
                or page.locator(SEL.format("YearSelect")).input_value() != str(year)
                or page.locator(SEL.format("ExaminationSelect")).input_value() != "lc"):
            return None
    except Exception:
        return None
    return _options(page, "SubjectSelect") or None


def _read_rows(page) -> list[dict] | None:
    try:
        page.wait_for_function(
            "() => [...document.querySelectorAll('tr')].some(r => /Level/.test(r.innerText))", timeout=10000)
    except Exception:
        return None
    rows = []
    for a in page.locator("a", has_text="Click Here").all():
        text = re.sub(r"\s+", " ", a.evaluate("e => e.closest('tr')?.cells[0]?.innerText || ''")).strip()
        level, version = ROW.search(text), VERSION.search(text)
        if not level or not version or version[1] != "EV":
            continue
        # "Section A&B / Higher Level (EV)" -> part "Section A&B"
        part = VERSION.sub("", ROW.sub("", text)).replace("/", " ").strip(" -–:")
        part = re.sub(r"\s+", " ", part)
        rows.append({"level": level[1].lower(), "part": part, "href": a.get_attribute("href")})
    return rows


def _year(page, view: str, year: int, names: re.Pattern) -> dict[str, list[dict]] | None:
    """Every English-version row the archive lists for the subject in one year, per subject name
    (History has two in some years). {} when the subject wasn't examined that year."""
    found: dict[str, list[dict]] = {}
    opts = _open_year(page, view, year)
    if opts is None:
        return None
    if not opts:
        return {}  # the archive has no such year for this view (schemes start in 2001)
    listings = [o for o in opts if names.search(o)]
    if not listings:
        return None  # every subject here is set every year, so this is a bad load, not an absence
    for i, listing in enumerate(listings):
        if i and _open_year(page, view, year) is None:  # the results page hides the form
            return None
        if not _select(page, "SubjectSelect", label=listing):
            return None
        rows = _read_rows(page)
        if rows is None:
            return None
        found[listing] = rows
    return found


# Most rows are PDFs; Geography's map, photograph and source paper also come as JPEG or TIFF
TYPES = {"application/pdf": ".pdf", "image/jpeg": ".jpg", "image/tiff": ".tif", "image/png": ".png"}


def _download(page, url: str) -> tuple[bytes, str] | None:
    resp = page.request.get(url, timeout=300000)
    ext = TYPES.get(resp.headers.get("content-type", "").split(";")[0].strip())
    if resp.ok and ext:
        return resp.body(), ext
    return None


def _retry(fn, *args):
    """Run one archive lookup up to four times; the site is slow and the connection can drop."""
    for attempt in range(4):
        try:
            result = fn(*args)
        except Exception as error:  # timeouts, dropped connections
            print(f"  retrying after: {str(error).splitlines()[0]}", flush=True)
            result = None
        if result is not None:
            return result
        print(f"  no answer from the archive, trying again ({attempt + 1}/4)", flush=True)
        time.sleep(5 * (attempt + 1))
    return None


def fetch(subject_id: str, retry_gaps: bool = False) -> None:
    """Fetch every year from the latest back to the subject's fromYear, or with retry_gaps only
    the years the last run couldn't read, keeping what it already found for the rest."""
    from playwright.sync_api import sync_playwright

    cfg = SUBJECTS[subject_id]
    names = re.compile(cfg["archiveName"])
    out = DOWNLOADS / subject_id
    out.mkdir(parents=True, exist_ok=True)
    manifest_path = out / "manifest.json"

    todo = [(view, kind, year) for view, kind in VIEWS.items()
            for year in range(LATEST_YEAR, cfg["fromYear"] - 1, -1)]
    entries, gaps = [], []
    if retry_gaps:
        old = json.loads(manifest_path.read_text())
        # The gaps the last run noted, plus any year it came back with nothing for
        have = {(e["year"], e["kind"]) for e in old["entries"]}
        retry = {(g["year"], g["kind"]) for g in old["gaps"]}
        retry |= {(t[2], t[1]) for t in todo if (t[2], t[1]) not in have}
        todo = [t for t in todo if (t[2], t[1]) in retry]
        entries = [e for e in old["entries"] if (e["year"], e["kind"]) not in retry]
    if not todo:
        print(f"{subject_id}: no gaps to retry")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_context().new_page()
        for view, kind, year in todo:
            print(f"{subject_id} {year} {kind}", flush=True)
            found = _retry(_year, page, view, year, names)
            if found is None:
                gaps.append({"year": year, "kind": kind, "reason": "the archive did not answer"})
                continue
            for listing, rows in found.items():
                variant = variant_for(cfg, listing)
                seen = set()
                for row in rows:
                    stem = "-".join(filter(None, [str(year), row["level"], kind, slug(variant), slug(row["part"])]))
                    if stem in seen:
                        continue  # the archive sometimes repeats a link
                    seen.add(stem)
                    have = [out / f"{stem}{ext}" for ext in TYPES.values() if (out / f"{stem}{ext}").exists()]
                    if have and have[0].stat().st_size:
                        dest = have[0]
                    else:
                        got = _retry(_download, page, urljoin(page.url, row["href"]))
                        if got is None:
                            gaps.append({"year": year, "kind": kind, "reason": f"{stem} did not download"})
                            continue
                        dest = out / f"{stem}{got[1]}"
                        dest.write_bytes(got[0])
                        page.wait_for_timeout(int(DELAY_S * 1000))
                    print(f"  {dest.name}", flush=True)
                    entries.append({"year": year, "level": row["level"], "kind": kind,
                                    "variant": variant, "part": row["part"],
                                    "listing": listing, "file": dest.name})
        browser.close()

    entries.sort(key=lambda e: (-e["year"], e["kind"] != "papers"))  # stable: keeps archive order
    manifest_path.write_text(json.dumps({"entries": entries, "gaps": gaps}, indent=2))
    print(f"{subject_id}: {len(entries)} files, {len(gaps)} gap(s)")
    for gap in gaps:
        print(f"  gap: {gap['year']} {gap['kind']}: {gap['reason']}")


def main() -> None:
    args = sys.argv[1:]
    retry_gaps = "--gaps" in args
    ids = [a for a in args if not a.startswith("--")]
    if ids == ["all"]:
        ids = list(SUBJECTS)
    if not ids or any(s not in SUBJECTS for s in ids):
        sys.exit(f"Usage: fetch_exam_papers.py [--gaps] <all|{'|'.join(SUBJECTS)}> [...]")
    for subject_id in ids:
        fetch(subject_id, retry_gaps)


if __name__ == "__main__":
    main()
