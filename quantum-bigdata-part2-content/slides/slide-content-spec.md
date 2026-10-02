# Part 2 — Gates, Circuits & Algorithms: slide-by-slide content spec (light-math version)

**Talk:** group seminar "Quantum Computing" for a university Big Data course (HCMUT). Part 2 of 3, presented by **[Person 2]**.
**Audience:** Computer Science students, not physicists. They need the **ideas** and a few memorable numbers, not proofs.
**Comes after:** Part 1 (qubits, superposition, measurement, entanglement; ends on "three quantum resources: superposition, entanglement, interference").
**Comes before:** Part 3 (Quantum × Big Data). Part 3 opens by re-showing this part's 3-qubit Grover histogram (93%), so keep that number identical.
**Length:** 19 main slides, ~15 min without slide 10, ~16 min with it; plus 3 backup slides (A1–A3) shown only if someone asks about the math.
**Core message:** quantum gates are reversible moves; a circuit chains them; the speedup comes from interference (wrong answers cancel, the right one adds up), not from "trying all answers at once"; Grover makes search √N, Shor makes factoring easy and breaks today's public-key crypto.

**Math policy:** on the main slides, keep only the signature items listed below; everything else is words, pictures or a concrete example. Backup slides hold the formulas.
Signature items allowed on main slides: |0⟩ and |1⟩ · "H gives 50/50" · the Bell state (|00⟩ + |11⟩)/√2 · the interference example +0.5 / −0.5 / +1 · N versus √N (and "about 0.8 × √N rounds") · 7, 4, 13, 1 → period 4 → 15 = 3 × 5 · QFT peaks at 0, 64, 128, 192.

This file is content only. Text under **On-slide text** is final wording (keep numbers exactly). Visuals point to files in `/assets`; see `ASSET-MANIFEST.md`. Styling, layout and colour are up to the slide designer.

Sections: **S1** Gates (1–6) · **S2** Circuits and the key idea (7–10) · **S3** Grover (11–13) · **S4** Shor and cryptography (14–16) · **S5** Live demo and handoff (17–19) · **Backup** (A1–A3).

---

## Slide 1 — Cover · 0:15
**On-slide text**
- Eyebrow: Part 2 of 3
- Title: **Gates, Circuits & Algorithms**
- Subtitle: From qubits to real computation
- Presenter line: [Person 2] · Big Data seminar
**Visual (optional):** `circuits/grover_2q_demo_circuit.svg` as a faint background motif

## Slide 2 — Rule #1: every quantum gate can be undone · 0:45
**Purpose:** reversibility in plain words; measurement is the exception.
**On-slide text**
- Title: Rule #1: every quantum gate can be undone
- A quantum gate never loses information: n qubits in, n qubits out, and you can always run it backwards.
- A classical AND gate does lose it: output 0 could come from 00, 01 or 10.
- The one step you can't undo: **measurement**.
- Small footnote: (in math terms, gates are "unitary" matrices — see backup A1)
**Visual:** a two-column picture: "AND: 2 bits → 1 bit, can't go back" vs "quantum gate: n → n, always reversible" (simple table or drawing; no image file needed)

## Slide 3 — Flip the bit, flip the sign: X and Z · 0:50
**Purpose:** two basic moves; the "invisible" sign that matters later.
**On-slide text**
- Title: Two basic moves: flip the bit, flip the sign
- **X** = quantum NOT: |0⟩ ↔ |1⟩
- **Z** = sign flip: |1⟩ gets a minus sign, |0⟩ is untouched
- The minus sign is invisible if you measure right away — but it decides what cancels later (slide 9).
- (Y does both at once.)
**Visual:** `book-figures/nc_fig1-5_single_qubit_gates.png` (Source: Nielsen & Chuang (2010), Fig. 1.5)

## Slide 4 — Hadamard: the coin flip · 0:50
**On-slide text**
- Title: Hadamard (H): the quantum coin flip
- H turns a certain |0⟩ into a 50/50 superposition
- Apply H twice → back to |0⟩ for certain (a real coin flipped twice stays random!)
- Almost every algorithm starts with H on every qubit: all inputs at once, equal weight
**Visual:** `illustrations/bloch_sphere_hadamard.svg` (H moves the "north pole" |0⟩ to the equator)

## Slide 5 — CNOT: the gate that links two qubits · 0:50
**On-slide text**
- Title: CNOT: "if the first is 1, flip the second"
- 00 → 00 · 01 → 01 · 10 → 11 · 11 → 10
- Give it a 50/50 first qubit and the two qubits become **linked**: (|00⟩ + |11⟩)/√2
- Linked = entangled: measure one, you know the other
**Visual:** `book-figures/nc_fig1-6_cnot_and_classical_gates.png` (Source: N&C Fig. 1.6 — classical gates next to CNOT)

## Slide 6 — A tiny toolkit builds everything · 0:40
**On-slide text**
- Title: A small toolkit builds any quantum program
- Classical computers: NAND alone can build any circuit
- Quantum computers: a handful of gates (**H, CNOT** and two "phase" gates) can build any quantum program
- A quantum computer can also run any classical program (Toffoli gate = reversible AND)
- But "can build anything" ≠ "fast": good algorithms are the ones that stay small
**Visual (optional):** `circuits/grover_2q_demo_circuit.svg` captioned "a whole algorithm from just H, X and CZ"
**Backup:** exact gate set, matrices and the Solovay–Kitaev theorem on slide A1

## Slide 7 — Reading a circuit: two gates make entanglement · 1:00
**On-slide text**
- Title: Reading a circuit: two gates make entanglement
- One line = one qubit · time runs left → right · ● = CNOT control, ⊕ = target · meter = measurement
- H makes the first qubit 50/50 → CNOT links the second to it
- Result: (|00⟩ + |11⟩)/√2
- Measured 1,024 times: **00: 503 · 11: 521 · 01 and 10: never**
**Visuals:** `circuits/bell_state_circuit.svg` · `charts/bell_state_histogram.png`

## Slide 8 — Quantum parallelism… and the trap · 0:45
**On-slide text**
- Title: "Computing all inputs at once" — and the catch
- H on n qubits → all 2ⁿ inputs in one state (3 qubits → 8; 53 qubits → ≈ 9 × 10¹⁵)
- One run of a function touches every input
- **The catch:** measuring gives back **one** random answer. Reading them all would take ~2ⁿ runs — no gain.
- So parallelism alone is not the trick.
**Visual:** `circuits/hadamard_n3_uniform_superposition_circuit.svg`

## Slide 9 — Interference: the real trick · 0:50
**On-slide text**
- Title: Interference: make wrong answers cancel
- Quantum "weights" (amplitudes) can be negative, so they add up or cancel — like waves
- Example, 2 qubits, answer = 11:
  1. Start: every answer +0.5
  2. Mark the answer: 11 becomes −0.5
  3. Amplify: wrong answers → 0, 11 → +1 → **100% on 11**
- Not "try everything at once" — **engineered cancellation**
**Visual:** `charts/interference_2q_amplitude_stages.png`

## Slide 10 — Deutsch–Jozsa (optional) · 0:40
**On-slide text**
- Title: One question instead of half a million
- A hidden function is either "always the same" or "half 0, half 1". Which?
- Classical, to be certain: up to **524,289** checks (20-bit inputs)
- Quantum: **1** check — interference makes the answer come out as "all zeros" or "never all zeros"
- A teaching example, not a practical speedup (random classical checks are nearly always right)
**Visuals:** `charts/deutsch_jozsa_outcomes.png` · optional `book-figures/nc_fig1-20_deutsch_jozsa_circuit.png` (Source: N&C Fig. 1.20)

## Slide 11 — Grover: finding a needle without an index · 0:50
**On-slide text**
- Title: Grover's search: √N instead of N
- N items, no order, no index; one is special. Find it.
- Classical: check one by one → about **N/2** checks
- Grover: about **√N** steps (0.8 × √N)
- 1,000,000 items: **500,000** vs **≈ 785**
- Proven to be the best possible for this problem · a big speedup, but not exponential
**Visuals:** `charts/grover_vs_classical_scaling.png` · `book-figures/nc_fig6-1_grover_schematic.png` (Source: N&C Fig. 6.1)
**Note:** Part 3 covers real databases (indexes, loading data) — don't repeat it here.

## Slide 12 — How one Grover round works · 1:00
**On-slide text**
- Title: Each round: mark, then amplify
- **Mark (oracle):** a checker that recognises the answer and puts a minus sign on it — without telling you which one it is
- **Amplify (diffusion):** flip every amplitude around the average — the marked one jumps up, the others shrink
- 3 qubits, looking for 101 — chance of 101: **12.5% → 78% → 94.5%** after 0, 1, 2 rounds
**Visual:** `charts/grover_3q_amplitudes_by_step.png` (bars: 101 grows, the rest shrink)

## Slide 13 — Rotate… and stop in time · 0:45
**On-slide text**
- Title: Each round turns the state toward the answer
- Picture: an arrow starting almost flat, turning a fixed angle each round toward "the answer"
- Best stop: about 0.8 × √N rounds
- Too many rounds overshoot: for 8 items, **94.5% → 33% → 1%**
- You don't need to know the answer to know when to stop — only how many items there are
**Visuals:** `book-figures/nc_fig6-3_grover_geometric_rotation.png` (Source: N&C Fig. 6.3) · `charts/grover_success_vs_iterations_N8.png`

## Slide 14 — Shor, part 1: factoring = finding a rhythm · 0:50
**On-slide text**
- Title: Shor's idea: factoring becomes finding a repeating pattern
- Take powers of 7, keep the remainder after dividing by 15: **7, 4, 13, 1, 7, 4, 13, 1 …**
- It repeats every **4** steps
- That period hands you the factors: **15 = 3 × 5**
- For a 2,048-bit number, the pattern is astronomically long — classical computers can't find it
**Visual:** `charts/shor_period_7_mod_15.png`
**Backup:** the gcd step and the exact conditions on slide A3

## Slide 15 — Shor, part 2: a quantum "tuner" finds the period · 0:45
**On-slide text**
- Title: The quantum Fourier transform: a tuner for hidden rhythms
- Like a guitar tuner turning a sound into its pitch, the QFT turns a repeating pattern into sharp peaks
- Toy run (15 = 3 × 5): peaks at **0, 64, 128, 192** → spacing 64 → period **4**
- Classical best: grows almost exponentially with the number of digits · Shor: grows only polynomially → factoring becomes feasible on a big enough machine
**Visual:** `charts/shor_qft_peaks_N15_a7.png`
**Backup:** QFT gate count, complexity formulas and circuits on slide A3

## Slide 16 — Why Shor matters: the crypto clock · 1:00
**On-slide text**
- Title: Why it matters: RSA and ECC have an expiry date
- **Breaks:** RSA, elliptic-curve crypto, Diffie–Hellman — the public-key part of HTTPS and digital signatures
- **Survives:** AES and hash functions — just use longer keys (AES-256)
- How close? RSA-2048: ~20 million noisy qubits (2019 estimate) → **under 1 million, under a week** (2025 estimate). No machine is close yet.
- Fix: NIST post-quantum standards (2024): **ML-KEM, ML-DSA, SLH-DSA**
- **"Harvest now, decrypt later"** → start migrating long-lived data now
- Big Data angle: every TLS link, encrypted data lake and signed pipeline artifact is on the list
**Visual:** a simple "breaks / survives" two-column table or a 2019 → 2024 → 2025 timeline

## Slide 17 — Live demo 1: 2 qubits · 1:10
**On-slide text**
- Title: Demo 1 — find 11 among 4
- Steps: H on both → mark 11 → amplify → measure
- Theory: 1 round, 100%
- Result: **{'11': 1024}** — every shot correct
**Visuals:** `circuits/grover_2q_demo_circuit.svg` · `charts/grover_demo_2q_histogram.png`

## Slide 18 — Live demo 2: 3 qubits · 1:10
**On-slide text**
- Title: Demo 2 — find 101 among 8
- Theory: 2 rounds, **94.5%**
- Result: **954 of 1,024 shots = 93.2%** on 101; the other seven ≈ 1% each
- Why not exactly 94.5%? Random shots wobble a little (about ±0.7 points)
**Visuals:** `circuits/grover_3q_one_iteration_circuit.svg` · `charts/grover_demo_3q_histogram.png` (seed 7 — the same run Part 3 shows)

## Slide 19 — Recap & handoff · 0:40
**On-slide text**
- Title: What we built
- **Gates:** reversible moves; a small toolkit is enough
- **Circuits:** two gates make entanglement
- **Interference:** the real trick — wrong answers cancel
- **Grover:** √N search, the best possible
- **Shor:** easy factoring → post-quantum crypto
- Handoff: *What does this buy a big-data system, and what hardware exists today?* → Part 3

---

# Backup slides (show only if asked)

## A1 — The math behind the gates
- Gates are unitary: U†U = I → probability preserved, U⁻¹ = U† (N&C §2.1.6, p. 70)
- Matrices: X = [[0,1],[1,0]] · Z = [[1,0],[0,−1]] · H = (1/√2)[[1,1],[1,−1]] · CNOT: |c,t⟩ → |c, t⊕c⟩
- Standard universal set {H, S, T, CNOT} (S = T²) approximates any operation to any accuracy (N&C §4.5.3, p. 194–195)
- Solovay–Kitaev: single-qubit gates need only O(log^c(1/ε)) gates, c ≈ 2 (N&C p. 197, Appendix 3); arbitrary n-qubit operations can still need exponentially many gates
**Visual:** `book-figures/nc_fig4-2_common_single_qubit_gates.png` (Source: N&C Fig. 4.2)

## A2 — Grover by the numbers
- Start angle θ with sin θ = 1/√N; each round rotates by 2θ; P(after k rounds) = sin²((2k+1)θ)
- Best k ≈ (π/4)√N; table: N = 4 → k = 1, 100% · N = 8 → 2, 94.5% · N = 16 → 3, 96.1% · N = 100 → 7, 99.5%
- Diffusion = reflect about the mean: a → 2·mean − a (3 qubits: 0.354 → 0.884 → 0.972)
- Optimal: no quantum algorithm beats order √N (Bennett et al., 1997; N&C §6.6, p. 269)
- Note: the demo's H-X-CZ-X-H diffusion adds a global minus sign, which never changes measurements
**Visuals:** `book-figures/nc_fig6-2_grover_iteration_circuit.png` (Source: N&C Fig. 6.2) · `data/grover_optimal_iterations.csv`

## A3 — Shor and the QFT by the numbers
- f(x) = aˣ mod N has period r; if r is even and a^(r/2) ≢ −1 (mod N), gcd(a^(r/2) ± 1, N) gives factors; true for at least half of random a (N&C §5.3)
- 15: gcd(48, 15) = 3, gcd(50, 15) = 5
- QFT on n qubits: n(n+1)/2 gates (N&C p. 219); its output is in amplitudes, not readable directly
- Best classical (number field sieve): exp(O(n^(1/3) (log n)^(2/3))) · Shor: about O(n² log n log log n)
**Visuals:** `book-figures/nc_fig5-4_order_finding_circuit.png` (Source: N&C Fig. 5.4) · optional `book-figures/nc_fig5-1_qft_circuit.png` (Fig. 5.1)
