# Quantum Computing — Part 2: Gates, Circuits & Algorithms — content package

Content-only handoff for building the Part 2 slides of a group seminar on Quantum Computing (Big Data course, HCMUT). **No design system is included or implied** — no colours, fonts, templates or layouts. Style the deck however you like; keep the wording and numbers.

This package is built from the group's two drafts (`Part_B_BigData.docx`, `Part_B_Speech_Script.docx`), checked against the group plan and the Nielsen & Chuang textbook, with errors fixed and every number re-run in code.

## What's inside
| Path | Contents |
|---|---|
| `slides/slide-content-spec.md` | **Start here.** 19 main slides (light on math, focused on meaning) + 3 backup slides A1–A3 with the formulas; on-slide text, assets, timing |
| `notes/speaker-notes-en.md` | Speaker notes in English, one per slide, plus prepared Q&A answers |
| `notes/speaker-notes-vi.md` | Vietnamese practice version of the same notes and Q&A |
| `ASSET-MANIFEST.md` | Every image: slide, source/credit, alt text |
| `assets/book-figures/` | 12 figures cropped from Nielsen & Chuang (Figs. 1.4, 1.5, 1.6, 1.12, 1.17, 1.20, 4.2, 5.1, 5.4, 6.1, 6.2, 6.3) |
| `assets/charts/` | 10 charts (PNG + SVG) generated from the data files |
| `assets/circuits/` | 5 circuit diagrams drawn with Qiskit (PNG + SVG) |
| `assets/illustrations/` | Labelled Bloch sphere showing the Hadamard gate (PNG + SVG) |
| `data/` | Raw numbers: Bell and Grover counts, amplitudes per step, success vs rounds, scaling table, Deutsch–Jozsa, Shor N = 15 |
| `code/` | `run_experiments.py`, `make_charts.py`, `draw_circuits.py`, `draw_bloch.py` |
| `references.md` | Reference list with corrected textbook sections and pages |
| `plan/seminar-group-plan-vi.md` | The whole group's seminar plan (Parts 1–3), Vietnamese, for context only |

## Constraints for the slide builder
- Slide text is **English**; keep every number exactly as in the spec.
- The 3-qubit demo result is **954 / 1,024 = 93.2%** (theory 94.5%). Part 3 re-shows the same run, so do not replace it with another number.
- Keep citations under the book figures. Figure 6.3 uses a different angle convention (start θ/2, rotation θ) from the slides (start θ, rotation 2θ); keep the note.
- Keep the main slides light on math: only the signature items listed at the top of the spec. Formulas go on backup slides A1–A3.
- Slide 10 (Deutsch–Jozsa) is optional. Target ~15 minutes without it, ~16 with it.
- Do not add the 10¹²-record example, database-index or QRAM discussion: Part 3 covers them.

## Reproduce the data and figures
```bash
pip install qiskit qiskit-aer numpy matplotlib cairosvg pylatexenc
cd code
python run_experiments.py   # -> data/*.csv
python make_charts.py       # -> assets/charts/
python draw_circuits.py     # -> assets/circuits/
python draw_bloch.py        # -> assets/illustrations/
```
Tested with Qiskit 2.x and qiskit-aer 0.17.
