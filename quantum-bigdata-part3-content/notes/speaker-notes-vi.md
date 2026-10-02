# Speaker notes — Tiếng Việt (bản luyện nói)

20 slide · ~10–11 phút + Q&A · Người trình bày: Phúc. Chữ in nghiêng trong ngoặc là ghi chú cho người nói, không đọc ra. Thay [Người 1] / [Người 2] bằng tên thật.

## Slide 1 — Quantum × Big Data (bìa) · ~0:10
"Cảm ơn [Người 2]. Các bạn vừa thấy Grover tìm ra đáp án mà không cần quét từng phần tử. Với môn Big Data, câu hỏi tự nhiên là: điều đó giúp gì cho dữ liệu lớn thật? Trong khoảng mười phút tới, mình sẽ nói về bốn điểm mà máy lượng tử chạm tới dữ liệu, hai nút thắt đang chặn chúng lại, và phần cứng năm 2026 thực sự đang ở đâu."

## Slide 2 — From the demo to real data · ~0:25
"Đây là kết quả của demo vừa rồi. Ba qubit cho ta tám chuỗi có thể có, từ 000 đến 111, tức tám bản ghi. Nhóm chạy mạch 1.024 lần; mỗi lần chạy gồm hai vòng Grover rồi đo một lần, và đếm xem mỗi chuỗi xuất hiện bao nhiêu lần. Kết quả là khoảng 93% số lần đo rơi đúng vào bản ghi bí mật 101, trong khi bảy bản ghi còn lại gần như bằng không. Máy tìm ra đáp án mà không phải mở từng bản ghi ra xem.

Nhưng tám bản ghi thì quá nhỏ. Câu hỏi thật là: với một bảng có một nghìn tỷ dòng, máy lượng tử thực sự mang lại gì?"

*(Nếu bị hỏi vì sao 93% mà không phải 94,5% như lý thuyết: phép đo là ngẫu nhiên, giống tung đồng xu 100 lần không chắc ra đúng 50 lần ngửa. Hai vòng quyết định xác suất trúng; 1.024 lần chạy chỉ để đếm kết quả.)*

## Slide 3 — Why quantum meets big data · ~0:30
"Sức hút của máy lượng tử bắt đầu từ một con số. Muốn mô tả trạng thái của n qubit, ta cần 2 mũ n con số biên độ, và cứ thêm một qubit thì con số này gấp đôi. Trục đứng của biểu đồ dùng thang log, nên đường 2 mũ n hiện ra như một đường thẳng dốc đều.

Chỉ 50 qubit đã cần khoảng 10 mũ 15 con số để mô tả, ngang quy mô một kho dữ liệu lớn. 300 qubit thì vượt cả số nguyên tử trong vũ trụ quan sát được, đường nét đứt trên hình.

Nhưng điểm mạnh không nằm ở chỗ 'lưu được nhiều giá trị'. Điểm mạnh là các biên độ này có thể âm, nên các đáp án sai có thể triệt tiêu nhau còn đáp án đúng thì cộng hưởng lên. Và khi đo, ta vẫn chỉ đọc được 50 bit. Nên đây mới là tiềm năng."

## Slide 4 — Data task → quantum tool · ~0:25
"Phần lớn công việc phân tích dữ liệu quy về bốn dạng toán. Tìm một bản ghi trong bảng thì có thuật toán Grover. Phân loại và học máy thì có quantum kernel và mạch biến phân. Hồi quy, PCA và giải hệ phương trình thì có thuật toán HHL. Còn lập lịch, chọn đặc trưng và phân cụm, tức chọn phương án tốt nhất trong vô số phương án, thì có QAOA và quantum annealing.

Mình sẽ đi lần lượt từng dòng, rồi giải thích vì sao đến giờ chưa cái nào thay được Spark hay Hadoop."

## Slide 5 — Quantum search over a database · ~0:55
"Hình bên trái lấy từ sách của Nielsen và Chuang. CPU nằm riêng, bộ nhớ nằm riêng, và CPU chỉ lấy dữ liệu bằng lệnh LOAD, từng ô một. Với một bảng chưa sắp xếp, máy thường phải dò trung bình một nửa bảng, còn Grover chỉ cần cỡ căn bậc hai số bản ghi.

Lấy một bảng một nghìn tỷ bản ghi. Máy thường dò trung bình năm trăm tỷ lần. Grover chỉ cần khoảng 790 nghìn vòng, nghe rất ấn tượng.

Nhưng cơ sở dữ liệu thật luôn có index, tức dữ liệu đã được sắp xếp. Khi đó ta tìm như tra từ điển: mở giữa, bỏ đi một nửa, cứ thế tiếp tục. Chỉ khoảng 40 lần chia đôi là tới đúng bản ghi, nhanh hơn cả Grover. Nên Grover chỉ có ích với những truy vấn mà không index nào hỗ trợ được. Và còn một câu hỏi về phần cứng mà lát nữa mình sẽ quay lại."

## Slide 6 — Quantum machine learning · ~0:40
"Hướng thứ hai, và cũng là hướng được nhắc tới nhiều nhất, là học máy lượng tử. Ý tưởng chung là đưa dữ liệu vào không gian trạng thái của các qubit, nơi có rất nhiều chiều, để dễ tách các nhóm dữ liệu ra hơn. Có hai cách tiếp cận chính.

Cách thứ nhất là quantum kernel. Ở đây máy lượng tử chỉ làm đúng một việc: đo xem hai điểm dữ liệu giống nhau đến đâu, cho ra một con số từ 0 đến 1. Sau đó, toàn bộ các con số này được giao cho một thuật toán cổ điển quen thuộc là SVM để vẽ ranh giới giữa các nhóm. Nhóm nghiên cứu của IBM công bố cách này trên tạp chí Nature năm 2019.

Cách thứ hai là mạch biến phân. Các bạn có thể hình dung nó như một mạng neural, nhưng các 'trọng số' là góc quay của các cổng lượng tử. Mạch này ngắn, nên chạy được ngay trên máy lượng tử còn nhiễu hiện nay, và các bạn có thể tự thử bằng Qiskit hoặc PennyLane.

Slide tiếp theo sẽ cho thấy cách thứ hai được huấn luyện ra sao, và sau đó là kết quả khi nhóm mình tự chạy thử cách thứ nhất."

## Slide 7 — The hybrid loop · ~0:15
"Đây là cách mạch biến phân được huấn luyện. Nó là một vòng lặp gồm bốn bước. Đầu tiên, ta đưa dữ liệu vào một mạch lượng tử có các góc quay θ. Mạch chạy xong thì ta đo kết quả. Tiếp theo, một máy tính thường so kết quả đó với đáp án đúng, xem sai bao nhiêu, rồi quyết định chỉnh các góc θ theo hướng nào cho bớt sai. Sau đó quay lại chạy mạch với góc mới, và cứ lặp như vậy cho đến khi đủ tốt.

Các bạn có thể hình dung giống như dò đài trên một chiếc radio cũ: vặn núm một chút, nghe thử, còn rè thì vặn tiếp theo hướng đỡ rè hơn. Cái radio là mạch lượng tử, còn người nghe và quyết định vặn tiếp là máy tính thường.

Người ta gọi đây là mô hình lai vì hai loại máy chia nhau công việc: máy lượng tử chỉ chạy những mạch ngắn, còn phần 'học' thì máy thường đảm nhận. Nhờ vậy mà máy lượng tử còn nhiễu hiện nay vẫn dùng được. Nhóm mình đã tự chạy thử cách thứ nhất, quantum kernel. Kết quả như sau."

## Slide 8 — A real quantum kernel, measured · ~1:05
"Để xem quantum kernel làm được gì thật, nhóm mình đã tự chạy một thí nghiệm nhỏ.

Dữ liệu ở giữa slide là bộ two-moons: 120 điểm chia thành hai nhóm, xếp thành hai vầng trăng khuyết lồng vào nhau. Đây là bài kiểm tra kinh điển, vì không thể kẻ một đường thẳng chia đôi hai nhóm này. Nhóm mình dùng 80 điểm để mô hình học, và giữ lại 40 điểm mô hình chưa từng thấy để kiểm tra.

Hình bên trái là ma trận kernel, tức bảng độ giống nhau giữa từng cặp điểm mà máy lượng tử tính ra. Các điểm đã được xếp theo nhóm, và hai đường nét đứt chia chỗ đổi nhóm. Nếu kernel tốt, các cặp cùng nhóm sẽ rất giống nhau, nên hai khối chéo sẽ sáng rõ như một bàn cờ. Nhưng ở đây, các khối chỉ khác nhau mờ mờ, nghĩa là trong không gian lượng tử hai nhóm chưa tách nhau rõ.

Kết quả bên phải xác nhận điều đó. Trên 40 điểm kiểm tra, quantum kernel đoán đúng 90%. Trong khi đó, SVM tuyến tính, cách đơn giản nhất, đạt 92,5%, còn kernel RBF cổ điển phổ biến đạt 97,5%. Cả ba đều dùng cùng dữ liệu, và các kernel cần chỉnh đều được chỉnh như nhau.

Vậy trên dữ liệu cổ điển này, quantum kernel không thắng. Điều đó không có nghĩa là ý tưởng thất bại. Nó có nghĩa là mỗi khi nghe một tuyên bố về lợi thế lượng tử, ta luôn phải hỏi: so với cái gì?"

*(Nếu bị hỏi thí nghiệm có công bằng không: "Dữ liệu nhỏ và chạy trên simulator, nên đây chỉ là minh họa. Nhưng cả ba mô hình dùng cùng cách chia dữ liệu và cùng mức tinh chỉnh. Nếu không chỉnh, quantum kernel chỉ đạt 77,5%.")*

## Slide 9 — HHL: exponential speedup, on paper · ~0:30
"Dòng thứ ba trong bảng là hồi quy, PCA và giải hệ phương trình. Nghe thì khác nhau, nhưng bên dưới cả ba đều quy về một bài toán: giải hệ Ax = b, giống ví dụ tìm giá táo và cam từ hai lần mua. Với dữ liệu lớn, hệ này có hàng triệu ẩn.

Năm 2009, ba tác giả Harrow, Hassidim và Lloyd đề xuất thuật toán lượng tử HHL cho bài toán này. Hai công thức trên slide so sánh chi phí. Cách cổ điển tốt, gọi là conjugate gradient, tốn cỡ N nhân s nhân κ, tăng theo số ẩn N. HHL tốn cỡ log N nhân s bình phương nhân κ bình phương chia ε, tức chỉ tăng theo log N. Đây là tăng tốc theo cấp số mũ, nên HHL từng làm giới Big Data rất hào hứng.

Biểu đồ minh họa sự khác biệt đó. Đường trắng là chi phí cổ điển, đi lên đều theo N. Đường xanh là HHL, gần như nằm phẳng, dù N tăng tới một nghìn tỷ.

Nhưng hãy nhìn đường nét đứt. HHL không trả về danh sách N con số nghiệm, mà trả về một trạng thái lượng tử. Muốn đọc hết từng con số ra thì phải đo đi đo lại rất nhiều lần, và chi phí lại quay về cỡ N, bằng cổ điển. Nên chữ 'on paper' trên tiêu đề có ý nghĩa: tăng tốc mũ chỉ đúng trên giấy, và đi kèm bốn điều kiện ở slide sau."

*(Nếu bị hỏi ký hiệu: "s là số ô khác 0 trên mỗi hàng của ma trận, κ đo độ nhạy của nghiệm, ε là độ chính xác mong muốn.")*

## Slide 10 — Four conditions attached · ~0:30
"Muốn HHL thật sự nhanh thì bài toán phải thỏa bốn điều kiện.

Thứ nhất, ma trận A phải thưa và ổn định. Thưa nghĩa là mỗi phương trình chỉ dính tới vài ẩn, chứ không phải tất cả. Ổn định nghĩa là con số κ nhỏ: nếu dữ liệu đầu vào lệch một chút thì nghiệm cũng chỉ lệch một chút. Khi κ lớn, ví dụ dữ liệu có hai cột gần trùng nhau, chi phí HHL tăng rất nhanh.

Thứ hai, vector b phải nạp nhanh vào máy lượng tử. Nếu b là một bảng dữ liệu lớn, riêng việc nạp đã tốn cỡ N bước. Điều kiện này sẽ quay lại ở phần nút thắt.

Thứ ba, đầu ra là một trạng thái lượng tử, không phải danh sách nghiệm. Mỗi lần đo chỉ cho ra một kết quả ngẫu nhiên, nên muốn đọc đủ N con số thì phải chạy lại và đo cỡ N lần trở lên.

Thứ tư, vì vậy HHL chỉ hữu ích khi ta cần một con số tóm tắt từ nghiệm, chứ không cần toàn bộ nghiệm. Ví dụ trong một lưới điện, ta chỉ cần biết tổng công suất tổn hao, chứ không cần điện áp ở từng nút.

Bài toán dữ liệu thật thường vi phạm ít nhất một trong bốn điều kiện này, nên lợi thế của HHL rất khó giữ được trong thực tế."

## Slide 11 — Quantum optimization · ~0:35
"Dòng cuối cùng trong bảng là tối ưu hóa. Nhiều việc trong dữ liệu có dạng: chọn ra phương án tốt nhất trong vô số phương án. Ví dụ có 50 cột dữ liệu và muốn chọn ra tập cột tốt nhất để dự đoán: mỗi cột chọn hoặc không chọn, nên có tới 2 mũ 50 cách chọn, không thể thử hết. Lập lịch, phân cụm hay tìm tuyến đường cũng vậy. Nhiều bài toán kiểu này viết được dưới một dạng chuẩn gọi là QUBO: mỗi biến là có hoặc không, và ta tìm tổ hợp cho điểm tốt nhất.

Có hai hướng lượng tử cho loại bài toán này. Hướng thứ nhất là QAOA, do Farhi và cộng sự đề xuất năm 2014. Nó là thuật toán lai, giống vòng lặp ở slide 7: mạch lượng tử ngắn xen kẽ hai loại lớp, còn máy thường thì chỉnh tham số. Vì mạch ngắn nên nó được thiết kế cho máy còn nhiễu hiện nay.

Hướng thứ hai là quantum annealing, mà hãng D-Wave đã làm thành máy thật với hàng nghìn qubit. Hình dung bài toán như một vùng đồi núi, và đáp án tốt nhất là thung lũng sâu nhất. Máy để hệ lượng tử từ từ 'lắng xuống' về phía thung lũng đó. Nhưng máy này chỉ chuyên cho tối ưu, không phải máy tính lượng tử đa dụng.

Dòng dưới cùng là phần nói thật: đến giờ, chưa có bằng chứng rõ ràng rằng hai hướng này thắng được các phương pháp cổ điển tốt nhất trên bài toán thực tế. Và tới đây là điểm mấu chốt của cả phần này."

## Slide 12 — The catch · ~0:10
*(Dừng một nhịp để khán giả đọc hết câu trên màn hình rồi mới nói.)*

"Mọi tăng tốc mình vừa trình bày, từ Grover, học máy lượng tử, HHL cho tới tối ưu hóa, đều ngầm giả định một điều: dữ liệu đã nằm sẵn bên trong máy lượng tử, ở dạng mà máy có thể xử lý cùng lúc. Nhưng dữ liệu lớn thật thì nằm trên ổ cứng, dưới dạng bit bình thường. Một nghìn tỷ bản ghi đâu có tự nhiên xuất hiện bên trong qubit. Vậy câu hỏi là: dữ liệu lớn đi vào máy lượng tử bằng cách nào?"

## Slide 13 — Bottleneck 1: loading the data · ~0:50
"Để Grover hỏi được nhiều bản ghi cùng lúc, máy lượng tử cần một loại bộ nhớ đặc biệt tên là QRAM. Với bộ nhớ thường, ta đưa vào một địa chỉ, ví dụ ô số 5, và nhận về đúng bản ghi ở ô số 5. Với QRAM, địa chỉ đưa vào ở dạng chồng chập, tức chỉ vào nhiều ô cùng lúc, và bộ nhớ trả về dữ liệu của tất cả các ô đó cùng lúc.

Hình bên phải lấy từ sách của Nielsen và Chuang, cho thấy cách xây QRAM cho một bộ nhớ 32 ô. Hãy hình dung một tòa nhà có 32 phòng. Từ cửa vào, hành lang cứ chia đôi liên tục, và ở mỗi ngã rẽ có một công tắc lượng tử, do một qubit của địa chỉ điều khiển: bit là 0 thì rẽ trái, bit là 1 thì rẽ phải. Khi địa chỉ ở dạng chồng chập, tín hiệu rẽ cả hai hướng cùng lúc, nên đi tới được mọi phòng.

Vấn đề là số công tắc. Bộ nhớ có bao nhiêu ô thì cây phải có cỡ bấy nhiêu ngã rẽ. Sách tính ra cần cỡ N log N công tắc lượng tử, tức gần bằng lượng phần cứng để lưu chính cơ sở dữ liệu. Với một nghìn tỷ bản ghi, ta cần cỡ một nghìn tỷ công tắc lượng tử, và tất cả phải giữ được trạng thái lượng tử không bị nhiễu. Trong khi đó, chip mạnh nhất hiện nay chỉ có khoảng một trăm qubit.

Nếu không có QRAM thì ta phải nạp từng bản ghi một vào máy, tốn cỡ N bước. Mà N bước thì đã bằng hoặc hơn thời gian máy thường dò hết cả bảng, nên tăng tốc của Grover hay HHL mất sạch. Đến nay, chưa ai xây được một QRAM lớn và chịu được nhiễu."

## Slide 14 — Nielsen & Chuang's conclusion · ~0:20
"Đây không phải ý kiến riêng của nhóm mình. Chính hai tác giả của cuốn giáo trình chuẩn về máy tính lượng tử cũng kết luận như vậy. Theo họ, công dụng chính của Grover có lẽ không phải là tìm kiếm trong cơ sở dữ liệu cổ điển, mà là tìm lời giải cho những bài toán khó như SAT hay bài toán người du lịch.

Lý do là với những bài toán đó, ta không cần nạp một bảng dữ liệu khổng lồ vào máy. Ta chỉ cần một mạch nhỏ để kiểm tra một lời giải có đúng luật hay không, còn các phương án thì đã nằm sẵn trong không gian của các qubit. Nhờ vậy mà tránh được nút thắt ở slide trước.

Đó là nút thắt thứ nhất. Nút thắt thứ hai nằm ở cách người ta công bố các tuyên bố về tăng tốc."

*(Nếu bị hỏi SAT là gì: "SAT là bài toán tìm cách gán đúng hoặc sai cho các biến sao cho thỏa mọi luật cho trước. Kiểm tra một cách gán thì nhanh, nhưng số cách gán thì khổng lồ.")*

## Slide 15 — Bottleneck 2: the fine print · ~0:55
"Nút thắt thứ hai là những điều kiện mà các bài báo thường để ở 'phần chữ nhỏ'. Slide này kể câu chuyện đó qua bốn mốc thời gian.

Năm 2009, HHL ra đời với lời hứa tăng tốc theo cấp số mũ, nhưng kèm những điều kiện rất chặt, như ta vừa thấy ở slide 10.

Năm 2015, nhà khoa học máy tính Scott Aaronson viết một bài trên tạp chí Nature Physics, tên đúng là 'Read the fine print', tức 'hãy đọc phần chữ nhỏ'. Ông liệt kê các điều kiện về dữ liệu đầu vào, về ma trận và về đầu ra mà các thuật toán học máy lượng tử ngầm cần.

Năm 2016, Kerenidis và Prakash công bố một thuật toán lượng tử cho hệ gợi ý, kiểu Netflix gợi ý phim cho bạn. Thuật toán này từng được xem là ví dụ tiêu biểu về tăng tốc mũ của học máy lượng tử.

Năm 2018, Ewin Tang, một sinh viên 18 tuổi, định chứng minh rằng máy tính thường không thể làm được như vậy. Nhưng cuối cùng cô lại tìm ra một thuật toán cổ điển nhanh gần bằng, với điều kiện máy cổ điển được truy cập dữ liệu theo cùng cách mà thuật toán lượng tử được giả định. Sau đó, nhiều thuật toán học máy lượng tử khác cũng bị 'giải lượng tử hóa' theo cách tương tự.

Bài học ở dòng cuối: khi cho máy cổ điển cùng giả định về dữ liệu, lợi thế lượng tử thường co lại rất nhiều. Điều này cũng giống hệt thí nghiệm kernel của nhóm mình: so công bằng thì quantum không còn thắng."

## Slide 16 — Hardware in 2026 · ~0:50
"Vậy phần cứng hiện nay đang ở đâu? Trong nhiều năm, ta ở giai đoạn mà người ta gọi là NISQ: máy có từ vài chục tới vài trăm qubit, nhưng rất nhiễu, nên chỉ chạy được những mạch ngắn. Bước ngoặt hiện nay là chuyển từ qubit vật lý sang qubit logic. Nghĩa là ghép nhiều qubit vật lý hay bị lỗi lại với nhau, dùng mã sửa lỗi, để tạo ra một qubit đáng tin cậy.

Bảng trên slide tóm tắt bốn hướng phần cứng chính. Google dùng công nghệ siêu dẫn. Tháng 12 năm 2024, chip Willow với 105 qubit lần đầu cho thấy khi mã sửa lỗi lớn lên thì lỗi lại giảm xuống, điều trước đó chưa ai làm được. IBM cũng dùng siêu dẫn. Chip Nighthawk có 120 qubit, và IBM đặt mục tiêu năm 2029 có máy Starling với 200 qubit logic, chạy được 100 triệu cổng. IonQ và Quantinuum dùng bẫy ion. Hướng này nổi bật về độ chính xác, với cổng hai qubit đạt tới 99,99%. Pasqal và QuEra dùng nguyên tử trung hòa, có hàng trăm qubit. Tháng 5 năm 2026, qubit logic trên hướng này đã làm tốt hơn qubit vật lý trên một bài toán phương trình vi phân.

Nhưng cần nhìn con số cho đúng: 200 qubit logic vào năm 2029 vẫn còn rất xa so với lượng phần cứng cần để xử lý dữ liệu cỡ terabyte, tức lại quay về đúng nút thắt QRAM.

Dòng cuối là về chính sách. Năm 2024, NIST đã chuẩn hóa mật mã hậu lượng tử, để chuẩn bị cho ngày máy lượng tử đủ mạnh để phá RSA. Và một sắc lệnh của Mỹ vào tháng 6 năm 2026 đặt mục tiêu có máy lượng tử chịu lỗi vào năm 2028."

*(Kiểm tra lại các số liệu này một hai ngày trước buổi thuyết trình, vì mảng này thay đổi rất nhanh.)*

## Slide 17 — Hardware in 2026 (hai công nghệ) · ~0:20
"Slide này cho các bạn thấy hai công nghệ dẫn đầu trông như thế nào.

Bên trái là hình minh họa một chip siêu dẫn, hướng mà Google và IBM đang theo. Các chấm tròn là qubit, xếp thành một lưới trên chip, và các đường nối là để điều khiển và đọc kết quả. Chip này phải được làm lạnh tới gần độ không tuyệt đối, lạnh hơn cả ngoài không gian, thì qubit mới giữ được trạng thái lượng tử. Đây là hình vẽ minh họa, không phải ảnh chụp chip thật.

Bên phải là sơ đồ lấy từ sách Nielsen và Chuang, cho thấy một máy tính lượng tử bẫy ion, hướng của IonQ và Quantinuum. Mỗi qubit ở đây là một nguyên tử bị mất electron, tức một ion. Bốn chấm nhỏ ở giữa hình chính là bốn ion, được giữ lơ lửng trong chân không nhờ điện trường của các thanh điện cực hình trụ xung quanh. Người ta dùng tia laser chiếu vào từng ion để thực hiện các cổng lượng tử, rồi dùng cảm biến ánh sáng để đọc kết quả.

Hai cách làm rất khác nhau, nhưng đều chung một thách thức: giữ cho qubit không bị nhiễu đủ lâu để chạy xong phép tính."

## Slide 18 — Three takeaways · ~0:40
"Để kết lại phần của mình, có ba điều mình mong các bạn nhớ.

Thứ nhất, máy tính lượng tử là một bộ đồng xử lý, không phải thứ thay thế máy tính thường. Nó sẽ không thay laptop hay cụm Spark của các bạn. Nó chỉ mạnh ở một số lớp bài toán hẹp: mô phỏng các hệ lượng tử như phân tử, phân tích thừa số, và một số bài toán tìm kiếm hay tối ưu.

Thứ hai, với dữ liệu lớn, nút thắt không nằm ở tốc độ tính toán, mà nằm ở việc đưa dữ liệu vào máy và lấy kết quả ra. Như ta đã thấy với QRAM và với HHL, cả hai chiều vào và ra đều tốn cỡ N bước, và bài toán này đến nay vẫn chưa có lời giải.

Thứ ba, hãy luôn hỏi 'so với cái gì?'. Mỗi khi đọc một tin kiểu 'máy lượng tử nhanh hơn hàng triệu lần', hãy xem người ta so với phương pháp cổ điển nào, và với giả định gì về dữ liệu. Như thí nghiệm kernel của nhóm mình và câu chuyện của Ewin Tang, khi so công bằng thì lợi thế thường co lại rất nhiều. Việc thiết thực nhất lúc này là theo dõi mật mã hậu lượng tử, và nếu tò mò thì tự thử học máy lượng tử lai trên simulator."

## Slide 19 — References · ~0:05
"Nguồn chính của phần này là sách Nielsen và Chuang, cùng các bài báo gốc về HHL, quantum kernel, QAOA và kết quả của Ewin Tang."

## Slide 20 — Thank you / Questions? · Q&A
"Cảm ơn mọi người đã lắng nghe. Nhóm mình xin nhận câu hỏi."

*(Phân tuyến câu hỏi: khái niệm cơ bản → [Người 1]; thuật toán và demo → [Người 2]; ứng dụng và phần cứng → Phúc.)*

**Câu trả lời soạn sẵn**

*Bao giờ Big Data dùng được máy lượng tử?* "Cần có QRAM lớn và máy chịu lỗi. Các lộ trình hiện nay nhắm tới vài trăm qubit logic quanh năm 2030, vẫn còn rất xa dữ liệu cỡ terabyte. Những bài toán nhỏ nhưng khó, như mô phỏng phân tử hay tối ưu hóa, sẽ được hưởng lợi trước."

*Học máy lượng tử có tốt hơn deep learning không?* "Hiện chưa có lợi thế thực tế nào trên dữ liệu cổ điển. Chính thí nghiệm của nhóm mình cho quantum kernel 90% so với 97,5% của kernel cổ điển, và nhiều kết quả khác đã bị giải lượng tử hóa. Nghiên cứu hiện nay nhắm vào dữ liệu vốn đã là lượng tử, ví dụ từ cảm biến lượng tử hay mô phỏng hóa học."

*Sao không lưu dữ liệu thẳng vào qubit?* "Qubit mất trạng thái chỉ sau vài micro giây đến mili giây vì nhiễu. Và định lý no-cloning khiến ta không sao lưu được trạng thái lượng tử như sao lưu bit thường."

*Grover có phá được mã hóa AES không?* "Grover chỉ tăng tốc ở mức căn bậc hai, nên chỉ cần dùng khóa dài gấp đôi, ví dụ AES-256, là đủ an toàn. Mối đe dọa thật sự là thuật toán Shor đối với RSA và mật mã đường cong elliptic."

*"Quantum-inspired" là gì?* "Là những thuật toán cổ điển mượn ý tưởng từ thuật toán lượng tử, như kết quả của Ewin Tang. Chúng chạy được ngay trên máy tính bình thường."

*Làm sao biết đáp án để dừng Grover đúng lúc?* "Không cần biết đáp án. Số vòng chỉ phụ thuộc vào kích thước không gian tìm kiếm và số đáp án. Chạy đủ số vòng đó, đo một lần, rồi dùng luật để kiểm tra kết quả, việc kiểm tra này rất nhanh."

---

Trước buổi thuyết trình: thay [Người 1] / [Người 2] bằng tên thật · kiểm tra lại số liệu phần cứng ở slide 16 một hai ngày trước buổi thuyết trình.
