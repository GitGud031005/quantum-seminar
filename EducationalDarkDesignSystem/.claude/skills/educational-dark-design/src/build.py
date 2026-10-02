"""Regenerate references/layouts.md and examples/showcase.html from assets/starter.html + src/snippets.html."""
import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
starter = (root/'assets/starter.html').read_text(encoding='utf-8')
snips = (root/'src/snippets.html').read_text(encoding='utf-8')
parts = re.split(r'<!--@ (.*?) -->\n', snips)[1:]
items = [(h.split(' | '), body.strip()) for h, body in zip(parts[::2], parts[1::2])]
start, end = '<!-- ================= SLIDES START ================= -->', '<!-- ================= SLIDES END ================= -->'
show = starter.replace('<title>DECK TITLE</title>', '<title>Educational Dark — Layout Showcase</title>')
show = show.replace(start + '\n\n' + end, start + '\n' + '\n\n'.join(f'<!-- layout: {m[0]} -->\n{b}' for m, b in items) + '\n' + end)
(root/'examples').mkdir(exist_ok=True); (root/'examples/showcase.html').write_text(show, encoding='utf-8')
md = ['# Layout catalog', '',
      'Every slide in a deck MUST be one of these layouts. Copy the snippet, keep the class names and every <svg class="deco"> motif line exactly; change only the text, numbers, images and (where the notes allow) item counts.',
      'Live preview of all layouts: `examples/showcase.html` (press O for overview).', '',
      '| # | id | Name | Use when |', '|---|---|---|---|']
md += [f'| {i+1} | `{m[0]}` | {m[1]} | {m[2]} |' for i, (m, _) in enumerate(items)]
md.append('')
for i, (m, b) in enumerate(items):
    md += [f'## {i+1}. `{m[0]}` — {m[1]}', '', m[2], '', '```html', b, '```', '']
(root/'references').mkdir(exist_ok=True); (root/'references/layouts.md').write_text('\n'.join(md), encoding='utf-8')
print(len(items), 'layouts')
