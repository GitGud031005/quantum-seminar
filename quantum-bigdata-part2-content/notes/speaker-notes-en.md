# Speaker notes — Part 2 (English, light-math version)
**19 slides · ~15 min (~16 min with slide 10) · Presenter: [Person 2]**

Meaning first, formulas only where they are the signature idea. Italic lines in brackets are cues, not to be read aloud. The math the audience might ask about is in the "If asked" lines and on backup slides A1–A3.

---

## Slide 1 — Cover · ~0:15
*[Take over after Person 1 ends on "three quantum resources: superposition, entanglement, interference".]*

"So now we know what a qubit is. The question is: what do you actually do with it? Person 1 gave us the clay; my job is to show how to shape it, with gates, circuits and algorithms. By the end you'll see two algorithms, Grover and Shor, that beat any classical computer on their problems, and I'll run one of them live."

## Slide 2 — Every gate can be undone · ~0:45
"Here's rule number one of quantum computing: every quantum gate can be undone. It never throws information away. Compare that with a classical AND gate: if I tell you the output was zero, you can't tell me the inputs, it could be zero-zero, zero-one or one-zero. That information is simply gone. A quantum gate always keeps it: as many qubits come out as went in, and you can run it backwards.

There's exactly one step you can't undo: measurement. Once you look, the superposition is gone. Keep that in mind; it's the reason the rest of this talk is tricky."

*If asked: "Mathematically, gates are unitary matrices; that's what guarantees both properties. It's on backup slide A1."*

## Slide 3 — Flip the bit, flip the sign · ~0:50
"The two basic moves on one qubit. X is the quantum NOT: it swaps zero and one. Z is stranger: it leaves zero alone but puts a minus sign on one. The bit doesn't change, only the sign.

Now, if you measure right after Z, you can't see that minus sign at all. So why care? Because inside a superposition, that minus sign decides what cancels out later. Remember this 'invisible minus sign'; it's the key to the whole speedup, and we'll see it at work in a few slides."

## Slide 4 — Hadamard: the coin flip · ~0:50
"The most important gate of all is the Hadamard, H. Think of it as a quantum coin flip: it takes a qubit that is definitely zero and turns it into a fifty-fifty superposition.

But here's the surprise. Flip a real coin twice and it's still random. Apply H twice and you get back zero, for certain. The two routes that lead to 'one' cancel each other out. That's our first glimpse of interference.

And almost every quantum algorithm starts the same way: H on every qubit, so you hold all possible inputs at once, with equal weight."

## Slide 5 — CNOT links two qubits · ~0:50
"Now a gate on two qubits: CNOT. The rule is one sentence: if the first qubit is one, flip the second. Zero-zero stays, zero-one stays, one-zero becomes one-one, one-one becomes one-zero.

The magic happens when the first qubit is a fifty-fifty coin. Then the second qubit gets tied to it: the pair is in 'both zero' and 'both one' at the same time. That's entanglement: measure one and you instantly know the other. One gate, and two qubits are linked."

## Slide 6 — A small toolkit builds everything · ~0:40
"You might think we need hundreds of different gates. We don't. In classical computing, the NAND gate alone can build any circuit. In quantum computing, a handful, H, CNOT and two small phase gates, can build any quantum program. And a quantum computer can run any classical program too, using a reversible version of AND called the Toffoli gate.

One honest note: 'can build anything' doesn't mean 'fast'. The art is finding algorithms that stay small. That's what Grover and Shor are."

*If asked about the exact gate set or the Solovay–Kitaev theorem: go to backup A1.*

## Slide 7 — Reading a circuit · ~1:00
"Let's read a circuit, because we'll see a few. Each line is one qubit, time runs left to right, boxes are gates, the dot and the circled plus are the two ends of a CNOT, and the meter is a measurement.

This one is only two gates: H makes the first qubit a coin flip, then CNOT ties the second qubit to it. We measured it 1,024 times: 503 times zero-zero, 521 times one-one, and never zero-one or one-zero. The two qubits always agree. That's the entangled state Person 1 described, now built from scratch."

## Slide 8 — Computing all inputs at once… and the catch · ~0:45
"Here's the idea everyone gets excited about. Put H on n qubits and you hold all 2-to-the-n inputs at once: 8 inputs with 3 qubits, about nine million billion with 53. Run a function once, and it touches every input.

Sounds like a free lunch. But here's the catch: when you measure, you get back one random answer. To read them all you'd need about 2-to-the-n runs, no better than a normal computer. So 'computing everything in parallel' is not where the speedup comes from."

## Slide 9 — Interference: the real trick · ~0:50
"The real trick is interference. Quantum weights, called amplitudes, can be negative, so they can add up or cancel out, just like waves in water.

Here's the smallest example, looking for eleven among four answers. Start: every answer has weight plus 0.5. Step two: we mark the answer by flipping its sign, so eleven is minus 0.5. Step three: an 'amplify' step that flips every weight around the average. The three wrong answers land exactly on zero, and eleven jumps to plus one.

So when we measure, we get eleven with 100% certainty. Not by trying everything, but by making the wrong answers cancel."

## Slide 10 — Deutsch–Jozsa (optional) · ~0:40
*[Skip if running long.]*

"A quick example of how powerful that is. You're given a hidden function that's either 'always the same answer' or 'half zeros, half ones'. To be sure classically with 20-bit inputs, you might need 524,289 checks. The quantum algorithm needs one: interference makes the answer come out as 'all zeros' for the first case and 'never all zeros' for the second.

To be fair, a few random classical checks are almost always right, so this is a teaching example, not a practical one. But it shows interference doing real work."

## Slide 11 — Grover: a needle without an index · ~0:50
"Now the algorithm closest to Big Data. You have N items, no order, no index, and one is special. Find it.

A normal computer checks them one by one: about half of them on average. Grover needs roughly the square root of N steps. For a million items, that's 500,000 checks against about 785.

And that's proven to be the best possible for this problem. It's a big speedup, but a square-root one, not exponential. Whether it helps real databases, which do have indexes, is exactly what Person 3 will look at."

## Slide 12 — How one round works · ~1:00
"Each Grover round has two steps. Step one, mark: a checker circuit recognises the answer, it knows the rules, and puts a minus sign on it, without ever telling us which item it is. That's the invisible minus sign from slide 3.

Step two, amplify: flip every weight around the average. The marked item was pulled far below average by its minus sign, so the flip throws it high above. Everyone else gets nudged down.

With three qubits, looking for one-zero-one: before any round the chance is 12.5%, after one round 78%, after two rounds 94.5%. The right answer rises; the rest fade."

## Slide 13 — Rotate, and stop in time · ~0:45
"A nice way to picture it: an arrow that starts almost flat, pointing at 'everything else', and each round turns it a fixed angle toward 'the answer'. After about 0.8 times the square root of N rounds, it points almost straight at the answer.

But don't keep turning. With eight items, two rounds give 94.5%, three rounds drop to 33%, four to about 1%: you've turned past the answer. And you don't need to know the answer to know when to stop; you only need to know how many items there are."

*If asked about the formula: backup A2.*

## Slide 14 — Shor: factoring = finding a rhythm · ~0:50
"The second algorithm is the famous one: Shor's algorithm for factoring. RSA encryption is safe because splitting a huge number into its prime factors is incredibly hard.

Shor's insight: turn factoring into finding a repeating pattern. Take powers of 7 and keep only the remainder after dividing by 15: you get 7, 4, 13, 1, and then it repeats: 7, 4, 13, 1. The rhythm is 4. With a little arithmetic, that rhythm hands you the factors: 15 is 3 times 5.

For a real 2,048-bit number, that pattern is astronomically long. No classical computer can find its rhythm. A quantum one can."

*If asked how the rhythm gives the factors: backup A3 (the gcd step).*

## Slide 15 — A quantum tuner · ~0:45
"How does it find the rhythm? With the quantum Fourier transform. Think of a guitar tuner: you play a note, and it tells you its pitch by turning a repeating sound wave into one clear frequency. The QFT does the same for our repeating pattern: it turns it into sharp peaks.

In our toy example, the peaks land at 0, 64, 128 and 192. They're 64 apart, which tells us the rhythm is 4.

The bottom line: the best classical method takes time that grows almost exponentially with the number of digits; Shor's grows only polynomially. That's the difference between 'impossible' and 'feasible', once a big enough machine exists."

## Slide 16 — Why Shor matters · ~1:00
"So what breaks? RSA, elliptic-curve cryptography and Diffie–Hellman: the public-key part of HTTPS and digital signatures. What survives? AES and hash functions; you just use longer keys.

How close is this? In 2019, breaking RSA-2048 was estimated to need about 20 million noisy qubits. In 2025 that estimate dropped to under a million, running for under a week. Nobody has that machine yet, but the target keeps getting closer.

The fix already exists: in 2024 NIST published three post-quantum standards. And there's a reason to act now: 'harvest now, decrypt later'. Data stolen today can be decrypted in the future. For Big Data, that means every TLS connection, every encrypted data lake and every signed pipeline artifact needs upgrading."

## Slide 17 — Demo 1 · ~1:10
*[Switch to the notebook.]*

"Let's see it run, on IBM's Qiskit simulator. Demo one: two qubits, four possible answers, the hidden one is eleven. Theory says one round is enough.

The code follows the recipe: H on both qubits, mark eleven, amplify, measure. *[Run.]* 1,024 shots, all 1,024 land on eleven. Exactly the plus-0.5, minus-0.5, plus-one story from the interference slide."

## Slide 18 — Demo 2 · ~1:10
"Now three qubits, eight answers, the hidden one is one-zero-one. Theory says two rounds and 94.5%.

*[Run.]* One bar towers over the rest: 954 out of 1,024, that's 93.2%, on one-zero-one. The other seven are around one percent each.

Why not exactly 94.5? Measurement is random, like flipping a coin a thousand times; you won't get exactly half heads. With 1,024 shots, results wobble by about seven-tenths of a percent."

*[If a live run gives a different count, say the number you see. The slide and Part 3 use the seed-7 run: 954.]*

## Slide 19 — Recap & handoff · ~0:40
"Quick recap. Gates are reversible moves, and a small toolkit builds anything. Two gates are enough for entanglement. The real trick is interference: wrong answers cancel. Grover searches in square-root time, the best possible. Shor makes factoring easy, which is why the world is moving to post-quantum crypto.

That's the theory. But what does it actually buy a big-data system, and what hardware exists today? [Person 3] will take it from here."

---

## Q&A — prepared answers

**What does "unitary" mean?** "It's the math condition that makes gates reversible and keeps total probability at 100%. Backup A1."

**Is Grover useful if the database has an index?** "Not directly. An index finds a record in about log N steps, far fewer than √N. Grover helps where there's no structure, like searching for a solution that satisfies a set of rules. Person 3 covers data loading."

**When will Shor break RSA?** "Not yet. The best 2025 estimate is under a million noisy qubits for under a week; today's machines have hundreds to a few thousand. That's why people migrate now."

**Why can't we read all the answers at the end?** "Measuring gives one outcome and destroys the rest. Reading everything would take as many runs as there are answers."

**Is Grover's speedup exponential?** "No, square-root. Shor's is the dramatic one."

**Does Grover break AES?** "It turns a 128-bit key search into about 2-to-the-64 steps, still very hard in practice; AES-256 stays safe. So: longer keys, not new algorithms."

**Why 93.2% and not 94.5%?** "94.5% is the exact chance; 93.2% is what we counted in 1,024 random shots."

**How do you know when to stop Grover without knowing the answer?** "The number of rounds depends only on how many items there are (and how many answers). Stop there, measure, and check the result with the rules."
