"""Draw the Part 2 circuits with Qiskit in black-and-white style (PNG + SVG)."""
import os
import matplotlib; matplotlib.use("Agg")
from qiskit import QuantumCircuit
HERE = os.path.dirname(os.path.abspath(__file__)); O = os.path.join(HERE, "..", "assets", "circuits")
def save(qc, name, scale=1.1):
    for ext in ("png", "svg"):
        fig = qc.draw("mpl", style="bw", scale=scale, fold=-1)
        fig.savefig(os.path.join(O, f"{name}.{ext}"), dpi=200 if ext == "png" else None, bbox_inches="tight", facecolor="white")
        matplotlib.pyplot.close(fig)
def diffusion(qc, qs):
    qc.h(qs); qc.x(qs); qc.h(qs[-1]); qc.ccx(qs[0], qs[1], qs[-1]); qc.h(qs[-1]); qc.x(qs); qc.h(qs)

bell = QuantumCircuit(2); bell.h(0); bell.cx(0, 1); bell.measure_all(); save(bell, "bell_state_circuit", 1.4)

g2 = QuantumCircuit(2); g2.h([0, 1]); g2.barrier(); g2.cz(0, 1); g2.barrier()
g2.h([0, 1]); g2.x([0, 1]); g2.cz(0, 1); g2.x([0, 1]); g2.h([0, 1]); g2.measure_all(); save(g2, "grover_2q_demo_circuit")

g3 = QuantumCircuit(3); g3.h([0, 1, 2]); g3.barrier()
g3.x(1); g3.h(2); g3.ccx(0, 1, 2); g3.h(2); g3.x(1); g3.barrier()
diffusion(g3, [0, 1, 2]); g3.barrier(); save(g3, "grover_3q_one_iteration_circuit", 0.9)

dj = QuantumCircuit(4, 3); dj.x(3); dj.h(range(4)); dj.barrier(); dj.cx(0, 3); dj.barrier(); dj.h(range(3)); dj.measure(range(3), range(3))
save(dj, "deutsch_jozsa_n3_balanced_circuit")

par = QuantumCircuit(3); par.h(range(3)); par.measure_all(); save(par, "hadamard_n3_uniform_superposition_circuit", 1.3)
print("circuits ok")
