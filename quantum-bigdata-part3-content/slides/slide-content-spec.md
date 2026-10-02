# Part 3 — Quantum × Big Data: slide-by-slide content spec

**Talk:** group seminar "Quantum Computing" for a university Big Data course (HCMUT). Part 3 of 3, presented by **Phúc**.
**Audience:** third-year Computer Science students; they have just seen Parts 1–2 (qubits, gates, Grover, Shor) and a live Grover demo.
**Length:** 14 slides, ~11 minutes + Q&A. **Slide language:** English.
**Core message:** quantum algorithms map onto real big-data tasks, but loading data (QRAM) and the fine print behind speedup claims block them today — always ask "compared to what?".

This file is content only. Text under **On-slide text** is final wording (keep numbers exactly). Visuals point to files in `/assets`; see `ASSET-MANIFEST.md` for sources, credits and alt text. Styling, layout and color are entirely up to the slide designer.

Sections: **S1** Setup (slides 1–3) · **S2** Four quantum building blocks for data (4–8) · **S3** The bottlenecks (9–11) · **S4** Hardware, takeaways, Q&A (12–14).

---

## Slide 1 — Cover · S1 · 0:10
**Purpose:** open Part 3 and hand over from Person 2.
**On-slide text**
- Eyebrow: Part 3 of 3
- Title: **Quantum × Big Data**
- Subtitle: Where it helps, where it breaks, and where the hardware stands in 2026
- Presenter line: Phúc · Big Data seminar
**Visual (optional, decorative):** `illustrations/atom.svg`

## Slide 2 — From the demo to real data · S1 · 0:25
**Purpose:** bridge from the live Grover demo to the big-data question.
**On-slide text**
- Title: From the demo to real data
- Chart caption: Our Grover demo: 3 qubits, 2 iterations, 93% of 1,024 shots land on the hidden record 101.
- Label: 8 records, 1 hidden — show the 8 states 000 001 010 011 100 **101** 110 111 with 101 highlighted
- Statement: Grover found it without checking the records one by one.
- Question: Now scale that to a table with 10¹² rows. What does quantum computing actually buy a big-data system?
**Visual:** `charts/grover_histogram_3q.png` (data: `data/grover_counts_3q.csv`) · optional `illustrations/quantum_circuit_h_cnot_measure.svg`

## Slide 3 — Why quantum meets big data · S1 · 0:45
**Purpose:** the scale argument + map each data task to a quantum building block.
**On-slide text**
- Title: Why quantum meets big data
- Headline stat: **2⁵⁰** — ≈ 1.1 × 10¹⁵ amplitudes, described by just 50 qubits
- Table "Data task → quantum tool":

| Big data task | Quantum building block |
|---|---|
| Record lookup | Grover search, O(√N) |
| Classification and learning | Quantum kernels, variational circuits |
| Regression, PCA, linear systems | HHL algorithm |
| Scheduling, feature selection, clustering | QAOA, quantum annealing |

**Visual:** `charts/qubit_amplitude_growth.png` (50 qubits → 10¹⁵; 300 qubits → 10⁹⁰, above the ≈10⁸⁰ atoms line)

## Slide 4 — Quantum search over a database · S2 · 0:55
**Purpose:** Grover on a database, with the textbook model — and why indexes beat it.
**On-slide text**
- Title: Quantum search over a database
- Figure caption: Classical model: the CPU reaches memory only through LOAD and STORE. Source: Nielsen & Chuang (2010), Fig. 6.8.
- Callout: Unsorted N records: classical search needs O(N) LOADs, Grover needs O(√N).
- Label: For N = 10¹² records
  - **5 × 10¹¹** — classical lookups on average (unsorted)
  - **7.9 × 10⁵** — Grover iterations, (π/4)·√N
  - **≈ 40** — comparisons with a sorted index (log₂ N), faster than Grover
**Visuals:** `book-figures/nc_fig6-8_cpu_memory_load_store.png` · `illustrations/amplitude_amplification.svg`

## Slide 5 — Quantum machine learning · S2 · 0:50
**Purpose:** the two main QML approaches, and the hybrid loop.
**On-slide text**
- Title: Quantum machine learning
- **Approach 1 — Quantum kernels (QSVM)**
  - Encode data x as a quantum state |φ(x)⟩
  - The quantum chip estimates similarity K(x, x′) = |⟨φ(x)|φ(x′)⟩|²
  - A classical SVM does the rest (Havlíček et al., Nature 2019)
  - Footnote: We ran one: results on the next slide
- **Approach 2 — Variational circuits (VQC)** · tag: runs today
  - Gates have trainable angles θ, like network weights
  - The quantum chip runs the circuit; a classical optimizer updates θ
  - Shallow circuits make it practical on NISQ devices
  - Footnote: Try it: Qiskit Machine Learning, PennyLane
- Loop: Data x → Circuit U(θ) → Measure → Classical optimizer → Update θ, repeat
**Visuals:** `illustrations/hybrid_quantum_classical_loop.svg` · optional icons `bloch_sphere.svg`, `quantum_circuit_h_cnot_measure.svg`

## Slide 6 — A real quantum kernel, measured · S2 · 1:05
**Purpose:** the group's own experiment — evidence for "compared to what?".
**On-slide text**
- Title: A real quantum kernel, measured
- Kernel caption: Training kernel, sorted by class; the colour scale shows similarity. Dashed lines split the two classes.
- Setup: 120 points, two interleaved moons · 80 train / 40 test · 2-qubit ZZ feature map on a simulator, same tuning for every kernel
- Test accuracy · 40 held-out points:
  - Quantum kernel (ZZ) **90.0%**
  - Linear SVM **92.5%**
  - RBF SVM **97.5%**
- Takeaway: On classical data, the quantum kernel did not beat a tuned classical one. "Compared to what?" matters.
**Visuals:** `charts/quantum_kernel_matrix.png` · `charts/two_moons_dataset.png` · `charts/kernel_accuracy_comparison.png` (data in `data/`, reproducible with `code/quantum_kernel_experiment.py`)

## Slide 7 — HHL: exponential speedup, on paper · S2 · 0:55
**Purpose:** HHL's promise and its four conditions.
**On-slide text**
- Title: HHL: exponential speedup, on paper
- Classical · conjugate gradient: **O(N · s · κ)**
- Quantum · HHL, 2009: **O(log N · s²κ² / ε)**
- Legend: s = sparsity · κ = condition number · ε = precision
- Heading: Four conditions attached
  1. A must be sparse and well-conditioned (small κ)
  2. The vector b must load into a quantum state |b⟩ quickly
  3. The output is a state |x⟩, not the vector: reading all N entries costs O(N)
  4. Useful only when you need a summary value such as ⟨x|M|x⟩
**Visuals:** `charts/hhl_scaling.png` · optional `illustrations/sparse_matrix.svg`

## Slide 8 — Quantum optimization · S2 · 0:35
**Purpose:** QUBO / QAOA / annealing, with an honest reality check.
**On-slide text**
- Title: Quantum optimization
- **Many data tasks are QUBO problems** — Feature selection, clustering, scheduling and routing all explode combinatorially. *(tag: The problem)*
- **QAOA (Farhi et al., 2014)** — A hybrid, shallow-circuit algorithm designed for today's noisy hardware. *(tag: Gate-based)*
- **Quantum annealing (D-Wave)** — Special-purpose hardware with thousands of qubits, but not a general-purpose computer. *(tag: Special-purpose)*
- Reality check: no clear advantage yet over the best classical heuristics on real-world problems.
**Visuals:** `illustrations/maxcut_graph.svg` · `illustrations/qaoa_circuit.svg` · `illustrations/energy_landscape.svg` (one per point)

## Slide 9 — The catch · S3 · 0:10
**Purpose:** a single-statement pause before the bottlenecks.
**On-slide text**
- Eyebrow: The catch
- Statement: **Every speedup so far assumes the data is already inside the quantum computer.**
- Follow-up: So how does big data get in?
**Visual (optional, decorative):** `illustrations/bloch_sphere.svg`

## Slide 10 — Bottleneck 1: loading the data · S3 · 1:10
**Purpose:** the QRAM / data-loading problem, straight from the textbook. *(most important slide of Part 3)*
**On-slide text**
- Title: Bottleneck 1: loading the data
- Big data lives on disks as classical bits, while the algorithms assume it is already a quantum state.
- That needs QRAM: memory addressed by an index held in superposition.
- The textbook design uses O(N log N) quantum switches, roughly the hardware of the database itself.
- Loading N records alone costs about O(N), erasing a √N or log N speedup. No large, noise-tolerant QRAM exists yet.
- Quote-style callout: Nielsen & Chuang conclude that Grover's main use is likely solving hard search problems such as SAT or TSP, not searching classical databases.
- Figure caption: Quantum addressing for a 32-cell memory. Source: Nielsen & Chuang (2010), Fig. 6.9.
**Visual:** `book-figures/nc_fig6-9_qram_quantum_addressing.png` (portrait)

## Slide 11 — Bottleneck 2: the fine print · S3 · 0:55
**Purpose:** a four-step timeline showing speedup claims shrinking under fair comparison.
**On-slide text**
- Title: Bottleneck 2: the fine print
- **2009 · HHL** — Exponential speedup for linear systems, under strict conditions.
- **2015 · Scott Aaronson** — "Read the fine print" in Nature Physics lists the input, matrix and output caveats.
- **2016 · Kerenidis–Prakash** — A quantum recommendation system, hailed as an exponential QML speedup.
- **2018 · Ewin Tang** — An 18-year-old student finds a classical algorithm nearly as fast, given the same data access.
- Lesson: give the classical side the same assumptions about the data, and the quantum advantage often shrinks. Many QML algorithms were later "dequantized" the same way.
**Visual:** a timeline built from the four entries (no image file needed)

## Slide 12 — Hardware in 2026 · S4 · 1:10
**Purpose:** where machines stand, and why it is still far from big-data scale.
**On-slide text**
- Title: Hardware in 2026
- Intro: From NISQ (noisy, intermediate-scale) toward early fault tolerance: many noisy physical qubits plus error correction make one reliable logical qubit.
- Table (also in `data/hardware_2026.csv`):

| Company | Technology | Milestone |
|---|---|---|
| Google | Superconducting | Willow, 105 qubits (Dec 2024): errors drop as the code grows, below threshold |
| IBM | Superconducting | Nighthawk, 120 qubits; Starling target (2029): 200 logical qubits, 100M gates |
| IonQ, Quantinuum | Trapped ion | Highest two-qubit gate fidelities, reported up to 99.99% |
| Pasqal, QuEra | Neutral atom | Hundreds of qubits; May 2026: logical beats physical qubits on a differential-equation task |

- Footer line: Policy: NIST post-quantum cryptography standards (2024) · a US order targets a fault-tolerant machine by 2028 (June 2026)
- Image captions: "Illustration: superconducting chip" · "Trapped ions · Nielsen & Chuang, Fig. 7.7"
**Visuals:** `illustrations/superconducting_chip.svg` (label it as an illustration, not a photo) · `book-figures/nc_fig7-7_ion_trap_schematic.png` · optional `illustrations/dilution_refrigerator.svg`
**Note:** hardware figures change monthly — re-check 1–2 days before the talk. Real press photos (Google Willow, IBM Quantum System Two) may replace the illustration if credited.

## Slide 13 — Three takeaways · S4 · 0:40
**On-slide text**
- Title: Three takeaways
1. **A co-processor, not a replacement** — Quantum computers win only on narrow problem classes: simulation, factoring, some search and optimization.
2. **The bottleneck is data I/O** — For big data, the hard part is getting data in and out of the machine, not computing fast.
3. **Always ask "compared to what?"** — Follow post-quantum cryptography, try hybrid QML on a simulator, and read the assumptions behind any speedup claim.
**Visuals (optional icons):** `quantum_chip_icon.svg` (1), a database icon (2), a search/magnifier icon (3), `entangled_qubit_pair.svg`

## Slide 14 — Questions? + References · S4
**On-slide text**
- Eyebrow: Thank you · Title: **Questions?** · Line: Part 3 · Quantum × Big Data
- References: see `references.md` (all 9 entries go on the slide)
