# Speaker notes — Part 2 (Tiếng Việt, bản ít toán)
**19 slide · ~15 phút (~16 phút nếu có slide 10) · Người trình bày: [Người 2]**

Ưu tiên ý nghĩa, chỉ giữ công thức khi nó là ý đặc trưng. Chữ nghiêng trong ngoặc là ghi chú cho người nói, không đọc ra. Phần toán mà khán giả có thể hỏi nằm ở các dòng "Nếu bị hỏi" và ở slide dự phòng A1–A3.

---

## Slide 1 — Bìa · ~0:15
*[Nhận lời sau khi Người 1 kết ở "ba tài nguyên lượng tử: chồng chập, rối lượng tử, giao thoa".]*

"Giờ ta đã biết qubit là gì. Câu hỏi tiếp theo là: làm gì với nó? Người 1 đưa cho ta đất sét, còn việc của mình là cho các bạn thấy cách nặn nó thành hình, bằng cổng, mạch và thuật toán. Cuối phần này các bạn sẽ thấy hai thuật toán, Grover và Shor, vượt mọi máy tính thường trên bài toán của chúng, và mình sẽ chạy trực tiếp một thuật toán."

## Slide 2 — Mọi cổng đều đảo ngược được · ~0:45
"Luật số một của máy tính lượng tử: mọi cổng lượng tử đều đảo ngược được. Nó không bao giờ vứt bỏ thông tin. So với cổng AND cổ điển: nếu mình nói đầu ra là 0, bạn không biết được đầu vào, vì có thể là 00, 01 hoặc 10. Thông tin đó mất hẳn. Cổng lượng tử thì luôn giữ lại: bao nhiêu qubit vào thì bấy nhiêu qubit ra, và luôn chạy ngược lại được.

Chỉ có đúng một bước không đảo ngược được: phép đo. Nhìn vào là chồng chập biến mất. Các bạn nhớ điểm này, vì nó là lý do mọi thứ phía sau trở nên khó."

*Nếu bị hỏi: "Về mặt toán, cổng là ma trận unitary, chính điều đó đảm bảo cả hai tính chất. Có ở slide dự phòng A1."*

## Slide 3 — Lật bit, lật dấu · ~0:50
"Hai động tác cơ bản trên một qubit. X là cổng NOT lượng tử: đổi 0 thành 1 và ngược lại. Z thì lạ hơn: giữ nguyên 0, nhưng gắn dấu trừ lên 1. Giá trị bit không đổi, chỉ có dấu đổi.

Nếu đo ngay sau Z thì không thấy dấu trừ đó đâu cả. Vậy quan tâm làm gì? Vì trong một chồng chập, chính dấu trừ đó quyết định cái gì sẽ triệt tiêu về sau. Các bạn nhớ 'dấu trừ vô hình' này, nó là chìa khóa của toàn bộ tăng tốc, và vài slide nữa ta sẽ thấy nó hoạt động."

## Slide 4 — Hadamard: đồng xu lượng tử · ~0:50
"Cổng quan trọng nhất là Hadamard, H. Hãy coi nó như tung một đồng xu lượng tử: nó biến một qubit chắc chắn là 0 thành trạng thái 50/50.

Nhưng có điều bất ngờ. Tung đồng xu thật hai lần thì vẫn ngẫu nhiên. Còn áp H hai lần thì ra 0, chắc chắn. Hai con đường dẫn tới 1 triệt tiêu lẫn nhau. Đó là lần đầu ta thấy giao thoa.

Và gần như mọi thuật toán lượng tử đều bắt đầu giống nhau: áp H lên mọi qubit, để ta nắm trong tay mọi đầu vào cùng lúc, với trọng số bằng nhau."

## Slide 5 — CNOT nối hai qubit · ~0:50
"Giờ là cổng hai qubit: CNOT. Luật chỉ có một câu: nếu qubit thứ nhất là 1 thì lật qubit thứ hai. 00 giữ nguyên, 01 giữ nguyên, 10 thành 11, 11 thành 10.

Điều kỳ diệu xảy ra khi qubit thứ nhất là một đồng xu 50/50. Khi đó qubit thứ hai bị gắn chặt với nó: cặp qubit ở trạng thái 'cả hai là 0' và 'cả hai là 1' cùng lúc. Đó là rối lượng tử: đo một qubit là biết ngay qubit kia. Chỉ một cổng, hai qubit đã được nối với nhau."

## Slide 6 — Bộ đồ nghề nhỏ dựng được mọi thứ · ~0:40
"Có thể các bạn nghĩ ta cần hàng trăm loại cổng. Không cần. Trong máy tính thường, chỉ cổng NAND thôi đã dựng được mọi mạch. Trong máy tính lượng tử, một nhúm cổng, gồm H, CNOT và hai cổng pha nhỏ, dựng được mọi chương trình lượng tử. Máy lượng tử cũng chạy được mọi chương trình cổ điển, nhờ một phiên bản thuận nghịch của cổng AND tên là Toffoli.

Một lưu ý trung thực: 'dựng được mọi thứ' không có nghĩa là 'nhanh'. Cái khó là tìm ra thuật toán giữ được mạch nhỏ. Grover và Shor chính là những thuật toán như vậy."

*Nếu bị hỏi về bộ cổng chính xác hay định lý Solovay–Kitaev: chuyển sang slide dự phòng A1.*

## Slide 7 — Đọc mạch · ~1:00
"Ta tập đọc một mạch, vì lát nữa sẽ gặp vài mạch. Mỗi đường ngang là một qubit, thời gian chạy từ trái sang phải, ô vuông là cổng, chấm đen và vòng tròn có dấu cộng là hai đầu của một CNOT, còn biểu tượng đồng hồ là phép đo.

Mạch này chỉ có hai cổng: H biến qubit đầu thành đồng xu 50/50, rồi CNOT gắn qubit thứ hai vào nó. Nhóm mình đo 1.024 lần: 503 lần ra 00, 521 lần ra 11, và không lần nào ra 01 hay 10. Hai qubit luôn trùng nhau. Đó là trạng thái rối lượng tử Người 1 đã nói, giờ được dựng từ đầu."

## Slide 8 — "Tính mọi đầu vào cùng lúc" và cái bẫy · ~0:45
"Đây là ý tưởng khiến ai cũng hào hứng. Áp H lên n qubit là ta nắm cả 2 mũ n đầu vào cùng lúc: 3 qubit là 8 đầu vào, 53 qubit là khoảng chín triệu tỷ. Chạy một hàm một lần là nó chạm tới mọi đầu vào.

Nghe như bữa trưa miễn phí. Nhưng có cái bẫy: khi đo, ta chỉ nhận lại một đáp án ngẫu nhiên. Muốn đọc hết thì phải chạy cỡ 2 mũ n lần, không hơn gì máy thường. Nên 'tính mọi thứ song song' không phải là nguồn gốc của tăng tốc."

## Slide 9 — Giao thoa: bí quyết thật sự · ~0:50
"Bí quyết thật sự là giao thoa. Các trọng số lượng tử, gọi là biên độ, có thể âm, nên chúng có thể cộng dồn hoặc triệt tiêu nhau, giống như sóng nước.

Ví dụ nhỏ nhất: tìm 11 trong bốn đáp án. Ban đầu mọi đáp án có trọng số cộng 0,5. Bước hai, đánh dấu đáp án bằng cách lật dấu, nên 11 thành trừ 0,5. Bước ba, bước 'khuếch đại', lật mọi trọng số qua giá trị trung bình. Ba đáp án sai rơi đúng về 0, còn 11 nhảy lên cộng 1.

Nên khi đo, ta chắc chắn 100% ra 11. Không phải nhờ thử mọi thứ, mà nhờ làm cho các đáp án sai triệt tiêu nhau."

## Slide 10 — Deutsch–Jozsa (tùy chọn) · ~0:40
*[Bỏ qua nếu trễ giờ.]*

"Một ví dụ nhanh cho thấy sức mạnh đó. Ta có một hàm ẩn, hoặc 'luôn cho cùng một đáp án', hoặc 'một nửa ra 0, một nửa ra 1'. Muốn chắc chắn bằng máy thường với đầu vào 20 bit, có thể phải kiểm tra 524.289 lần. Thuật toán lượng tử chỉ cần một lần: giao thoa làm kết quả ra 'toàn số 0' trong trường hợp đầu, và 'không bao giờ toàn số 0' trong trường hợp sau.

Nói cho công bằng, máy thường thử vài lần ngẫu nhiên cũng gần như luôn đúng, nên đây là ví dụ để học, không phải ứng dụng thực tế. Nhưng nó cho thấy giao thoa thật sự làm việc."

## Slide 11 — Grover: tìm kim khi không có mục lục · ~0:50
"Giờ là thuật toán gần với Big Data nhất. Có N phần tử, không sắp xếp, không có chỉ mục, và một phần tử đặc biệt. Hãy tìm nó.

Máy thường kiểm tra từng cái: trung bình khoảng một nửa. Grover chỉ cần cỡ căn bậc hai của N bước. Với một triệu phần tử, đó là 500.000 lần kiểm tra so với khoảng 785 bước.

Và điều này đã được chứng minh là tốt nhất có thể cho bài toán này. Đây là tăng tốc lớn, nhưng là căn bậc hai, không phải cấp số mũ. Còn nó có giúp được cơ sở dữ liệu thật, vốn có chỉ mục, hay không, thì Người 3 sẽ phân tích."

## Slide 12 — Một vòng Grover hoạt động thế nào · ~1:00
"Mỗi vòng Grover có hai bước. Bước một, đánh dấu: một mạch kiểm tra nhận ra đáp án, vì nó biết luật, và gắn dấu trừ lên đáp án đó, mà không hề cho ta biết đó là phần tử nào. Chính là 'dấu trừ vô hình' ở slide 3.

Bước hai, khuếch đại: lật mọi trọng số qua giá trị trung bình. Phần tử được đánh dấu bị dấu trừ kéo xuống rất thấp so với trung bình, nên khi lật nó bị hất lên cao hẳn. Các phần tử khác bị đẩy xuống một chút.

Với ba qubit, tìm 101: trước vòng nào thì cơ hội là 12,5%, sau một vòng là 78%, sau hai vòng là 94,5%. Đáp án đúng nổi lên, phần còn lại mờ dần."

## Slide 13 — Quay, và dừng đúng lúc · ~0:45
"Có một cách hình dung dễ thương: một mũi tên ban đầu nằm gần như phẳng, chỉ vào 'phần còn lại', và mỗi vòng quay nó một góc cố định về phía 'đáp án'. Sau khoảng 0,8 nhân căn N vòng, nó gần như chỉ thẳng vào đáp án.

Nhưng đừng quay mãi. Với tám phần tử, hai vòng cho 94,5%, ba vòng tụt xuống 33%, bốn vòng còn khoảng 1%: ta đã quay quá đáp án. Và không cần biết đáp án mới biết khi nào dừng, chỉ cần biết có bao nhiêu phần tử."

*Nếu bị hỏi công thức: slide dự phòng A2.*

## Slide 14 — Shor: phân tích thừa số = tìm nhịp lặp · ~0:50
"Thuật toán thứ hai là thuật toán nổi tiếng: Shor, để phân tích thừa số. Mã hóa RSA an toàn vì việc tách một số khổng lồ thành các thừa số nguyên tố cực kỳ khó.

Ý tưởng của Shor: biến việc phân tích thừa số thành việc tìm một mẫu lặp lại. Lấy các lũy thừa của 7, chỉ giữ số dư khi chia cho 15: ta được 7, 4, 13, 1, rồi lặp lại: 7, 4, 13, 1. Nhịp lặp là 4. Thêm một chút tính toán, nhịp đó cho ta luôn các thừa số: 15 bằng 3 nhân 5.

Với một số RSA thật dài 2.048 bit, mẫu lặp đó dài không tưởng. Không máy tính thường nào tìm được nhịp của nó. Máy lượng tử thì tìm được."

*Nếu bị hỏi nhịp lặp cho ra thừa số bằng cách nào: slide dự phòng A3 (bước ước chung lớn nhất).*

## Slide 15 — Bộ chỉnh âm lượng tử · ~0:45
"Vậy máy lượng tử tìm nhịp bằng cách nào? Bằng biến đổi Fourier lượng tử, gọi tắt là QFT. Hãy nghĩ tới cái máy chỉnh dây đàn guitar: bạn gảy một nốt, nó cho biết cao độ bằng cách biến sóng âm lặp lại thành một tần số rõ ràng. QFT làm điều tương tự với mẫu lặp của ta: biến nó thành những đỉnh nhọn.

Trong ví dụ nhỏ, các đỉnh nằm ở 0, 64, 128 và 192. Chúng cách nhau 64, cho biết nhịp lặp là 4.

Tóm lại: cách cổ điển tốt nhất tốn thời gian tăng gần theo cấp số mũ với số chữ số, còn Shor chỉ tăng theo đa thức. Đó là khác biệt giữa 'bất khả thi' và 'làm được', một khi có máy đủ lớn."

## Slide 16 — Vì sao Shor quan trọng · ~1:00
"Vậy cái gì bị phá? RSA, mật mã đường cong elliptic và Diffie–Hellman, tức phần khóa công khai của HTTPS và chữ ký số. Cái gì còn an toàn? AES và hàm băm, chỉ cần dùng khóa dài hơn.

Còn bao xa? Năm 2019, phá RSA-2048 được ước tính cần khoảng 20 triệu qubit nhiễu. Năm 2025, ước tính giảm xuống dưới một triệu, chạy chưa tới một tuần. Chưa ai có cỗ máy đó, nhưng đích đến cứ gần hơn.

Giải pháp đã có: năm 2024, NIST công bố ba chuẩn mật mã hậu lượng tử. Và có lý do để hành động ngay: 'thu thập bây giờ, giải mã sau'. Dữ liệu bị đánh cắp hôm nay có thể bị giải mã trong tương lai. Với Big Data, nghĩa là mọi kết nối TLS, mọi kho dữ liệu mã hóa và mọi sản phẩm có chữ ký trong pipeline đều cần nâng cấp."

## Slide 17 — Demo 1 · ~1:10
*[Chuyển sang notebook.]*

"Giờ xem nó chạy thật, trên simulator Qiskit của IBM. Demo một: hai qubit, bốn đáp án, đáp án ẩn là 11. Lý thuyết nói một vòng là đủ.

Code làm đúng công thức nấu ăn: H lên cả hai qubit, đánh dấu 11, khuếch đại, đo. *[Chạy.]* 1.024 lần đo, cả 1.024 lần đều ra 11. Đúng câu chuyện cộng 0,5, trừ 0,5, cộng 1 ở slide giao thoa."

## Slide 18 — Demo 2 · ~1:10
"Giờ ba qubit, tám đáp án, đáp án ẩn là 101. Lý thuyết nói hai vòng, 94,5%.

*[Chạy.]* Một cột vọt hẳn lên: 954 trên 1.024, tức 93,2%, rơi vào 101. Bảy trạng thái còn lại mỗi cái khoảng 1%.

Vì sao không đúng 94,5%? Vì phép đo ngẫu nhiên, giống tung đồng xu một nghìn lần thì hiếm khi ra đúng một nửa mặt ngửa. Với 1.024 lần đo, kết quả dao động khoảng bảy phần mười phần trăm."

*[Nếu chạy trực tiếp ra số khác thì nói đúng số đang thấy. Slide và Part 3 dùng lần chạy seed 7: 954.]*

## Slide 19 — Tóm tắt và chuyển giao · ~0:40
"Tóm lại. Cổng là những động tác đảo ngược được, và một bộ đồ nghề nhỏ là đủ dựng mọi thứ. Hai cổng là đủ để tạo rối lượng tử. Bí quyết thật sự là giao thoa: đáp án sai triệt tiêu nhau. Grover tìm kiếm trong thời gian căn bậc hai, tốt nhất có thể. Shor làm việc phân tích thừa số trở nên dễ, vì thế thế giới đang chuyển sang mật mã hậu lượng tử.

Đó là lý thuyết. Nhưng nó thực sự mang lại gì cho một hệ thống dữ liệu lớn, và phần cứng hôm nay đang ở đâu? [Người 3] sẽ tiếp tục."

---

## Q&A — câu trả lời soạn sẵn

**"Unitary" nghĩa là gì?** "Là điều kiện toán học làm cho cổng đảo ngược được và giữ tổng xác suất luôn bằng 100%. Có ở slide dự phòng A1."

**Grover có ích không nếu cơ sở dữ liệu có chỉ mục?** "Không trực tiếp. Chỉ mục tìm một bản ghi trong khoảng log N bước, ít hơn nhiều so với căn N. Grover có ích khi không có cấu trúc, ví dụ tìm một nghiệm thỏa một bộ luật. Người 3 sẽ nói về chuyện nạp dữ liệu."

**Bao giờ Shor phá được RSA?** "Chưa đâu. Ước tính tốt nhất năm 2025 là dưới một triệu qubit nhiễu chạy chưa tới một tuần; máy hiện nay có vài trăm tới vài nghìn qubit. Vì vậy mọi người chuyển đổi ngay từ bây giờ."

**Sao không đọc hết các đáp án ở cuối?** "Phép đo chỉ cho một kết quả và xóa phần còn lại. Muốn đọc hết thì phải chạy nhiều lần bằng số đáp án."

**Tăng tốc của Grover có phải cấp số mũ không?** "Không, là căn bậc hai. Tăng tốc ngoạn mục là của Shor."

**Grover có phá được AES không?** "Nó biến việc dò khóa 128 bit thành khoảng 2 mũ 64 bước, trên thực tế vẫn rất khó; AES-256 vẫn an toàn. Nên chỉ cần khóa dài hơn, không cần thuật toán mới."

**Vì sao 93,2% mà không phải 94,5%?** "94,5% là xác suất chính xác; 93,2% là số đếm được trong 1.024 lần đo ngẫu nhiên."

**Không biết đáp án thì sao biết khi nào dừng Grover?** "Số vòng chỉ phụ thuộc vào số phần tử (và số đáp án). Dừng ở đó, đo, rồi dùng luật kiểm tra kết quả."
