# Handoff: barebones — Landing Page

## Overview
Marketing landing page for **barebones**, a web-app study assistant for Irish **Leaving Cert** students. The product promise is a two-step method: **(1) Learn the content** (AI flashcards & quizzes) → **(2) Practice exam questions** (exam-style questions, marked instantly). Tone is **bold & punchy**. The brand is a retro **dot-matrix / LED** look: orange pixels on warm grey.

The page is **web-app first** — primary CTAs are "Get started free" / "Sign in" (no app-store download).

## About the Design Files
The files in this bundle are **design references created in plain HTML/CSS/JS** — a working prototype that shows the intended look, layout, copy, and behavior. They are **not meant to be shipped as-is**. The task is to **recreate this design in your target codebase** (React, Vue, Next, Astro, SwiftUI, etc.) using its existing conventions, component primitives, and styling approach. If the project has no front-end yet, pick the most appropriate framework and implement it there.

Open `Landing.html` in a browser to see the live reference. The bundled React (`react@18.3.1`) + Babel is **only** used to render the in-page "Tweaks" dev panel — see "Tweaks panel" below. **Do not port the Tweaks panel**; it is an authoring tool, not a product feature. Pick ONE hero direction (see below) and build that.

## Fidelity
**High-fidelity (hifi).** Final colors, typography, spacing, copy, and interactions are intended to be matched closely. Recreate pixel-accurately using your codebase's libraries.

## Brand assets
- `assets/logo-wordmark.png` — the "barebones" dot-matrix wordmark, transparent PNG, orange pixels (1258×252, ~5:1 aspect). Used in nav (~52px tall), hero B, the sign-up section, and footer.
- `assets/logo-bb.png` — "BB" dot-matrix monogram, transparent PNG (680×538). Not currently placed on the page; included for favicon / app-icon / social use.
- The wordmark/monogram are the brand's hero asset. **Recreate them as `<img>`** — do not try to redraw the pixels in code. Ideally re-export as **SVG** for crispness at large sizes.

## Design Tokens
Defined as CSS custom properties in `styles.css` `:root`.

| Token | Value | Use |
|---|---|---|
| `--orange` | `#fa4c06` | Primary brand orange (logo color, buttons, accents) |
| `--orange-700` | `color-mix(in srgb, var(--orange) 80%, #000)` | Hover / pressed orange |
| `--orange-200` | `color-mix(in srgb, var(--orange) 22%, #fff)` | Light orange tint |
| `--bg` | `#c9c7c2` | Page background (warm grey, matches logo bg). NOTE: prototype's saved default is `#d6d4cf`; ship with `#c9c7c2`. |
| `--bg-2` | `#bebcb6` | Alternating section band background |
| `--ink` | `#1a1512` | Near-black warm text / dark panels |
| `--ink-2` | `#57514a` | Muted text |
| `--card` | `#edebe6` | Warm off-white card surface |
| `--card-2` | `#f6f4f0` | Lighter card / phone screen surface |
| `--line` | `rgba(26,21,18,0.16)` | Borders |
| `--line-soft` | `rgba(26,21,18,0.09)` | Soft borders / dividers |
| `--radius` | `14px` | Base radius |
| `--maxw` | `1200px` | Centered content max-width |
| `--shadow` | `0 24px 60px -28px rgba(26,21,18,0.55)` | Elevation (phones, cards) |

**Spacing:** section vertical padding `110px` desktop / `80px` ≤940px (`.section-pad`). Content gutter `28px` (`.wrap`). Common gaps: 14/18/22/24px.

**Radii used:** buttons 11px; cards 18–22px; large panels/CTA 26–30px; phone frame 46px (screen 36px); chips 999px.

## Typography
Two Google Fonts:
- **Archivo** (`--font-display`) — weights 500/600/700/800/900. Used for all headings, eyebrows, buttons, numbers, UI labels. Display headings use **800**, `letter-spacing: -0.02em`, `line-height: 0.98`, frequently **UPPERCASE**.
- **Hanken Grotesk** (`--font-body`) — weights 400/500/600/700. Body copy, lede paragraphs, list text. Base body `18px`, `line-height 1.55`.

Type scale (clamps are `min, preferred, max`):
- Hero `h1`: `clamp(44px, 7vw, 90px)`, uppercase, weight 800.
- Section `h2`: `clamp(34px, 5vw, 60px)`, uppercase.
- Eyebrow/kicker: Archivo 700, `13px`, `letter-spacing 0.16em`, uppercase, color `--ink-2`. Has a leading 3-dot orange motif drawn with `box-shadow` on `::before`.
- Lede: `clamp(18px, 2.2vw, 23px)`, color `--ink-2`.
- Step card `h3`: `30px` uppercase. Feature `h3`: `21px`. Body/feature `p`: 16–17px.

## The "dot-matrix" accent system (`pixelfont.js`)
Short labels and numbers are rendered as LED pixel text matching the logo. `pixelfont.js` exposes `window.PixelText` and auto-processes any `<span class="pix" data-text="01">`:
- 5×7 bitmap font (digits + a subset of A–Z). Each "on" pixel is a rounded square (`border-radius ~28%` of dot size) in `--orange` (override via `data-color`).
- Attributes: `data-text`, `data-size` (px per dot, default 5), `data-gap`, `data-color`, `data-dim` ("1" shows faint off-pixels).
- Used for: hero B step chips ("01"/"02"), the big method step numbers ("01"/"02" at `data-size=11`), and a "FREE"/"LEARN→PRACTICE" accent in the "Bold" LED-accents mode.

**To reimplement:** either (a) port this tiny renderer (it's framework-agnostic, ~140 lines), or (b) pre-render these few labels as SVG. Don't hand-author the bitmaps differently — reuse `pixelfont.js`'s `FONT` map.

---

## Page structure (top → bottom)

The prototype ships **three interchangeable hero directions** (toggled via the Tweaks panel `data-hero` on `<body>`). **Choose ONE** for production — recommended: **Direction C (orange block)**, which is the current default and the boldest. All three share the same lower sections.

### 0. Sticky nav (`header.nav`)
- Full-bleed (spans the **entire viewport width**, not the 1200px column): logo hugs the left corner, CTA hugs the right corner. Horizontal padding `clamp(20px, 3.5vw, 60px)`. Height `76px`. Background `--bg` at 86% with `backdrop-filter: blur(10px)`, bottom hairline.
- **Left:** wordmark `<img>` ~52px tall, links to top.
- **Center:** nav links "Method", "Features", "The App" (Hanken 600, `--ink-2`, hover `--ink`). Hidden ≤940px.
- **Right:** **"Sign in"** button — `.btn.btn-primary` (solid orange, white text).

### 1. Hero — pick ONE direction

**Direction A — Editorial split** (`#hero-a`)
- 2-col grid `1.05fr / 0.95fr`, vertically centered.
- Left: eyebrow "For Leaving Cert students" → `h1` "THE LEAVING CERT, STRIPPED **BACK.**" (last word in `--orange` via `.accent`) → lede → CTA row (`Get started free` primary + `See how it works` ghost) → micro line with a "01" pixel.
- Right: a phone mockup showing the **Flashcard** screen, sitting over a soft radial orange `.glow`.

**Direction B — Centered** (`#hero-b`)
- Centered column. Large wordmark `<img>` (~78% width) → `h1` (single line, no accent span) → lede → centered CTA row → a row of two step **chips** ("01 Learn the content" → arrow → "02 Practice exam questions") → two phones side by side (Flashcard + Exam).

**Direction C — Orange block** (`#hero-c`) ← recommended default
- 2-col grid `1fr / 0.92fr`.
- Left: a solid **orange panel** (`--orange`, radius 26px, padding 60×54px) containing a faint white dotted texture (`.dotfield`, radial-dot background), eyebrow "625 is closer than you think", white `h1`, white lede, and CTA row. Inside the panel the primary button is **dark** (`--ink`) instead of orange; the ghost button has a white border.
- Right: phone mockup showing the **Exam** screen.
- IMPORTANT: panel text/buttons must sit **above** `.dotfield` (give content `position:relative; z-index:1`) so the dot texture never shows on top of the dark button.

Hero `h1` copy options (the prototype lets you swap; ship one): "The Leaving Cert, stripped back." (default) / "Learn it. Nail the exam." / "No notes mountain. Just marks."

### 2. Method — "Two steps. That's it." (`#method`, `.band` background)
- Section head: eyebrow "The method" → `h2` "TWO STEPS. THAT'S IT." → lede.
- 2-col grid of two **step cards** (`--card`, radius 22px, padding 38×36px):
  - Card 1: big LED **"01"** → tag "LEARN" (orange) → `h3` "LEARN THE CONTENT" → copy → mini illustration (dark mini-flashcard "Define homeostasis.").
  - Card 2: big LED **"02"** → tag "PRACTICE" → `h3` "PRACTICE EXAM QUESTIONS" → copy → mini illustration (two MCQ option rows, the correct one outlined in orange).

### 3. Features — "Less app. More marks." (`#features`)
- Section head (eyebrow "What's inside" + `h2`).
- 3-col grid of feature cards (`--card`, radius 18px). Each: a 46px rounded icon tile (orange-tinted bg, orange 2px stroke line-icon) + `h3` + `p`:
  1. **AI flashcards & quizzes** — "Drop in a topic and get clean, on-spec flashcards and quizzes in seconds…"
  2. **Real exam questions** — "Practise the question styles that actually come up, with marking that mirrors the real exam scheme."
  3. **Know where you stand** — "Every subject shows what you've nailed and what still needs work…"

### 4. Product — "Open it. Start studying." (`#product`, `.band`)
- 2-col grid `0.9fr / 1.1fr`.
- Left: two overlapping phone mockups (Flashcard rotated −4°, Exam rotated +3°) over a glow.
- Right: eyebrow "The app" → `h2` "OPEN IT. START STUDYING." → numbered list (orange square badge "1/2/3" + title + copy): "Pick a subject & topic" / "Learn with flashcards" / "Sit exam questions" → `Get started free` button.

### 5. Sign-up CTA (`#start`)  ← all CTAs scroll here
- A dark rounded panel (`.cta`, `--ink` bg, radius 30px, padding 72×60px) with a faint dotted texture, 2-col.
- Left: small wordmark, `h2` "GET IT BEFORE THE NEXT EXAM." (white), subcopy "Free to use — study right in your browser. No install needed."
- Right: **"Get started free"** primary button (orange, 18px) + note "Already have an account? **Sign in**" (white underlined link).

### 6. Footer (`footer.site`)
- Left: wordmark + tagline "The bare-bones way to study for the Leaving Cert."
- Right: two link columns — **PRODUCT** (Method, Features, The app, Sign in) and **COMPANY** (About, Contact, Privacy).
- Bottom bar: "© 2026 barebones. Made in Ireland." + "Not affiliated with the State Examinations Commission."

---

## App mockup screens (the phone UI)
The phones are CSS frames (radius 46px, dark bezel, dynamic-island pill, status bar "08:15"). Two screens, defined once as `<template>` and stamped into every `.phone[data-screen]`:

**Flashcard screen** (`data-screen="flash"`)
- Top row: subject "● Biology" + progress "12 / 40 cards".
- Segmented tabs "Learn"(active) / "Practice".
- A dark flashcard (`--ink`): tiny "FLASHCARD" label (orange), a 3×2 orange pixel dot motif top-right, big question "Define homeostasis.", "↺ Tap to flip" footer.

**Exam screen** (`data-screen="exam"`)
- Top row: "● Biology" + "Q4 · 6 marks".
- Tabs "Learn" / "Practice"(active).
- Meta "EXAM QUESTION · HIGHER LEVEL", question "Homeostasis is best described as…", four MCQ option rows (A–D, each with a square key badge). Option **A is "correct"** — orange border + tinted bg + orange key. A full-width orange "Check answer" button.

> Note: subject/data ("Biology", "homeostasis", "08:15") is placeholder demo content.

## Interactions & Behavior
- **Tap-to-flip flashcard:** clicking any `.flashcard` toggles a `.flipped` state that swaps the question text for the answer ("The maintenance of a stable internal environment…") and the label "Flashcard"↔"Answer". (Prototype does this by mutating textContent; in your framework use component state.)
- **Scroll reveal:** elements with `.reveal` fade up (`opacity 0→1`, `translateY(16px)→0`, 0.7s ease) when they enter the viewport (IntersectionObserver, threshold 0.01, `rootMargin: 0 0 -8% 0`). A 1.2s safety timer reveals anything already in view. Respect `prefers-reduced-motion`.
- **Hover states:** primary button → darker orange + `translateY(-2px)`; ghost → border darkens + lift; badges/cards → subtle lift.
- **Smooth scroll:** in-page anchors (`#method`, `#features`, `#product`, `#start`) scroll smoothly.
- **Responsive:** ≤940px nav links hide, all 2-col grids collapse to 1-col, section padding drops to 80px; ≤560px phones shrink and product phones stack.

## Tweaks panel (authoring tool — DO NOT SHIP)
`tweaks-panel.jsx` + the inline React block render a floating "Tweaks" panel used during design to flip hero direction, headline, brand orange, LED-accent intensity, and background. It drives `body[data-hero]`, `body[data-accent]`, and the `--orange`/`--bg` CSS variables. **Omit entirely from production.** Use it only to preview the options and decide which to build.

## Files in this bundle
- `Landing.html` — the full prototype markup + inline scripts (phone stamping, reveal, flip, Tweaks app).
- `styles.css` — all styles and design tokens. **This is the source of truth for visual values.**
- `pixelfont.js` — the LED dot-matrix label renderer (`window.PixelText`).
- `tweaks-panel.jsx` — design-only Tweaks shell (do not ship).
- `assets/logo-wordmark.png`, `assets/logo-bb.png` — brand marks (transparent PNG; consider re-exporting as SVG).

## How to use this in your repo
1. Unzip this folder somewhere inside your project (e.g. `docs/design/barebones-landing/`).
2. Open `Landing.html` in a browser to see the live reference; read `styles.css` for exact values.
3. Point your coding agent at this folder, e.g. *"Implement the landing page described in `docs/design/barebones-landing/README.md`, recreating it with our existing React + Tailwind components. Use Direction C (orange block) for the hero. The HTML/CSS here is reference only."*
