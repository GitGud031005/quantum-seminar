# Quantum Computing × Big Data: group seminar

Content, speaker notes and slide decks for a three-part group seminar on Quantum Computing, given in the Big Data course at HCMUT. Slides are in English; each part also has Vietnamese speaker notes for rehearsal.

| Part | Topic | Input folder | Deck |
|---|---|---|---|
| 1 | Quantum foundations: qubits, superposition, interference, entanglement, no-cloning | [`quantum-bigdata-part1-content`](quantum-bigdata-part1-content) | `part1-slides.html` / `.pdf` |
| 2 | Gates, circuits and algorithms: Hadamard, CNOT, Grover, Shor | [`quantum-bigdata-part2-content`](quantum-bigdata-part2-content) | `part2-slides.html` / `.pdf` |
| 3 | Quantum × Big Data: where quantum helps data work, the two bottlenecks, hardware in 2026 | [`quantum-bigdata-part3-content`](quantum-bigdata-part3-content) | `part3-slides.html` / `.pdf` |

## How this repo works

Each part is built in three steps:

```
input folder  ──►  slide skill  ──►  partN-slides.html  ──►  Ctrl+P  ──►  partN-slides.pdf
(content, notes,   (educational-dark-design)   (one self-contained file)
 assets, data)
```

The **input folder** is the source of truth for facts, wording, numbers, figures and speaker notes. The **skill** decides how that content becomes slides. The deck is generated output and can be rebuilt from the input at any time.

```
quantum-seminar/
├── quantum-bigdata-part1-content/      input + output for Part 1
├── quantum-bigdata-part2-content/      input + output for Part 2
├── quantum-bigdata-part3-content/      input + output for Part 3
├── quantum-bigdata-part-template/      empty skeleton for a new part (see below)
├── .claude/skills/educational-dark-design/   the slide skill (design system + deck builder)
└── material/                           reference book (local only, not committed)
```

## The standard input folder

Every part uses the same layout. `quantum-bigdata-part-template/` is the blank version with placeholders; copy it to `quantum-bigdata-part{N}-content` to start a new part.

```
quantum-bigdata-part{N}-content/
├── README.md                    what is inside, constraints for the slide builder, how to regenerate data
├── slides/slide-content-spec.md START HERE: slides in order with purpose, final on-slide text, assets, timing
├── notes/speaker-notes-en.md    what the presenter says, one block per slide, with timing and Q&A answers
├── notes/speaker-notes-vi.md    Vietnamese rehearsal version of the same notes
├── ASSET-MANIFEST.md            every image: slide, source or credit, alt text
├── references.md                full reference list
├── assets/
│   ├── book-figures/            figures cropped from Nielsen & Chuang (cite on the slide)
│   ├── charts/                  PNG + SVG, generated from data/
│   └── illustrations/           original vector drawings (PNG + SVG); Part 2 also has circuits/
├── data/                        raw numbers behind charts and demos (CSV)
├── code/                        scripts that regenerate data/ and assets/
├── plan/seminar-group-plan-vi.md  the whole group's plan, identical in every part, for context
├── part{N}-slides.html          generated deck
└── part{N}-slides.pdf           PDF saved from the deck
```

Conventions that keep the parts consistent:

- **Folder name** `quantum-bigdata-part{N}-content`; deck files `part{N}-slides.html` and `part{N}-slides.pdf`.
- **No design in the input.** No colours, fonts or layouts. The skill owns the look.
- **Numbers are final in the spec.** The slide builder must not change or invent figures. Unknown numbers are listed, not guessed.
- **Every figure has a manifest row.** Book figures keep their citation visible on the slide.
- **Notes are keyed to slide numbers.** If the generated deck ends up with a different slide list than the plan, you re-sync the notes by hand afterwards (see step 5 below).

## Building a deck with the skill

### 1. Install the skill

Nothing to install. The skill ships in the repo at `.claude/skills/educational-dark-design/`, and Claude Code loads it when opened in the repo root. After `git clone` or `git pull`, open Claude Code in `quantum-seminar/` (restart it if it was already running) and type `/`: `educational-dark-design` should be listed.

To use the same skill in other projects, copy `.claude/skills/educational-dark-design/` to that project's `.claude/skills/`, or to `~/.claude/skills/` for every project. The skill's own README (in its folder, in Vietnamese) covers installing it in the Claude app and editing the design system.

### 2. Ask for the deck

Point the skill at one input folder and state the constraints. A prompt that works well:

> Use the educational-dark-design skill to build Part 3 from `quantum-bigdata-part3-content`. Read its README, `slides/slide-content-spec.md`, `notes/speaker-notes-en.md`, `ASSET-MANIFEST.md` and `assets/`. Slides in English (`lang="en"`), about 11 minutes. Keep every number and wording from the spec, keep the book-figure citations visible, and do not add facts. Show me the outline table first. Save the result as `quantum-bigdata-part3-content/part3-slides.html`.

### 3. Review the outline: the deck will usually grow

The skill's workflow is: gather content, **write an outline table (slide number, layout, one-sentence message), show it to you**, build, validate, deliver. Expect the outline to have **more slides than the spec**. That is by design and usually helps the presentation:

- The skill enforces one message per slide, titles of at most 30 characters, 3–5 bullets of at most 10 words, and a hard rule that overfull content is split into two slides, never shrunk.
- It adds structure slides the spec does not list: contents, section dividers, and a blue "focus" slide for the one idea the audience must remember.
- It never uses the same layout twice in a row, which breaks long runs of text into a figure, a table, a diagram.

In this repo the effect is visible: the Part 3 spec has 14 slides and the finished deck has 20.

When the outline arrives, check it against the clock instead of just approving it:

- **Time per slide.** Divide the talk length by the slide count. Part 3 is 20 slides in about 11 minutes, roughly 33 seconds a slide; dividers and focus slides are shorter, so content slides get more. If the total runs over, ask the skill to merge or drop low-value slides rather than rushing.
- **Key slides stay whole.** Each part's README names its key slides (for example QRAM loading and the kernel experiment in Part 3). Do not let the split scatter their argument over too many slides.
- **Hand-offs.** Part 1 ends on the three quantum resources and Part 2 opens from them; Part 2's 3-qubit demo result is re-shown in Part 3. Expansion must not change those words or numbers.
- **Optional and backup slides.** Say whether they stay in the main deck or go after it.

Reply with edits to the table (merge slides 7 and 8, drop the divider before the last section, and so on) and the skill builds from the approved version. The built deck can still differ from the table in small ways, which is why step 5 exists.

### 4. Validate

The skill runs `scripts/check_deck.py --render`, which checks colours, fonts, layout rules, text overflow and text touching decoration, and writes a contact sheet. Look at the contact sheet yourself; the validator does not judge whether a slide reads well.

### 5. Sync the notes to the final deck yourself

**The generated deck may not match the plan.** The skill decides the final slide list, so slide numbers, splits and extra slides in the output can differ from `slide-content-spec.md` and from the notes. Do not expect the notes to line up automatically.

After you approve and export the deck, update `notes/speaker-notes-en.md` and `notes/speaker-notes-vi.md` yourself: renumber the blocks, move text to follow any split slides, and add or trim timings so there is one block per final slide. Leave the spec as the record of the original plan unless you want it to match too.

In this repo, Part 3's notes have been synced to its 20-slide deck while its spec still shows the original 14. Parts 1 and 2 notes still follow their original spec numbering and have not been synced to their final decks.

### 6. Present or export

Open the `.html` in a browser.

| Key | Action |
|---|---|
| → / Space, ← | next / previous slide |
| Home / End | first / last slide |
| F | fullscreen |
| O | overview grid |
| P | print / save as PDF |
| `#7` in the URL | open slide 7 directly |

The deck is one self-contained HTML file, but its web fonts load from Google Fonts, so it needs internet. **For offline presenting, save a PDF:**

1. Open the deck in Chrome or Edge and press **Ctrl+P** (or **P** in the deck).
2. Destination: **Save as PDF**.
3. Margins: **None**.
4. Tick **Background graphics**. Without it the navy background disappears.
5. Save as `part{N}-slides.pdf` in the part's folder.

The skill also has `scripts/export_pdf.py`, which needs `pip install playwright pillow` and `playwright install chromium`. Ctrl+P is enough for normal use.

## Starting a new part

1. Copy `quantum-bigdata-part-template` to `quantum-bigdata-part{N}-content`.
2. Fill in `slides/slide-content-spec.md` first, then the notes, assets, `ASSET-MANIFEST.md` and `references.md`.
3. Generate data and charts with the scripts in `code/` so every number can be re-run.
4. Follow "Building a deck with the skill" above.

## Reference material

`material/` holds the course textbook, *Quantum Computation and Quantum Information* (Nielsen & Chuang, 10th anniversary ed.). The PDF is not committed to this repo. Put your own copy in that folder. Figures cropped from it appear in the decks for classroom use with the citation shown on the slide.

## Regenerating data and charts

Each input folder's README lists the exact commands. In short:

```bash
pip install qiskit qiskit-aer numpy matplotlib scikit-learn
cd quantum-bigdata-part3-content/code
python grover_demo.py
python quantum_kernel_experiment.py
python make_charts.py
```

Tested with Qiskit 2.x and qiskit-aer 0.17.
