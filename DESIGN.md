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

### Sidebar (Left Panel)
Two-level: subject header buttons → chapter list (collapsed/expanded). Subject headers have an orange dot indicator on active/hover. Chapters: muted, `--panel-2` bg, small font. Both levels use `--r-md` radius.

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

### Profile Avatar
Fixed top-right. 46px circle, orange bg, white initial, `--accent-light` ring. Shows level % badge to its left.

## Layout
Two-column grid: `270px` left sidebar + `1fr` right workbench. Both panels fill `calc(100vh - 5.5rem)` and scroll independently (`overflow-y: auto; overscroll-behavior: contain`). Page itself never scrolls (`body: overflow: hidden`).
