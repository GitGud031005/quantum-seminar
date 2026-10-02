"""Reproduce every number used in Part 2 (Qiskit 2.x + qiskit-aer, numpy).
Run: pip install qiskit qiskit-aer numpy ; python run_experiments.py
Writes CSV files into ../data/"""
import csv, math, os
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(HERE, "..", "data")
sim = AerSimulator(seed_simulator=7)          # same seed as Part 3's histogram
def wcsv(name, header, rows):
    with open(os.path.join(D, name), "w", newline="") as f:
        w = csv.writer(f); w.writerow(header); w.writerows(rows)

def diffusion(qc, qs):
    qc.h(qs); qc.x(qs); qc.h(qs[-1]); qc.ccx(qs[0], qs[1], qs[-1]); qc.h(qs[-1]); qc.x(qs); qc.h(qs)

# ---- Bell state ----
bell = QuantumCircuit(2); bell.h(0); bell.cx(0, 1)
bc = sim.run(transpile(bell.measure_all(inplace=False), sim), shots=1024).result().get_counts()
wcsv("bell_counts.csv", ["state", "count"], [[k, bc.get(k, 0)] for k in ["00", "01", "10", "11"]])
print("Bell:", bc)

# ---- Grover 2 qubits, mark |11> ----
g2 = QuantumCircuit(2); g2.h([0, 1]); g2.cz(0, 1)
g2.h([0, 1]); g2.x([0, 1]); g2.cz(0, 1); g2.x([0, 1]); g2.h([0, 1])
c2 = sim.run(transpile(g2.measure_all(inplace=False), sim), shots=1024).result().get_counts()
wcsv("grover_counts_2q.csv", ["state", "count"], [[format(i, "02b"), c2.get(format(i, "02b"), 0)] for i in range(4)])
print("Grover 2q:", c2)
# amplitude table (big-endian labels |q1 q0>)
def amps(qc): return np.real(Statevector(qc).data)
s0 = QuantumCircuit(2); s0.h([0, 1]); s1 = s0.copy(); s1.cz(0, 1)
# note: the H-X-CZ-X-H diffusion used in the demo equals -(2|s><s|-I); we remove that global phase (-1 per diffusion)
# so the table matches the textbook "inversion about the mean". Global phase never changes measurement results.
rows = [[format(i, "02b"), round(amps(s0)[i], 3), round(amps(s1)[i], 3), round(-amps(g2)[i], 3) + 0.0] for i in range(4)]
wcsv("grover_2q_amplitudes.csv", ["state", "after_H", "after_oracle", "after_diffusion"], rows)

# ---- Grover 3 qubits, mark |101>, 2 iterations ----
def oracle101(qc): qc.x(1); qc.h(2); qc.ccx(0, 1, 2); qc.h(2); qc.x(1)
g3 = QuantumCircuit(3); g3.h([0, 1, 2]); stages = [("init", g3.copy())]
for k in (1, 2):
    oracle101(g3); stages.append((f"oracle_{k}", g3.copy())); diffusion(g3, [0, 1, 2]); stages.append((f"round_{k}", g3.copy()))
c3 = sim.run(transpile(g3.measure_all(inplace=False), sim), shots=1024).result().get_counts()
wcsv("grover_counts_3q.csv", ["state", "count", "share"], [[format(i, "03b"), c3.get(format(i, "03b"), 0), round(c3.get(format(i, "03b"), 0) / 1024, 4)] for i in range(8)])
print("Grover 3q:", c3)
def n_diffusions(name):                       # diffusions applied before this snapshot
    if name == "init": return 0
    k = int(name.split("_")[1]); return k if name.startswith("round") else k - 1
wcsv("grover_3q_amplitudes_by_step.csv", ["state"] + [n for n, _ in stages],
     [[format(i, "03b")] + [round((-1) ** n_diffusions(n) * amps(q)[i], 3) + 0.0 for n, q in stages] for i in range(8)])

# ---- Success probability vs iterations and optimal k ----
rows = []
for N in (4, 8, 16, 100, 10**6):
    th = math.asin(1 / math.sqrt(N)); k = math.floor(math.pi / (4 * th))
    rows.append([N, k, round(math.sin((2 * k + 1) * th) ** 2, 4)])
wcsv("grover_optimal_iterations.csv", ["N", "k_opt_floor(pi/(4theta))", "success_probability"], rows); print(rows)
th8 = math.asin(1 / math.sqrt(8))
wcsv("grover_success_vs_k_N8.csv", ["k", "success_probability"], [[k, round(math.sin((2 * k + 1) * th8) ** 2, 4)] for k in range(0, 9)])
rows = []
for e in (3, 10, 20, 30, 40, 50):
    N = 2 ** e; cl = N / 2; gr = math.pi / 4 * math.sqrt(N); rows.append([f"2^{e}", N, f"{cl:.4g}", f"{gr:.4g}", f"{cl/gr:.4g}"])
wcsv("grover_vs_classical_scaling.csv", ["N_label", "N", "classical_avg_N/2", "grover_pi/4*sqrtN", "ratio"], rows)
for r in rows: print(r)

# ---- Deutsch-Jozsa, n = 3 ----
def dj(kind):
    n = 3; qc = QuantumCircuit(n + 1); qc.x(n); qc.h(range(n + 1))
    if kind == "constant_1": qc.x(n)                      # f(x)=1 for all x
    if kind == "balanced_x0": qc.cx(0, n)                  # f(x)=x0
    if kind == "balanced_parity": [qc.cx(i, n) for i in range(n)]  # f(x)=x0^x1^x2
    qc.h(range(n))
    p = Statevector(qc).probabilities(list(range(n)))
    return round(float(p[0]), 4)
rows = [[k, dj(k)] for k in ("constant_0", "constant_1", "balanced_x0", "balanced_parity")]
wcsv("deutsch_jozsa_n3.csv", ["function", "P(measure_000)"], rows); print(rows)

# ---- Shor toy example: N=15, a=7 ----
N, a = 15, 7
wcsv("shor_powers_7_mod_15.csv", ["x", "7^x mod 15"], [[x, pow(a, x, N)] for x in range(16)])
r = next(x for x in range(1, N) if pow(a, x, N) == 1)
print("period", r, "gcds", math.gcd(a ** (r // 2) - 1, N), math.gcd(a ** (r // 2) + 1, N))
t = 8; Q = 2 ** t          # counting register (textbook: t ~ 2*log2(N))
probs = np.zeros(Q)
for v in set(pow(a, x, N) for x in range(Q)):                   # sum over outcomes of 2nd register
    xs = [x for x in range(Q) if pow(a, x, N) == v]
    vec = np.zeros(Q, complex); vec[xs] = 1 / math.sqrt(len(xs))
    ft = np.fft.ifft(vec) * math.sqrt(Q)                           # QFT convention e^{+2pi i xy/Q}
    probs += (len(xs) / Q) * np.abs(ft) ** 2
wcsv("shor_qft_distribution_N15_a7_t8.csv", ["y", "probability"], [[y, round(float(probs[y]), 6)] for y in range(Q)])
print("QFT peaks:", [(y, round(float(probs[y]), 3)) for y in range(Q) if probs[y] > 1e-6])

# ---- misc facts used on slides ----
print("2^53 =", f"{2**53:.3e}", "; seconds since Big Bang ~", f"{13.8e9*365.25*86400:.3e}")
print("DJ classical worst n=20:", 2 ** 19 + 1, " QFT gates n(n+1)/2 for n=8:", 8 * 9 // 2)
