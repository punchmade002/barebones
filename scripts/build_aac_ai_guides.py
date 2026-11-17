"""Build one AI review guide PDF per AAC subject from aac-guides.js.

The PDF is a prompt: a student attaches it with their draft to a chatbot, which then
reviews every paragraph (left untouched, with an example rewording and the reason
underneath) and, where the SEC publishes section marks, marks the draft before and after.

Run: python3 scripts/build_aac_ai_guides.py   (needs Google Chrome for HTML -> PDF)
"""
import html
import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "aac-ai-guides"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
COLORS = ["#3B82F6", "#14B8A6", "#F59E0B", "#F97316", "#EF4444", "#0EA5E9", "#64748B"]  # = AAC_STAGE_COLORS

# What the guide data can't say: what to ask for first, what can't be reviewed as text,
# and whether the SEC mark breakdown is solid enough to give a number.
SUBJECTS = {
    "biology": {
        "ask": ["their level (Higher or Ordinary)"],
        "marking": "Mark each of the four criteria out of 50 (200 in total).",
        "notes": [
            "Tables and graphs: do not reproduce them. Check each has a title, labelled axes or columns with units, and is referred to in the text.",
            "Criterion D covers the whole report, so judge it last, after reading everything.",
        ],
    },
    "chemistry": {
        "ask": ["their level (Higher or Ordinary)"],
        "marking": "Mark each of the four criteria out of 50 (200 in total).",
        "notes": [
            "Tables and graphs: do not reproduce them. Check each has a title, labelled axes or columns with units, and is referred to in the text.",
            "Criterion D covers the whole report, so judge it last, after reading everything.",
        ],
    },
    "business": {
        "ask": ["their level (Higher or Ordinary)"],
        "marking": "Mark out of 200: Introduction 20, Investigation and Analysis 100, Conclusions 30, Overall coherence 50.",
        "notes": [
            "Check each section against its suggested word count and the 1,500-word total. References, data tables, graphs, diagrams, images and labels do not count.",
            "Overall coherence is judged across the whole report, so mark it last.",
        ],
    },
    "geography": {
        "ask": ["their level (Higher or Ordinary)"],
        "marking": "Mark out of 100 by stage: 5, 5, 40, 30 and 20.",
        "notes": [
            "Each stage has a hard word cap (50, 100, 450 and 400 words). A rewording must never take a stage over its cap; if the student is over, the rewording must be shorter.",
            "Illustrations are hand-drawn images. Do not judge the drawing; check only that each has a title and caption and that the text refers to it.",
            "The splits inside Stages 3 and 4 (two methods plus coherence; results, conclusions, evaluation plus coherence) come from a teacher source. Use them to reason, but report marks per stage.",
        ],
    },
    "history": {
        "ask": ["their level (Higher or Ordinary), because the extended essay length differs (Higher 1,200 to 1,500 words, Ordinary 600 to 800)"],
        "marking": "Mark out of 100: outline plan 15, evaluation of sources 25, extended essay 50, review of the research process 10.",
        "notes": [
            "Check that every source evaluated is actually used in the extended essay, and that the essay answers the title set in the outline plan.",
        ],
    },
    "home-economics": {
        "ask": [
            "which piece of work this is: one Food Studies assignment (Areas A, A, B, D or E) or the Elective 2 Textiles folder",
            "their level (Higher or Ordinary)",
        ],
        "marking": (
            "Food Studies: mark one assignment out of 80 (Investigation 32, Planning and preparation 8, Implementation 28, Evaluation 12). "
            "Implementation is partly judged on a practical the teacher supervised, so mark only the written account and say so. "
            "Textiles: mark the folder only, out of 25 (design brief, analysis and research 15, implementation 4, evaluation 6). Never estimate the garment's 75 marks."
        ),
        "notes": [
            "Each Food Studies assignment is a separate piece of work. Review only the one the student names.",
            "The Food Studies hand-in date for 2027 (2 November 2026) has passed. If the student is still working on it, note this once and continue.",
        ],
    },
    "pe": {
        "ask": ["which part they are sharing: Physical Activity Project Section A, B or C, or the spoken introduction to their Performance Assessment video"],
        "marking": None,
        "no_marks_reason": "The SEC has not published section marks for the Physical Activity Project, and the only split available comes from a single teacher presentation, so a number would be guesswork.",
        "notes": [
            "The Performance Assessment is a video and cannot be reviewed. If the student pastes the script of their spoken introduction, review that against the video guidance; otherwise skip it.",
            "Use the top-band descriptors in the reference to say what each section would need to reach the top band.",
        ],
    },
}


def esc(s):
    return html.escape(str(s), quote=False)


def split_name(name):
    kicker, _, title = name.partition(" – ")
    return (kicker, title) if title else ("", name)


def full_title(g):
    t, subj = g["title"], g["subjectTitle"]
    return t if t.startswith(subj) else f"{subj} {t}"


def instructions(g, cfg):
    subj = g["subjectTitle"]
    ask = "".join(f"<li>{esc(a)}</li>" for a in ["their draft, as text or an attached file", *cfg["ask"]])
    notes = "".join(f"<li>{esc(n)}</li>" for n in cfg["notes"])
    if cfg["marking"]:
        marks = f"""
<h3>Step 5. Mark the draft before and after</h3>
<p>{esc(cfg["marking"])}</p>
<p>Give a table with one row per section and these columns: Section, Out of, Mark now, Mark with the rewordings, What the difference is for. Add a total row.</p>
<ul>
<li>Mark as a strict SEC examiner would, using only the marking reference below and the text supplied. Use whole numbers.</li>
<li>"Mark now" is for the draft exactly as written. "Mark with the rewordings" assumes the student rewrites each flagged paragraph to the standard of your example, in their own words.</li>
<li>Gaps marked [ADD …] are not counted in the second column, because they need the student's real data. List the marks they could add underneath the table.</li>
<li>Finish the table with this sentence: "This is an estimate from the published marking criteria. Your teacher's feedback and the SEC examiner's mark are what count."</li>
</ul>"""
    else:
        marks = f"""
<h3>Step 5. No mark</h3>
<p>Do not give a mark, grade or percentage for this component. {esc(cfg["no_marks_reason"])} Tell the student this in one sentence.</p>"""
    return f"""
<section class="ai">
<p class="eyebrow">Instructions for the AI</p>
<h2>You are reviewing a Leaving Certificate {esc(full_title(g))} for 2027</h2>
<p>Act as an experienced Leaving Certificate {esc(subj)} teacher who has examined this component for the SEC. Judge the work only against the marking reference in this document. Where this document and your own knowledge disagree, follow this document.</p>

<h3>Step 0. Get what you need</h3>
<p>Before reviewing, make sure the student has given you:</p>
<ul>{ask}</ul>
<p>If anything is missing, ask for it in one short message and wait.</p>

<h3>Step 1. Map the draft</h3>
<p>Work out which section of the marking reference each paragraph belongs to. Say in one line which sections are present and which are missing.</p>

<h3>Step 2. Review every paragraph</h3>
<p>Go through the draft in order. For each paragraph, output exactly this:</p>
<div class="format">
<p><b>Paragraph [number] · [section name]</b></p>
<p>&gt; [the student's paragraph, copied exactly]</p>
<p><b>Example rewording:</b> [how you would phrase it]</p>
<p><b>Why:</b> [one to three sentences naming the criterion, rule or checklist step it serves, and what it gains]</p>
</div>
<ul>
<li>Copy the student's paragraph character for character. Never correct, shorten, merge, reorder or skip it, even to fix spelling.</li>
<li>If a paragraph already meets the top standard, write "No change needed" and why, instead of a rewording. Do not change wording for the sake of it.</li>
<li>Keep the student's own facts, data, results, sources and opinions. Never invent data, measurements, results, quotations or sources.</li>
<li>Where something the marks need is missing, put a placeholder in the rewording, such as [ADD: the number of sites you sampled], and do not fill it in.</li>
<li>Keep the student's voice and level: plain, clear English a sixth-year student could write, with Irish spelling. For Ordinary level, keep sentences simpler.</li>
<li>Respect every word limit in the reference. A rewording should be no longer than the original unless it adds required content.</li>
<li>Treat headings as section markers, not paragraphs. Do not reproduce tables, graphs or images; comment on them in one line where the reference says how they are marked.</li>
</ul>

<h3>Step 3. Rule breaks</h3>
<p>Check the draft against "Rules you can't break" and the formatting and submission points in the reference. List each problem with where it is. Give the word count of each section against its limit.</p>

<h3>Step 4. Missing for full marks</h3>
<p>Go through the full-marks checklist for each section. List every step the draft does not show yet, and what would show it.</p>
{marks}

<h3>Step 6. Finish</h3>
<ul>
<li>Give the three changes that would gain the most marks, most valuable first.</li>
<li>Remind the student that the rewordings are examples to learn from. The SEC does not allow AI to write coursework content, so they must write the final version themselves.</li>
<li>Give them a filled-in acknowledgement entry for this review to add to their references, with: your tool name and version, the developer, today's date, "Feedback on the wording and structure of my draft against the published marking criteria; I wrote the final text myself", and the prompt they sent.</li>
</ul>

<h3>Notes for this subject</h3>
<ul>{notes}</ul>
</section>"""


def reference(g):
    b = g["brief"]
    lst = f"<ul>{''.join(f'<li>{esc(x)}</li>' for x in b.get('list', []))}</ul>" if b.get("list") else ""
    facts = "".join(f"<tr><th>{esc(k)}</th><td>{esc(v)}</td></tr>" for k, v in b["facts"])
    stages = []
    for i, s in enumerate(g["stages"]):
        kicker, title = split_name(s["name"])
        meta = " · ".join(x for x in [f"{s['marks']} marks" if s.get("marks") else "", s.get("marksNote") or ""] if x)
        checks = "".join(f"<li>{esc(c)}</li>" for c in s["checklist"])
        depth = "".join(
            f"<h4>{esc(sec['h'])}</h4><ul>{''.join(f'<li>{esc(p)}</li>' for p in sec['points'])}</ul>" for sec in s["guide"]
        )
        stages.append(f"""
<section class="stage" style="--sec:{COLORS[i % len(COLORS)]}">
<div class="stage-head"><p class="kicker">{esc(kicker or f"Part {i + 1}")}</p><h3>{esc(title)}</h3><p class="meta">{esc(meta)}</p></div>
<p class="label">Full-marks checklist</p><ul class="checks">{checks}</ul>
<p class="label">Full guide</p>{depth}
</section>""")
    sources = "".join(f"<li>{esc(s['label'])}: {esc(s['url'])}</li>" for s in g["sources"])
    return f"""
<section class="ref">
<p class="eyebrow">Marking reference</p>
<h2>The 2027 brief</h2>
<p>{esc(b["task"])}</p>{lst}
<table>{facts}</table>
<p class="small">Source: {esc(b["source"]["label"])}, {esc(b["source"]["url"])}</p>
<h2>Sections, marks and what earns them</h2>
<p>{esc(g["summary"])}</p>
{''.join(stages)}
<h2>Sources this guide is pooled from</h2>
<ul class="small">{sources}</ul>
</section>"""


def page(g, cfg):
    scored = "mark it before and after" if cfg["marking"] else "show what each section needs"
    return f"""<!doctype html><html lang="en-IE"><head><meta charset="utf-8">
<title>{esc(g["subjectTitle"])} AAC: AI review guide</title>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
@page {{ size: A4; margin: 16mm 17mm 18mm; }}
:root {{ --ink:#1A1916; --ink2:#5b584f; --line:#dedad2; --accent:#fa4c06; --accent-strong:#c23504; --tint:#fff8f4; }}
* {{ box-sizing: border-box; }}
body {{ font: 10pt/1.5 'Outfit', system-ui, sans-serif; color: var(--ink); margin: 0; }}
h1 {{ font-size: 25pt; line-height: 1.1; margin: 4pt 0 6pt; letter-spacing: -.01em; }}
h2 {{ font-size: 14pt; margin: 18pt 0 6pt; }}
h2, h3, h4 {{ break-after: avoid; }}
h3 {{ font-size: 11pt; margin: 12pt 0 3pt; }}
h4 {{ font-size: 10pt; margin: 8pt 0 2pt; }}
p {{ margin: 0 0 5pt; }}
ul {{ margin: 0 0 6pt; padding-left: 15pt; }}
li {{ margin-bottom: 2pt; }}
.eyebrow, .kicker, .label {{ font: 700 8pt 'Courier New', Courier, monospace; letter-spacing: .08em; text-transform: uppercase; color: var(--accent-strong); margin: 0 0 2pt; }}
.cover {{ border-left: 5pt solid var(--accent); padding: 2pt 0 2pt 14pt; margin-bottom: 14pt; }}
.lede {{ font-size: 11.5pt; color: var(--ink2); }}
.stats {{ display: flex; gap: 22pt; margin: 10pt 0 0; }}
.stats div {{ border-top: 1.5pt solid var(--ink); padding-top: 3pt; }}
.stats b {{ display: block; font-size: 13pt; }}
.stats span {{ font: 700 7.5pt 'Courier New', monospace; text-transform: uppercase; letter-spacing: .08em; color: var(--ink2); }}
.box {{ border: 1pt solid var(--line); border-radius: 6pt; padding: 9pt 12pt; margin: 8pt 0; break-inside: avoid; }}
.box.warn {{ background: var(--tint); border-color: #fcb48a; }}
.steps {{ counter-reset: none; padding-left: 16pt; }}
.ai {{ break-before: page; }}
.ai h2 {{ margin-top: 2pt; }}
.format {{ border-left: 3pt solid var(--accent); background: #f6f5f2; padding: 7pt 11pt; margin: 4pt 0 8pt; }}
.format p {{ margin: 0 0 2pt; }}
.ref {{ break-before: page; }}
.ref h2:first-of-type {{ margin-top: 2pt; }}
table {{ border-collapse: collapse; width: 100%; margin: 6pt 0; }}
th, td {{ text-align: left; vertical-align: top; border-top: 1pt solid var(--line); padding: 4pt 6pt 4pt 0; }}
th {{ width: 28%; font-weight: 600; }}
.stage {{ border-top: 3pt solid var(--sec); margin-top: 14pt; padding-top: 6pt; }}
.stage-head {{ break-after: avoid; }}
.stage .kicker {{ color: var(--sec); filter: brightness(.75); }}
.stage h3 {{ margin: 0 0 1pt; font-size: 12.5pt; }}
.meta {{ color: var(--ink2); font-weight: 500; }}
.stage .label {{ margin-top: 8pt; color: var(--ink2); }}
.checks {{ list-style: none; padding-left: 0; }}
.checks li {{ padding-left: 16pt; position: relative; }}
.checks li::before {{ content: ''; position: absolute; left: 0; top: 3pt; width: 8pt; height: 8pt; border: 1.2pt solid var(--sec); border-radius: 2pt; }}
.small {{ font-size: 8.5pt; color: var(--ink2); word-break: break-word; }}
</style></head><body>
<header class="cover">
<p class="eyebrow">Barebones · AAC AI review guide · 2027</p>
<h1>{esc(full_title(g))}</h1>
<p class="lede">Attach this PDF to an AI chatbot with your draft. It will go through your work paragraph by paragraph, leave your writing exactly as it is, show how each paragraph could be phrased for more marks and why, and {scored}.</p>
<div class="stats"><div><b>{esc(g["weight"])}</b><span>Of your grade</span></div><div><b>{esc(g["marks"] or "Descriptors")}</b><span>{"Marks" if g["marks"] else "Marked by"}</span></div><div><b>{esc(g["level"])}</b><span>Level</span></div></div>
</header>

<h2>How to use it</h2>
<ol class="steps">
<li>Open ChatGPT, Claude, Gemini or Copilot and start a new chat.</li>
<li>Attach this PDF and your draft, or paste your draft's text into the message.</li>
<li>Send: <b>Review my project using the attached guide.</b> Answer any question it asks first, such as your level.</li>
</ol>

<div class="box warn">
<p class="label">Keep it your own work</p>
<p>The SEC does not allow AI to write coursework content. Use the example rewordings to see what earns marks, then write your final version yourself. Never paste them into your project.</p>
<p>Any AI you use must be acknowledged in your references. The review ends with an entry you can add. Show your teacher how you used it, and anything not yours and not referenced is treated as plagiarism.</p>
</div>
<div class="box">
<p class="label">What it checks</p>
<p>Every paragraph against the 2027 brief and the SEC marking criteria, rule breaks such as word limits and formatting, steps missing for full marks, and the three changes worth the most marks.</p>
</div>
{instructions(g, cfg)}
{reference(g)}
</body></html>"""


def main():
    raw = (ROOT / "aac-guides.js").read_text()
    guides = json.loads(raw[raw.index("{"): raw.rindex("}") + 1])
    assert set(guides) == set(SUBJECTS), f"subjects differ: {set(guides) ^ set(SUBJECTS)}"
    OUT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for sid, g in guides.items():
            src = Path(tmp) / f"{sid}.html"
            src.write_text(page(g, SUBJECTS[sid]))
            pdf = OUT / f"{sid}.pdf"
            subprocess.run(
                [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=4000",
                 f"--print-to-pdf={pdf}", src.as_uri()],
                check=True, capture_output=True,
            )
            print(f"{pdf.relative_to(ROOT)}  {pdf.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
