# Part 1 — Quantum Foundations: slide-by-slide content spec

**Talk:** group seminar "Quantum Computing" for a university Big Data course (HCMUT). Part 1 of 3, presented by **[Person 1]**.
**Audience:** students with no physics background. Part 1 opens the talk. Part 2 (gates, algorithms, Grover demo) and Part 3 (big data applications, hardware) build on it.
**Length:** 12 slides, about 13 minutes. **Slide language:** English.
**Core message:** a qubit can hold a mix of 0 and 1, and many qubits together hold a huge amount of information. Reading them gives back very little. Quantum computers work by using three effects (superposition, entanglement and interference) to steer toward the right answer before reading.

**Writing rule for this part:** no formulas on the slides. The only maths allowed is plain counting and percentages: doubling (2, 4, 8 … 2ⁿ), ½ + ½ = 1, ½ − ½ = 0, 50%, 75% and 85%. The notation |0⟩ and |1⟩ appears only as a name tag for the two basic states. Every hard idea has a picture next to it.

This file is content only. Text under **On-slide text** is final wording (keep the numbers exactly). Visuals point to files in `/assets`. See `ASSET-MANIFEST.md` for alt text. Styling, layout and colour are up to the slide designer. **Main** marks the visual that carries the idea. **Support** marks one that can go on the same slide or be dropped if space is short.

**Hand-offs:** gates (H, CNOT) are Part 2's topic. Slide 7 only previews H as "one extra step", and slide 9 shows what a Bell pair does, not the circuit that makes it (Part 2, slide 7, builds it with the same 503 / 521 run). Part 3 (slide 3) reuses the doubling chart from slide 2, so keep those numbers identical.
**Backup:** slide A1 at the end holds the formulas, shown only if someone asks.

Sections: **S1** Why quantum (slides 1–2) · **S2** One qubit (3–7) · **S3** Many qubits (8–11) · **S4** Hand-over (12).

---

## Words we use (for the designer and the speaker; not a slide)

| Word on the slides | What it means in plain language |
|---|---|
| **qubit** | the quantum version of a bit; it can be 0, 1 or a mix of both |
| **superposition** | that mix: 0 and 1 held at the same time, each with a weight |
| **weight** (physicists say *amplitude*) | how strongly 0 or 1 is present in the mix; it can be positive or negative |
| **plus / minus** | the two standard 50/50 mixes; same weights, different sign |
| **phase** | the sign (more generally, the direction) of the weights; invisible to a plain reading |
| **reading** (physicists say *measurement*) | asking the qubit "0 or 1?"; gives one random answer and destroys the mix |
| **interference** | weights adding up or cancelling, like waves |
| **entanglement** | qubits linked so strongly that they can only be described together |
| **no-cloning** | the rule that an unknown qubit cannot be copied |

---

## Slide 1 — Cover · S1 · 0:15
**Purpose:** open the seminar and Part 1.
**On-slide text**
- Eyebrow: Part 1 of 3
- Title: **Quantum Foundations**
- Subtitle: From bits to qubits: the ideas behind quantum computing
- Presenter line: [Person 1] · Big Data seminar
**Visual (optional, decorative):** `illustrations/bit_vs_qubit.svg`

## Slide 2 — Why quantum computing? · S1 · 1:30
**Purpose:** give two reasons ordinary computers are running out of room, then Feynman's idea.
**On-slide text**
- Title: Why quantum computing?
- **Limit 1: chips.** Transistors are now only a few dozen atoms wide. Any smaller and quantum effects break the circuit.
- **Limit 2: nature.** To imitate a quantum system, every extra particle *doubles* the numbers a normal computer must store.
  - 50 particles → about a million billion numbers
  - 300 particles → more numbers than there are atoms in the universe
- Quote: "…if you want to make a simulation of nature, you'd better make it quantum mechanical." (Richard Feynman, lecture 1981, published 1982)
- Takeaway: A quantum computer is a specialist for certain problems, not a faster laptop.
**Visuals**
- Main: `illustrations/chessboard_doubling.svg`. The rice-on-a-chessboard story makes "doubling" feel real.
- Support: `charts/qubit_amplitude_growth.png`. The same growth as a graph, for the numbers.

## Slide 3 — Bit vs qubit · S2 · 1:15
**Purpose:** say what a qubit is, using a picture instead of a formula.
**On-slide text**
- Title: Bit vs qubit
- **Bit:** a switch. It is either 0 or 1.
- **Qubit:** an arrow on a sphere. Pointing up means 0, pointing down means 1, and anywhere else means a mix of both.
- Each part of the mix has a **weight**. The bigger the weight, the more likely you read that value.
- Small print: physicists write the two basic states as |0⟩ and |1⟩. The brackets are just name tags.
- Table:

| | Bit | Qubit |
|---|---|---|
| What it holds | 0 or 1 | 0, 1 or a mix of both |
| Reading it | gives the stored value | gives 0 or 1 at random |
| After reading | unchanged | changed for good |
| Copying | easy | impossible |

**Visual**
- Main: `illustrations/bit_vs_qubit.svg`
- Support (optional): `book-figures/nc_fig1-2_qubit_as_atom_levels.png`. A real qubit: two energy levels of an atom (Source: Nielsen & Chuang (2010), Fig. 1.2).

## Slide 4 — Superposition · S2 · 1:15
**Purpose:** define superposition, introduce "plus" and "minus", and rule out the two common misunderstandings.
**On-slide text**
- Title: Superposition: 0 and 1 at the same time
- Definition: a qubit holding 0 and 1 at once, each with its own weight.
- Weights can be **positive or negative**. Ordinary chances (probabilities) can't be negative. This is what makes quantum different.
- Two key examples:
  - **plus:** equal weights, both positive
  - **minus:** equal weights, opposite signs
- Both read as 50% 0 and 50% 1, **yet they are different states**. Only the sign differs.
- ✗ Not a hidden coin that is secretly already 0 or 1.
- ✗ Not "trying every answer at once": reading gives back only one result.
**Visuals**
- Main: `illustrations/plus_minus_amplitudes.svg`. Shows plus and minus as two bar pairs of the same size, one bar flipped.
- Main (emphasis): `illustrations/hidden_coin_vs_qubit.svg`. The misunderstanding next to the right picture.

## Slide 5 — Picturing a qubit · S2 · 1:15
**Purpose:** show a picture of one qubit that makes the hidden "phase" visible.
**On-slide text**
- Title: Picturing a qubit: the Bloch sphere
- North pole = 0 · South pole = 1 · Equator = the 50/50 mixes, such as plus and minus
- **Height** → the chance of reading 0 or 1
- **Direction around** → the *phase*. A plain reading can't see it, but it changes what happens next.
- Plus and minus sit on opposite sides of the equator: same height, opposite direction.
- Line: Quantum gates simply rotate this arrow (Part 2).
- Footnote: This picture works for one qubit only.
**Visuals**
- Main: `illustrations/bloch_sphere_labeled.svg`
- Support (emphasis): `illustrations/phase_compass.svg`. Asking "0 or 1?" can't tell plus from minus, but asking "east or west?" can, so the phase is real information.

## Slide 6 — Reading a qubit · S2 · 1:30
**Purpose:** cover the most surprising rule, then show our own simulator run.
**On-slide text**
- Title: Reading a qubit: a one-way door
- **Random:** even if you know the qubit exactly, you only know the odds, never the single result.
- **Collapse:** after reading, the qubit *becomes* the answer. The mix is gone for good.
- **Small door:** n qubits hold 2ⁿ weights inside, but reading gives back only n bits.
- Chart caption: Our run, 1,024 runs each: state 0 → 0 every time · plus → 51% / 49% · minus → 51% / 49%. Plus and minus look identical.
- Line: That is why quantum programs are run thousands of times.
**Visuals**
- Main: `illustrations/measurement_collapse.svg`. The arrow snaps to a pole.
- Main (emphasis): `illustrations/big_store_small_door.svg`. A huge store with a tiny exit.
- Support: `charts/single_qubit_measurement.png` (data: `data/single_qubit_counts.csv`)
- Support (optional): `book-figures/nc_fig1-22_stern_gerlach.png`. A real reading: a beam of atoms splits into exactly two spots, never in between (Source: N&C Fig. 1.22).

## Slide 7 — Interference · S2 · 1:00
**Purpose:** show that the hidden sign matters, and plant the idea Part 2 builds on.
**On-slide text**
- Title: Interference: weights can cancel
- Weights behave like waves: **in step they add up, out of step they cancel.**
- Add one extra step (a gate called H) before reading. Now each result can be reached along two paths:
  - plus: both paths carry +½ → ½ + ½ = **1** → always 0
  - minus: one path +½, the other −½ → ½ − ½ = **0** → never 0, always 1
- Chart caption: Our run, 1,024 runs: 100% and 100%. The 50/50 became certain.
- Takeaway: Ordinary chances can only add up. Quantum weights can cancel. Algorithms use this to boost the right answer and cancel the wrong ones.
**Visuals**
- Main: `illustrations/water_waves.svg`. The everyday intuition.
- Main: `illustrations/interference_paths.svg`. The two paths adding or cancelling.
- Support: `charts/interference_result.png`

## Slide 8 — From one qubit to many · S3 · 0:45
**Purpose:** show where the doubling comes from, and prepare the idea of entanglement.
**On-slide text**
- Title: From one qubit to many
- 1 qubit → 2 combinations · 2 qubits → 4 · 3 qubits → 8 · n qubits → **2ⁿ**, each with its own weight
- This is the doubling from slide 2.
- **Independent qubits:** each can be described on its own. That is easy for a normal computer.
- **Entangled qubits:** only the whole group can be described. All 2ⁿ weights are needed.
- Takeaway: Entanglement is a big reason quantum computers are so hard to imitate.
**Visual**
- Main: `illustrations/combinations_grid.svg`

## Slide 9 — Entanglement · S3 · 1:15
**Purpose:** show what an entangled pair does and what "linked" means, with our run (the circuit that builds it comes in Part 2).
**On-slide text**
- Title: Entanglement: two qubits, one story
- The simplest **entangled pair** is called a "Bell pair". (Part 2 shows the two-step recipe that makes it.)
- Chart caption: Our run, 1,024 runs. Independent qubits: all four results about 25% each. Entangled pair: 00 49%, 11 51%, and 01 or 10 never.
- Read one qubit and the other always agrees, however far apart they are.
- Each qubit on its own is pure chance. The information lives in the **link** between them.
- Footnote: This cannot send messages faster than light. Each side sees only random bits until they compare notes.
**Visuals**
- Main: `illustrations/entangled_pair_distance.svg`. The pair far apart, always agreeing.
- Not on this slide: `illustrations/bell_pair_circuit.svg` (H + CNOT). Gates are Part 2's topic and Part 2 builds this exact circuit (slide 7, same 503 / 521 run), so keep the circuit for Q&A only.
- Support: `charts/two_qubit_histograms.png` (data: `data/two_qubit_counts.csv`)

## Slide 10 — Stronger than any ordinary link · S3 · 1:15
**Purpose:** answer "isn't that just two gloves in two boxes?" with a number.
**On-slide text**
- Title: Stronger than any ordinary link
- Einstein (1935) asked whether the pair simply carries answers fixed in advance, like two gloves in two boxes.
- Bell's game: Alice and Bob each get question A or B at random and answer 0 or 1, with no talking. They win if the answers match, unless both got B; then the answers must differ.
  - **Best plan agreed in advance: 75%**
  - **With entangled qubits: 85%** (our simulation 85.1%; theory 85.4%)
- Line: Real experiments confirm it. They won the Nobel Prize in Physics in 2022 (Aspect, Clauser, Zeilinger).
- Takeaway: Entanglement is not answers fixed in advance. It is a genuinely new resource.
**Visuals**
- Main: `illustrations/gloves_in_boxes.svg`. The ordinary explanation, which turns out to be wrong.
- Main: `illustrations/chsh_game.svg`. The rules of the game.
- Support: `charts/chsh_win_rates.png` (data: `data/chsh_results.csv`)

## Slide 11 — No-cloning · S3 · 1:00
**Purpose:** cover the rule that matters most to data people.
**On-slide text**
- Title: You cannot copy a qubit
- **Rule:** no machine can copy an unknown qubit.
- **Why, in short:** a machine that copies 0 and 1 correctly turns a mix into a linked (entangled) pair, not two copies. Reading first doesn't help: one reading gives one bit and destroys the mix.
- Bits are fine, which is why ordinary data can be copied freely.
- **Good news, security:** an eavesdropper can't copy the signals, so she must read them, and reading leaves errors (quantum key distribution).
- **Bad news, data systems:** no backup, replication or caching of quantum data.
**Visuals**
- Main: `illustrations/no_cloning.svg`
- Main (emphasis): `illustrations/eavesdropper_qkd.svg`. The same rule turned into a security feature.

## Slide 12 — Three quantum resources · S4 · 0:45
**Purpose:** summarise Part 1 and hand over to Part 2.
**On-slide text**
- Title: Three quantum resources
  1. **Superposition:** opens up 2ⁿ possibilities
  2. **Entanglement:** links qubits into one system
  3. **Interference:** pushes the odds toward the right answer
- Two rules to remember: reading gives only one bit per qubit · qubits cannot be copied
- Hand-over: Next, the gates and circuits that put these resources to work.
**Visual**
- Main: `illustrations/three_resources.svg`

---

# Backup slide (show only if asked; formulas allowed here)

## A1 — The math behind Part 1
- A qubit: |ψ⟩ = α|0⟩ + β|1⟩, where the weights α, β are complex numbers with |α|² + |β|² = 1; reading gives 0 with chance |α|² and 1 with chance |β|² (N&C §1.2, p. 13; §2.2, p. 84)
- plus = (|0⟩ + |1⟩)/√2 · minus = (|0⟩ − |1⟩)/√2
- Bloch sphere: |ψ⟩ = cos(θ/2)|0⟩ + e^(iφ) sin(θ/2)|1⟩ — θ is the height (latitude), φ the direction around (phase) (N&C p. 15)
- n qubits: 2ⁿ complex weights; independent qubits need only 2 per qubit
- Bell pair: (|00⟩ + |11⟩)/√2
- Bell's game (CHSH): best fixed plan 75%; entangled pair cos²(π/8) ≈ 85.4%, the most quantum physics allows (N&C §2.6, p. 111–117)
- No-cloning in one line: a copier that maps |0⟩|0⟩ → |0⟩|0⟩ and |1⟩|0⟩ → |1⟩|1⟩ must, by linearity, send α|0⟩ + β|1⟩ to α|00⟩ + β|11⟩ (an entangled pair), not to the two copies (α|0⟩ + β|1⟩)(α|0⟩ + β|1⟩) (N&C Box 12.1, p. 532; Wootters & Zurek 1982)
**Visuals:** `book-figures/nc_fig1-3_bloch_sphere.png` (Fig. 1.3) · `book-figures/nc_fig1-11_copying_circuits.png` (Fig. 1.11: the bit-copying circuit turns a|0⟩ + b|1⟩ into a|00⟩ + b|11⟩) · `book-figures/nc_fig2-4_bell_experiment_setup.png` (Fig. 2.4)
