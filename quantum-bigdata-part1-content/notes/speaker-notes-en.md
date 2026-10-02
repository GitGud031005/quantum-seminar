# Speaker notes — English (as spoken on the slides)

One block per slide, in order. Placeholders to replace: [Person 2]. Part 3 is presented by Phúc.
Cues in *italics* say which picture to point at. The words "weight" and "reading" are used on purpose instead of "amplitude" and "measurement". Say the technical word once if you like, then stay with the plain one.

## Slide 1 — Cover

Hello everyone. Our group's topic today is quantum computing, and what it could mean for big data. I'll start with the foundations: what a qubit is, and the three ideas that make quantum computers different. Then [Person 2] will show how those ideas become algorithms, with a live demo, and Phúc will connect everything to big data and today's hardware.

## Slide 2 — Why quantum computing?

Why do we need a new kind of computer at all? There are two reasons.

The first is chips. For decades computers got faster because transistors got smaller. Today a transistor is only a few dozen atoms wide. Go much smaller and quantum effects start to break the circuit, so we can't keep shrinking forever.

The second reason matters more. Some problems are simply too big for normal computers, and the clearest example is nature itself. *(Point to the chessboard.)* You may know the old story: one grain of rice on the first square of a chessboard, two on the next, then four, then eight. It starts small, but the last square alone holds about nine billion billion grains. Imitating a quantum system on a normal computer works the same way. Every extra particle doubles the numbers you must store. Fifty particles already need about a million billion numbers. Three hundred need more numbers than there are atoms in the universe. Yet nature "runs" these systems every second, inside every molecule.

So in 1981, in a lecture published in 1982, Richard Feynman suggested a simple idea: if nature is quantum, build the computer out of quantum parts. One warning from the start: a quantum computer is a specialist for certain problems, not a faster laptop.

## Slide 3 — Bit vs qubit

*(Point to the switch.)* A normal bit is like a light switch: it is 0 or it is 1.

*(Point to the sphere.)* A qubit is better pictured as an arrow on a ball. Pointing straight up means 0. Pointing straight down means 1. And the arrow can point anywhere in between, which means the qubit is a mix of 0 and 1.

Each part of the mix has a weight. The bigger the weight of 0, the more likely you'll read 0. You'll see physicists write the two basic states as |0⟩ and |1⟩. Don't worry about the brackets; they are just name tags.

The table sums it up. A qubit can hold more than a bit, but reading it is random, reading it changes it, and you can't copy it. Those differences shape everything that follows.

## Slide 4 — Superposition

This mix of 0 and 1 is called superposition. Here is the surprising part: the weights can be positive *or negative*. Ordinary chances can never be negative. You can't have minus thirty percent chance of rain. Quantum weights can, and that one detail is what makes quantum computing work.

*(Point to the bars.)* The two most important examples are called plus and minus. Plus has equal weights on 0 and 1, both positive. Minus has the same equal weights, but one of them is negative. When you read either one, you get 0 half the time and 1 half the time. So are they the same? No. They are different states, and in two slides we'll prove it.

*(Point to the coin and the sphere.)* Two common misunderstandings. First, superposition is not a coin hidden under a cup that is secretly already heads or tails. If it were, plus and minus would be exactly the same thing. Second, a quantum computer does not "try every answer at once" and hand you all of them. When you read it, you get one answer, and everything else is gone.

## Slide 5 — Picturing a qubit

*(Point to the sphere.)* This picture is called the Bloch sphere, and it's the arrow from slide 3 drawn properly. The north pole is 0, the south pole is 1, and the equator holds all the fifty-fifty mixes, including plus and minus.

The height of the arrow tells you the odds. The closer to the north pole, the more likely you'll read 0. The direction around the sphere is called the phase. That is where the plus-or-minus sign lives. Plus and minus sit at the same height, on opposite sides of the equator.

*(Point to the compass.)* Here's the key point. If you only ask "0 or 1?", you are only checking the height, and plus and minus both give fifty-fifty. They look identical. But if you could ask "east or west?", plus would always say east and minus would always say west. So the phase is real information; a plain reading just can't see it. In Part 2 you'll see that quantum gates are simply ways of rotating this arrow. One limitation: this picture only works for a single qubit.

## Slide 6 — Reading a qubit

Reading, or measuring, a qubit is the strangest rule, so I'll make three points.

First, the result is random. Even if I know the qubit perfectly, I can only tell you the odds, never the single result. That's not a flaw in our equipment; it's how nature behaves.

Second, collapse. *(Point to the arrow snapping.)* Once you read the qubit, it becomes the answer. If you read plus and get 0, the qubit is now just 0. The mix, including the sign, is gone for good.

Third, and most important for computing. *(Point to the store and the door.)* A group of n qubits holds 2-to-the-n weights inside, a huge store, but reading it gives back only n bits. It's a huge warehouse with a tiny door.

Here is our own simulator run, 1,024 runs for each state. State 0 gives 0 every time. Plus gives about fifty-one, forty-nine. And minus gives the same picture. By reading directly, you cannot tell plus from minus. And because one run gives one random answer, quantum programs are always run thousands of times.

## Slide 7 — Interference

Now the trick that makes everything work. *(Point to the waves.)* Think of two water waves meeting. If they are in step, they build a bigger wave. If they are out of step, they cancel and the water goes flat. Quantum weights do exactly this.

*(Point to the two paths.)* We add one extra step, a gate called H, just before reading. After this step, each result can be reached along two paths, and each path carries a weight of one half. For plus, both halves are positive: one half plus one half is one, so we always read 0. For minus, one half is negative: one half minus one half is zero, so we never read 0 and always read 1.

Our run confirms it: one hundred percent and one hundred percent. The fifty-fifty became certain. So plus and minus really were different, and the hidden sign was real.

This is the heart of quantum computing. Ordinary chances can only add up. Quantum weights can cancel. Quantum algorithms arrange the paths so that wrong answers cancel and the right answer grows, and [Person 2] will show you exactly that.

## Slide 8 — From one qubit to many

*(Point to the grid.)* One qubit has two possible results. Two qubits have four: 00, 01, 10 and 11. Three qubits have eight. Every extra qubit doubles the list, and each combination has its own weight. This is exactly the doubling from the chessboard on slide 2.

Now an important difference. If the qubits are independent, you can describe each one on its own, and a normal computer handles that easily. But qubits can also be linked so tightly that you can only describe the whole group at once. Then you really need all 2-to-the-n weights. That link is called entanglement, and it's a big reason quantum computers are so hard to imitate.

## Slide 9 — Entanglement

The simplest entangled pair is called a Bell pair. [Person 2] will show you the two-step recipe that makes one; for now, let's look at what it does.

Look at our run. On the left, two independent qubits: all four results show up about a quarter of the time. On the right, the entangled pair: only 00 and 11, never 01 or 10.

*(Point to Alice and Bob far apart.)* So if I read my qubit and get 0, yours will also give 0, even if you've carried it a thousand kilometres away. And here's the strange part: each qubit on its own is completely random. Neither qubit "has" the answer. The information lives in the link between them.

And no, this can't send messages faster than light. Each side just sees random 0s and 1s. The match only shows up when they compare their lists by phone or email.

## Slide 10 — Stronger than any ordinary link

A fair objection, and Einstein raised it in 1935. *(Point to the gloves.)* Put a pair of gloves in two boxes and ship them apart. Open one, see a left glove, and you instantly know the other is the right one. Nothing mysterious: the answer was fixed from the start. Maybe entangled particles are just like that.

In 1964 John Bell found a way to test this, and the simplest version is a game. *(Point to the game.)* Alice and Bob sit in separate rooms. A referee gives each of them question A or question B at random, and each answers 0 or 1, without talking. They win if their answers match, except when both got question B; then their answers must differ.

They can agree on any plan beforehand. That's the gloves idea: answers fixed in advance. And it turns out the best any such plan can do is win 75% of the time, because the four rules contradict each other. With an entangled pair, they win about 85% of the time. Our simulation gave 85.1%; the theory says 85.4%.

Real experiments have confirmed this many times, and they won the 2022 Nobel Prize in Physics. So entanglement is not answers fixed in advance. It's a genuinely new resource.

## Slide 11 — No-cloning

The last rule, and the one data people care about most: you cannot copy an unknown qubit.

*(Point to the copier.)* Why? Imagine a machine that copies 0 and 1 perfectly. Now feed it a mix. The rules of quantum physics force that same machine to produce a linked, entangled pair, not two copies of the mix. This was proved in 1982 and is called the no-cloning theorem. And you can't cheat by reading the qubit first and rebuilding it, because one reading gives only one bit and destroys the mix. Normal bits are just 0s and 1s, which such a machine copies fine; that's why ordinary data can be copied as often as we like.

*(Point to Alice, Bob and Eve.)* This rule has a good side. If a spy, Eve, taps a line carrying quantum signals, she can't copy them quietly. She has to read them, and reading disturbs them. Alice and Bob compare a small sample, see the errors, and know someone was listening. That's the basis of quantum key distribution.

And it has a bad side for big data: no backups, no replication and no caching of quantum data. Phúc will come back to what that means.

## Slide 12 — Three quantum resources

To sum up Part 1: quantum computing rests on three resources. Superposition opens up 2-to-the-n possibilities. Entanglement links qubits into one system that quickly grows too big for a normal computer to imitate. Interference pushes the odds toward the right answer.

And two rules we have to live with: reading gives back only one bit per qubit, and qubits can't be copied.

So the real question is how to use these resources to compute something useful. [Person 2] will show you the gates and circuits that do it.
