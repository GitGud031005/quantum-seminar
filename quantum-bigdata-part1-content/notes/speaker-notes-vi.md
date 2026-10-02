# Speaker notes — Tiếng Việt (bản luyện nói)

Khớp thứ tự 12 slide. Thay [Người 2] bằng tên thật.
Chữ *nghiêng* là gợi ý chỉ vào hình nào. Cả phần cố ý dùng từ đời thường: "trọng số" thay cho "biên độ", "đọc" thay cho "đo". Có thể nói thuật ngữ gốc một lần rồi dùng từ đời thường.

**Từ dùng trong phần này**
- **Qubit:** bit lượng tử, có thể là 0, là 1, hoặc là một hỗn hợp của cả hai.
- **Chồng chập:** chính hỗn hợp đó. Qubit giữ 0 và 1 cùng lúc, mỗi bên có một trọng số.
- **Trọng số** (biên độ): mức độ 0 hoặc 1 có mặt trong hỗn hợp. Trọng số có thể dương hoặc âm.
- **Pha:** dấu (tổng quát hơn là "hướng") của trọng số. Đọc thẳng thì không thấy pha.
- **Đọc** (đo): hỏi qubit "0 hay 1?". Kết quả ngẫu nhiên, và hỗn hợp bị phá.
- **Giao thoa:** các trọng số cộng dồn hoặc triệt tiêu nhau, giống sóng nước.
- **Rối lượng tử:** các qubit liên kết chặt đến mức chỉ mô tả được cả nhóm, không tách riêng từng cái.
- **Không sao chép:** không thể copy một qubit chưa biết.

## Slide 1 — Quantum Foundations (bìa)

"Chào mọi người. Chủ đề của nhóm hôm nay là máy tính lượng tử và ý nghĩa của nó với dữ liệu lớn. Mình mở đầu bằng phần nền tảng: qubit là gì, và ba ý tưởng làm máy tính lượng tử khác máy tính thường. Sau đó [Người 2] sẽ cho thấy các ý tưởng này thành thuật toán ra sao, có demo chạy thật. Cuối cùng Phúc sẽ nối tất cả với Big Data và phần cứng hiện nay."

## Slide 2 — Why quantum computing?

"Vì sao cần một loại máy tính mới? Có hai lý do.

Thứ nhất là chip. Mấy chục năm qua máy tính nhanh lên nhờ transistor nhỏ đi. Giờ một transistor chỉ rộng vài chục nguyên tử. Nhỏ hơn nữa thì hiệu ứng lượng tử bắt đầu làm mạch chạy sai, nên không thể thu nhỏ mãi.

Thứ hai, quan trọng hơn: có những bài toán quá lớn với máy thường, và ví dụ rõ nhất chính là tự nhiên. *(Chỉ vào bàn cờ.)* Chắc mọi người biết chuyện hạt gạo trên bàn cờ: ô đầu một hạt, ô sau hai hạt, rồi bốn, rồi tám. Lúc đầu ít, nhưng riêng ô cuối cùng đã khoảng chín tỷ tỷ hạt. Dùng máy thường để giả lập một hệ lượng tử cũng y như vậy: thêm một hạt là số con số phải lưu tăng gấp đôi. 50 hạt đã cần khoảng một triệu tỷ con số. 300 hạt cần nhiều con số hơn cả số nguyên tử trong vũ trụ. Trong khi đó tự nhiên vẫn 'chạy' những hệ như vậy mỗi giây, trong từng phân tử.

Nên năm 1981, trong một bài giảng được đăng năm 1982, Richard Feynman đưa ra một ý rất đơn giản: nếu tự nhiên là lượng tử, hãy làm máy tính bằng chính các thành phần lượng tử. Lưu ý ngay từ đầu: máy tính lượng tử là máy chuyên dụng cho một số bài toán, không phải laptop nhanh hơn."

## Slide 3 — Bit vs qubit

"*(Chỉ vào công tắc.)* Bit thường giống công tắc đèn: hoặc 0, hoặc 1.

*(Chỉ vào quả cầu.)* Qubit thì nên hình dung như một mũi tên trên quả bóng. Chỉ thẳng lên là 0. Chỉ thẳng xuống là 1. Mũi tên chỉ lưng chừng ở đâu đó thì qubit là một hỗn hợp của 0 và 1.

Mỗi phần trong hỗn hợp có một trọng số. Trọng số của 0 càng lớn thì càng dễ đọc ra 0. Các bạn sẽ thấy người ta viết hai trạng thái cơ bản là |0⟩ và |1⟩. Đừng lo về dấu ngoặc, nó chỉ là thẻ tên.

Bảng này tóm lại: qubit chứa được nhiều hơn bit. Nhưng đọc nó thì ra ngẫu nhiên, đọc xong nó bị thay đổi, và không copy được. Mấy khác biệt này chi phối toàn bộ phần sau."

## Slide 4 — Superposition

"Hỗn hợp 0 và 1 như vậy gọi là chồng chập. Điểm bất ngờ là trọng số có thể dương *hoặc âm*. Xác suất bình thường thì không bao giờ âm: không ai nói 'khả năng mưa là âm 30%'. Trọng số lượng tử thì âm được, và chính chi tiết nhỏ này làm nên máy tính lượng tử.

*(Chỉ vào hai cặp cột.)* Hai ví dụ quan trọng nhất tên là plus và minus. Plus có trọng số của 0 và 1 bằng nhau, cả hai đều dương. Minus cũng có hai trọng số bằng nhau, nhưng một cái âm. Đọc cái nào cũng ra 0 một nửa số lần, ra 1 một nửa số lần. Vậy chúng giống nhau à? Không. Đây là hai trạng thái khác nhau, và hai slide nữa mình sẽ chứng minh.

*(Chỉ vào cái cốc và quả cầu.)* Có hai hiểu lầm hay gặp. Một: chồng chập không phải đồng xu bị úp dưới cốc, thật ra đã sấp hoặc ngửa từ trước, chỉ là mình chưa nhìn. Nếu đúng như vậy thì plus và minus phải giống hệt nhau. Hai: máy lượng tử không 'thử mọi đáp án cùng lúc' rồi đưa hết cho mình. Đọc ra thì chỉ được một đáp án, phần còn lại mất."

## Slide 5 — Picturing a qubit

"*(Chỉ vào quả cầu.)* Hình này gọi là mặt cầu Bloch. Nó chính là mũi tên ở slide 3, vẽ cho đầy đủ. Cực bắc là 0, cực nam là 1, và đường xích đạo chứa tất cả các hỗn hợp năm mươi–năm mươi, trong đó có plus và minus.

Độ cao của mũi tên cho biết khả năng: càng gần cực bắc càng dễ đọc ra 0. Hướng quay quanh quả cầu gọi là pha, và dấu cộng–trừ nằm ở đây. Plus và minus cùng độ cao nhưng nằm ở hai phía đối diện của xích đạo.

*(Chỉ vào la bàn.)* Ý quan trọng: nếu chỉ hỏi '0 hay 1?' thì mình chỉ kiểm tra độ cao. Plus và minus đều ra năm mươi–năm mươi, trông giống hệt nhau. Nhưng nếu hỏi được 'đông hay tây?' thì plus luôn trả lời đông, minus luôn trả lời tây. Vậy pha là thông tin thật, chỉ là cách đọc thông thường không nhìn thấy nó. Ở phần 2, các bạn sẽ thấy cổng lượng tử thực chất chỉ là cách xoay mũi tên này. Một hạn chế: hình này chỉ dùng được cho một qubit."

## Slide 6 — Reading a qubit

"Đọc, hay đo, một qubit là quy tắc lạ nhất, nên mình nói ba ý.

Một, kết quả ngẫu nhiên. Dù biết qubit chính xác đến đâu, mình cũng chỉ nói được khả năng, không bao giờ đoán trước được một lần đọc cụ thể. Đó không phải do máy kém, mà là cách tự nhiên vận hành.

Hai, sụp đổ. *(Chỉ vào mũi tên bật về cực.)* Đọc xong, qubit trở thành đúng đáp án vừa đọc. Đọc plus ra 0 thì từ đó qubit chỉ còn là 0. Hỗn hợp, kể cả dấu, mất hẳn.

Ba, quan trọng nhất với tính toán. *(Chỉ vào kho và cửa.)* Một nhóm n qubit chứa bên trong 2 mũ n trọng số, một kho khổng lồ, nhưng đọc ra chỉ được n bit. Giống một nhà kho rất lớn mà chỉ có một cánh cửa rất nhỏ.

Đây là kết quả nhóm chạy trên simulator, mỗi trạng thái 1.024 lần. Trạng thái 0 lần nào cũng ra 0. Plus ra khoảng 51–49. Minus cũng ra y như vậy. Đọc thẳng thì không phân biệt được plus với minus. Và vì mỗi lần chạy chỉ ra một đáp án ngẫu nhiên, chương trình lượng tử luôn phải chạy hàng nghìn lần."

## Slide 7 — Interference

"Giờ đến mẹo làm nên mọi thứ. *(Chỉ vào sóng nước.)* Hãy nghĩ tới hai con sóng nước gặp nhau. Cùng nhịp thì dồn thành sóng to hơn. Ngược nhịp thì triệt tiêu, mặt nước phẳng lặng. Trọng số lượng tử cư xử đúng như vậy.

*(Chỉ vào hai đường đi.)* Mình thêm một bước nữa ngay trước khi đọc: một cổng tên là H. Sau bước này, mỗi kết quả có thể tới theo hai đường, mỗi đường mang trọng số một nửa. Với plus, cả hai nửa đều dương: một nửa cộng một nửa bằng một, nên lần nào cũng đọc ra 0. Với minus, một nửa bị âm: một nửa trừ một nửa bằng không, nên không bao giờ ra 0, lần nào cũng ra 1.

Kết quả chạy xác nhận: một trăm phần trăm và một trăm phần trăm. Năm mươi–năm mươi đã thành chắc chắn. Vậy plus và minus thật sự khác nhau, và cái dấu ẩn kia là có thật.

Đây là trái tim của tính toán lượng tử. Xác suất thường chỉ cộng dồn được. Trọng số lượng tử thì triệt tiêu được. Thuật toán lượng tử sắp xếp các đường đi sao cho đáp án sai tự xóa nhau, còn đáp án đúng được dồn lên. [Người 2] sẽ cho các bạn thấy đúng điều đó."

## Slide 8 — From one qubit to many

"*(Chỉ vào bảng tổ hợp.)* Một qubit có hai kết quả. Hai qubit có bốn: 00, 01, 10, 11. Ba qubit có tám. Mỗi qubit thêm vào làm danh sách dài gấp đôi, và mỗi tổ hợp có trọng số riêng. Đây chính là chuyện nhân đôi trên bàn cờ ở slide 2.

Giờ phân biệt một điều quan trọng. Nếu các qubit độc lập, mình mô tả riêng từng cái được, máy thường xử lý dễ dàng. Nhưng các qubit cũng có thể liên kết chặt đến mức chỉ mô tả được cả nhóm cùng lúc. Khi đó mình thật sự cần đủ 2 mũ n trọng số. Liên kết đó gọi là rối lượng tử, và đó là một lý do lớn khiến máy lượng tử khó giả lập đến vậy."

## Slide 9 — Entanglement

"Cặp rối đơn giản nhất gọi là cặp Bell. [Người 2] sẽ cho các bạn thấy công thức hai bước để tạo ra nó; giờ mình xem nó làm được gì.

Nhìn kết quả chạy. Bên trái là hai qubit độc lập: cả bốn kết quả đều xuất hiện khoảng một phần tư số lần. Bên phải là cặp rối: chỉ có 00 và 11, không bao giờ có 01 hay 10.

*(Chỉ vào An và Bình ở xa nhau.)* Vậy nếu mình đọc qubit của mình ra 0, qubit của bạn cũng ra 0, dù bạn đã mang nó đi xa cả nghìn cây số. Điều lạ là mỗi qubit riêng lẻ lại hoàn toàn ngẫu nhiên. Không qubit nào 'giữ' đáp án. Thông tin nằm ở mối liên kết giữa hai qubit.

Và không, cách này không gửi tin nhanh hơn ánh sáng được. Mỗi bên chỉ thấy một dãy 0 và 1 ngẫu nhiên. Sự trùng khớp chỉ lộ ra khi hai bên so danh sách với nhau qua điện thoại hay email."

## Slide 10 — Stronger than any ordinary link

"Một phản bác hợp lý, và chính Einstein nêu ra năm 1935. *(Chỉ vào găng tay.)* Bỏ một đôi găng vào hai hộp rồi gửi đi hai nơi. Mở một hộp thấy găng trái là biết ngay hộp kia găng phải. Chẳng có gì bí ẩn: đáp án đã cố định từ đầu. Biết đâu các hạt rối cũng chỉ như vậy.

Năm 1964, John Bell tìm ra cách kiểm tra điều này, và phiên bản đơn giản nhất là một trò chơi. *(Chỉ vào sơ đồ trò chơi.)* An và Bình ngồi hai phòng riêng. Trọng tài đưa mỗi người câu hỏi A hoặc B một cách ngẫu nhiên. Mỗi người trả lời 0 hoặc 1, không được nói chuyện. Họ thắng nếu hai câu trả lời giống nhau, trừ khi cả hai cùng nhận câu B, lúc đó hai câu trả lời phải khác nhau.

Trước khi chơi, họ được bàn chiến thuật thoải mái. Đó chính là ý tưởng găng tay: đáp án định sẵn từ trước. Và hóa ra mọi kế hoạch kiểu đó thắng tối đa 75%, vì bốn yêu cầu mâu thuẫn nhau, không thể thỏa mãn cả bốn. Dùng một cặp qubit rối thì họ thắng khoảng 85%. Mô phỏng của nhóm ra 85,1%, lý thuyết là 85,4%.

Thí nghiệm thật đã xác nhận điều này nhiều lần, và được giải Nobel Vật lý năm 2022. Vậy rối lượng tử không phải đáp án định sẵn, mà là một tài nguyên thật sự mới."

## Slide 11 — No-cloning

"Quy tắc cuối cùng, và là quy tắc dân dữ liệu quan tâm nhất: không thể copy một qubit chưa biết.

*(Chỉ vào máy photocopy.)* Tại sao? Hãy tưởng tượng một cái máy copy hoàn hảo 0 và 1. Giờ đưa vào một hỗn hợp. Các quy luật lượng tử buộc chính cái máy đó tạo ra một cặp rối lượng tử, chứ không phải hai bản sao của hỗn hợp. Điều này được chứng minh năm 1982 và gọi là định lý không sao chép (no-cloning). Cũng không thể ăn gian bằng cách đọc qubit trước rồi dựng lại, vì một lần đọc chỉ cho một bit và phá luôn hỗn hợp. Bit thường chỉ là 0 và 1, loại máy đó copy được bình thường, nên dữ liệu thường copy bao nhiêu lần cũng được.

*(Chỉ vào An, Bình và kẻ nghe lén.)* Quy tắc này có mặt tốt. Nếu một kẻ nghe lén chen vào đường truyền tín hiệu lượng tử, cô ta không thể lặng lẽ copy. Cô ta buộc phải đọc, và đọc thì làm tín hiệu bị xáo trộn. An và Bình chỉ cần so một phần nhỏ kết quả, thấy có lỗi là biết có người nghe lén. Đó là nền tảng của phân phối khóa lượng tử (QKD).

Và có mặt xấu cho Big Data: không sao lưu, không nhân bản, không cache được dữ liệu lượng tử. Phúc sẽ quay lại ý này."

## Slide 12 — Three quantum resources

"Tóm lại phần 1: tính toán lượng tử dựa trên ba tài nguyên. Chồng chập mở ra 2 mũ n khả năng. Rối lượng tử liên kết các qubit thành một hệ lớn nhanh đến mức máy thường sớm không giả lập nổi. Giao thoa đẩy khả năng về phía đáp án đúng.

Và hai quy tắc phải chấp nhận: đọc ra chỉ được một bit cho mỗi qubit, và qubit không copy được.

Vậy câu hỏi thật sự là dùng các tài nguyên này để tính ra thứ gì đó có ích như thế nào. Mời [Người 2] trình bày về cổng và mạch lượng tử."

---

### Phân tuyến Q&A
Khái niệm → Người 1 (phần này) · thuật toán & demo → Người 2 · ứng dụng & phần cứng → Phúc.
Trả lời bằng lời thường trước. Công thức trong ngoặc chỉ dùng khi người hỏi muốn đi sâu.

| Câu hỏi dự kiến | Ý trả lời |
|---|---|
| Qubit có thật sự "vừa 0 vừa 1" không? | Không theo nghĩa đời thường. Nó ở một trạng thái thứ ba: hỗn hợp có trọng số và có dấu. Bằng chứng là plus và minus cùng ra 50/50, nhưng thêm một bước H thì phân biệt được 100% (slide 7). |
| Vì sao không đọc hết 2ⁿ trọng số ra? | Đọc chỉ trả về n bit và phá trạng thái. Muốn ước lượng trọng số phải chạy lại rất nhiều lần. Vì vậy thuật toán dùng giao thoa để dồn đáp án về một chỗ trước khi đọc. |
| Pha là gì? | Là dấu, tổng quát hơn là "hướng", của trọng số. Đọc thẳng thì không thấy, nhưng nó quyết định các trọng số cộng dồn hay triệt tiêu. Trên mặt cầu Bloch, pha là hướng quay quanh xích đạo. |
| Ngẫu nhiên lượng tử có thật, hay chỉ là mình chưa biết đủ? | Trò chơi của Bell (slide 10) loại bỏ khả năng "đáp án định sẵn". Ngẫu nhiên này là bản chất, và còn được dùng để tạo số ngẫu nhiên thật. |
| Rối có gửi tin nhanh hơn ánh sáng không? | Không. Mỗi bên chỉ thấy bit ngẫu nhiên. Sự trùng khớp chỉ lộ ra khi so kết quả qua kênh bình thường. |
| Chồng chập và rối khác nhau thế nào? | Chồng chập có ở một qubit: một qubit giữ 0 và 1 cùng lúc. Rối cần từ hai qubit trở lên: cả nhóm chỉ mô tả được chung, không tách riêng. Hai qubit plus độc lập thì chồng chập nhưng không rối. Cặp Bell thì rối. |
| Sao ½ + ½ lại ra "luôn luôn"? | Khả năng đọc ra một kết quả bằng bình phương trọng số. Tổng trọng số bằng 1 nên khả năng là 1, tức 100%. (Nếu cần: plus = (\|0⟩ + \|1⟩)/√2, và (1/√2)² = ½, nên mỗi bên 50%.) |
| Trọng số âm thì có nghĩa vật lý gì? | Giống hai con sóng ngược nhịp. Riêng một con sóng thì dấu không quan trọng, nhưng khi hai con gặp nhau thì dấu quyết định chúng mạnh lên hay triệt tiêu. |
| Không copy được thì sửa lỗi kiểu gì? | Dùng mã sửa lỗi lượng tử: trải thông tin của một qubit ra nhiều qubit rối, rồi kiểm tra "triệu chứng lỗi" mà không đọc dữ liệu. Phúc nói thêm ở phần phần cứng (qubit logic). |
| Kết quả mô phỏng có đáng tin không? | Đây là simulator lý tưởng (Qiskit Aer), không có nhiễu. Số liệu khớp lý thuyết (50/50, 100%, 85,4%). Máy thật có nhiễu nên con số sẽ lệch một chút. |
