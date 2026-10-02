# Seminar Quantum Computing — Agenda nội dung chi tiết & phân mảng cho 3 người

> **Môn:** Big Data · **45 phút** (~41p nội dung + ~4p Q&A) · **Nhóm 3 người**
> Chia thành **3 mảng nội dung**, mỗi người phụ trách nghiên cứu + trình bày 1 mảng.
> Định hướng: cân bằng nhập môn QC + liên hệ Big Data · toán vừa phải (bra-ket, ma trận cơ bản) · có demo.
> Tài liệu gốc: **Nielsen & Chuang** (N&C).

## Bản đồ nội dung

| Mảng | Người | Nội dung | Thời lượng |
|------|:-----:|----------|:----------:|
| **A** | 1 | Nền tảng lượng tử (động lực → qubit → superposition → đo → entanglement) | ~13p |
| **B** | 2 | Cổng, mạch & thuật toán + demo Grover | ~17p |
| **C** | 3 | Ứng dụng Big Data & hiện trạng phần cứng | ~11p + Q&A (~4p) |

---

## MẢNG A — Người 1: Nền tảng lượng tử

*Mục tiêu: người nghe hiểu qubit là gì và 3 hiện tượng lõi. Đây là phần "vỡ lòng", nói sai chỗ này thì cả bài sập.*

### A1. Bối cảnh & động lực (~3p)
- **Giới hạn tính toán cổ điển:** Moore's law chững lại (giới hạn vật lý transistor); một lớp bài toán có độ phức tạp tăng theo lũy thừa → cổ điển bó tay ở quy mô lớn.
- **Ý tưởng Feynman (1982):** muốn mô phỏng hệ lượng tử thì nên dùng chính máy tính lượng tử.
- **Chốt:** *n* qubit mã hóa **2ⁿ biên độ** cùng lúc → nguồn gốc sức mạnh (và cả cái khó sau này).

### A2. Bit vs Qubit + ký hiệu Dirac (~2p)
- Bit cổ điển ∈ {0, 1}. Qubit: **|ψ⟩ = α|0⟩ + β|1⟩**, với α, β là số phức, **|α|² + |β|² = 1** (chuẩn hóa).
- Ký hiệu bra-ket: |0⟩ = (1,0)ᵀ, |1⟩ = (0,1)ᵀ. Giải thích tại sao dùng vector cột.

### A3. Superposition — chồng chập (~1.5p)
- Qubit ở **tổ hợp tuyến tính** của 0 và 1 *cho đến khi đo*.
- ⚠️ Đính chính hiểu lầm phổ biến: **không phải** "vừa 0 vừa 1" theo nghĩa cổ điển — đó là *biên độ xác suất*, và song song lượng tử ≠ chạy nhiều bản sao song song.
- Ví dụ: |+⟩ = (|0⟩ + |1⟩)/√2.

### A4. Bloch sphere (~1.5p)
- Biểu diễn hình học 1 qubit: |ψ⟩ = cos(θ/2)|0⟩ + e^{iφ} sin(θ/2)|1⟩.
- Cực bắc = |0⟩, cực nam = |1⟩, xích đạo = các superposition. **Pha (φ)** là gì và vì sao nó quan trọng (interference sau này dựa vào pha).

### A5. Đo lường & collapse (~2p) — *khái niệm phản trực giác nhất*
- Đo theo cơ sở tính toán: ra `0` với xác suất **|α|²**, ra `1` với **|β|²**.
- Sau khi đo → trạng thái **sụp** về kết quả đo được, **không thể hoàn tác**.
- Hệ quả then chốt: **không đọc trực tiếp được toàn bộ biên độ** → thuật toán phải khéo để đáp án lộ ra khi đo.

### A6. Đa qubit & Entanglement — rối lượng tử (~2p)
- Ghép qubit bằng **tích tensor**: n qubit → không gian 2ⁿ chiều.
- Trạng thái **tích** (tách rời được) vs **rối** (không tách rời).
- **Bell state** (|00⟩ + |11⟩)/√2: đo 1 qubit ra `0` thì qubit kia chắc chắn `0`, dù ở xa → "tương quan" mạnh hơn cổ điển.

### A7. No-cloning theorem (~1p)
- Không thể sao chép một trạng thái lượng tử tùy ý. Nêu nhanh hệ quả: nền tảng cho phân phối khóa lượng tử (QKD).

### Chốt mảng A → "3 tài nguyên lượng tử: **superposition, entanglement, interference**" (bắc cầu sang mảng B).

**📚 Tìm hiểu:** N&C Ch.1 (tổng quan), 2.1 (đại số tuyến tính), 2.2 (postulates), 2.4 (measurement), 1.3.6 (no-cloning). Tìm thêm: bài giải thích Bloch sphere trực quan; ví dụ Bell state.

---

## MẢNG B — Người 2: Cổng, mạch & thuật toán

*Mục tiêu: từ "gạch" (cổng) → "nhà" (thuật toán), và cho thấy vì sao QC nhanh với vài bài toán.*

### B1. Thuận nghịch & unitary (~1p)
- Mọi cổng lượng tử là **ma trận unitary** (U†U = I) → bảo toàn chuẩn, **thuận nghịch**.
- Khác cổng cổ điển: AND/OR mất thông tin (không thuận nghịch).

### B2. Cổng 1 qubit (~2p)
- **Pauli X** (NOT lượng tử), **Z** (phase flip), Y.
- **Hadamard H** = (1/√2)[[1, 1], [1, −1]] → biến |0⟩ thành |+⟩: **cổng tạo superposition** (quan trọng nhất).
- Phase gates S, T (nhắc nhanh). Cho xem tác động lên |0⟩, |1⟩ bằng số cụ thể.

### B3. Cổng nhiều qubit (~2p)
- **CNOT (CX):** control–target, bảng chân trị; đây là **cổng tạo entanglement**.
- Toffoli (CCNOT). Khái niệm **bộ cổng phổ quát** (universal gate set) — vài cổng đủ dựng mọi mạch.

### B4. Mạch lượng tử & Bell pair (~1.5p)
- Cách đọc sơ đồ mạch: mỗi dây = 1 qubit, thời gian chạy trái → phải.
- Ráp **H + CNOT → Bell state**, giải thích từng bước (nối lại với A6).

### B5. Song song lượng tử & Interference — *chìa khóa* (~1.5p)
- Áp H lên n qubit → superposition đều **2ⁿ** trạng thái "cùng lúc".
- Nhưng đo chỉ ra **1** kết quả → cần **interference**: khuếch đại biên độ đáp án đúng, triệt tiêu đáp án sai. Đây là cơ chế thật sự tạo tăng tốc, không phải "thử mọi đáp án song song rồi đọc hết".

### B6. (Tùy chọn) Deutsch–Jozsa (~1p)
- Ví dụ "đồ chơi": phân biệt hàm *constant* vs *balanced* chỉ với 1 truy vấn → minh họa interference rõ nhất. Đưa vào nếu còn giờ.

### B7. Grover — thuật toán tìm kiếm (~3p) — *phần liên hệ Big Data nhất*
- **Bài toán:** tìm phần tử được đánh dấu trong N phần tử phi cấu trúc.
- **Độ phức tạp:** cổ điển O(N) vs Grover **O(√N)**.
- **Cơ chế:** (1) *oracle* đánh dấu đáp án bằng lật pha; (2) *diffusion* (đảo quanh giá trị trung bình) khuếch đại biên độ đáp án.
- **Số vòng lặp tối ưu ≈ (π/4)·√N.** Trực quan hóa bằng đồ thị biên độ tăng dần.

### B8. Shor — phân tích thừa số (~2p)
- **Bài toán:** phân tích số lớn ra thừa số nguyên tố ↔ quy về **tìm chu kỳ (period finding)**.
- Vai trò **QFT** (Quantum Fourier Transform). Speedup **mũ/siêu đa thức** so với thuật toán cổ điển tốt nhất.
- **Hệ quả:** phá được RSA → thúc đẩy **mật mã hậu lượng tử (PQC)**. Nói *ý nghĩa* là chính, không sa đà toán.

### B9. Demo Grover (~4p)
Chạy Grover trên simulator, histogram **dồn xác suất vào đúng đáp án**. Cài đặt: `pip install qiskit qiskit-aer`. Đã test trên Qiskit 2.5.2 / qiskit-aer 0.17.2.

**Bản 2 qubit (đánh dấu `11`):**
```python
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

sim = AerSimulator()

qc = QuantumCircuit(2)
qc.h([0, 1])          # 1) Chồng chập đều 4 trạng thái: 00, 01, 10, 11
qc.cz(0, 1)           # 2) Oracle: đánh dấu đáp án |11> bằng lật pha
# 3) Diffusion (đảo quanh giá trị trung bình) — khuếch đại biên độ đáp án
qc.h([0, 1]); qc.x([0, 1]); qc.cz(0, 1); qc.x([0, 1]); qc.h([0, 1])
qc.measure_all()

print(qc.draw())
result = sim.run(transpile(qc, sim), shots=1024).result()
counts = result.get_counts()
print(counts)          # -> {'11': 1024}
plot_histogram(counts)
```
Kết quả: `{'11': 1024}` — 1 vòng lặp, gần như 100% ra đúng đáp án.

**Bản mở rộng 3 qubit, 8 trạng thái (đánh dấu `101`) — histogram ấn tượng hơn:**
```python
def diffusion(qc, qs):
    qc.h(qs); qc.x(qs)
    qc.h(qs[-1]); qc.ccx(qs[0], qs[1], qs[-1]); qc.h(qs[-1])   # CCZ = H-CCX-H
    qc.x(qs); qc.h(qs)

g = QuantumCircuit(3)
g.h([0, 1, 2])
for _ in range(2):                    # 2 vòng lặp là tối ưu cho N=8
    g.x(1)                            # oracle đánh dấu trạng thái ẩn |101>
    g.h(2); g.ccx(0, 1, 2); g.h(2)
    g.x(1)
    diffusion(g, [0, 1, 2])
g.measure_all()

counts = sim.run(transpile(g, sim), shots=1024).result().get_counts()
print(counts)          # ~93–95% vào '101' (tùy lần chạy), còn lại rải rác rất nhỏ
plot_histogram(counts)
```
Kết quả: ~`{'101': ~970, ...}` — 1 cột vọt hẳn giữa 8 trạng thái, minh họa "tìm 1 bản ghi giữa cả tập dữ liệu".

**Liên hệ khi trình bày:** cổ điển cần trung bình N/2 bước dò tuần tự; Grover cần ~(π/4)√N bước. Với N=8 (3 qubit) chỉ cần 2 vòng lặp mà xác suất đúng đã ~93–95% (lý thuyết ≈ 94,5%).

**📚 Tìm hiểu:** N&C Ch.4 (mạch & cổng), 5.1 (QFT), 5.3 (Shor), 6.1–6.2 (Grover), 1.4.3–1.4.4. Tìm thêm: Qiskit textbook (Grover, Deutsch–Jozsa); animation amplitude amplification.

---

## MẢNG C — Người 3 (Phúc): Ứng dụng Big Data & hiện trạng

*Mục tiêu: trả lời "liên quan gì tới môn học?" một cách trung thực — vừa nêu tiềm năng vừa chỉ rõ giới hạn. Đây là phần ăn điểm với giảng viên.*
*Deck Part 3 đã hoàn thiện: **14 slide tiếng Anh**, ~11 phút. Nội dung, hình và speaker note chi tiết xem file "Mảng C — Slide & Speaker notes".*

### C0. Cầu nối từ demo (~0.5p)
- Dùng lại histogram demo Grover (93% vào `101`) → "giờ nhân lên 10¹² bản ghi thì sao?"

### C1. Vì sao QC dính tới Big Data (~0.75p)
- n qubit ↔ 2ⁿ biên độ: 50 qubit ≈ 10¹⁵, 300 qubit ≈ 10⁹⁰ (> 10⁸⁰ nguyên tử) — minh họa bằng biểu đồ 2ⁿ.
- Bảng ánh xạ: tìm kiếm → Grover · học máy → quantum kernel/VQC · hồi quy/PCA → HHL · tối ưu → QAOA/annealing.

### C2. Quantum search cho dữ liệu (~1p)
- Mô hình CPU–memory LOAD/STORE (**N&C §6.5, Fig. 6.8**). Với N = 10¹²: cổ điển ~5×10¹¹ lần dò, Grover ~7,9×10⁵ vòng lặp.
- Nhưng CSDL có index chỉ cần ~log₂N ≈ 40 bước → Grover chỉ có ý nghĩa với truy vấn không index nào hỗ trợ.

### C3. Quantum Machine Learning — QML (~2p, 2 slide)
- **Quantum kernels / QSVM** (Havlíček et al., *Nature* 2019) và **Variational Quantum Circuits** (vòng lặp lai lượng tử–cổ điển, hợp NISQ).
- ⭐ **Thí nghiệm của nhóm:** ZZ feature map 2 qubit trên dữ liệu two-moons (80 train / 40 test): quantum kernel **90,0%**, linear SVM **92,5%**, RBF SVM **97,5%** → trên dữ liệu cổ điển, quantum kernel không thắng. Kết quả thật, chạy bằng Qiskit + scikit-learn.

### C4. HHL — giải hệ tuyến tính Ax = b (~1p)
- Cổ điển O(N·s·κ) vs HHL O(log N·s²κ²/ε) — tăng tốc mũ **có điều kiện**: A thưa & κ nhỏ, nạp |b⟩ nhanh, đầu ra là trạng thái (đọc hết lại tốn N), chỉ hữu ích cho đại lượng tổng hợp. Minh họa bằng biểu đồ N vs log N.

### C5. Quantum optimization (~0.5p)
- Bài toán QUBO (MaxCut, feature selection, lập lịch); **QAOA** (Farhi et al. 2014); **annealing** (D-Wave). Chưa có lợi thế rõ so với heuristic cổ điển.

### C6. ⭐ NÚT THẮT — phần trung thực học thuật (~2.5p, 3 slide) *(quan trọng nhất mảng C)*
- Slide nhấn: "mọi tăng tốc đều giả định dữ liệu đã nằm sẵn trong máy lượng tử".
- **Data loading / QRAM** (**N&C Fig. 6.9**): cần O(N log N) công tắc lượng tử; nạp N bản ghi đã tốn ~O(N); N&C kết luận Grover hữu ích nhất cho bài toán khó (SAT, TSP), không phải tìm trong CSDL cổ điển.
- **Fine print & dequantization:** timeline 2009 HHL → 2015 Aaronson "Read the fine print" → 2016 Kerenidis–Prakash → 2018 Ewin Tang.

### C7. Hiện trạng phần cứng 2026 (~1.2p)
- NISQ → chịu lỗi sớm; qubit vật lý vs qubit logic.
- Google Willow 105 qubit (12/2024, dưới ngưỡng) · IBM Nighthawk 120 qubit, Starling 2029: 200 qubit logic · IonQ/Quantinuum (bẫy ion, **N&C Fig. 7.7**) · Pasqal/QuEra (nguyên tử trung hòa, 05/2026 qubit logic vượt vật lý) · NIST PQC 2024.
- ⚠️ *Số liệu đổi nhanh — kiểm tra lại 1–2 ngày trước buổi thuyết trình.*

### C8. Kết luận & take-home (~0.7p)
1. QC là **bộ đồng xử lý**, không thay thế; chỉ mạnh cho lớp bài toán hẹp.
2. Với Big Data, nghẽn chính ở **I/O dữ liệu**, không phải tốc độ tính.
3. Luôn hỏi **"compared to what?"** — theo dõi PQC, thử QML lai trên simulator.

**📚 Tìm hiểu:** N&C §6.5 (tr. 265–268), Ch.7 (Fig. 7.7); Harrow–Hassidim–Lloyd (2009); Havlíček et al. (2019); Biamonte et al. (2017); Aaronson (2015); Tang (2019); Farhi et al. (2014); Preskill (2018).

---

## Ghi chú chia việc
- **Điểm nối giữa các mảng:** A kết ở "3 tài nguyên lượng tử" → B mở ở cổng; B kết ở Grover/demo → C mở ở "áp Grover vào dữ liệu". Ba người nên thống nhất chỗ giao để chuyển mượt.
- **Ký hiệu chung:** cả nhóm dùng thống nhất bra-ket + cách viết ma trận (A chốt quy ước).
