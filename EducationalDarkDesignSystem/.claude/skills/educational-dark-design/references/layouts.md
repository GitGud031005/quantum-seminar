# Layout catalog

Every slide in a deck MUST be one of these layouts. Copy the snippet, keep the class names and every <svg class="deco"> motif line exactly; change only the text, numbers, images and (where the notes allow) item counts.
Live preview of all layouts: `examples/showcase.html` (press O for overview).

| # | id | Name | Use when |
|---|---|---|---|
| 1 | `cover` | Bìa (Cover) | Slide 1 of every deck. Title ≤ 2 lines (≤ 36 characters), optional keyword in white with .hl. Meta = team, advisor, date. |
| 2 | `toc` | Mục lục (Table of contents) | Right after the cover. 3–6 chapters (5 = source layout, 3 + 2). Heading ≤ 14 characters, description ≤ 10 words. |
| 3 | `whoa` | Mở đầu ấn tượng (Whoa!) | A one-word hook (≤ 10 characters) + one line: intro yourself, a surprising turn, "Tại sao?". |
| 4 | `section` | Chương (Section header, centered) | Opens each chapter listed in the TOC. Alternate with "section-alt". Title ≤ 18 characters. |
| 5 | `section-alt` | Chương – biến thể trái (Section header, number left) | Same role as "section", number left of a left-aligned title. |
| 6 | `text2` | Hai đoạn văn (Title + two paragraphs) | Context / background explained in two short paragraphs (≤ 35 words each), centered. |
| 7 | `bullets` | Gạch đầu dòng (Title + bullets) | Default content slide: one lead line + 3–5 bullets, ≤ 10 words each. |
| 8 | `steps` | Bốn bước đánh số (Numbered steps) | 3–4 parallel or sequential items. Set --n on .cols to the count. Heading ≤ 12 characters, text ≤ 18 words. |
| 9 | `zig2` | Hai ý so le (Two staggered items) | Two ideas, problem vs. solution, before vs. after. Heading ≤ 16 characters, text ≤ 25 words. |
| 10 | `zig3` | Ba ý so le (Three staggered items) | Three features / pillars / user groups. Heading ≤ 12 characters, text ≤ 15 words. |
| 11 | `zig4` | Bốn ý so le (Four staggered items) | Four stakeholders / principles / requirements. Heading ≤ 12 characters, text ≤ 10 words. |
| 12 | `five` | Năm ý (Five items, 3 + 2) | Five modules / requirements / tips. Heading ≤ 12 characters, text ≤ 10 words. |
| 13 | `statement` | Thông điệp lớn (Main point) | One punchline, ≤ 3 lines of ≤ 18 characters. |
| 14 | `focus` | Nhấn mạnh (Accent / pacing slide) | A pause on the one idea the audience must remember, on a blue canvas: "The catch", a key finding, a turning point. Use sparingly (about one per section, never two in a row). Eyebrow ≤ 20 characters, idea ≤ 90 characters (≤ 3 lines), follow-up ≤ 12 words. Class "accent" also works on whoa and quote slides. |
| 15 | `quote` | Trích dẫn (Quote) | A quote from a user interview, expert or advisor. ≤ 25 words. |
| 16 | `photo` | Ảnh toàn trang (Full-bleed photo) | Emotional / context moment. Warm, candid photo in color. Caption ≤ 45 characters. |
| 17 | `phototext` | Chữ trái + ảnh phải (Text + photo) | Illustrate a concept with a photo. Title ≤ 3 lines, text ≤ 30 words. |
| 18 | `bignum` | Con số lớn (Big number) | One headline metric + 1-line caption. ≤ 10 characters in the number. |
| 19 | `stats` | Ba chỉ số (Three stats) | Three metrics, value ≤ 10 characters + caption ≤ 8 words. |
| 20 | `donuts` | Phần trăm vòng tròn (Percent donuts) | Exactly 3 percentages. Arc length = first stroke-dasharray value (0–100). Heading ≤ 12 characters, text ≤ 12 words. |
| 21 | `pie` | Biểu đồ tròn + chú giải (Donut chart + legend) | Share of a whole in 2–4 parts. Segment n: dasharray = its %, dashoffset = minus the sum before it. Colors in order: cyan, blue, grey, white. |
| 22 | `computer` | Demo máy tính (Computer mockup) | Show a web screen. Screenshot in class "shot" inside .scr. Text ≤ 30 words. |
| 23 | `tablet` | Demo máy tính bảng (Tablet mockup) | Show a wide screen or dashboard. One line of context ≤ 20 words above. |
| 24 | `phone` | Demo điện thoại (Phone mockup) | Show a mobile screen. Title ≤ 2 lines, text ≤ 30 words. |
| 25 | `table` | Bảng số liệu (Data table) | Test results, metrics. ≤ 5 rows × 5 cols. Headers ≤ 12 characters. Use td.v for big numbers, .dot for yes/no marks. |
| 26 | `compare` | So sánh giải pháp (Comparison table) | Existing solutions vs. ours. ≤ 4 criteria rows × 4 option cols. Mark support with .dot (ours: .dot, others: .dot grey). |
| 27 | `figure` | Hình / biểu đồ + ý chính (Figure + side text) | A chart, diagram or textbook figure with its caption / citation, plus 1–3 key numbers or points beside it. Charts: inline SVG with .f-*/.s-* classes; images: <img class="fig-img">. Add "alt" to put the figure on the right, "portrait" for a tall figure in a narrow right column with a wide text column; "wide" (drop .side) for full width, with one .cell per figure for 2–3 figures side by side. Caption ≤ 25 words, side ≤ 45 words. |
| 28 | `timeline` | Dòng thời gian (Timeline, 5 points) | Milestones / history / sprints. Exactly 5 points; labels alternate above (.up) and below (.dn). Heading ≤ 10 characters, text ≤ 8 words. |
| 29 | `hub` | Sơ đồ trung tâm (Hub, center + 6) | One core concept with 6 parts: modules around the system, factors around a problem. Heading ≤ 12 characters, text ≤ 6 words. |
| 30 | `stairs` | Bậc thang (Stairs, 4 levels) | Growth path, maturity levels, graduation plan. Level label ≤ 10 characters, heading ≤ 12 characters, text ≤ 10 words. Level 1 is the bottom step. |
| 31 | `gantt` | Kế hoạch theo tháng (Gantt roadmap) | Project plan / progress report. 3–4 phases × 4–6 months (set --m). Bar: grid-column = "start / span n" counting month columns from 2. ≤ 3 tasks per bar. |
| 32 | `team` | Thành viên (Team) | 2–5 members (default markup has 4). For 5 members add class "five" to .grid. Photos square, in color. Full name ≤ 2 lines (≈ 20 characters), role ≤ 5 words. |
| 33 | `diagram` | Sơ đồ tự do (Free diagram canvas) | Architecture, flows, ERD overview. Draw with .node boxes or inline SVG using .f-*/.s-* classes only. |
| 34 | `thanks` | Cảm ơn / Q&A (Closing) | Last slide. Question prompt + contact, repo and demo links. |

## 1. `cover` — Bìa (Cover)

Slide 1 of every deck. Title ≤ 2 lines (≤ 36 characters), optional keyword in white with .hl. Meta = team, advisor, date.

```html
<section class="slide l-cover">
  <svg class="deco" style="left:697.2px;top:-0px;width:262.8px;height:87.6px"><use href="#m1a"/></svg>
  <svg class="deco" style="left:913.3px;top:423.9px;width:30.9px;height:97.5px"><use href="#m1b"/></svg>
  <svg class="deco" style="left:-79.9px;top:-81.5px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <svg class="deco" style="left:0px;top:450.9px;width:257.4px;height:89.1px"><use href="#m1d"/></svg>
  <div class="cv">
    <h1 class="cv-title">[Tên đề tài, tối đa hai dòng]</h1>
    <p class="cv-sub">[Phụ đề một dòng cho đề tài]</p>
    <p class="cv-meta"><b>[Nhóm]</b> · GVHD: [Học vị. Họ tên]<br>[Khoa] · [Trường] · [Tháng/Năm]</p>
  </div>
</section>
```

## 2. `toc` — Mục lục (Table of contents)

Right after the cover. 3–6 chapters (5 = source layout, 3 + 2). Heading ≤ 14 characters, description ≤ 10 words.

```html
<section class="slide l-toc">
  <svg class="deco" style="left:-79.5px;top:-81.5px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <svg class="deco" style="left:913.3px;top:423.9px;width:30.9px;height:97.5px"><use href="#m1b"/></svg>
  <svg class="deco" style="left:0px;top:450.9px;width:222.6px;height:89.1px"><use href="#m12c"/></svg>
  <svg class="deco" style="left:872.4px;top:-0px;width:87.6px;height:87.6px"><use href="#m12d"/></svg>
  <svg class="deco" style="left:13.1px;top:99.6px;width:30.9px;height:97.5px"><use href="#m1b"/></svg>
  <h2 class="title">Nội dung</h2>
  <div class="toc">
    <div class="it"><div class="num">01</div><div class="h3">Vấn đề</div><p>[Mô tả ngắn cho chương 1]</p></div>
    <div class="it"><div class="num">02</div><div class="h3">Giải pháp</div><p>[Mô tả ngắn cho chương 2]</p></div>
    <div class="it"><div class="num">03</div><div class="h3">Hệ thống</div><p>[Mô tả ngắn cho chương 3]</p></div>
    <div class="it"><div class="num">04</div><div class="h3">Kết quả</div><p>[Mô tả ngắn cho chương 4]</p></div>
    <div class="it"><div class="num">05</div><div class="h3">Hướng đi</div><p>[Mô tả ngắn cho chương 5]</p></div>
  </div>
</section>
```

## 3. `whoa` — Mở đầu ấn tượng (Whoa!)

A one-word hook (≤ 10 characters) + one line: intro yourself, a surprising turn, "Tại sao?".

```html
<section class="slide l-whoa">
  <svg class="deco" style="left:876.1px;top:335.9px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <svg class="deco" style="left:22.7px;top:423.9px;width:30.9px;height:97.5px"><use href="#m1b"/></svg>
  <svg class="deco" style="left:301.9px;top:0px;width:356.2px;height:89.0px"><use href="#m8c"/></svg>
  <div class="big">Tại sao?</div>
  <p class="sub">[Một câu dẫn vào vấn đề, tối đa 20 từ.]</p>
</section>
```

## 4. `section` — Chương (Section header, centered)

Opens each chapter listed in the TOC. Alternate with "section-alt". Title ≤ 18 characters.

```html
<section class="slide l-section">
  <svg class="deco" style="left:0px;top:450.7px;width:355.9px;height:89.3px"><use href="#m2a"/></svg>
  <svg class="deco" style="left:604.2px;top:-0px;width:355.8px;height:89.0px"><use href="#m2b"/></svg>
  <svg class="deco" style="left:903.4px;top:416.1px;width:31.0px;height:97.5px"><use href="#m2c"/></svg>
  <svg class="deco" style="left:-82.6px;top:56.6px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <div class="sec-num">01</div>
  <div class="sec-title">Vấn đề</div>
  <p class="sec-sub">[Câu hỏi hoặc bối cảnh mở đầu chương]</p>
</section>
```

## 5. `section-alt` — Chương – biến thể trái (Section header, number left)

Same role as "section", number left of a left-aligned title.

```html
<section class="slide l-section alt">
  <svg class="deco" style="left:604.1px;top:0px;width:355.9px;height:89.3px"><use href="#m2a"/></svg>
  <svg class="deco" style="left:-0px;top:201.1px;width:89.0px;height:355.9px"><use href="#m14b"/></svg>
  <svg class="deco" style="left:10.9px;top:12.8px;width:31.0px;height:97.5px"><use href="#m2c"/></svg>
  <svg class="deco" style="left:877.1px;top:366.7px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <div class="sec-num">02</div>
  <div class="sec-title">Giải pháp</div>
  <p class="sec-sub">[Câu hỏi hoặc bối cảnh mở đầu chương]</p>
</section>
```

## 6. `text2` — Hai đoạn văn (Title + two paragraphs)

Context / background explained in two short paragraphs (≤ 35 words each), centered.

```html
<section class="slide l-text2">
  <svg class="deco" style="left:0px;top:450.7px;width:178.6px;height:89.3px"><use href="#m24a"/></svg>
  <svg class="deco" style="left:802.9px;top:450.7px;width:157.1px;height:89.3px"><use href="#m24b"/></svg>
  <svg class="deco" style="left:16.7px;top:19.3px;width:30.9px;height:97.5px"><use href="#m1b"/></svg>
  <svg class="deco" style="left:904.1px;top:156.9px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <h2 class="title">Bối cảnh</h2>
  <div class="paras">
    <p>[Đoạn 1: bối cảnh chung của đề tài, tối đa 35 từ. Nêu điều đang xảy ra và ai bị ảnh hưởng.]</p>
    <p>[Đoạn 2: vì sao vấn đề đáng giải quyết ngay bây giờ, tối đa 35 từ.]</p>
  </div>
</section>
```

## 7. `bullets` — Gạch đầu dòng (Title + bullets)

Default content slide: one lead line + 3–5 bullets, ≤ 10 words each.

```html
<section class="slide l-bullets">
  <svg class="deco" style="left:-79.5px;top:-81.5px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <svg class="deco" style="left:15.8px;top:423.9px;width:30.9px;height:97.5px"><use href="#m6b"/></svg>
  <svg class="deco" style="left:737.4px;top:450.9px;width:222.6px;height:89.1px"><use href="#m6c"/></svg>
  <h2 class="title">Mục tiêu đề tài</h2>
  <div class="body">
    <p>[Câu mở đầu giới thiệu danh sách:]</p>
    <ul class="ul">
      <li>[Mục tiêu 1, tối đa 10 từ]</li>
      <li>[Mục tiêu 2, tối đa 10 từ]</li>
      <li>[Mục tiêu 3, tối đa 10 từ]</li>
      <li>[Mục tiêu 4, tối đa 10 từ]</li>
    </ul>
  </div>
</section>
```

## 8. `steps` — Bốn bước đánh số (Numbered steps)

3–4 parallel or sequential items. Set --n on .cols to the count. Heading ≤ 12 characters, text ≤ 18 words.

```html
<section class="slide l-steps">
  <svg class="deco" style="left:0px;top:488px;width:142.0px;height:53.5px"><use href="#m15a"/></svg>
  <svg class="deco" style="left:10.9px;top:12.8px;width:31.0px;height:97.5px"><use href="#m2c"/></svg>
  <svg class="deco" style="left:901.3px;top:208.3px;width:164.2px;height:164.1px"><use href="#m15c"/></svg>
  <h2 class="title">Quy trình thực hiện</h2>
  <div class="cols" style="--n:4">
    <div class="it"><div class="num">01</div><div class="h3">[Bước 1]</div><p>[Mô tả ngắn cho bước 1, tối đa 18 từ.]</p></div>
    <div class="it"><div class="num">02</div><div class="h3">[Bước 2]</div><p>[Mô tả ngắn cho bước 2, tối đa 18 từ.]</p></div>
    <div class="it"><div class="num">03</div><div class="h3">[Bước 3]</div><p>[Mô tả ngắn cho bước 3, tối đa 18 từ.]</p></div>
    <div class="it"><div class="num">04</div><div class="h3">[Bước 4]</div><p>[Mô tả ngắn cho bước 4, tối đa 18 từ.]</p></div>
  </div>
</section>
```

## 9. `zig2` — Hai ý so le (Two staggered items)

Two ideas, problem vs. solution, before vs. after. Heading ≤ 16 characters, text ≤ 25 words.

```html
<section class="slide l-zig n2">
  <svg class="deco" style="left:876.1px;top:197px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <svg class="deco" style="left:22.7px;top:423.9px;width:30.9px;height:97.5px"><use href="#m1b"/></svg>
  <svg class="deco" style="left:301.9px;top:451px;width:356.2px;height:89.0px"><use href="#m8c"/></svg>
  <h2 class="title">[Tiêu đề so sánh hai ý]</h2>
  <div class="zz">
    <div class="it"><div class="h3">[Ý 1]</div><p>[Mô tả ý 1, tối đa 25 từ.]</p></div>
    <div class="it"><div class="h3">[Ý 2]</div><p>[Mô tả ý 2, tối đa 25 từ.]</p></div>
  </div>
</section>
```

## 10. `zig3` — Ba ý so le (Three staggered items)

Three features / pillars / user groups. Heading ≤ 12 characters, text ≤ 15 words.

```html
<section class="slide l-zig n3">
  <svg class="deco" style="left:874.9px;top:-81.5px;width:164.2px;height:164.2px"><use href="#m25a"/></svg>
  <svg class="deco" style="left:15.4px;top:423.9px;width:30.9px;height:97.5px"><use href="#m6b"/></svg>
  <svg class="deco" style="left:737.1px;top:450.9px;width:222.5px;height:89.1px"><use href="#m25c"/></svg>
  <svg class="deco" style="left:-0.4px;top:-0px;width:87.6px;height:87.6px"><use href="#m25d"/></svg>
  <h2 class="title">Tính năng chính</h2>
  <div class="zz">
    <div class="it"><div class="h3">[Tính năng 1]</div><p>[Mô tả ngắn, tối đa 15 từ.]</p></div>
    <div class="it"><div class="h3">[Tính năng 2]</div><p>[Mô tả ngắn, tối đa 15 từ.]</p></div>
    <div class="it"><div class="h3">[Tính năng 3]</div><p>[Mô tả ngắn, tối đa 15 từ.]</p></div>
  </div>
</section>
```

## 11. `zig4` — Bốn ý so le (Four staggered items)

Four stakeholders / principles / requirements. Heading ≤ 12 characters, text ≤ 10 words.

```html
<section class="slide l-zig n4">
  <svg class="deco" style="left:722.3px;top:461.5px;width:237.7px;height:79.2px"><use href="#m26a"/></svg>
  <svg class="deco" style="left:18.4px;top:22.1px;width:31.0px;height:97.5px"><use href="#m2c"/></svg>
  <svg class="deco" style="left:878.4px;top:-81.5px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <h2 class="title">Các bên liên quan</h2>
  <div class="zz">
    <div class="it"><div class="h3">[Đối tượng 1]</div><p>[Mô tả ngắn, tối đa 10 từ]</p></div>
    <div class="it"><div class="h3">[Đối tượng 2]</div><p>[Mô tả ngắn, tối đa 10 từ]</p></div>
    <div class="it"><div class="h3">[Đối tượng 3]</div><p>[Mô tả ngắn, tối đa 10 từ]</p></div>
    <div class="it"><div class="h3">[Đối tượng 4]</div><p>[Mô tả ngắn, tối đa 10 từ]</p></div>
  </div>
</section>
```

## 12. `five` — Năm ý (Five items, 3 + 2)

Five modules / requirements / tips. Heading ≤ 12 characters, text ≤ 10 words.

```html
<section class="slide l-five">
  <svg class="deco" style="left:802.9px;top:450.7px;width:157.1px;height:89.3px"><use href="#m24b"/></svg>
  <svg class="deco" style="left:921.4px;top:7.9px;width:31.0px;height:97.5px"><use href="#m2c"/></svg>
  <svg class="deco" style="left:-105.3px;top:353.9px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <h2 class="title">Yêu cầu chức năng</h2>
  <div class="grid">
    <div class="it"><div class="h3">[Chức năng 1]</div><p>[Mô tả ngắn, tối đa 10 từ]</p></div>
    <div class="it"><div class="h3">[Chức năng 2]</div><p>[Mô tả ngắn, tối đa 10 từ]</p></div>
    <div class="it"><div class="h3">[Chức năng 3]</div><p>[Mô tả ngắn, tối đa 10 từ]</p></div>
    <div class="it"><div class="h3">[Chức năng 4]</div><p>[Mô tả ngắn, tối đa 10 từ]</p></div>
    <div class="it"><div class="h3">[Chức năng 5]</div><p>[Mô tả ngắn, tối đa 10 từ]</p></div>
  </div>
</section>
```

## 13. `statement` — Thông điệp lớn (Main point)

One punchline, ≤ 3 lines of ≤ 18 characters.

```html
<section class="slide l-statement">
  <svg class="deco" style="left:697.2px;top:-0px;width:262.8px;height:87.6px"><use href="#m1a"/></svg>
  <svg class="deco" style="left:913.3px;top:423.9px;width:30.9px;height:97.5px"><use href="#m1b"/></svg>
  <svg class="deco" style="left:-79.9px;top:-81.5px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <svg class="deco" style="left:0px;top:450.9px;width:257.4px;height:89.1px"><use href="#m1d"/></svg>
  <div class="big">[Thông điệp chính, ngắn gọn]</div>
</section>
```

## 14. `focus` — Nhấn mạnh (Accent / pacing slide)

A pause on the one idea the audience must remember, on a blue canvas: "The catch", a key finding, a turning point. Use sparingly (about one per section, never two in a row). Eyebrow ≤ 20 characters, idea ≤ 90 characters (≤ 3 lines), follow-up ≤ 12 words. Class "accent" also works on whoa and quote slides.

```html
<section class="slide l-statement accent">
  <svg class="deco" style="left:697.2px;top:-0px;width:262.8px;height:87.6px"><use href="#m1a"/></svg>
  <svg class="deco" style="left:913.3px;top:423.9px;width:30.9px;height:97.5px"><use href="#m1b"/></svg>
  <svg class="deco" style="left:-79.9px;top:-81.5px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <svg class="deco" style="left:0px;top:450.9px;width:257.4px;height:89.1px"><use href="#m1d"/></svg>
  <div class="st">
    <p class="eyebrow">[Nhãn ngắn]</p>
    <div class="big">[Ý chính khán giả cần nhớ, tối đa 90 ký tự]</div>
    <div class="rule"></div>
    <p class="sub">[Câu hỏi hoặc câu dẫn sang phần tiếp theo]</p>
  </div>
</section>
```

## 15. `quote` — Trích dẫn (Quote)

A quote from a user interview, expert or advisor. ≤ 25 words.

```html
<section class="slide l-quote">
  <svg class="deco" style="left:0.1px;top:-0px;width:262.8px;height:87.6px"><use href="#m13a"/></svg>
  <svg class="deco" style="left:15.9px;top:423.9px;width:30.9px;height:97.5px"><use href="#m6b"/></svg>
  <svg class="deco" style="left:875.8px;top:-81.5px;width:164.2px;height:164.2px"><use href="#m25a"/></svg>
  <svg class="deco" style="left:702.7px;top:450.9px;width:257.4px;height:89.1px"><use href="#m13d"/></svg>
  <div class="qw">
    <blockquote class="qt">“[Trích dẫn ngắn, tối đa 25 từ.]”</blockquote>
    <p class="by">—[Nguồn trích dẫn]</p>
  </div>
</section>
```

## 16. `photo` — Ảnh toàn trang (Full-bleed photo)

Emotional / context moment. Warm, candid photo in color. Caption ≤ 45 characters.

```html
<section class="slide l-photo">
  <svg class="deco" style="left:-0px;top:0.3px;width:88.9px;height:89.0px"><use href="#ms16a"/></svg>
  <svg class="deco" style="left:915.8px;top:426.5px;width:31.0px;height:97.5px"><use href="#m2c"/></svg>
  <svg class="deco" style="left:612.4px;top:-89.4px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <div class="bg"><div class="ph">[ẢNH: mô tả, dùng &lt;img class="photo"&gt;]</div></div>
  <div class="cap">[Một câu chú thích cho bức ảnh]</div>
</section>
```

## 17. `phototext` — Chữ trái + ảnh phải (Text + photo)

Illustrate a concept with a photo. Title ≤ 3 lines, text ≤ 30 words.

```html
<section class="slide l-phototext">
  <svg class="deco" style="left:-0.6px;top:451.6px;width:355.9px;height:89.3px"><use href="#m17a"/></svg>
  <svg class="deco" style="left:917.5px;top:430.6px;width:30.9px;height:97.5px"><use href="#m17b"/></svg>
  <svg class="deco" style="left:-81.9px;top:10px;width:164.2px;height:164.2px"><use href="#m17c"/></svg>
  <div class="txt">
    <div class="tt">[Tiêu đề khái niệm]</div>
    <p>[Đoạn mô tả, tối đa 30 từ. Hình ảnh truyền tải nhiều thông tin, nên dùng ảnh thay vì đoạn văn dài.]</p>
  </div>
  <div class="pic"><div class="ph">[ẢNH vuông]</div></div>
</section>
```

## 18. `bignum` — Con số lớn (Big number)

One headline metric + 1-line caption. ≤ 10 characters in the number.

```html
<section class="slide l-bignum">
  <svg class="deco" style="left:0.1px;top:-0px;width:262.8px;height:87.6px"><use href="#m13a"/></svg>
  <svg class="deco" style="left:15.9px;top:423.9px;width:30.9px;height:97.5px"><use href="#m6b"/></svg>
  <svg class="deco" style="left:875.8px;top:-81.5px;width:164.2px;height:164.2px"><use href="#m25a"/></svg>
  <svg class="deco" style="left:702.7px;top:450.9px;width:257.4px;height:89.1px"><use href="#m13d"/></svg>
  <div class="num">[98.300.000]</div>
  <p class="cap">[Mô tả ngắn cho số liệu, một dòng]</p>
</section>
```

## 19. `stats` — Ba chỉ số (Three stats)

Three metrics, value ≤ 10 characters + caption ≤ 8 words.

```html
<section class="slide l-stats">
  <svg class="deco" style="left:768.9px;top:464.6px;width:164.2px;height:164.2px"><use href="#m28a"/></svg>
  <svg class="deco" style="left:20.4px;top:18.9px;width:31.0px;height:97.5px"><use href="#m28b"/></svg>
  <svg class="deco" style="left:737.4px;top:0.4px;width:222.6px;height:89.0px"><use href="#m28c"/></svg>
  <svg class="deco" style="left:0px;top:452.7px;width:87.6px;height:87.6px"><use href="#m28d"/></svg>
  <div class="zz">
    <div class="it"><div class="v">[1,2 giây]</div><p>[Mô tả chỉ số 1]</p></div>
    <div class="it"><div class="v">[12.500]</div><p>[Mô tả chỉ số 2]</p></div>
    <div class="it"><div class="v">[98%]</div><p>[Mô tả chỉ số 3]</p></div>
  </div>
</section>
```

## 20. `donuts` — Phần trăm vòng tròn (Percent donuts)

Exactly 3 percentages. Arc length = first stroke-dasharray value (0–100). Heading ≤ 12 characters, text ≤ 12 words.

```html
<section class="slide l-donuts">
  <svg class="deco" style="left:-0.2px;top:461.5px;width:237.7px;height:79.2px"><use href="#m5a"/></svg>
  <svg class="deco" style="left:910.4px;top:22.1px;width:31.0px;height:97.5px"><use href="#m5b"/></svg>
  <svg class="deco" style="left:879.2px;top:461.5px;width:164.2px;height:164.2px"><use href="#m25a"/></svg>
  <h2 class="title">[Tiêu đề kết quả]</h2>
  <div class="zz">
    <div class="col">
      <svg class="ring" viewBox="0 0 100 100"><circle class="s-grey" cx="50" cy="50" r="38" fill="none" stroke-width="20"/><circle class="s-blue" cx="50" cy="50" r="38" fill="none" stroke-width="20" pathLength="100" stroke-dasharray="15 100" transform="rotate(-90 50 50)"/></svg>
      <div class="stat">[15%]</div><div class="h3">[Chỉ số 1]</div><p>[Giải thích ngắn]</p>
    </div>
    <div class="col">
      <div class="stat">[70%]</div><div class="h3">[Chỉ số 2]</div><p>[Giải thích ngắn]</p>
      <svg class="ring" viewBox="0 0 100 100"><circle class="s-grey" cx="50" cy="50" r="38" fill="none" stroke-width="20"/><circle class="s-blue" cx="50" cy="50" r="38" fill="none" stroke-width="20" pathLength="100" stroke-dasharray="70 100" transform="rotate(-90 50 50)"/></svg>
    </div>
    <div class="col">
      <svg class="ring" viewBox="0 0 100 100"><circle class="s-grey" cx="50" cy="50" r="38" fill="none" stroke-width="20"/><circle class="s-blue" cx="50" cy="50" r="38" fill="none" stroke-width="20" pathLength="100" stroke-dasharray="55 100" transform="rotate(-90 50 50)"/></svg>
      <div class="stat">[55%]</div><div class="h3">[Chỉ số 3]</div><p>[Giải thích ngắn]</p>
    </div>
  </div>
</section>
```

## 21. `pie` — Biểu đồ tròn + chú giải (Donut chart + legend)

Share of a whole in 2–4 parts. Segment n: dasharray = its %, dashoffset = minus the sum before it. Colors in order: cyan, blue, grey, white.

```html
<section class="slide l-pie">
  <svg class="deco" style="left:0px;top:488px;width:142.0px;height:53.5px"><use href="#m15a"/></svg>
  <svg class="deco" style="left:10.9px;top:12.8px;width:31.0px;height:97.5px"><use href="#m2c"/></svg>
  <svg class="deco" style="left:901.3px;top:208.3px;width:164.2px;height:164.1px"><use href="#m15c"/></svg>
  <h2 class="title">[Tiêu đề biểu đồ]</h2>
  <svg class="chart" viewBox="0 0 320 300">
    <g fill="none" stroke-width="62" transform="rotate(-90 160 150)">
      <circle class="s-cyan" cx="160" cy="150" r="104" pathLength="100" stroke-dasharray="45 100"/>
      <circle class="s-grey" cx="160" cy="150" r="104" pathLength="100" stroke-dasharray="20 100" stroke-dashoffset="-45"/>
      <circle class="s-blue" cx="160" cy="150" r="104" pathLength="100" stroke-dasharray="35 100" stroke-dashoffset="-65"/>
    </g>
  </svg>
  <div class="legend">
    <div class="row"><span class="dot"></span><span class="stat">45%</span><div><div class="h4">[Nhóm 1]</div><p class="sm">[Mô tả ngắn]</p></div></div>
    <div class="row"><span class="dot grey"></span><span class="stat">20%</span><div><div class="h4">[Nhóm 2]</div><p class="sm">[Mô tả ngắn]</p></div></div>
    <div class="row"><span class="dot blue"></span><span class="stat">35%</span><div><div class="h4">[Nhóm 3]</div><p class="sm">[Mô tả ngắn]</p></div></div>
  </div>
  <p class="foot">[Nguồn số liệu: khảo sát N người, tháng/năm]</p>
</section>
```

## 22. `computer` — Demo máy tính (Computer mockup)

Show a web screen. Screenshot in class "shot" inside .scr. Text ≤ 30 words.

```html
<section class="slide l-computer">
  <svg class="deco" style="left:-79.5px;top:-81.5px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <svg class="deco" style="left:913.3px;top:423.9px;width:30.9px;height:97.5px"><use href="#m1b"/></svg>
  <svg class="deco" style="left:0px;top:450.9px;width:222.6px;height:89.1px"><use href="#m12c"/></svg>
  <svg class="deco" style="left:872.4px;top:-0px;width:87.6px;height:87.6px"><use href="#m12d"/></svg>
  <div class="mon"><div class="scr"><div class="ph">[SCREENSHOT web, dùng &lt;img class="shot"&gt;]</div></div><div class="neck"></div><div class="base"></div></div>
  <div class="txt">
    <div class="h3">[Tên màn hình]</div>
    <p>[Mô tả luồng chính trên màn hình này, tối đa 30 từ.]</p>
  </div>
</section>
```

## 23. `tablet` — Demo máy tính bảng (Tablet mockup)

Show a wide screen or dashboard. One line of context ≤ 20 words above.

```html
<section class="slide l-tablet">
  <svg class="deco" style="left:722.3px;top:461.5px;width:237.7px;height:79.2px"><use href="#m26a"/></svg>
  <svg class="deco" style="left:18.4px;top:22.1px;width:31.0px;height:97.5px"><use href="#m2c"/></svg>
  <svg class="deco" style="left:878.4px;top:-81.5px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <h2 class="title">[Tên màn hình dashboard]</h2>
  <p class="sub">[Một câu mô tả màn hình, tối đa 20 từ.]</p>
  <div class="tab"><div class="ph" style="background:var(--white)">[SCREENSHOT ngang]</div></div>
</section>
```

## 24. `phone` — Demo điện thoại (Phone mockup)

Show a mobile screen. Title ≤ 2 lines, text ≤ 30 words.

```html
<section class="slide l-phone">
  <svg class="deco" style="left:850.3px;top:502.1px;width:97.5px;height:31.0px"><use href="#m20a"/></svg>
  <svg class="deco" style="left:-82.9px;top:458px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <svg class="deco" style="left:-0px;top:0px;width:356.2px;height:89.0px"><use href="#m8c"/></svg>
  <div class="txt">
    <div class="tt">[Ứng dụng di động]</div>
    <p>[Mô tả chức năng của màn hình, tối đa 30 từ.]</p>
  </div>
  <div class="ph-frame"><div class="ph" style="background:var(--white)">[SCREENSHOT dọc]</div></div>
</section>
```

## 25. `table` — Bảng số liệu (Data table)

Test results, metrics. ≤ 5 rows × 5 cols. Headers ≤ 12 characters. Use td.v for big numbers, .dot for yes/no marks.

```html
<section class="slide l-table">
  <svg class="deco" style="left:799.8px;top:487.3px;width:160.2px;height:53.4px"><use href="#m16a"/></svg>
  <svg class="deco" style="left:18.4px;top:22.1px;width:31.0px;height:97.5px"><use href="#m2c"/></svg>
  <svg class="deco" style="left:-83.8px;top:461.5px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <h2 class="title">[Tiêu đề bảng]</h2>
  <div class="tblwrap">
    <table class="tbl">
      <thead><tr><th>[Hạng mục]</th><th>[Mô tả]</th><th>[Tỉ lệ]</th><th>[Số lượng]</th></tr></thead>
      <tbody>
        <tr><td class="rh">[Mục 1]</td><td>[Mô tả ngắn]</td><td class="v">[45%]</td><td class="v">[4.500]</td></tr>
        <tr><td class="rh">[Mục 2]</td><td>[Mô tả ngắn]</td><td class="v">[85%]</td><td class="v">[1.200]</td></tr>
        <tr><td class="rh">[Mục 3]</td><td>[Mô tả ngắn]</td><td class="v">[15%]</td><td class="v">[9.400]</td></tr>
      </tbody>
    </table>
  </div>
</section>
```

## 26. `compare` — So sánh giải pháp (Comparison table)

Existing solutions vs. ours. ≤ 4 criteria rows × 4 option cols. Mark support with .dot (ours: .dot, others: .dot grey).

```html
<section class="slide l-table">
  <svg class="deco" style="left:799.8px;top:487.3px;width:160.2px;height:53.4px"><use href="#m16a"/></svg>
  <svg class="deco" style="left:18.4px;top:22.1px;width:31.0px;height:97.5px"><use href="#m2c"/></svg>
  <svg class="deco" style="left:-83.8px;top:461.5px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <h2 class="title">So sánh giải pháp hiện có</h2>
  <div class="tblwrap">
    <table class="tbl">
      <thead><tr><th>Tiêu chí</th><th>[Giải pháp 1]</th><th>[Giải pháp 2]</th><th>[Giải pháp 3]</th><th>Của nhóm</th></tr></thead>
      <tbody>
        <tr><td class="rh">[Tiêu chí 1]</td><td><span class="dot grey"></span></td><td></td><td><span class="dot grey"></span></td><td><span class="dot"></span></td></tr>
        <tr><td class="rh">[Tiêu chí 2]</td><td></td><td><span class="dot grey"></span></td><td></td><td><span class="dot"></span></td></tr>
        <tr><td class="rh">[Tiêu chí 3]</td><td></td><td></td><td><span class="dot grey"></span></td><td><span class="dot"></span></td></tr>
        <tr><td class="rh">[Tiêu chí 4]</td><td><span class="dot grey"></span></td><td></td><td></td><td><span class="dot"></span></td></tr>
      </tbody>
    </table>
  </div>
</section>
```

## 27. `figure` — Hình / biểu đồ + ý chính (Figure + side text)

A chart, diagram or textbook figure with its caption / citation, plus 1–3 key numbers or points beside it. Charts: inline SVG with .f-*/.s-* classes; images: <img class="fig-img">. Add "alt" to put the figure on the right, "portrait" for a tall figure in a narrow right column with a wide text column; "wide" (drop .side) for full width, with one .cell per figure for 2–3 figures side by side. Caption ≤ 25 words, side ≤ 45 words.

```html
<section class="slide l-figure">
  <svg class="deco" style="left:799.8px;top:487.3px;width:160.2px;height:53.4px"><use href="#m16a"/></svg>
  <svg class="deco" style="left:18.4px;top:22.1px;width:31.0px;height:97.5px"><use href="#m2c"/></svg>
  <svg class="deco" style="left:-83.8px;top:461.5px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <h2 class="title">[Tiêu đề hình]</h2>
  <div class="fig"><div class="ph">[HÌNH / BIỂU ĐỒ: inline SVG hoặc &lt;img class="fig-img"&gt;]</div></div>
  <p class="figcap">[Chú thích ngắn. Nguồn: Tác giả (năm), Hình x.y.]</p>
  <div class="side">
    <div class="kv"><div class="v">[93%]</div><p>[Ý nghĩa của số liệu, tối đa 12 từ]</p></div>
    <div class="kv"><div class="v">[1.024]</div><p>[Ý nghĩa của số liệu, tối đa 12 từ]</p></div>
    <p>[Một câu kết luận ngắn, tối đa 20 từ.]</p>
  </div>
</section>
```

## 28. `timeline` — Dòng thời gian (Timeline, 5 points)

Milestones / history / sprints. Exactly 5 points; labels alternate above (.up) and below (.dn). Heading ≤ 10 characters, text ≤ 8 words.

```html
<section class="slide l-timeline">
  <svg class="deco" style="left:0px;top:488px;width:142.0px;height:53.5px"><use href="#m15a"/></svg>
  <svg class="deco" style="left:10.9px;top:12.8px;width:31.0px;height:97.5px"><use href="#m2c"/></svg>
  <svg class="deco" style="left:901.3px;top:208.3px;width:164.2px;height:164.1px"><use href="#m15c"/></svg>
  <h2 class="title">[Tiêu đề dòng thời gian]</h2>
  <div class="axis"></div>
  <div class="zz">
    <div class="st up"><div class="it"><p>[Mô tả ngắn mốc 1]</p><div class="h3">[Mốc 1]</div></div><div class="num">01</div></div>
    <div class="st dn"><div class="num">02</div><div class="it"><div class="h3">[Mốc 2]</div><p>[Mô tả ngắn mốc 2]</p></div></div>
    <div class="st up"><div class="it"><p>[Mô tả ngắn mốc 3]</p><div class="h3">[Mốc 3]</div></div><div class="num">03</div></div>
    <div class="st dn"><div class="num">04</div><div class="it"><div class="h3">[Mốc 4]</div><p>[Mô tả ngắn mốc 4]</p></div></div>
    <div class="st up"><div class="it"><p>[Mô tả ngắn mốc 5]</p><div class="h3">[Mốc 5]</div></div><div class="num">05</div></div>
  </div>
</section>
```

## 29. `hub` — Sơ đồ trung tâm (Hub, center + 6)

One core concept with 6 parts: modules around the system, factors around a problem. Heading ≤ 12 characters, text ≤ 6 words.

```html
<section class="slide l-hub">
  <svg class="deco" style="left:-0.2px;top:461.5px;width:237.7px;height:79.2px"><use href="#m5a"/></svg>
  <svg class="deco" style="left:910.4px;top:22.1px;width:31.0px;height:97.5px"><use href="#m5b"/></svg>
  <svg class="deco" style="left:879.2px;top:461.5px;width:164.2px;height:164.2px"><use href="#m25a"/></svg>
  <h2 class="title">[Tiêu đề sơ đồ]</h2>
  <div class="core"><div class="h3">[Hệ thống]</div></div>
  <div class="ln" style="left:479px;top:204px;width:2px;height:24px"></div>
  <div class="ln" style="left:479px;top:320px;width:2px;height:32px"></div>
  <div class="ln" style="left:344px;top:196px;width:2px;height:124px"></div>
  <div class="ln" style="left:344px;top:273px;width:28px;height:2px"></div>
  <div class="ln" style="left:614px;top:196px;width:2px;height:124px"></div>
  <div class="ln" style="left:588px;top:273px;width:28px;height:2px"></div>
  <div class="it top"><div class="h3">[Phần 1]</div><p>[Mô tả rất ngắn]</p></div>
  <div class="it l1"><div class="h3">[Phần 2]</div><p>[Mô tả rất ngắn]</p></div>
  <div class="it r1"><div class="h3">[Phần 3]</div><p>[Mô tả rất ngắn]</p></div>
  <div class="it l2"><div class="h3">[Phần 4]</div><p>[Mô tả rất ngắn]</p></div>
  <div class="it r2"><div class="h3">[Phần 5]</div><p>[Mô tả rất ngắn]</p></div>
  <div class="it bot"><div class="h3">[Phần 6]</div><p>[Mô tả rất ngắn]</p></div>
</section>
```

## 30. `stairs` — Bậc thang (Stairs, 4 levels)

Growth path, maturity levels, graduation plan. Level label ≤ 10 characters, heading ≤ 12 characters, text ≤ 10 words. Level 1 is the bottom step.

```html
<section class="slide l-stairs">
  <svg class="deco" style="left:-0.2px;top:461.5px;width:237.7px;height:79.2px"><use href="#m5a"/></svg>
  <svg class="deco" style="left:910.4px;top:22.1px;width:31.0px;height:97.5px"><use href="#m5b"/></svg>
  <svg class="deco" style="left:879.2px;top:461.5px;width:164.2px;height:164.2px"><use href="#m25a"/></svg>
  <h2 class="title">[Lộ trình phát triển]</h2>
  <div class="zz">
    <div class="lv">[Mức 1]</div><div class="lv">[Mức 2]</div><div class="lv">[Mức 3]</div><div class="lv">[Mức 4]</div>
  </div>
  <div class="zz">
    <div class="it"><div class="h3">[Giai đoạn 1]</div><p>[Mô tả ngắn, tối đa 10 từ]</p></div>
    <div class="it"><div class="h3">[Giai đoạn 2]</div><p>[Mô tả ngắn, tối đa 10 từ]</p></div>
    <div class="it"><div class="h3">[Giai đoạn 3]</div><p>[Mô tả ngắn, tối đa 10 từ]</p></div>
    <div class="it"><div class="h3">[Giai đoạn 4]</div><p>[Mô tả ngắn, tối đa 10 từ]</p></div>
  </div>
</section>
```

## 31. `gantt` — Kế hoạch theo tháng (Gantt roadmap)

Project plan / progress report. 3–4 phases × 4–6 months (set --m). Bar: grid-column = "start / span n" counting month columns from 2. ≤ 3 tasks per bar.

```html
<section class="slide l-gantt">
  <svg class="deco" style="left:722.3px;top:461.5px;width:237.7px;height:79.2px"><use href="#m26a"/></svg>
  <svg class="deco" style="left:18.4px;top:22.1px;width:31.0px;height:97.5px"><use href="#m2c"/></svg>
  <svg class="deco" style="left:878.4px;top:-81.5px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <h2 class="title">Kế hoạch thực hiện</h2>
  <div class="g" style="--m:6">
    <div></div><div class="mo">Th 1</div><div class="mo">Th 2</div><div class="mo">Th 3</div><div class="mo">Th 4</div><div class="mo">Th 5</div><div class="mo">Th 6</div>
    <div class="ph-l">[Giai đoạn 1]</div><div class="bar" style="grid-column:2 / span 2"><span>[Việc 1]</span><span>[Việc 2]</span></div>
    <div class="ph-l">[Giai đoạn 2]</div><div class="bar cyan" style="grid-column:3 / span 3"><span>[Việc 1]</span><span>[Việc 2]</span></div>
    <div class="ph-l">[Giai đoạn 3]</div><div class="bar" style="grid-column:5 / span 3"><span>[Việc 1]</span><span>[Việc 2]</span></div>
  </div>
</section>
```

## 32. `team` — Thành viên (Team)

2–5 members (default markup has 4). For 5 members add class "five" to .grid. Photos square, in color. Full name ≤ 2 lines (≈ 20 characters), role ≤ 5 words.

```html
<section class="slide l-team">
  <svg class="deco" style="left:722.3px;top:461.5px;width:237.7px;height:79.2px"><use href="#m26a"/></svg>
  <svg class="deco" style="left:916.5px;top:221.2px;width:30.9px;height:97.5px"><use href="#m1b"/></svg>
  <svg class="deco" style="left:-80.1px;top:87.4px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <h2 class="title">Thành viên nhóm</h2>
  <div class="grid">
    <div class="m"><div class="face"><div class="ph">[ẢNH]</div></div><div class="h4">[Thành viên 1]</div><p>[Vai trò 1]</p></div>
    <div class="m"><div class="face"><div class="ph">[ẢNH]</div></div><div class="h4">[Thành viên 2]</div><p>[Vai trò 2]</p></div>
    <div class="m"><div class="face"><div class="ph">[ẢNH]</div></div><div class="h4">[Thành viên 3]</div><p>[Vai trò 3]</p></div>
    <div class="m"><div class="face"><div class="ph">[ẢNH]</div></div><div class="h4">[Thành viên 4]</div><p>[Vai trò 4]</p></div>
  </div>
</section>
```

## 33. `diagram` — Sơ đồ tự do (Free diagram canvas)

Architecture, flows, ERD overview. Draw with .node boxes or inline SVG using .f-*/.s-* classes only.

```html
<section class="slide l-diagram">
  <svg class="deco" style="left:722.3px;top:461.5px;width:237.7px;height:79.2px"><use href="#m26a"/></svg>
  <svg class="deco" style="left:18.4px;top:22.1px;width:31.0px;height:97.5px"><use href="#m2c"/></svg>
  <svg class="deco" style="left:878.4px;top:-81.5px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <h2 class="title">[Kiến trúc hệ thống]</h2>
  <div class="stage">
    <svg width="780" height="300" viewBox="0 0 780 300">
      <g class="f-none s-cyan" stroke-width="2"><rect x="20" y="115" width="160" height="70"/><rect x="310" y="115" width="160" height="70"/></g>
      <rect class="f-blue" x="600" y="40" width="160" height="70"/><rect class="f-blue" x="600" y="190" width="160" height="70"/>
      <g class="s-cyan" stroke-width="2"><line x1="180" y1="150" x2="310" y2="150"/><polyline class="f-none" points="470,150 535,150 535,75 600,75"/><polyline class="f-none" points="535,150 535,225 600,225"/></g>
      <g class="f-cyan"><path d="M310 150 l-10 -6 v12 z"/><path d="M600 75 l-10 -6 v12 z"/><path d="M600 225 l-10 -6 v12 z"/></g>
      <g class="f-white" font-size="18" text-anchor="middle"><text x="100" y="156">[Client]</text><text x="390" y="156">[API]</text><text x="680" y="81">[Dịch vụ A]</text><text x="680" y="231">[CSDL]</text></g>
      <g class="f-cyan" font-size="14" text-anchor="middle"><text x="245" y="140">[HTTPS]</text></g>
    </svg>
  </div>
</section>
```

## 34. `thanks` — Cảm ơn / Q&A (Closing)

Last slide. Question prompt + contact, repo and demo links.

```html
<section class="slide l-thanks">
  <svg class="deco" style="left:18.4px;top:22.1px;width:31.0px;height:97.5px"><use href="#m2c"/></svg>
  <svg class="deco" style="left:878.4px;top:-81.5px;width:164.2px;height:164.2px"><use href="#m1c"/></svg>
  <svg class="deco" style="left:722.3px;top:461.5px;width:237.7px;height:79.2px"><use href="#m26a"/></svg>
  <svg class="deco" style="left:0px;top:277.2px;width:87.6px;height:262.8px"><use href="#m29d"/></svg>
  <div class="ty">
    <div class="big">Cảm ơn!</div>
    <p class="ask">Thầy cô và các bạn có câu hỏi nào không?</p>
    <p>[email]<br>[github/link repo]<br>[link demo]</p>
    <div class="icons">
      <svg class="icon" viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
      <svg class="icon" viewBox="0 0 24 24"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/><path d="M9 18c-4.51 2-5-2-7-2"/></svg>
      <svg class="icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>
    </div>
  </div>
</section>
```
