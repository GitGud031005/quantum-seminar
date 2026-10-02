"""The CHSH game (Bell test) for Part 1 (Qiskit 2.x + qiskit-aer).
Run: python chsh_game.py   -> writes ../data/chsh_results.csv (slide 10)

Rules: a referee sends a random bit x to Alice and y to Bob. They answer a and b without talking.
They win if a XOR b == x AND y  (answers equal, except when x = y = 1, then answers must differ).

Classical: try all 16 deterministic strategies (a0, a1, b0, b1). The best wins 3 of 4 cases = 75%.
Quantum: share the Bell pair (|00> + |11>)/sqrt(2). Each player measures along an angle that
depends on the question: Alice 0 or pi/2, Bob pi/4 or -pi/4 (angles on the Bloch sphere, x-z plane).
Theory: cos^2(pi/8) = 85.4% in every case.
"""
import csv, itertools, math, os
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

HERE = os.path.dirname(os.path.abspath(__file__))
sim = AerSimulator(seed_simulator=7)
SHOTS = 4096

# classical: exhaustive search over deterministic strategies
best = 0.0
for a0, a1, b0, b1 in itertools.product((0, 1), repeat=4):
    wins = sum(((a1 if x else a0) ^ (b1 if y else b0)) == (x & y) for x in (0, 1) for y in (0, 1))
    best = max(best, wins / 4)
print("classical best:", best)

# quantum: measure along axis at angle t in the x-z plane = rotate by Ry(-t), then measure Z
ALICE = {0: 0.0, 1: math.pi / 2}
BOB = {0: math.pi / 4, 1: -math.pi / 4}
per_case = {}
for x in (0, 1):
    for y in (0, 1):
        qc = QuantumCircuit(2)
        qc.h(0); qc.cx(0, 1)                      # Bell pair
        qc.ry(-ALICE[x], 0); qc.ry(-BOB[y], 1)    # choose measurement direction
        qc.measure_all()
        counts = sim.run(transpile(qc, sim), shots=SHOTS).result().get_counts()
        win = 0
        for bits, c in counts.items():            # bits = "b a" (qubit 1, qubit 0)
            b, a = int(bits[0]), int(bits[1])
            win += c if (a ^ b) == (x & y) else 0
        per_case[(x, y)] = win / SHOTS
        print(f"x={x} y={y} win={per_case[(x, y)]:.3f}")
quantum = sum(per_case.values()) / 4
theory = math.cos(math.pi / 8) ** 2
print(f"quantum simulated: {quantum:.4f}   theory: {theory:.4f}")

with open(os.path.join(HERE, "..", "data", "chsh_results.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["strategy", "win_rate", "note"])
    w.writerow(["classical_best", round(best, 4), "exhaustive over 16 deterministic strategies"])
    w.writerow(["quantum_simulated", round(quantum, 4), f"Bell pair, {SHOTS} shots per question pair, Aer seed 7"])
    w.writerow(["quantum_theory", round(theory, 4), "cos^2(pi/8), the maximum quantum mechanics allows"])
