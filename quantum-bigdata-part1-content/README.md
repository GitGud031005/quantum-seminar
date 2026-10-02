# Quantum × Big Data — Part 1 content package

Content-only handoff for building the Part 1 slides of a group seminar on Quantum Computing (Big Data course, HCMUT). **No design system is included or implied**: no colours, fonts, templates or layouts. Style the deck however you like; keep the wording and numbers. The layout of this package matches the Part 3 package, so both parts can be built the same way.

## What's inside
| Path | Contents |
|---|---|
| `slides/slide-content-spec.md` | **Start here.** A plain-word glossary, then 12 slides in order: purpose, final on-slide text, which picture goes where (main / support), timing |
| `notes/speaker-notes-en.md` | Speaker notes in English, one per slide, with cues for which picture to point at |
| `notes/speaker-notes-vi.md` | Vietnamese practice version of the notes, with a short glossary, Q&A routing and prepared answers for concept questions |
| `ASSET-MANIFEST.md` | Every image: slide, source/credit, alt text |
| `assets/book-figures/` | 5 figures cropped from Nielsen & Chuang (Figs. 1.2, 1.3, 1.11, 1.22, 2.4); two optional on slides 3 and 6, three on backup slide A1 |
| `assets/charts/` | 5 charts (PNG + SVG) generated from the data files |
| `assets/illustrations/` | 18 original drawings (SVG + PNG), including everyday pictures for the hard ideas: rice on a chessboard, hidden coin, compass, big store with a small door, water waves, gloves in boxes, photocopier, eavesdropper |
| `data/` | Raw simulator results: single-qubit measurements, two-qubit (Bell) counts, CHSH game win rates |
| `code/` | Reproducible scripts: `single_qubit_demo.py`, `bell_pair_demo.py`, `chsh_game.py`, `make_charts.py`, `make_illustrations.py` |
| `references.md` | Full reference list |
| `plan/seminar-group-plan-vi.md` | The whole group's seminar plan (Parts 1–3), Vietnamese, for context only |

## Constraints for the slide builder
- Slide text is **English**; keep all numbers exactly as in the spec.
- Part 1 is for a general audience with no physics background. **No formulas on the slides.** The only maths is counting and percentages: doubling (2ⁿ), ½ + ½ = 1, ½ − ½ = 0, 50%, 75% and 85%. |0⟩ and |1⟩ appear once, as name tags.
- Use the plain words from the glossary at the top of the spec ("weight", "reading", "plus", "minus") the same way on every slide.
- Every hard idea has a picture. Keep the visuals marked **Main**; the ones marked **Support** can be dropped if a slide gets crowded.
- Target about 13 minutes for the 12 slides. Slide 6 (reading a qubit) and slide 7 (interference) are the key slides, because Part 2 builds on them.
- Slide 12 hands over to Part 2 (gates and circuits). Keep its three resources word for word, because Part 2 opens from them.
- Gates belong to Part 2: slide 7 only previews H, and slide 9 does **not** show the H + CNOT circuit (Part 2 builds it).
- Backup slide A1 holds the formulas for Q&A; keep it after the main deck.

## Reproduce the data and charts
```bash
pip install qiskit qiskit-aer numpy matplotlib
cd code
python single_qubit_demo.py   # -> data/single_qubit_counts.csv
python bell_pair_demo.py      # -> data/two_qubit_counts.csv
python chsh_game.py           # -> data/chsh_results.csv
python make_charts.py         # -> assets/charts/*.png, *.svg
python make_illustrations.py  # -> assets/illustrations/*.svg (+ .png if cairosvg is installed)
```
Tested with Qiskit 2.5.2 and qiskit-aer 0.17.2 (same versions as the Part 2 demo).
