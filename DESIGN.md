# bare bones — Design System

## Color Tokens
All defined as CSS custom properties on `:root`.

### Surfaces
| Token | Value | Use |
|---|---|---|
| `--bg` | `#EDEBE6` | Page background (warm greige) |
| `--panel` | `#FFFFFF` | Cards, workbench, left sidebar |
| `--panel-2` | `#F5F3EE` | Inset areas, code bg, tab bar |
| `--panel-3` | `#ECEAE5` | Deeper insets, mark-wrong bg |

### Ink
| Token | Value | Use |
|---|---|---|
| `--ink` | `#1A1916` | Primary text |
| `--ink-2` | `#38362F` | Secondary text, body copy |
| `--muted` | `#7A7870` | Captions, metadata, placeholders |
| `--line` | `#DEDAD2` | Borders, dividers |

### Orange Accent Scale
| Token | Value | Use |
|---|---|---|
| `--accent` | `#F97316` | Buttons, active states, avatar, progress fills |
| `--accent-2` | `#FB923C` | Gradient start in progress bars |
| `--accent-3` | `#FCA55D` | Lighter gradient accents |
| `--accent-light` | `#FED7AA` | Hover borders, chip borders |
| `--accent-xlight` | `#FFF1E0` | Hover backgrounds, tag backgrounds |
| `--accent-xxlight` | `#FFFAF4` | Very subtle tints, note blocks |
| `--accent-strong` | `#C2410C` | Text on light accent bg, headings in notes |
| `--accent-dark` | `#7C2D12` | High-contrast accent text |

### Semantic
| Token | Value | Use |
|---|---|---|
| `--success` | `#16A34A` | Correct answers |
| `--danger` | `#DC2626` | Errors |

## Typography
**Font:** Outfit (Google Fonts), weights 300–800. Loaded via CDN.

| Role | Size | Weight | Notes |
|---|---|---|---|
| Body | 15px | 400 | Base |
| Headings (h2–h4) | — | — | `letter-spacing: -0.025em; line-height: 1.25` |
| Small/muted | 0.875rem | 400 | `.small` utility |
| Buttons | 0.9rem | 600 | All buttons |
| Tab pills | 0.85rem | 600 | |
| Sidebar chapters | 0.83rem | 500 | `.graph-chapter` |
| Exam source tags | 0.78rem | 700 | Uppercase feel |
| Progress labels | 0.66rem | 600 | Column chart labels |
| ASCII logo | Courier New | — | Brand mark only, scaled 24% |

**KaTeX** loaded via CDN for maths rendering.

## Spacing & Radius
```
--r-xs:   8px
--r-sm:   12px
--r-md:   18px
--r-lg:   24px
--r-xl:   32px    ← main cards, workbench, sidebar
--r-full: 999px   ← pill buttons, chips, progress bars
```

## Shadows
```
--s0: 0 1px 3px rgba(0,0,0,0.04)    subtle
--s1: 0 2px 10px rgba(0,0,0,0.06)   cards
--s2: 0 6px 24px rgba(0,0,0,0.09)   hover elevation
--s3: 0 24px 72px rgba(0,0,0,0.15)  modals/overlays
--so: 0 4px 22px rgba(249,115,22,0.32)  orange glow (primary buttons)
```

## Motion
```
--t:    180ms
--ease: cubic-bezier(0.22, 1, 0.36, 1)   (spring-like, fast settle)
```
All interactive transitions use `var(--t) var(--ease)`. Modal entrance: `0.24s`. Login overlay: `2.5s` total with scan animation.

## Key Components

### Cards
`.card` — `background: --panel; border: 1.5px solid --line; border-radius: --r-xl; padding: 1.25rem; box-shadow: --s1`

### Buttons
- **Primary** `.button-primary` — orange bg, white text, `--so` shadow. Hover: darken to `--accent-strong`, lift `-1px`.
- **Secondary** `.button-secondary` — white bg, `--ink-2` text, `--line` border. Hover: `--accent-xlight` bg, `--accent-strong` text.
- All buttons: `border-radius: --r-sm; padding: 0.6rem 1rem; font-weight: 600`

### Tab Pills
`.tabs` — flex row, `background: --panel-2`, `border-radius: --r-full`, `border: 1.5px solid --line`, `padding: 0.28rem`.
Active tab: orange bg, white text, `--so` shadow.

### Subject header (`layout.css`)
On `/app/<subject>/` pages: a back link ("‹ Your subjects" on the subject's home, "‹ Biology" inside a section), the subject name ("Leaving Cert" is in the heading but visually hidden) (`clamp(2rem, 4.2vw, 3rem)`/800), and inside a section its name in `--accent-strong`. No tab row: the home view's section tiles (icon + name, min-height 10rem) are the only navigation, with this subject's Study time card beneath them. Sections: Paper guide, AAC guide (only where `aac-guides.js` has one), Flashcards, Notes, Tests, Exam; Maths has Paper guide and Exam. Exam has its own pill switch: By chapter / By type / Full papers. By type only offers a type with at least 4 questions (`MIN_TYPE_QUESTIONS`).

Paper guide and AAC guide sit on one plain `--panel` card that scrolls when it is taller than the screen. Above 860px their sections are a sideways accordion (the open one widest). At 860px and below they are a sideways row of cards, all open, `min(85%, 24rem)` wide, that snap as you swipe; the marks bar above stays, tapping a segment slides to that section and swiping moves its highlight.

Tile icons are inline line SVGs (`ICONS` in `dashboard.js`, 24×24, 1.8 stroke, `currentColor`) in a `--accent-xlight` square with `--accent-strong` ink.

### Account Menu
Two panes inside the avatar dropdown. Main pane: username as the headline (1.3rem/800), email beneath, then settings-style rows. "Subject choices" opens the second pane, where subjects are toggle switches rather than checkboxes; at least one must stay on. No sign-in or add-account control lives here.

### Flashcard Study Box
`.flashcard-study` — `--r-lg` card, min-height 160px, grid layout. Contains: chapter title, progress bar, study face (term/definition), 4-button control row (Prev/Flip/Next/Mark Learned), keyword chip row.

### Progress Bars
Two variants:
- **Horizontal** `.progress-bar` — 8px height, `--accent-xlight` track, orange gradient fill.
- **Vertical column chart** `.progress-chart` — columns with `--accent-xlight` track, orange fill from bottom.
- **Overview bars** `.overview-total-bar` (20px, subject level) and `.overview-progress-bar` (36px, chapter rows).

### Keyword Chips
`.keyword-chip` — small pill, `--accent-xxlight` bg, `--accent-light` border. States: `.hit` (solid orange), `.miss` (grey).

### Exam Groups
`.exam-group` — bordered card with `--r-lg`. Header strip: `--accent-xxlight` bg. Source tag: small, bold, `--accent-strong`. Case study variant has orange border.

### Modals / Overlays
Full-screen backdrop: `rgba(26,25,22,0.6)` + `backdrop-filter: blur(6px)`. Card: `--r-xl`, `--s3`. Entrance animation: scale+translate in 0.24s.

Full Notes is edge-to-edge (no backdrop), `background: --bg`.

In a chapter with subsections, Full Notes pages through them: round arrows sit at mid-height either side of the reading column (beside the title on phones), the arrow keys and a sideways swipe do the same, and each page ends on a "Next subsection" link. Paging leaves the subsection being studied unchanged. The subsection grid has its own Full notes pill, which opens on the first subsection.

### Progress Page
Not an overlay: `.progress-screen` is a fixed, full-viewport page on `--bg`. Title is orange, `clamp(2.4rem, 5vw, 3.6rem)`, weight 800. Body is a `min(1180px, 100%)` column: a summary band, then one row per subject carrying the percentage, an overall bar and a strip of per-chapter columns, with a "Chapter detail" link into a named-chapter list.

### Profile Avatar
Fixed top-right. 46px circle, orange bg, white initial, `--accent-light` ring. Shows level % badge to its left.

## Layout
`app.html` is the dashboard; `/app/<subject>/index.html` are generated from it by `scripts/build_subject_pages.ts` (re-run after editing `app.html`). Both are one centred column, `min(1180px, 100%)`: the subject header (or dashboard heading), then the open section, which scrolls on its own (`overflow-y: auto; overscroll-behavior: contain`). The page itself never scrolls. Section content sits in one `.section-card` (`--panel`, `--r-xl`, `--s1`); lists inside are rows divided by 1px `--line`, never nested cards.

The dashboard is "Your subjects" as a grid of tiles (one per subject: name, % learned, time studied in the chosen range, a 6px progress bar; the whole tile links to the subject page), then "Study time" underneath: four stats and a daily bar chart that always opens on 7 days (30 days / 3 months on request). Bars are orange-600 `#EA580C` (the brand orange is under 3:1 on white), 70% of their column up to 6rem, 6px rounded tops; each full-height column is the hover target for its tooltip. Subject tiles carry the subject's icon.

### Phone (≤640px)
Lives in `responsive.css`, loaded after `styles.css`, and follows the landing-page phone mockups (`index.html` screen templates).
- **One screen at a time.** `app.js` sets `data-screen` on `#subjectArea` (`home` on the dashboard; otherwise from `viewMode`). Inside a subject section:
  1. `subject`: the section's chapter list (or its whole content: Notes, Tests, Exam by type / papers).
  2. `chapter`: a chapter's subsection grid (Flashcards) or its exam questions.
  3. `study` (chapters with subsections only): "‹ Biology · 13. Enzymes" back to the grid, then the flashcards.

  While on `chapter`/`study` the subject header shrinks to the name and tabs. Each step down (and Progress / Full notes / a paper) is a `history.pushState` entry, so back steps up a level; section tabs are hash links, so back also returns to the previous section. A running test ignores back.
- **Top bar** (`--phone-bar`, 3.6rem): 22px wordmark left; timer and 38px avatar right. The level % rides on the avatar as a small badge. The timer's menu drops downward, and the timer hides on Progress and Full notes, whose Close button sits in the same corner.
- **Study header:** chapter title (two-line clamp) with a Full notes pill beside it, then a segmented Learn/Test/Exam switch: grey track, white active segment.
- **Learn card:** dark (`--ink`) and fills the remaining height. An orange "Flashcard"/"Answer" label sits above the face, and tapping the face flips it. Controls are pinned to the bottom, with key words above them.
- **Heights** use `100dvh` so Safari's toolbars don't hide the card. Text fields are 16px so iOS doesn't zoom on focus.
