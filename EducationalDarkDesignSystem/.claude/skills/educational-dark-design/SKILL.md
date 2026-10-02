---
name: educational-dark-design
description: Build HTML presentation slides in the "Educational Dark" design system — navy canvas, cyan Signika headings, Bauhaus-style corner motifs (quarter circles, donuts, stripes, dot grids). Use whenever someone asks for slides, a deck, a presentation or "slide HTML" in the educational dark / dark navy style, or for a lecture, seminar, workshop, project report or student talk that should use this template, even if they don't name the design system.
---

# Educational Dark: slide design system and deck builder

This skill produces **one self-contained HTML file** per deck: 16:9 slides (960×540 px canvas, the exact size of the source PPTX) that scale to any screen, go fullscreen with F, and print to PDF. The look is taken from slides 1–35 of the Slidesgo template "Choosing a Career for Students": every slide on a **dark navy canvas**, centered cyan Signika titles, white body text, and **geometric motif clusters flush in the corners**.

Files in this skill:

| Path | What it is |
|---|---|
| `assets/starter.html` | The deck shell: design tokens, the motif sprite (exact PPTX shapes), all layout CSS, and the runtime. **Every deck starts as a copy of this file.** |
| `references/layouts.md` | Catalogue of the 34 allowed layouts, each with a copy-paste HTML snippet. |
| `examples/showcase.html` | Every layout rendered with sample content. Open it to see the target look. |
| `scripts/check_deck.py` | Validator. Static checks need no dependencies; `--render` also screenshots each slide and flags text that overflows, touches a motif, or (on cover / section / whoa / statement / quote / big-number / thanks slides) isn't centred on the canvas (uses Playwright, or falls back to a local Chrome / Edge). |
| `scripts/export_pdf.py` | HTML → PDF (one slide per page, fonts embedded). Needs Playwright. |

## Workflow

1. **Get the content first.** Ask for, or pull from the repo or docs: the purpose (defense, lecture, progress report, demo day), the time limit, the audience, and real facts (numbers, features, architecture, results). Do not invent data. When a number is unknown, show `[số liệu]` as a placeholder and list it for the user.
2. **Write the outline as a table** with slide number, layout id and key message (one sentence). For a defense, use the outline below. Show it to the user before building if they are available.
3. **Build the deck.** Copy `assets/starter.html` to the output path **with a file copy (e.g. `cp`)**, never by retyping it: it carries an ~60 KB sprite of motif paths that must stay byte-identical. Set `<title>` and `<html lang>` (`vi` for Vietnamese, `en` for English — it switches the body font, see Typography). Paste one snippet per slide from `references/layouts.md` between the `SLIDES START` and `SLIDES END` markers. Replace the text only. Keep every class name and every `<svg class="deco">` line exactly as in the snippet.
4. **Validate.** Run `python3 <skill>/scripts/check_deck.py deck.html --render /tmp/deck-check` and fix every ERROR. Then look at `contact-sheet.png` (or the `slide-NN.png` files) yourself. If the web fonts can't be downloaded in your environment, add `--wide-font`, which stress-tests with a wider font. When a slide overflows, shorten the text. Do not shrink the font or move motifs.
5. **Deliver** the single `.html` file. Offer a PDF made with `scripts/export_pdf.py`, or Chrome → Print → Save as PDF with Margins "None" and "Background graphics" ticked. The PDF is the safest file for presenting offline, because the HTML loads its fonts from Google Fonts.

## Hard rules (the design system)

### Colour: only these five, always through the CSS variables

| Token | Hex | Used for |
|---|---|---|
| `--navy` | `#0D1030` | the canvas of **every** slide, donut holes, stripe gaps |
| `--cyan` | `#79E0FF` | slide titles, item headings (`.h3`/`.h4`), `<b>`, lines and table rules, motifs |
| `--blue` | `#0F5AFF` | motifs, chart series, gantt bars, highlight nodes, the canvas of accent (pacing) slides |
| `--grey` | `#C2C2C2` | step / section numbers (`.num`), secondary values (`td.v`), meta text |
| `--white` | `#FFFFFF` | body text, big values (`.stat`), motifs, keyword highlight inside cyan display text (`.hl`) |

No other colours: no red or green for good/bad, no tints, no opacity on content, no light slides. The five hex values are the ones printed on the template's own "Fonts & colors used" slide. In SVG, paint with the `.f-navy / .f-cyan / .f-blue / .f-grey / .f-white` and `.s-*` classes, never with hex values.

### Typography: Signika for display, Lato for body, fixed scale

| Role | Token | Size | Font / weight / colour |
|---|---|---|---|
| Slide title | `--fs-h2` | 46.7px (35pt) | Signika 700, cyan, centered, **one line** |
| Item heading | `--fs-h3` | 29.3px (22pt) | Signika 700, cyan |
| Compact heading, table header | `--fs-h4` | 24px (18pt) | Signika 700, cyan |
| Body | `--fs-body` | 18.7px (14pt) | Lato 400, white |
| Caption / dense text | `--fs-sm` | 16px (12pt) | Lato 400 |
| Step number / percentage | `--fs-stat` | 40px (30pt) | Signika 700, grey (`.num`) or white (`.stat`) |
| Section title / number | `--fs-sec` / `--fs-d2` | 50.7px / 80px | Signika 700, cyan / grey |
| Cover title | `--fs-cv` | 69.3px (52pt) | Signika 700, cyan |
| Big number | `--fs-d1` | 96px | Signika 700, cyan |

**Vietnamese:** Lato has no glyphs for ạ, ế, ộ…, so with `<html lang="vi">` the body font switches automatically to Nunito Sans (the closest humanist sans that has them). Signika covers Vietnamese. Never override this.

Never set a font size in px on a slide; use the tokens. Titles are sentence case. No UPPERCASE except the gantt month labels, no italics, no underlines, no emoji, no text shadows. Vietnamese needs full diacritics.

### Motifs (the decoration system)
- The motifs are the **exact vector shapes of the PPTX layouts** (quarter circles, donuts, split squares, pills, stripe bands, concentric arcs, dot grids). They live once in the sprite `<svg class="sprite">` at the top of `<body>` in the starter. Each snippet places its source layout's set with lines like `<svg class="deco" style="left:…;top:…;width:…;height:…"><use href="#m1a"/></svg>`.
- Copy those lines **verbatim**. Never add, move, resize, recolour or swap motifs, never draw your own, and never edit the sprite. The validator compares the sprite with the starter and rejects unknown `#m…` ids or more than 5 `.deco` per slide.
- Motifs sit only in corners or on an edge, and text must stay clear of their boxes (the validator checks it).

### Grid and components
- Canvas 960×540. Titles sit in the box x 75–885, y 47–107. Keep all text inside x 20–940 and y 8–532, and clear of motifs.
- Flat design: no shadows, no cards, no borders except table rules, outlined boxes (`.node`, `.core`, `.lv`) and device frames. Square corners except motifs, dots and device frames.
- Photos are warm, candid and in colour (`<img class="photo">`), cropped to a rectangle — never full-bleed except in `photo`. Product screenshots use `<img class="shot">` inside a device mockup (`computer`, `tablet`, `phone`). Placeholders use `<div class="ph">[ẢNH: mô tả]</div>`.
- Icons are inline SVG line icons (24-unit viewBox, Lucide / Phosphor-regular style) with `class="icon"`: cyan outline at 40 px. Never filled or multicolour.
- Charts are inline SVG in cyan / blue / grey (+ white): donut rings, bars. No 3D, no gridline clutter, direct labels.

### Content density
- One message per slide. The slide title states it in **≤ 30 characters** (one line at 46.7px). Longer titles fail the validator.
- Bullets: 3–5 per slide, ≤ 10 words each, one nesting level at most.
- Respect the per-layout limits in `references/layouts.md` (item counts, character and word counts). If content doesn't fit, split it into two slides. Never shrink the text.
- Don't use the same layout on consecutive slides. Alternate `section` / `section-alt`.
- **Pacing:** give the one idea the audience must remember its own blue `focus` slide (eyebrow, the idea in big type, follow-up). The colour change is the pause. Use it about once per section and never twice in a row; `accent` also works on `whoa` and `quote`, but don't stack it on every hero slide or it stops signalling anything.
- Numbers use the Vietnamese format in Vietnamese decks (`1,2 giây`, `12.500 người dùng`).

## Recommended outline: project presentation (15–20 min, ~18–24 slides)

| # | Layout | Content |
|---|---|---|
| 1 | `cover` | Project name, one-line subtitle, team, advisor (GVHD), date |
| 2 | `toc` | 4–5 chapters: Vấn đề · Giải pháp · Hệ thống · Kết quả (· Hướng đi) |
| 3 | `section` | 01 Vấn đề |
| 4 | `text2` or `bignum` | Context and the one striking statistic |
| 5 | `quote` / `donuts` | Evidence from user research |
| 6 | `compare` | Existing solutions and their gaps |
| 7 | `section-alt` | 02 Giải pháp |
| 8 | `focus` or `statement` | The product idea in one line |
| 9 | `zig3` / `five` | Key features / functional requirements |
| 10 | `section` | 03 Hệ thống |
| 11 | `diagram` / `hub` | Architecture, or modules around the core |
| 12 | `steps` | Main flow / pipeline / development process |
| 13 | `computer` / `phone` / `tablet` | Screenshots (one slide per key screen) |
| 14 | `section-alt` | 04 Kết quả |
| 15 | `figure` / `table` / `stats` / `pie` | Test and evaluation results (charts, figures with citations) |
| 16 | `timeline` / `gantt` | What was done, and when |
| 17 | `stairs` | Future work (Hướng phát triển) |
| 18 | `team` | Members and roles |
| 19 | `thanks` | Q&A, contacts, repo and demo links |

For a progress report (báo cáo tiến độ), use `cover`, `toc`, `gantt` (done / doing / next), `five` (completed tasks), `zig4` (risks), `computer` (demo) and `thanks`. For a lecture, seminar or workshop, lean on `figure` (charts, textbook figures with citations), `whoa`, `bullets`, `steps`, `phototext`, `quote` and `bignum`. Redraw charts from their data as inline SVG in the palette; recolour black-on-white figures to white-on-navy rather than pasting white rectangles.

## When no layout fits
Use `diagram` (title plus a free canvas) and build inside `.stage` with the primitives: `.node` / `.node.blue` / `.node.cyan`, `.tbl`, `.ul`, `.dot`, `.stat`, `.num` and inline SVG with the paint classes. Keep the canvas bounds, the palette and the diagram snippet's motifs. If you truly need a new CSS rule, put it in the `DECK-SPECIFIC` block of the copied starter, using only the tokens. Never edit `:root`.

## Runtime (tell the presenter)
→ / Space: next slide. ←: previous. Home / End: first / last. **F**: fullscreen. **O**: overview grid (click a slide to jump). **P**: print or save as PDF. `deck.html#7` opens slide 7.
