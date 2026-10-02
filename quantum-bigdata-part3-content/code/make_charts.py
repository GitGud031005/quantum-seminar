"""Neutral (unstyled) charts for Part 3 -- white background, black/grey only, so any slide
design can restyle them. Reads ../data/*.csv. Run after grover_demo.py and quantum_kernel_experiment.py."""
import csv, os
import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(HERE, "..", "data"); O = os.path.join(HERE, "..", "assets", "charts")
plt.rcParams.update({"font.size": 16, "axes.spines.top": False, "axes.spines.right": False})
INK, MID, LIGHT = "#111111", "#777777", "#cccccc"
def save(fig, name): fig.tight_layout(); fig.savefig(os.path.join(O, name + ".png"), dpi=200, facecolor="white"); fig.savefig(os.path.join(O, name + ".svg"), facecolor="white"); plt.close(fig)

# 1 Grover histogram (slide 2)
rows = list(csv.DictReader(open(os.path.join(D, "grover_counts_3q.csv"))))
fig, ax = plt.subplots(figsize=(9, 5))
ax.bar([r["state"] for r in rows], [float(r["probability"]) for r in rows], color=[INK if r["state"] == "101" else LIGHT for r in rows])
ax.set_ylim(0, 1); ax.set_yticks([0, .25, .5, .75, 1]); ax.set_yticklabels(["0%", "25%", "50%", "75%", "100%"])
ax.set_xlabel("measured state"); ax.set_ylabel("share of 1,024 shots"); ax.set_title("3-qubit Grover, 2 iterations: 93% on hidden record 101")
save(fig, "grover_histogram_3q")

# 2 Amplitude growth 2^n (slide 3)
n = np.arange(0, 321); fig, ax = plt.subplots(figsize=(9, 4.5))
ax.plot(n, n * np.log10(2), color=INK, lw=3); ax.axhline(80, color=MID, ls="--", lw=1.5)
ax.text(5, 83, "atoms in observable universe ≈ 10⁸⁰", color=MID, fontsize=14)
for q in (50, 300): ax.plot(q, q * np.log10(2), "o", ms=11, color=INK)
ax.annotate("50 qubits → 10¹⁵", (50, 15), (70, 12), fontsize=14); ax.annotate("300 qubits → 10⁹⁰", (300, 90.3), (175, 97), fontsize=14)
ax.set_xlim(0, 330); ax.set_ylim(0, 110); ax.set_yticks([0, 50, 100]); ax.set_yticklabels(["10⁰", "10⁵⁰", "10¹⁰⁰"])
ax.set_xlabel("number of qubits n"); ax.set_ylabel("amplitudes 2ⁿ")
save(fig, "qubit_amplitude_growth")

# 3 HHL scaling (slide 7)
N = np.logspace(2, 12, 200); fig, ax = plt.subplots(figsize=(10, 4.5))
ax.loglog(N, N, color=INK, lw=3, label="classical (conjugate gradient) ~ N")
ax.loglog(N, np.log2(N), color=MID, lw=3, label="HHL ~ log N")
ax.loglog(N, N * 1.6, color=INK, lw=2, ls=(0, (6, 5)), label="HHL + reading out all of x ~ N")
ax.set_xlabel("matrix size N"); ax.set_ylabel("cost (arbitrary units)"); ax.legend(frameon=False, fontsize=14, loc="upper left"); ax.minorticks_off()
save(fig, "hhl_scaling")

# 4 Quantum kernel matrix (slide 6)
Km = np.loadtxt(os.path.join(D, "quantum_kernel_matrix_train.csv"), delimiter=","); nA = 40
fig, ax = plt.subplots(figsize=(7.4, 6.4)); im = ax.imshow(Km, cmap="Greys", vmin=0, vmax=1)
ax.axhline(nA - .5, color=INK, lw=1.5, ls="--"); ax.axvline(nA - .5, color=INK, lw=1.5, ls="--")
ax.set_xticks([]); ax.set_yticks([]); ax.set_title("Quantum kernel, 80 training points\nsorted by class (dashed = class split)", fontsize=15); fig.colorbar(im, ax=ax, fraction=.046, label="similarity |⟨φ(x)|φ(x′)⟩|²")
save(fig, "quantum_kernel_matrix")

# 5 Two-moons dataset (slide 6)
pts = list(csv.DictReader(open(os.path.join(D, "two_moons.csv"))))
fig, ax = plt.subplots(figsize=(7, 4.5))
for lab, m, fc in (("0", "o", "white"), ("1", "s", INK)):
    P = [(float(p["x1_scaled"]), float(p["x2_scaled"])) for p in pts if p["label"] == lab]
    ax.scatter(*zip(*P), marker=m, s=45, facecolors=fc, edgecolors=INK, label=f"class {lab}")
ax.set_xticks([]); ax.set_yticks([]); ax.legend(frameon=False); ax.set_title("Two-moons dataset (120 points)")
save(fig, "two_moons_dataset")

# 6 Kernel accuracy bars (slide 6)
acc = [r for r in csv.DictReader(open(os.path.join(D, "kernel_accuracy.csv"))) if "untuned" not in r["model"]]
labels = ["Quantum kernel (ZZ)", "Linear SVM", "RBF SVM"]; vals = [float(r["test_accuracy"]) * 100 for r in acc]
fig, ax = plt.subplots(figsize=(9, 3.8)); b = ax.barh(labels[::-1], vals[::-1], color=[INK, LIGHT, MID][::-1])
for rect, v in zip(b, vals[::-1]): ax.text(v + .5, rect.get_y() + rect.get_height() / 2, f"{v:.1f}%", va="center", fontsize=15)
ax.set_xlim(0, 105); ax.set_xlabel("test accuracy on 40 held-out points (%)")
save(fig, "kernel_accuracy_comparison")
print("charts ok")
