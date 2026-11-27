"""One-off: subsection catalogues and prereq batches for Chemistry and Home Ec (see CRUNCH_MODE.md)."""
import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from crunch_points import items

s = (ROOT / "subject-index.js").read_text()
TRACK = {"4": "Elective 1 (Home Design and Management)", "5": "Elective 2 (Textiles, Fashion and Design)", "6": "Elective 3 (Social Studies)"}
for subj, nb in (("chemistry", 2), ("home-economics", 4)):
    titles = dict(re.findall(r'\{"id":"([a-z]+\d*(?:-[a-z]+)*)","title":"([^"]*)","learningOutcomes"', s[s.index(f'"{subj}": {{"chapters"'):]))
    out, ids = [], []
    for sid in items(subj):
        d = json.loads((ROOT / "content" / subj / f"{sid}.json").read_text())
        ch = titles[d["chapterId"]]
        if subj == "home-economics":
            ch += " | " + TRACK.get(str(d.get("syllabusRef", "1"))[0], "Core")
        heads = "; ".join(b.get("h", "") for b in d["notes"] if b.get("h"))
        out.append(f"{sid} | {ch} | {d['subsection']}\n  covers: {heads}")
        ids.append(sid)
    here = ROOT / "drafts" / "crunch" / subj
    (here / "catalogue.txt").write_text("\n".join(out) + "\n")
    size = -(-len(ids) // nb)
    for b in range(nb):
        (here / f"batch-{b + 1}.txt").write_text("\n".join(ids[b * size:(b + 1) * size]) + "\n")
    print(subj, len(ids), "subsections,", nb, "batches,", len("\n".join(out)) // 1000, "KB catalogue")
