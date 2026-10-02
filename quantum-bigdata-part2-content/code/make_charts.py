"""Neutral (unstyled) charts for Part 2 from ../data/*.csv — black/grey on white, PNG + SVG."""
import csv, os, math
import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(HERE, "..", "data"); O = os.path.join(HERE, "..", "assets", "charts")
plt.rcParams.update({"font.size": 15, "axes.spines.top": False, "axes.spines.right": False})
INK, MID, LIGHT = "#111111", "#777777", "#cccccc"
rd = lambda n: list(csv.DictReader(open(os.path.join(D, n))))
def save(fig, name):
    fig.tight_layout(); fig.savefig(os.path.join(O, name + ".png"), dpi=200, facecolor="white"); fig.savefig(os.path.join(O, name + ".svg"), facecolor="white"); plt.close(fig)

# 1 Interference: 2-qubit Grover amplitudes in three stages
r = rd("grover_2q_amplitudes.csv"); labels = [x["state"] for x in r]
fig, axs = plt.subplots(1, 3, figsize=(13, 4.2), sharey=True)
for ax, col, title in zip(axs, ["after_H", "after_oracle", "after_diffusion"], ["1. After H⊗H", "2. After oracle (sign flip)", "3. After diffusion"]):
    v = [float(x[col]) for x in r]
    ax.bar(labels, v, color=[INK if l == "11" else LIGHT for l in labels], edgecolor=INK)
    ax.axhline(0, color=MID, lw=1); ax.set_title(title, fontsize=15); ax.set_ylim(-0.7, 1.1)
    for i, val in enumerate(v): ax.text(i, val + (0.05 if val >= 0 else -0.12), f"{val:+.2f}", ha="center", fontsize=13)
axs[0].set_ylabel("amplitude"); save(fig, "interference_2q_amplitude_stages")

# 2 Grover 3-qubit amplitudes, step by step (signed)
r = rd("grover_3q_amplitudes_by_step.csv"); labels = [x["state"] for x in r]
cols = [("init", "Start (H⊗3)"), ("oracle_1", "Round 1: oracle"), ("round_1", "Round 1: diffusion"), ("oracle_2", "Round 2: oracle"), ("round_2", "Round 2: diffusion")]
fig, axs = plt.subplots(1, 5, figsize=(18, 4.2), sharey=True)
for ax, (c, t) in zip(axs, cols):
    v = [float(x[c]) for x in r]
    ax.bar(labels, v, color=[INK if l == "101" else LIGHT for l in labels], edgecolor=INK)
    ax.axhline(0, color=MID, lw=1); ax.set_title(t, fontsize=14); ax.tick_params(axis="x", rotation=90, labelsize=11); ax.set_ylim(-1, 1.05)
axs[0].set_ylabel("amplitude"); save(fig, "grover_3q_amplitudes_by_step")

# 3 Success vs iterations N=8
r = rd("grover_success_vs_k_N8.csv"); k = [int(x["k"]) for x in r]; p = [float(x["success_probability"]) * 100 for x in r]
fig, ax = plt.subplots(figsize=(9, 4.6))
ax.plot(k, p, "-o", color=INK, lw=2.5, ms=8); ax.plot(2, p[2], "o", ms=16, mfc="none", mec=INK, mew=2)
for kk, pp in zip(k, p): ax.text(kk, pp + 4, f"{pp:.1f}%", ha="center", fontsize=12)
ax.set_xlabel("Grover iterations k"); ax.set_ylabel("P(marked state) %"); ax.set_ylim(0, 112); ax.set_xticks(k)
ax.set_title("N = 8: stop at k = 2 (94.5%); more rounds overshoot"); save(fig, "grover_success_vs_iterations_N8")

# 4 Scaling: classical N/2 vs Grover pi/4 sqrt(N)
N = np.logspace(1, 15, 200); fig, ax = plt.subplots(figsize=(9, 4.8))
ax.loglog(N, N / 2, color=INK, lw=3, label="classical, average N/2 checks")
ax.loglog(N, np.pi / 4 * np.sqrt(N), color=MID, lw=3, ls="--", label="Grover, (π/4)·√N oracle calls")
ax.set_xlabel("search space size N"); ax.set_ylabel("queries"); ax.legend(frameon=False); ax.minorticks_off()
save(fig, "grover_vs_classical_scaling")

# 5-6 demo histograms
for name, fn, mark, title in [("grover_demo_2q_histogram", "grover_counts_2q.csv", "11", "2 qubits, 1 iteration: 1,024 / 1,024 on 11"),
                              ("grover_demo_3q_histogram", "grover_counts_3q.csv", "101", "3 qubits, 2 iterations: 954 / 1,024 (93.2%) on 101")]:
    r = rd(fn); s = [x["state"] for x in r]; c = [int(x["count"]) for x in r]
    fig, ax = plt.subplots(figsize=(9, 4.6)); ax.bar(s, c, color=[INK if x == mark else LIGHT for x in s], edgecolor=INK)
    for i, v in enumerate(c): ax.text(i, v + 12, str(v), ha="center", fontsize=12)
    ax.set_ylim(0, 1130); ax.set_ylabel("count (of 1,024 shots)"); ax.set_xlabel("measured state"); ax.set_title(title); save(fig, name)

# 7 Bell
r = rd("bell_counts.csv"); s = [x["state"] for x in r]; c = [int(x["count"]) for x in r]
fig, ax = plt.subplots(figsize=(7.5, 4.4)); ax.bar(s, c, color=[INK if x in ("00", "11") else LIGHT for x in s], edgecolor=INK)
for i, v in enumerate(c): ax.text(i, v + 10, str(v), ha="center", fontsize=12)
ax.set_ylim(0, 620); ax.set_ylabel("count (of 1,024 shots)"); ax.set_title("Bell state: only 00 and 11 appear"); save(fig, "bell_state_histogram")

# 8 Deutsch-Jozsa
r = rd("deutsch_jozsa_n3.csv"); lab = ["constant\nf(x)=0", "constant\nf(x)=1", "balanced\nf(x)=x₀", "balanced\nf(x)=x₀⊕x₁⊕x₂"]
v = [float(x["P(measure_000)"]) * 100 for x in r]
fig, ax = plt.subplots(figsize=(9, 4.4)); ax.bar(lab, v, color=[INK, INK, LIGHT, LIGHT], edgecolor=INK)
for i, val in enumerate(v): ax.text(i, val + 3, f"{val:.0f}%", ha="center", fontsize=13)
ax.set_ylim(0, 115); ax.set_ylabel("P(measure 000) %"); ax.set_title("Deutsch–Jozsa, n = 3: one query decides"); save(fig, "deutsch_jozsa_outcomes")

# 9 Shor: 7^x mod 15
r = rd("shor_powers_7_mod_15.csv"); x = [int(a["x"]) for a in r]; y = [int(a["7^x mod 15"]) for a in r]
fig, ax = plt.subplots(figsize=(10, 4.2)); ax.plot(x, y, "-o", color=INK, lw=2, ms=8)
for xx, yy in zip(x, y): ax.text(xx, yy + 0.7, str(yy), ha="center", fontsize=12)
for s in (0, 4, 8, 12): ax.axvspan(s - 0.4, s + 3.4, color=LIGHT if s % 8 == 0 else "#eeeeee", zorder=0)
ax.set_xticks(x); ax.set_ylim(0, 16); ax.set_xlabel("x"); ax.set_ylabel("7ˣ mod 15"); ax.set_title("f(x) = 7ˣ mod 15 repeats every r = 4 steps"); save(fig, "shor_period_7_mod_15")

# 10 Shor: QFT output
r = rd("shor_qft_distribution_N15_a7_t8.csv"); yv = [int(a["y"]) for a in r]; pv = [float(a["probability"]) for a in r]
fig, ax = plt.subplots(figsize=(10, 4.2)); ax.bar(yv, pv, width=2.2, color=INK)
for yy, pp in zip(yv, pv):
    if pp > 0.01: ax.text(yy, pp + 0.01, f"y = {yy}", ha="center", fontsize=12)
ax.set_xlim(-6, 262); ax.set_ylim(0, 0.32); ax.set_xlabel("measured value y (8 counting qubits, 0–255)"); ax.set_ylabel("probability")
ax.set_title("After the QFT: peaks at multiples of 256 / r = 64  →  r = 4"); save(fig, "shor_qft_peaks_N15_a7")
print("charts ok")
