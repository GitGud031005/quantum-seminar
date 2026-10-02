"""Quantum-kernel vs classical-kernel experiment (slide 6).
Run: pip install qiskit scikit-learn numpy ; python quantum_kernel_experiment.py
Writes ../data/two_moons.csv, ../data/kernel_accuracy.csv, ../data/quantum_kernel_matrix_train.csv"""
import csv, os
import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
from qiskit.circuit.library import zz_feature_map
from qiskit.quantum_info import Statevector

HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.join(HERE, "..", "data")
X, y = make_moons(n_samples=120, noise=0.15, random_state=3)
X = MinMaxScaler((0, np.pi)).fit_transform(X)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.33, random_state=3, stratify=y)
fm = zz_feature_map(2, reps=2)
states = lambda A: np.array([Statevector(fm.assign_parameters(a)).data for a in A])
K = lambda A, B: np.abs(A.conj() @ B.T) ** 2          # fidelity kernel |<phi(x)|phi(x')>|^2

rows = []
q_scores = {}
for sc in [0.1, 0.2, 0.3, 0.5, 0.75, 1.0]:            # same small tuning budget as RBF gamma
    Str, Ste = states(Xtr * sc), states(Xte * sc)
    q_scores[sc] = SVC(kernel="precomputed").fit(K(Str, Str), ytr).score(K(Ste, Str), yte)
best_sc = max(q_scores, key=q_scores.get)
rbf = {g: SVC(kernel="rbf", gamma=g).fit(Xtr, ytr).score(Xte, yte) for g in [0.1, 0.3, 1, 3, 10]}
best_g = max(rbf, key=rbf.get)
lin = SVC(kernel="linear").fit(Xtr, ytr).score(Xte, yte)
rows = [["Quantum kernel (ZZ feature map, tuned)", round(q_scores[best_sc], 4), f"scale={best_sc}"],
        ["Quantum kernel (ZZ feature map, untuned)", round(q_scores[1.0], 4), "scale=1.0"],
        ["Linear SVM", round(lin, 4), ""],
        ["RBF SVM (tuned)", round(rbf[best_g], 4), f"gamma={best_g}"]]
for r in rows: print(r)
with open(os.path.join(DATA, "kernel_accuracy.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["model", "test_accuracy", "setting"]); w.writerows(rows)
with open(os.path.join(DATA, "two_moons.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["x1_scaled", "x2_scaled", "label", "split"])
    tr = {tuple(p) for p in Xtr}
    for p, lab in zip(X, y): w.writerow([round(p[0], 5), round(p[1], 5), int(lab), "train" if tuple(p) in tr else "test"])
Str = states(Xtr * best_sc); Ktr = K(Str, Str); o = np.argsort(ytr, kind="stable")
np.savetxt(os.path.join(DATA, "quantum_kernel_matrix_train.csv"), Ktr[o][:, o], delimiter=",", fmt="%.5f",
           header=f"80x80 training kernel sorted by class; first {int((ytr==0).sum())} rows/cols = class 0", comments="# ")
