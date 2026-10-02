# Quantum × Big Data — Part 3 content package

Content-only handoff for building the Part 3 slides of a group seminar on Quantum Computing (Big Data course, HCMUT). **No design system is included or implied** — no colours, fonts, templates or layouts. Style the deck however you like; keep the wording and numbers.

## What's inside
| Path | Contents |
|---|---|
| `slides/slide-content-spec.md` | **Start here.** 14 slides in order: purpose, final on-slide text, which asset goes where, timing |
| `notes/speaker-notes-en.md` | Speaker notes in English, one per slide (as used in the talk) |
| `notes/speaker-notes-vi.md` | Vietnamese practice version of the notes + Q&A routing and prepared answers |
| `ASSET-MANIFEST.md` | Every image: slide, source/credit, alt text |
| `assets/book-figures/` | 3 figures cropped from Nielsen & Chuang (Figs. 6.8, 6.9, 7.7) |
| `assets/charts/` | 6 charts (PNG + SVG) generated from the data files |
| `assets/illustrations/` | 13 original vector drawings (SVG + PNG): circuits, MaxCut, QAOA, energy landscape, chip, fridge, Bloch sphere, atom… |
| `data/` | Raw data: Grover counts, quantum-kernel results, kernel matrix, two-moons dataset, hardware table |
| `code/` | Reproducible scripts: `grover_demo.py`, `quantum_kernel_experiment.py`, `make_charts.py` |
| `references.md` | Full reference list |
| `plan/seminar-group-plan-vi.md` | The whole group's seminar plan (Parts 1–3), Vietnamese, for context only |

## Constraints for the slide builder
- Slide text is **English**; keep all numbers exactly as in the spec.
- Keep citations under the three book figures, and label drawn hardware images as *Illustration*.
- Slide 12's hardware numbers are as of Sept 2026 and should be re-checked shortly before the talk.
- Target ~11 minutes for the 14 slides; slide 10 (loading data / QRAM) and slide 6 (kernel experiment) are the key slides.

## Reproduce the data and charts
```bash
pip install qiskit qiskit-aer scikit-learn numpy matplotlib
cd code
python grover_demo.py              # -> data/grover_counts_3q.csv
python quantum_kernel_experiment.py # -> data/kernel_accuracy.csv, two_moons.csv, quantum_kernel_matrix_train.csv
python make_charts.py              # -> assets/charts/*.png, *.svg
```
Tested with Qiskit 2.x and qiskit-aer 0.17.
