# Asset manifest

All images are neutral (black and grey on white) so they can be restyled to any design. SVG files are editable. PNGs are 3× resolution (illustrations) or 200 dpi (charts). All illustrations are original drawings made for this talk and are free to restyle. `code/make_illustrations.py` regenerates them.

**Main** means the picture carries the idea on that slide. **Support** means it can be dropped if space is short.

## Illustrations (18)

| File (under `assets/illustrations/`) | Slide | Role | Alt text |
|---|---|---|---|
| `bit_vs_qubit` | 1 (optional), 3 | Main | Left: a switch with positions 0 and 1, captioned "Bit: a switch, only 0 or 1". Right: a sphere with an arrow from the centre, 0 at the top and 1 at the bottom, captioned "Qubit: an arrow on a sphere. Up = 0, down = 1, anything in between = a mix" |
| `chessboard_doubling` | 2 | Main | Seven chessboard squares holding 1, 2, 4, 8, 16, 32 and 64 dots, then a dashed box: "square 64: 9 billion billion grains". Caption: each square doubles the one before, and a quantum system does the same with every extra particle |
| `plus_minus_amplitudes` | 4 | Main | Two small bar charts. Plus: bars for 0 and 1 of the same height, both above the line. Minus: the bar for 0 above the line, the bar for 1 the same size but below it. Caption: same size, same 50/50 when read, only the sign differs |
| `hidden_coin_vs_qubit` | 4 | Main (emphasis) | Left, marked ✗: a cup hiding a coin with a question mark, "Already heads or tails, we just can't see it. Not how a qubit works". Right, marked ✓: a sphere with the arrow on the equator, "Genuinely undecided until read, and the arrow also has a direction" |
| `bloch_sphere_labeled` | 5 | Main | A sphere with 0 at the north pole, 1 at the south pole, and "plus" and "minus" as dots on opposite sides of the equator, plus an arrow. Side notes: height (latitude) → the chance of reading 0 or 1; equator = 50/50 mixes; direction around (longitude) → the phase |
| `phase_compass` | 5 | Support (emphasis) | The equator seen from above as a compass: plus points east, minus points west. Box 1, "Ask 0 or 1?": plus 50/50, minus 50/50, they look identical. Box 2, "Ask east or west?": plus always E, minus always W, so the phase is real information |
| `measurement_collapse` | 6 | Main | A sphere with the arrow on the equator, an arrow into a meter labelled "read it", then two small spheres with the arrow snapped to the north pole (0, 50%) or the south pole (1, 50%). Caption: after reading, the arrow snaps to a pole and everything else is lost |
| `big_store_small_door` | 6 | Main (emphasis) | A large box full of dots, "Inside: 2ⁿ weights at once", narrowing into a thin exit that lets out four bits, 0 1 1 0, "Out: n bits". Caption: a huge store with a tiny door |
| `water_waves` | 7 | Main | Two rows of waves. "In step": wave + wave = a wave twice as tall ("stronger"). "Out of step": wave + opposite wave = a flat line ("cancelled") |
| `interference_paths` | 7 | Main | Two rows, each with two curved paths from a start dot to the result 0. "Plus, then H": +½ and +½ give 1, always 0. "Minus, then H": +½ and a dashed −½ give 0, never 0 |
| `combinations_grid` | 8 | Main | Rows of boxes: 1 qubit → 0, 1 (= 2); 2 qubits → 00, 01, 10, 11 (= 4); 3 qubits → 000 … 111 (= 8); n qubits → 2ⁿ combinations, each with its own weight |
| `bell_pair_circuit` | Q&A only (gates are Part 2's topic; Part 2 slide 7 builds this circuit) | — | Two-qubit circuit: both wires start at 0, an H box on the top wire, a CNOT linking top to bottom, and two meters. Result text: "always 00 or 11, never 01 or 10" |
| `entangled_pair_distance` | 9 | Main (emphasis) | Two spheres labelled Alice and Bob, joined by a wavy dashed line "1,000 km apart". Between them, five runs: 0·0, 1·1, 1·1, 0·0, 1·1, "each run: always the same". Caption: each side alone sees random 0s and 1s, and the link shows only when they compare |
| `gloves_in_boxes` | 10 | Main | Two boxes shipped apart, one with a left glove and one with a right glove. Caption: open one box and you instantly know the other; the answers were fixed from the start |
| `chsh_game` | 10 | Main | A referee sends "question A or B" to Alice and to Bob, who are separated by a dashed "no talking" line; each returns "answer 0 or 1". Rule: win if the answers match, unless both got question B, then they must differ |
| `no_cloning` | 11 | Main | Top row: a sheet of paper → copier → two sheets, ✓ "bits: fine". Bottom row: a small qubit sphere → copier → two spheres crossed out, "qubits: impossible". Caption: a copier that works for 0 and 1 turns a mix into a linked pair, not two copies |
| `eavesdropper_qkd` | 11 | Main (emphasis) | Alice sends dots along a line to Bob. Eve taps the line with a meter; after her, some dots are hollow and marked "!" ("disturbed"). Caption: Eve cannot copy, so she must read, and reading leaves errors that Alice and Bob detect |
| `three_resources` | 12 | Main | Three boxes linked by arrows: Superposition (opens up 2ⁿ possibilities) → Entanglement (links qubits together) → Interference (pushes toward the answer). Below, a dashed box: "Two rules: reading gives one bit per qubit; qubits cannot be copied" |

Each file exists as `.svg` and `.png`.

## Charts (5)

| File (under `assets/charts/`) | Slide | Role | Source | Alt text |
|---|---|---|---|---|
| `qubit_amplitude_growth` | 2 | Support | Computed: 2ⁿ (`code/make_charts.py`) | Line chart of the numbers needed against the number of qubits. 50 qubits → about 10¹⁵ numbers; 300 qubits → about 10⁹⁰, above the dashed line for the ~10⁸⁰ atoms in the universe |
| `single_qubit_measurement` | 6 | Support | Group run: `code/single_qubit_demo.py` (Qiskit Aer) → `data/single_qubit_counts.csv` | Three bar pairs, 1,024 runs each: state 0 gives 0 in 100% of runs; plus and minus both give about 51% / 49%. Title: plus and minus look identical |
| `interference_result` | 7 | Support | Group run: `code/single_qubit_demo.py` → `data/single_qubit_counts.csv` | Two bar pairs: plus then H gives 0 in 100% of runs; minus then H gives 1 in 100% of runs. Title: one extra step before reading, and 50/50 becomes certain |
| `two_qubit_histograms` | 9 | Support | Group run: `code/bell_pair_demo.py` → `data/two_qubit_counts.csv` | Two histograms: two independent qubits give 00, 01, 10 and 11 about 25% each; the entangled pair gives only 00 (49%) and 11 (51%) |
| `chsh_win_rates` | 10 | Support | Group run: `code/chsh_game.py` → `data/chsh_results.csv` | Bars: best plan agreed in advance 75.0%, entangled qubits 85.1%, with a dashed line at the 75% limit. The theory value, 85.4%, is in the CSV |

**Book figures** (cropped from Nielsen & Chuang, *Quantum Computation and Quantum Information*, 10th Anniv. ed., 2010, for classroom use; keep the citation under each figure). The main slides stay formula-free, so the figures with formulas go on backup slide A1:

| File (under `assets/`) | Slide | Source | Alt text |
|---|---|---|---|
| `book-figures/nc_fig1-2_qubit_as_atom_levels.png` | 3 (optional) | N&C (2010) Fig. 1.2, p. 14 | An atom with two electron orbits labelled |0⟩ and |1⟩: a qubit as two energy levels |
| `book-figures/nc_fig1-22_stern_gerlach.png` | 6 (optional) | N&C Fig. 1.22, p. 44 | Stern–Gerlach schematic: atoms from an oven pass a magnet and split into two beams |
| `book-figures/nc_fig1-3_bloch_sphere.png` | A1 (backup) | N&C Fig. 1.3, p. 15 | Bloch sphere with |0⟩ and |1⟩ at the poles and a state at angles θ and φ |
| `book-figures/nc_fig1-11_copying_circuits.png` | A1 (backup) | N&C Fig. 1.11, p. 25 | Left: a circuit copies a classical bit. Right: the same circuit on a|0⟩ + b|1⟩ gives the entangled a|00⟩ + b|11⟩ |
| `book-figures/nc_fig2-4_bell_experiment_setup.png` | A1 (backup) | N&C Fig. 2.4, p. 115 | Alice and Bob boxes, each choosing one of two ±1 measurements |


**All simulator results** come from an ideal, noise-free simulator (Qiskit Aer, fixed seeds). Real hardware would show small deviations.
