# Speaker notes — English (as spoken on the slides)

20 slides · ~10–11 minutes + Q&A · Presenter: Phúc. Italic text in parentheses is a cue for the speaker, not read aloud. Replace [Person 1] / [Person 2] with real names.

## Slide 1 — Quantum × Big Data (cover) · ~0:10
"Thanks, [Person 2]. You just saw Grover find the answer without scanning every item. For a Big Data class, the natural question is: what does that buy us with real, large datasets? In the next ten minutes, I'll cover four places where quantum computing meets data, the two bottlenecks holding them back, and where hardware really stands in 2026."

## Slide 2 — From the demo to real data · ~0:25
"This is the result of the demo we just ran. Three qubits give us eight possible strings, from 000 to 111, so eight records. We ran the circuit 1,024 times; each run did two Grover rounds and then one measurement, and we counted how often each string came up. About 93% of all measurements landed on the hidden record, 101, while the other seven stayed close to zero. The machine found the answer without opening the records one by one.

But eight records is tiny. The real question is: with a table of a trillion rows, what does quantum computing actually buy us?"

*(If asked why 93% and not the theoretical 94.5%: measurement is random, like flipping a coin 100 times and not getting exactly 50 heads. The two rounds set the success probability; the 1,024 runs only count the results.)*

## Slide 3 — Why quantum meets big data · ~0:30
"The appeal starts with one number. To describe the state of n qubits, you need 2 to the n amplitudes, and every extra qubit doubles that count. The vertical axis uses a log scale, so 2 to the n shows up as a straight, steady line.

Just 50 qubits already need about 10 to the 15 numbers to describe, the scale of a large data warehouse. 300 qubits need more than the number of atoms in the observable universe, the dashed line on the chart.

But the power is not about 'storing many values'. The power is that these amplitudes can be negative, so wrong answers can cancel each other out while the right answer adds up. And when you measure, you still only read 50 bits. So this is potential, not a result yet."

## Slide 4 — Data task → quantum tool · ~0:25
"Most data-analysis work comes down to four kinds of math. Finding one record in a table: that's Grover's algorithm. Classification and machine learning: quantum kernels and variational circuits. Regression, PCA and solving systems of equations: the HHL algorithm. And scheduling, feature selection and clustering, meaning picking the best option out of countless options: QAOA and quantum annealing.

I'll go through these rows in order, then explain why none of them has replaced Spark or Hadoop yet."

## Slide 5 — Quantum search over a database · ~0:55
"The figure on the left is from Nielsen and Chuang's textbook. The CPU is separate from memory, and it can only fetch data with a LOAD instruction, one cell at a time. For an unsorted table, a classical machine has to check half the table on average, while Grover only needs about the square root of the number of records.

Take a table with a trillion records. A classical machine checks about 500 billion records on average. Grover needs only about 790 thousand rounds. That sounds very impressive.

But real databases always have an index, meaning the data is already sorted. Then you search like looking up a word in a dictionary: open in the middle, throw away half, and repeat. About 40 halvings get you to the exact record, faster than Grover. So Grover only helps with queries that no index can serve. And there's a hardware question here that I'll come back to shortly."

## Slide 6 — Quantum machine learning · ~0:40
"The second direction, and the most talked about, is quantum machine learning. The general idea is to map data into the state space of qubits, which has a huge number of dimensions, so the groups in the data become easier to separate. There are two main approaches.

The first is the quantum kernel. Here the quantum computer does exactly one job: it measures how similar two data points are, giving a number between 0 and 1. All these numbers are then handed to a familiar classical algorithm, the SVM, which draws the boundary between groups. IBM's research team published this approach in Nature in 2019.

The second is the variational circuit. You can picture it as a neural network whose 'weights' are the rotation angles of quantum gates. These circuits are short, so they run on today's noisy quantum hardware, and you can try them yourself with Qiskit or PennyLane.

The next slide shows how the second approach is trained, and after that, the results when our group actually ran the first one."

## Slide 7 — The hybrid loop · ~0:15
"This is how a variational circuit gets trained. It's a loop with four steps. First, we feed the data into a quantum circuit with rotation angles θ. Once the circuit runs, we measure the result. Next, a regular computer compares that result with the correct answer, sees how wrong it is, and decides which way to adjust the angles θ to reduce the error. Then we run the circuit again with the new angles, and repeat until it's good enough.

Think of tuning an old radio: turn the knob a little, listen, and if it's still fuzzy, turn it further in the direction that sounds clearer. The radio is the quantum circuit; the person listening and deciding how to turn is the classical computer.

It's called hybrid because the two machines split the work: the quantum computer only runs short circuits, and the classical computer does the 'learning'. That's why today's noisy quantum hardware can still be useful. Our group ran the first approach, the quantum kernel, ourselves. Here's what happened."

## Slide 8 — A real quantum kernel, measured · ~1:05
"To see what a quantum kernel can really do, our group ran a small experiment ourselves.

The data in the middle is the two-moons dataset: 120 points in two groups, shaped like two crescent moons hooked into each other. It's a classic test, because no straight line can split these two groups. We used 80 points to train the model and held back 40 points it had never seen for testing.

The picture on the left is the kernel matrix, the table of similarities between every pair of points computed by the quantum circuit. The points are sorted by group, and the two dashed lines mark where the group changes. With a good kernel, pairs from the same group would be very similar, so the two diagonal blocks would light up clearly, like a checkerboard. Here the blocks are only faintly different, which means the two groups aren't clearly separated in the quantum space.

The results on the right confirm it. On the 40 test points, the quantum kernel got 90% right. Meanwhile a linear SVM, the simplest method, got 92.5%, and the popular classical RBF kernel got 97.5%. All three used the same data, and every kernel that needed tuning got the same tuning.

So on this classical data, the quantum kernel did not win. That doesn't mean the idea failed. It means that whenever we hear a claim about quantum advantage, we should always ask: compared to what?"

*(If asked whether the test was fair: "The dataset is small and it ran on a simulator, so it's an illustration. But all three models used the same data split and the same amount of tuning. Without tuning, the quantum kernel only got 77.5%.")*

## Slide 9 — HHL: exponential speedup, on paper · ~0:30
"The third row of the table is regression, PCA and solving systems of equations. They sound different, but underneath they all come down to one problem: solving Ax = b, like working out the price of apples and oranges from two shopping trips. With big data, this system has millions of unknowns.

In 2009, Harrow, Hassidim and Lloyd proposed a quantum algorithm for it, called HHL. The two formulas on the slide compare the cost. A good classical method, conjugate gradient, costs about N times s times κ, growing with the number of unknowns N. HHL costs about log N times s squared times κ squared over ε, growing only with log N. That's an exponential speedup, which is why HHL got the Big Data world so excited.

The chart shows the difference. The white line is the classical cost, rising steadily with N. The blue line is HHL, nearly flat even as N goes up to a trillion.

But look at the dashed line. HHL doesn't return a list of N numbers; it returns a quantum state. To read every number out, you have to measure again and again, and the cost goes back to about N, the same as classical. That's why the title says 'on paper': the exponential speedup only holds on paper, and it comes with four conditions on the next slide."

*(If asked about the symbols: "s is the number of nonzero entries per row of the matrix, κ measures how sensitive the solution is, and ε is the precision you want.")*

## Slide 10 — Four conditions attached · ~0:30
"For HHL to really be fast, the problem has to meet four conditions.

First, the matrix A has to be sparse and stable. Sparse means each equation only involves a few unknowns, not all of them. Stable means κ is small: if the input shifts a little, the solution only shifts a little. When κ is large, for example when two data columns are almost identical, HHL's cost grows very fast.

Second, the vector b has to load into the quantum computer quickly. If b is a large data table, just loading it costs about N steps. This condition will come back in the bottleneck section.

Third, the output is a quantum state, not a list of solutions. Each measurement gives only one random result, so reading all N numbers means running and measuring about N times or more.

Fourth, and because of that, HHL only helps when you need one summary number from the solution, not the whole solution. For example, in a power grid you might only need the total power loss, not the voltage at every node.

Real data problems usually break at least one of these four conditions, so HHL's advantage is very hard to keep in practice."

## Slide 11 — Quantum optimization · ~0:35
"The last row of the table is optimization. Many data tasks look like this: pick the best option out of countless options. Say you have 50 data columns and want the best subset for prediction: each column is either in or out, so there are 2 to the 50 choices, far too many to try. Scheduling, clustering and routing are the same. Many of these problems can be written in a standard form called QUBO: each variable is yes or no, and you look for the combination with the best score.

There are two quantum approaches. The first is QAOA, proposed by Farhi and colleagues in 2014. It's a hybrid algorithm, like the loop on slide 7: a short quantum circuit alternating two kinds of layers, with a classical computer tuning the parameters. Because the circuit is short, it's designed for today's noisy hardware.

The second is quantum annealing, which D-Wave has built into real machines with thousands of qubits. Picture the problem as hilly terrain, where the best answer is the deepest valley. The machine lets the quantum system slowly 'settle' toward that valley. But these machines only do optimization; they're not general-purpose quantum computers.

The bottom line is the honest part: so far, there's no clear evidence that either approach beats the best classical methods on real-world problems. And that brings us to the key point of this whole section."

## Slide 12 — The catch · ~0:10
*(Pause so the audience can read the statement before you speak.)*

"Every speedup I've just shown, from Grover and quantum machine learning to HHL and optimization, quietly assumes one thing: the data is already inside the quantum computer, in a form the machine can process all at once. But real big data sits on hard drives as ordinary bits. A trillion records don't just appear inside qubits. So the question is: how does big data get into a quantum computer?"

## Slide 13 — Bottleneck 1: loading the data · ~0:50
"For Grover to query many records at once, the quantum computer needs a special kind of memory called QRAM. With normal memory, you give an address, say cell 5, and get back exactly the record in cell 5. With QRAM, the address is in superposition, pointing to many cells at once, and the memory returns the data from all of those cells at once.

The figure on the right is from Nielsen and Chuang's textbook and shows how to build QRAM for a 32-cell memory. Picture a building with 32 rooms. From the entrance, the corridor keeps splitting in two, and at each fork there's a quantum switch controlled by one qubit of the address: a 0 turns left, a 1 turns right. When the address is in superposition, the signal turns both ways at once, so it reaches every room.

The problem is the number of switches. The tree needs about as many forks as the memory has cells. The book estimates about N log N quantum switches, roughly as much hardware as storing the database itself. For a trillion records, that's about a trillion quantum switches, and all of them must stay in a quantum state without noise. Meanwhile, the best chips today have around a hundred qubits.

Without QRAM, we'd have to load the records into the machine one by one, which costs about N steps. And N steps is already as long as a classical machine takes to scan the whole table, so the speedup from Grover or HHL disappears. So far, nobody has built a large, noise-tolerant QRAM."

## Slide 14 — Nielsen & Chuang's conclusion · ~0:20
"This isn't just our group's opinion. The two authors of the standard quantum computing textbook reach the same conclusion. In their view, Grover's main use is probably not searching classical databases, but finding solutions to hard problems like SAT or the travelling salesman problem.

The reason is that for those problems, you don't need to load a huge data table into the machine. You only need a small circuit that checks whether a candidate solution follows the rules, and all the candidates already live in the qubits' state space. That avoids the bottleneck on the previous slide.

So that's bottleneck number one. Bottleneck number two is about how speedup claims get reported."

*(If asked what SAT is: "SAT is the problem of assigning true or false to variables so that every given rule is satisfied. Checking one assignment is fast, but the number of possible assignments is enormous.")*

## Slide 15 — Bottleneck 2: the fine print · ~0:55
"The second bottleneck is the conditions papers tend to leave in the 'fine print'. This slide tells that story through four dates.

In 2009, HHL arrived with a promise of exponential speedup, but with very strict conditions, as we just saw on slide 10.

In 2015, computer scientist Scott Aaronson wrote a piece in Nature Physics literally titled 'Read the fine print'. He listed the conditions on input data, on the matrix and on the output that quantum machine learning algorithms quietly rely on.

In 2016, Kerenidis and Prakash published a quantum algorithm for recommendation systems, the Netflix-style kind that suggests movies to you. It was seen as a flagship example of exponential speedup in quantum machine learning.

In 2018, Ewin Tang, an 18-year-old student, set out to prove that classical computers couldn't do the same. Instead, she found a classical algorithm that was almost as fast, as long as the classical machine gets the same kind of data access the quantum algorithm assumed. After that, many other quantum machine learning algorithms were 'dequantized' in the same way.

The lesson on the bottom line: give the classical side the same assumptions about the data, and the quantum advantage often shrinks a lot. That's exactly what we saw in our own kernel experiment: in a fair comparison, quantum no longer wins."

## Slide 16 — Hardware in 2026 · ~0:50
"So where does the hardware stand today? For years we've been in what's called the NISQ era: machines with tens to hundreds of qubits, but very noisy, so they can only run short circuits. The turning point now is the move from physical qubits to logical qubits. That means combining many error-prone physical qubits and using error correction to create one reliable qubit.

The table sums up four main hardware directions. Google uses superconducting technology. In December 2024, its 105-qubit Willow chip showed for the first time that as the error-correcting code gets bigger, errors actually go down, something nobody had achieved before. IBM also uses superconducting qubits. Its Nighthawk chip has 120 qubits, and IBM aims to have its Starling machine in 2029, with 200 logical qubits running 100 million gates. IonQ and Quantinuum use trapped ions. This approach stands out for accuracy, with two-qubit gates reaching up to 99.99%. Pasqal and QuEra use neutral atoms, with hundreds of qubits. In May 2026, logical qubits on this platform outperformed physical qubits on a differential-equation task.

But let's read these numbers correctly: 200 logical qubits in 2029 is still very far from the hardware needed to process terabyte-scale data, which brings us right back to the QRAM bottleneck.

The last line is about policy. In 2024, NIST standardized post-quantum cryptography, to prepare for the day quantum computers become strong enough to break RSA. And a US executive order in June 2026 set a target of a fault-tolerant quantum computer by 2028."

*(Re-check these figures a day or two before the talk; this field changes quickly.)*

## Slide 17 — Hardware in 2026 (two technologies) · ~0:20
"This slide shows what the two leading technologies look like.

On the left is an illustration of a superconducting chip, the approach Google and IBM follow. The dots are qubits arranged in a grid on the chip, and the lines are for control and readout. The chip has to be cooled to near absolute zero, colder than outer space, for the qubits to keep their quantum state. This is an illustration, not a photo of a real chip.

On the right is a diagram from Nielsen and Chuang's textbook showing a trapped-ion quantum computer, the approach of IonQ and Quantinuum. Each qubit here is an atom that has lost an electron, an ion. The four small dots in the middle are the four ions, held floating in a vacuum by the electric field of the cylindrical electrodes around them. Lasers aimed at each ion carry out the quantum gates, and light sensors read the results.

The two approaches are very different, but they share one challenge: keeping the qubits free from noise long enough to finish the computation."

## Slide 18 — Three takeaways · ~0:40
"To wrap up my part, there are three things I hope you'll remember.

First, a quantum computer is a co-processor, not a replacement for regular computers. It won't replace your laptop or your Spark cluster. It's only strong on a few narrow classes of problems: simulating quantum systems like molecules, factoring numbers, and some search and optimization problems.

Second, for big data, the bottleneck isn't computing speed; it's getting data into the machine and getting results out. As we saw with QRAM and with HHL, both directions cost about N steps, and that problem is still unsolved.

Third, always ask 'compared to what?'. Whenever you read news like 'quantum computer a million times faster', check which classical method it was compared with, and under what assumptions about the data. As our kernel experiment and Ewin Tang's story show, in a fair comparison the advantage often shrinks a lot. The most practical things to do right now are to follow post-quantum cryptography, and if you're curious, try hybrid quantum machine learning on a simulator yourself."

## Slide 19 — References · ~0:05
"The main source for this part is Nielsen and Chuang's textbook, along with the original papers on HHL, quantum kernels, QAOA and Ewin Tang's result."

## Slide 20 — Thank you / Questions? · Q&A
"Thank you for listening. Our group is happy to take your questions."

*(Question routing: basic concepts → [Person 1]; algorithms and the demo → [Person 2]; applications and hardware → Phúc.)*

**Prepared answers**

*When can big data use quantum computers?* "It needs large QRAM and fault-tolerant machines. Current roadmaps aim for a few hundred logical qubits around 2030, still very far from terabyte-scale data. Small but hard problems, like molecule simulation or optimization, will benefit first."

*Is quantum machine learning better than deep learning?* "There's no practical advantage on classical data yet. Our own experiment gave the quantum kernel 90% versus 97.5% for a classical kernel, and many other results have been dequantized. Research now focuses on data that's already quantum, for example from quantum sensors or chemistry simulations."

*Why not just store the data directly in qubits?* "Qubits lose their state within microseconds to milliseconds because of noise. And the no-cloning theorem means you can't back up a quantum state the way you back up ordinary bits."

*Can Grover break AES encryption?* "Grover only gives a square-root speedup, so using a key twice as long, like AES-256, is enough to stay safe. The real threat is Shor's algorithm against RSA and elliptic-curve cryptography."

*What does "quantum-inspired" mean?* "It means classical algorithms that borrow ideas from quantum algorithms, like Ewin Tang's result. They run today on ordinary computers."

*How do you know when to stop Grover without knowing the answer?* "You don't need the answer. The number of rounds depends only on the size of the search space and the number of solutions. You run that many rounds, measure once, and check the result against the rules, which is fast."

---

Before the talk: replace [Person 1] / [Person 2] with real names · re-check the hardware figures on slide 16 a day or two before the talk.
