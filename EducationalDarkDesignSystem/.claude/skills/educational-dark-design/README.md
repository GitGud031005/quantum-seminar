# educational-dark-design: Design system cho slide HTML phong cách Educational Dark

Skill này giúp Claude (và AI khác) tạo slide HTML đúng phong cách template "Choosing a Career for Students" của Slidesgo (slide 1–35). Phong cách gồm nền xanh navy đậm `#0D1030`, tiêu đề xanh cyan `#79E0FF` font Signika, màu nhấn xanh dương `#0F5AFF` và xám `#C2C2C2`, chữ nội dung màu trắng, cùng các cụm hình học ở góc slide (phần tư hình tròn, vòng tròn rỗng, sọc chéo, lưới chấm, các vòng tròn đồng tâm).

## Cài đặt

### Cách 1 — Claude Code (qua repo, cả nhóm dùng chung)
1. Thư mục skill đã nằm sẵn ở `.claude/skills/educational-dark-design/` trong project này (tên thư mục chính là tên lệnh `/educational-dark-design`). Nếu copy sang repo khác, chép cả thư mục `educational-dark-design` vào `.claude/skills/` của repo đó.
2. `git pull` là có. Mở Claude Code trong repo, gõ `/` sẽ thấy `educational-dark-design`.
3. Nếu thư mục `.claude/skills/` được tạo lúc Claude Code đang mở → khởi động lại Claude Code một lần.
4. (Tuỳ chọn) Script kiểm tra tự dùng Chrome hoặc Edge có sẵn trên máy để chụp slide. Muốn xuất PDF bằng script thì cài thêm: `pip install playwright pillow && playwright install chromium`.

### Cách 2 — Ứng dụng Claude (claude.ai, desktop, Cowork)
1. Bật **Code execution** trong Settings → Capabilities.
2. Nén thư mục skill thành file zip (xem lệnh ở cuối trang), rồi vào **Customize → Skills → + → Create skill → Upload a skill** và chọn file zip đó.
3. Kiểm tra skill đang được bật trong danh sách Skills. Mỗi người tự upload vào tài khoản của mình.
4. Khi skill có bản mới: upload lại file zip mới (nếu ứng dụng báo trùng tên thì xoá bản cũ trước).

## Cách dùng

Chỉ cần yêu cầu tự nhiên, ví dụ:

> Tạo slide thuyết trình 20 phút từ nội dung trong docs/. Dùng skill educational-dark-design.

Claude sẽ lập dàn ý, chọn layout cho từng slide, ghép HTML từ các mẫu, chạy script kiểm tra rồi giao cho bạn một file `.html` duy nhất (khoảng 90 KB, phần lớn là hình hoạ tiết).

Khi trình chiếu: phím → / ← để chuyển slide, **F** để toàn màn hình, **O** để xem tổng quan, **P** để in hoặc lưu PDF.

> Font Signika, Lato và Nunito Sans được tải từ Google Fonts nên máy cần có mạng. Khi thuyết trình ở nơi không có mạng, hãy xuất PDF trước: `python3 scripts/export_pdf.py deck.html`, hoặc mở trong Chrome, nhấn Ctrl/Cmd+P, chọn Save as PDF, Margins: None và tick **Background graphics** (nếu không tick, nền navy sẽ mất).

> Vì font Lato không có đủ dấu tiếng Việt (ạ, ế, ộ…), deck có `<html lang="vi">` sẽ tự dùng Nunito Sans cho chữ nội dung. Deck tiếng Anh (`lang="en"`) dùng đúng Lato như template gốc.

## Cấu trúc

```
SKILL.md                 quy tắc thiết kế + quy trình, dành cho AI đọc
assets/starter.html      khung deck: token màu/chữ, sprite hoạ tiết (hình gốc từ PPTX), CSS của các layout, điều khiển trình chiếu
references/layouts.md    danh mục 34 layout kèm đoạn HTML mẫu (được sinh tự động)
examples/showcase.html   xem trước toàn bộ layout (được sinh tự động)
scripts/check_deck.py    kiểm tra màu/font/layout/hoạ tiết, chụp từng slide, phát hiện chữ tràn, đè lên hoạ tiết, hoặc slide bìa/chương/trích dẫn/cảm ơn bị lệch tâm
scripts/export_pdf.py    xuất PDF 16:9
src/snippets.html        nguồn của các layout mẫu
src/build.py             sinh lại references/layouts.md và examples/showcase.html
```

## Chỉnh sửa design system

1. Sửa CSS trong `assets/starter.html` hoặc sửa và thêm layout trong `src/snippets.html`. Mỗi layout bắt đầu bằng dòng `<!--@ id | Tên | Khi nào dùng -->`.
2. Chạy `python3 src/build.py` để sinh lại danh mục và trang showcase.
3. Chạy `python3 scripts/check_deck.py examples/showcase.html --render /tmp/check` rồi xem ảnh `contact-sheet.png`.
4. Nếu thêm layout mới với class `l-...` mới, nhớ thêm class đó vào `LAYOUTS` trong `scripts/check_deck.py`.
5. Hoạ tiết là hình vector lấy chính xác từ các layout của file PPTX gốc, nằm trong sprite `<svg class="sprite">` của `assets/starter.html`. Không sửa tay sprite; mỗi layout trong `src/snippets.html` dùng lại các dòng `<svg class="deco">…<use href="#m…"/></svg>` của layout nguồn tương ứng.

> Mỗi khi sửa skill, tạo lại file zip để upload lên ứng dụng Claude, ví dụ:
> `cd .claude/skills && zip -r ../../educational-dark-design.zip educational-dark-design -x "*.DS_Store" "*__pycache__*"` (xoá file zip cũ trước).
