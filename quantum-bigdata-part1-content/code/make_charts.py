"""Neutral (unstyled) charts for Part 1 -- white background, black/grey only, so any slide
design can restyle them. Reads ../data/*.csv. Run after the three demo scripts."""
import csv, os
import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(HERE, "..", "data"); O = os.path.join(HERE, "..", "assets", "charts")
plt.rcParams.update({"font.size": 16, "axes.spines.top": False, "axes.spines.right": False})
INK, MID, LIGHT = "#111111", "#777777", "#cccccc"
def save(fig, name): fig.tight_layout(); fig.savefig(os.path.join(O, name + ".png"), dpi=200, facecolor="white"); fig.savefig(os.path.join(O, name + ".svg"), facecolor="white"); plt.close(fig)
def load(name): return list(csv.DictReader(open(os.path.join(D, name))))
def pct_axis(ax): ax.set_ylim(0, 1.08); ax.set_yticks([0, .5, 1]); ax.set_yticklabels(["0%", "50%", "100%"])

# 1 Amplitude growth 2^n (slide 2)
n = np.arange(0, 321); fig, ax = plt.subplots(figsize=(9, 4.5))
ax.plot(n, n * np.log10(2), color=INK, lw=3); ax.axhline(80, color=MID, ls="--", lw=1.5)
ax.text(5, 83, "atoms in observable universe ≈ 10⁸⁰", color=MID, fontsize=14)
for q in (50, 300): ax.plot(q, q * np.log10(2), "o", ms=11, color=INK)
ax.annotate("50 qubits → about 10¹⁵ numbers", (50, 15), (62, 10), fontsize=14); ax.annotate("300 qubits → about 10⁹⁰", (300, 90.3), (150, 97), fontsize=14)
ax.set_xlim(0, 330); ax.set_ylim(0, 110); ax.set_yticks([0, 50, 100]); ax.set_yticklabels(["10⁰", "10⁵⁰", "10¹⁰⁰"])
ax.set_xlabel("number of qubits"); ax.set_ylabel("numbers needed")
save(fig, "qubit_amplitude_growth")

sq = {}
for r in load("single_qubit_counts.csv"): sq.setdefault(r["experiment"], {})[r["outcome"]] = float(r["probability"])

def pair_panel(ax, exp, title):
    p = sq[exp]; b = ax.bar(["0", "1"], [p["0"], p["1"]], color=[INK, MID], width=.6)
    for rect, v in zip(b, (p["0"], p["1"])): ax.text(rect.get_x() + rect.get_width() / 2, v + .03, f"{v:.0%}", ha="center", fontsize=14)
    pct_axis(ax); ax.set_title(title, fontsize=15); ax.set_xlabel("measured")

# 2 Measuring |0>, |+>, |-> (slide 6)
fig, axs = plt.subplots(1, 3, figsize=(11, 4), sharey=True)
for ax, (e, t) in zip(axs, (("zero", "state 0  |0⟩"), ("plus", "plus  |+⟩"), ("minus", "minus  |−⟩"))): pair_panel(ax, e, t)
axs[0].set_ylabel("share of 1,024 runs"); fig.suptitle("Reading three states: plus and minus look identical", fontsize=16)
save(fig, "single_qubit_measurement")

# 3 Interference: apply H again before measuring (slide 7)
fig, axs = plt.subplots(1, 2, figsize=(8, 4), sharey=True)
for ax, (e, t) in zip(axs, (("plus_H", "plus, then H"), ("minus_H", "minus, then H"))): pair_panel(ax, e, t)
axs[0].set_ylabel("share of 1,024 runs"); fig.suptitle("One extra step before reading: 50/50 becomes certain", fontsize=16)
save(fig, "interference_result")

# 4 Product state vs Bell pair (slide 9)
tq = {}
for r in load("two_qubit_counts.csv"): tq.setdefault(r["experiment"], {})[r["outcome"]] = float(r["probability"])
fig, axs = plt.subplots(1, 2, figsize=(11, 4), sharey=True)
for ax, (e, t) in zip(axs, (("product", "Two independent qubits"), ("bell", "Entangled pair (Bell pair)"))):
    ks = ["00", "01", "10", "11"]; vals = [tq[e][k] for k in ks]
    b = ax.bar(ks, vals, color=[INK if v > .1 else LIGHT for v in vals], width=.6)
    for rect, v in zip(b, vals): ax.text(rect.get_x() + rect.get_width() / 2, v + .03, f"{v:.0%}", ha="center", fontsize=13)
    pct_axis(ax); ax.set_title(t, fontsize=15); ax.set_xlabel("result of the pair")
axs[0].set_ylabel("share of 1,024 runs")
save(fig, "two_qubit_histograms")

# 5 CHSH game win rates (slide 10)
ch = {r["strategy"]: float(r["win_rate"]) for r in load("chsh_results.csv")}
fig, ax = plt.subplots(figsize=(9, 3.4))
labels = ["Entangled qubits (our simulation)", "Best plan agreed in advance"]; vals = [ch["quantum_simulated"] * 100, ch["classical_best"] * 100]
b = ax.barh(labels, vals, color=[INK, LIGHT], edgecolor=INK)
for rect, v in zip(b, vals): ax.text(v + .8, rect.get_y() + rect.get_height() / 2, f"{v:.1f}%", va="center", fontsize=15)
ax.axvline(75, color=MID, ls="--", lw=1.5); ax.set_ylim(-0.55, 1.85); ax.text(75.8, 1.6, "limit 75%", color=MID, fontsize=13)
ax.set_xlim(50, 100); ax.set_xlabel("win rate in Bell's game (%)")
save(fig, "chsh_win_rates")
print("charts ok")
