# Quantum × Big Data — Part {N} content package

Content-only input for building the Part {N} slides of a group seminar on Quantum Computing (Big Data course, HCMUT). **No design system is included or implied**: no colours, fonts, templates or layouts. The slide builder styles the deck; keep the wording and numbers.

This folder is the shared skeleton for Parts 1, 2 and 3. Copy it to `quantum-bigdata-part{N}-content`, replace every `{N}` and `{...}` placeholder, and delete this paragraph.

## What's inside
| Path | Contents |
|---|---|
| `slides/slide-content-spec.md` | **Start here.** Slides in order: purpose, final on-slide text, which asset goes where, timing |
| `notes/speaker-notes-en.md` | Speaker notes in English, one block per slide |
| `notes/speaker-notes-vi.md` | Vietnamese practice version of the notes, with Q&A routing and prepared answers |
| `ASSET-MANIFEST.md` | Every image: slide, source/credit, alt text |
| `assets/book-figures/` | Figures cropped from Nielsen & Chuang: {list figure numbers} |
| `assets/charts/` | Charts (PNG + SVG) generated from the data files |
| `assets/illustrations/` | Original vector drawings (SVG + PNG) |
| `data/` | Raw data behind the charts and demos |
| `code/` | Reproducible scripts that generate `data/` and `assets/` |
| `references.md` | Full reference list |
| `plan/seminar-group-plan-vi.md` | The whole group's seminar plan (Parts 1–3), Vietnamese, for context only; identical in every part |

The built deck is not part of the input. When it exists, it sits at the folder root as `part{N}-slides.html` (plus `part{N}-slides.pdf` if exported).

## Constraints for the slide builder
- Slide text is **English**; keep all numbers exactly as in the spec.
- The slide count in the spec is a baseline. The builder may split or add slides after confirming with the presenter; the notes stay as the content source.
- {Part-specific constraints: audience level, math allowed on slides, hand-offs with neighbouring parts, key slides, target length}

## Reproduce the data and charts
```bash
pip install {packages}
cd code
python {script}.py   # -> data/{output}.csv
python make_charts.py   # -> assets/charts/*.png, *.svg
```
Tested with {versions}.
