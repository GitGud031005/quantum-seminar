"""Single-qubit demos for Part 1 (Qiskit 2.x + qiskit-aer).
Run: pip install qiskit qiskit-aer ; python single_qubit_demo.py
Writes ../data/single_qubit_counts.csv (slides 6 and 7).

Five experiments, 1,024 shots each:
  zero      : measure |0>                      -> always 0
  plus      : H|0>  = |+>, then measure        -> about 50/50
  minus     : H X|0> = |->, then measure       -> about 50/50 (same as |+>!)
  plus_H    : |+> then H again, then measure   -> always 0  (constructive interference)
  minus_H   : |-> then H again, then measure   -> always 1  (destructive interference on 0)
"""
import csv, os
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

HERE = os.path.dirname(os.path.abspath(__file__))
SHOTS = 1024
_seed = [7]

def run(qc):
    qc.measure_all()
    sim = AerSimulator(seed_simulator=_seed[0]); _seed[0] += 1   # seeds 7..11, one per experiment
    return sim.run(transpile(qc, sim), shots=SHOTS).result().get_counts()

experiments = {}
qc = QuantumCircuit(1);                        experiments["zero"] = run(qc)
qc = QuantumCircuit(1); qc.h(0);               experiments["plus"] = run(qc)
qc = QuantumCircuit(1); qc.x(0); qc.h(0);      experiments["minus"] = run(qc)
qc = QuantumCircuit(1); qc.h(0); qc.h(0);      experiments["plus_H"] = run(qc)
qc = QuantumCircuit(1); qc.x(0); qc.h(0); qc.h(0); experiments["minus_H"] = run(qc)

with open(os.path.join(HERE, "..", "data", "single_qubit_counts.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["experiment", "outcome", "count", "probability"])
    for name, counts in experiments.items():
        print(f"{name:8s}", counts)
        for k in ("0", "1"):
            w.writerow([name, k, counts.get(k, 0), round(counts.get(k, 0) / SHOTS, 4)])
