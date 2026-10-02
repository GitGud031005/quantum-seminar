"""Two-qubit demos for Part 1 (Qiskit 2.x + qiskit-aer).
Run: python bell_pair_demo.py   -> writes ../data/two_qubit_counts.csv (slide 9)

  product : H on both qubits -> |+>|+>, four outcomes ~25% each, the two qubits are independent
  bell    : H on qubit 0, then CNOT -> (|00> + |11>)/sqrt(2), only 00 and 11 ever appear
Qiskit prints bitstrings as q1q0; for these two states the order does not change the result.
"""
import csv, os
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

HERE = os.path.dirname(os.path.abspath(__file__))
sim = AerSimulator(seed_simulator=7)
SHOTS = 1024

prod = QuantumCircuit(2); prod.h([0, 1]); prod.measure_all()
bell = QuantumCircuit(2); bell.h(0); bell.cx(0, 1); bell.measure_all()
print(bell.draw())

rows = []
for name, qc in (("product", prod), ("bell", bell)):
    counts = sim.run(transpile(qc, sim), shots=SHOTS).result().get_counts()
    print(f"{name:8s}", counts)
    for k in ("00", "01", "10", "11"):
        rows.append([name, k, counts.get(k, 0), round(counts.get(k, 0) / SHOTS, 4)])

with open(os.path.join(HERE, "..", "data", "two_qubit_counts.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["experiment", "outcome", "count", "probability"]); w.writerows(rows)
