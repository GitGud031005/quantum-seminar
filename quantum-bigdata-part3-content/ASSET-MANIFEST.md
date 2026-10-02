# Asset manifest

All images are neutral (black/grey, white or transparent background) so they can be restyled to any design. SVG files are editable; PNGs are 2–3× resolution.

| File (under `assets/`) | Slide | Source / credit | Alt text | Notes |
|---|---|---|---|---|
| `book-figures/nc_fig6-8_cpu_memory_load_store.png` | 4 | Nielsen & Chuang (2010), Fig. 6.8, p. 266 — cropped from the textbook | Diagram: a CPU connected to an N-cell memory by LOAD and STORE arrows | Cite on slide: "Source: Nielsen & Chuang (2010), Fig. 6.8." |
| `book-figures/nc_fig6-9_qram_quantum_addressing.png` | 10 | Nielsen & Chuang (2010), Fig. 6.9, p. 268 — cropped from the textbook | Binary tree of quantum switches x4…x0 routing into a 32-cell memory d1…d32 and back out | Portrait. Cite on slide. |
| `book-figures/nc_fig7-7_ion_trap_schematic.png` | 12 | Nielsen & Chuang (2010), Fig. 7.7, p. 311 — cropped from the textbook | Schematic of an ion-trap quantum computer: four ions between cylindrical electrodes, addressed by modulated lasers, read by photodetectors | Wide. Cite on slide. |
| `charts/grover_histogram_3q.png/.svg` | 2 | Group demo: code/grover_demo.py (Qiskit Aer, seed 7) → data/grover_counts_3q.csv | Histogram of 8 measured states; 101 holds 93% of 1,024 shots, the rest near zero | Re-render freely from the CSV. |
| `charts/qubit_amplitude_growth.png/.svg` | 3 | Computed: 2ⁿ (code/make_charts.py) | Line chart: amplitudes grow as 2ⁿ; 50 qubits reach 10¹⁵, 300 qubits pass the 10⁸⁰ atoms line |  |
| `charts/quantum_kernel_matrix.png/.svg` | 6 | Group experiment: code/quantum_kernel_experiment.py → data/quantum_kernel_matrix_train.csv | 80×80 quantum kernel heatmap sorted by class; class blocks are only faintly visible | Faint blocks are the point — the kernel separates classes poorly. |
| `charts/two_moons_dataset.png/.svg` | 6 | Group experiment → data/two_moons.csv | Scatter plot of two interleaved crescent-shaped classes, 120 points |  |
| `charts/kernel_accuracy_comparison.png/.svg` | 6 | Group experiment → data/kernel_accuracy.csv | Bars: quantum kernel 90.0%, linear SVM 92.5%, RBF SVM 97.5% | The deck showed these as bars; any chart form is fine. |
| `charts/hhl_scaling.png/.svg` | 7 | Computed: N vs log₂N (code/make_charts.py) | Log-log chart: classical ~N, HHL ~log N, but HHL plus reading out all of x ~N again |  |
| `illustrations/amplitude_amplification.svg/.png` | 4 | Original vector drawing made for this talk (free to restyle) | Bar chart sketch: one marked state towers above a dashed mean line while the other seven stay small |  |
| `illustrations/hybrid_quantum_classical_loop.svg/.png` | 5 | Original vector drawing made for this talk (free to restyle) | Hybrid loop: Data x → parameterized circuit U(θ) → measure → classical optimizer, with a dashed arrow back to the circuit labelled update θ and repeat |  |
| `illustrations/maxcut_graph.svg/.png` | 8 | Original vector drawing made for this talk (free to restyle) | MaxCut example: five nodes split into two groups (filled vs light); solid edges cross the cut, dashed edges do not |  |
| `illustrations/qaoa_circuit.svg/.png` | 8 | Original vector drawing made for this talk (free to restyle) | QAOA circuit sketch: three qubit wires with alternating problem layers (wave symbol) and mixer layers, repeated twice, then measurement |  |
| `illustrations/energy_landscape.svg/.png` | 8 | Original vector drawing made for this talk (free to restyle) | Energy landscape: a curve with several valleys; a ball starts high and tunnels (dashed arc) into the lowest valley |  |
| `illustrations/sparse_matrix.svg/.png` | 7 (optional) | Original vector drawing made for this talk (free to restyle) | 10x10 grid with filled diagonal and a few scattered filled cells: a sparse matrix |  |
| `illustrations/superconducting_chip.svg/.png` | 12 | Original vector drawing made for this talk (free to restyle) | Superconducting quantum chip illustration: diamond-shaped lattice of qubits with couplers, wired out to connectors on both sides | Illustration, not a photo |
| `illustrations/dilution_refrigerator.svg/.png` | 12 (optional) | Original vector drawing made for this talk (free to restyle) | Dilution refrigerator (the chandelier): five stacked cooling plates linked by wiring, chip at the coldest bottom stage | Illustration, not a photo |
| `illustrations/quantum_circuit_h_cnot_measure.svg/.png` | 2, 5 (optional) | Original vector drawing made for this talk (free to restyle) | Three-qubit circuit sketch: Hadamard gates, a CNOT, two generic gates, then measurement meters |  |
| `illustrations/bloch_sphere.svg/.png` | 5, 9 (optional) | Original vector drawing made for this talk (free to restyle) | Bloch sphere: sphere with dashed equator and vertical axis, a state vector pointing up and to the right |  |
| `illustrations/atom.svg/.png` | 1 (optional) | Original vector drawing made for this talk (free to restyle) | Atom icon: three elliptical orbits around a nucleus with electrons |  |
| `illustrations/quantum_chip_icon.svg/.png` | 13 (optional) | Original vector drawing made for this talk (free to restyle) | Small chip icon with a 3x3 grid of qubits and pins on four sides |  |
| `illustrations/entangled_qubit_pair.svg/.png` | 13 (optional) | Original vector drawing made for this talk (free to restyle) | Two qubits joined by a wavy line, one spin up and one spin down: an entangled pair |  |

**Book figures:** reproduced from the course reference textbook for classroom use; keep the citation visible on the slide.

**Not included:** real press photos of Google Willow / IBM Quantum System Two (could not be downloaded). If the slide agent can fetch licensed press images, they may replace `superconducting_chip` / `dilution_refrigerator` on slide 12 with credit.
