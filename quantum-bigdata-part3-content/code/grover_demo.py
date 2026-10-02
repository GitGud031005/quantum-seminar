"""Grover demos used in the seminar (Qiskit 2.x + qiskit-aer).
Run: pip install qiskit qiskit-aer ; python grover_demo.py
Writes ../data/grover_counts_3q.csv (the histogram on slide 2)."""
import csv, os
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

HERE = os.path.dirname(os.path.abspath(__file__))
sim = AerSimulator(seed_simulator=7)

# 2 qubits, marked state |11>, 1 iteration -> ~100% '11'
qc = QuantumCircuit(2)
qc.h([0, 1]); qc.cz(0, 1)                                            # superposition + oracle
qc.h([0, 1]); qc.x([0, 1]); qc.cz(0, 1); qc.x([0, 1]); qc.h([0, 1])  # diffusion
qc.measure_all()
print("2-qubit:", sim.run(transpile(qc, sim), shots=1024).result().get_counts())

# 3 qubits, marked state |101>, 2 iterations -> ~93-95% '101' (theory 94.5%)
def diffusion(c, qs):
    c.h(qs); c.x(qs); c.h(qs[-1]); c.ccx(qs[0], qs[1], qs[-1]); c.h(qs[-1]); c.x(qs); c.h(qs)
g = QuantumCircuit(3); g.h([0, 1, 2])
for _ in range(2):
    g.x(1); g.h(2); g.ccx(0, 1, 2); g.h(2); g.x(1)   # oracle marks |101>
    diffusion(g, [0, 1, 2])
g.measure_all()
counts = sim.run(transpile(g, sim), shots=1024).result().get_counts()
print("3-qubit:", counts)
with open(os.path.join(HERE, "..", "data", "grover_counts_3q.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["state", "count", "probability"])
    for i in range(8):
        k = format(i, "03b"); w.writerow([k, counts.get(k, 0), round(counts.get(k, 0) / 1024, 4)])
