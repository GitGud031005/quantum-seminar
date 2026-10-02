#!/usr/bin/env python3
"""Validate a deck built with the educational-dark-design design system.

Usage:
  python3 check_deck.py deck.html                 # static checks only (no deps)
  python3 check_deck.py deck.html --render out/   # + render every slide to PNG and run layout checks
Rendering uses Playwright when installed (pip install playwright; playwright install chromium),
otherwise a locally installed Chrome / Edge in headless mode. Pillow (optional) adds contact-sheet.png.
Options:
  --wide-font   render with a wider fallback font (Verdana) to stress-test text overflow
                when Signika / Lato cannot be downloaded (offline machines).

Exit code 0 = no errors (warnings may still be printed).
"""
import re, sys, json, html as htmllib, pathlib, argparse, shutil, subprocess, tempfile

PALETTE = {'#0d1030', '#79e0ff', '#0f5aff', '#c2c2c2', '#ffffff', '#fff'}
RGBA_OK = (['255', '255', '255'], ['13', '16', '48'])
LAYOUTS = {'l-cover', 'l-toc', 'l-whoa', 'l-section', 'l-text2', 'l-bullets', 'l-steps', 'l-zig', 'l-five', 'l-statement',
           'l-quote', 'l-photo', 'l-phototext', 'l-bignum', 'l-stats', 'l-donuts', 'l-pie', 'l-computer', 'l-tablet',
           'l-phone', 'l-table', 'l-figure', 'l-timeline', 'l-hub', 'l-stairs', 'l-gantt', 'l-team', 'l-diagram', 'l-thanks'}
ALLOWED_FONTS = {'signika', 'lato', 'nunito sans', 'arial', 'sans-serif', 'inherit', 'var(--font-display)', 'var(--font-body)'}
EMOJI = re.compile('[\U0001F300-\U0001FAFF\u2600-\u27BF]')


def static_checks(html):
    errs, warns = [], []
    # 1. palette
    for m in set(re.findall(r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b', html)):
        if m.lower() not in PALETTE:
            errs.append(f'color {m} is not in the palette (navy #0D1030, cyan #79E0FF, blue #0F5AFF, grey #C2C2C2, white)')
    for m in set(re.findall(r'rgba?\(([^)]*)\)', html)):
        if [x.strip() for x in m.split(',')][:3] not in RGBA_OK:
            errs.append(f'rgba({m}) is not a palette color')
    # 2. fonts
    for m in re.findall(r'font-family\s*:\s*([^;}"]+)', html):
        if {f.strip().strip('\'"').lower() for f in m.split(',')} - ALLOWED_FONTS:
            errs.append(f'font-family {m.strip()} — only Signika (display) and Lato / Nunito Sans (body) are allowed')
    # 3. tokens untouched: every :root block must match the starter's exactly
    root_re = re.compile(r'^:root\{.*?^\}|^:root:lang\(vi\)\{.*?\}', re.S | re.M)
    starter = pathlib.Path(__file__).resolve().parent.parent / 'assets' / 'starter.html'
    sprite_re = re.compile(r'<svg class="sprite".*?</defs></svg>', re.S)
    if starter.is_file():
        ref = starter.read_text(encoding='utf-8')
        if root_re.findall(ref) != root_re.findall(html):
            errs.append('design tokens in :root were modified or removed — start from assets/starter.html')
        if sprite_re.findall(ref) != sprite_re.findall(html):
            errs.append('the motif sprite was modified or removed — start from assets/starter.html')
    elif '--navy:  #0D1030' not in html or '--cyan:  #79E0FF' not in html:
        errs.append('design tokens in :root were modified or removed — start from assets/starter.html')
    symbols = set(re.findall(r'<symbol id="([\w-]+)"', html))
    for ref_id in sorted(set(re.findall(r'<use href="#([\w-]+)"', html)) - symbols):
        errs.append(f'motif #{ref_id} does not exist in the sprite — copy motif lines from the snippet unchanged')
    # 4. slides, layouts, motif budget
    blocks = re.findall(r'<section\s+class=["\']slide\b([^"\']*)["\'](.*?)</section>', html, re.S)
    if not blocks:
        errs.append('no <section class="slide ..."> found')
    for i, (cls, body) in enumerate(blocks, 1):
        ls = [c for c in cls.split() if c.startswith('l-')]
        if len(ls) != 1 or ls[0] not in LAYOUTS:
            errs.append(f'slide {i}: must have exactly one known layout class (got {ls or "none"})')
        if 'l-zig' in ls and not re.search(r'\bn[234]\b', cls):
            errs.append(f'slide {i}: l-zig needs n2, n3 or n4')
        tokens = [c.split() for _, c in re.findall(r'class=(["\'])(.*?)\1', body)]
        n_deco = sum('deco' in t for t in tokens)
        if n_deco > 5:
            errs.append(f'slide {i}: too many motifs ({n_deco} .deco, max 5 — use the snippet\'s set unchanged)')
        if n_deco == 0:
            warns.append(f'slide {i}: no motifs — every source slide has at least three corner clusters')
        if EMOJI.search(re.sub(r'<svg.*?</svg>', '', body, flags=re.S)):
            errs.append(f'slide {i}: emoji are not part of the style')
    if blocks and 'l-cover' not in blocks[0][0]:
        warns.append('slide 1 is not l-cover')
    if blocks and 'l-thanks' not in blocks[-1][0]:
        warns.append('last slide is not l-thanks')
    # 5. forbidden styling in what the deck author wrote (inline styles + DECK-SPECIFIC block)
    authored = ' '.join(v for _, v in re.findall(r'style=(["\'])(.*?)\1', html))
    ds = re.search(r'=+ DECK-SPECIFIC.*?\*/(.*?)/\* =+ Presentation shell', html, re.S)
    authored += ds.group(1) if ds else ''
    for pat, why in [(r'box-shadow\s*:(?!\s*none)', 'shadows are not part of the style (flat design)'),
                     (r'gradient\(', 'gradients are not part of the style'),
                     (r'border-radius\s*:', 'rounded corners belong to motifs / mockups only'),
                     (r'font-size\s*:\s*[\d.]+px', 'set font sizes with the --fs-* tokens, never in px'),
                     (r'opacity\s*:', 'no transparency on slide content')]:
        if re.search(pat, authored):
            warns.append(why)
    if re.search(r'<img(?![^>]*class="[^"]*(photo|shot|fig-img))', html):
        warns.append('<img> must use class "photo" (photos), "shot" (screenshots) or "fig-img" (charts / figures)')
    return blocks, errs, warns


JS_CHECK = r"""
(idx) => {
  const s = document.querySelectorAll('.slide')[idx];
  const sr = s.getBoundingClientRect();
  const k = sr.width / 960;
  const deco = [...s.querySelectorAll('.deco')].map(e => e.getBoundingClientRect());
  const out = [];
  const box = {x1: 1e9, y1: 1e9, x2: -1e9, y2: -1e9};
  const walker = document.createTreeWalker(s, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = walker.nextNode())) {
    if (!n.textContent.trim()) continue;
    const el = n.parentElement;
    if (el.closest('svg') || el.closest('.ph') || el.closest('.deco')) continue;
    const r = document.createRange(); r.selectNodeContents(n);
    for (const b of r.getClientRects()) {
      const x = (b.left - sr.left) / k, y = (b.top - sr.top) / k, x2 = x + b.width / k, y2 = y + b.height / k;
      box.x1 = Math.min(box.x1, x); box.y1 = Math.min(box.y1, y); box.x2 = Math.max(box.x2, x2); box.y2 = Math.max(box.y2, y2);
      const txt = n.textContent.trim().slice(0, 40);
      if (x < 20 || y < 8 || x2 > 940 || y2 > 532) { out.push(`text outside safe area: "${txt}"`); break; }
      let hit = false;
      for (const d of deco) {
        const dx = (d.left - sr.left) / k, dy = (d.top - sr.top) / k, dw = d.width / k, dh = d.height / k;
        if (x < dx + dw - 1 && x2 > dx + 1 && y < dy + dh - 1 && y2 > dy + 1) { hit = true; break; }
      }
      if (hit) { out.push(`text overlaps a motif: "${txt}"`); break; }
    }
  }
  // hero slides (no title bar) must read as one block centred on the canvas
  if (['l-cover', 'l-whoa', 'l-section', 'l-statement', 'l-quote', 'l-bignum', 'l-thanks'].some(c => s.classList.contains(c)) && box.x2 > box.x1) {
    const dy = (box.y1 + box.y2) / 2 - 270, dx = (box.x1 + box.x2) / 2 - 480;
    if (Math.abs(dy) > 40) out.push(`content block sits ${Math.round(Math.abs(dy))}px ${dy > 0 ? 'below' : 'above'} the slide's centre`);
    if (Math.abs(dx) > 40 && !s.classList.contains('alt')) out.push(`content block sits ${Math.round(Math.abs(dx))}px ${dx > 0 ? 'right' : 'left'} of the slide's centre`);
  }
  for (const t of s.querySelectorAll('svg text')) {
    const b = t.getBoundingClientRect(), v = t.closest('svg').getBoundingClientRect();
    if (b.left < v.left - 1 || b.right > v.right + 1 || b.top < v.top - 1 || b.bottom > v.bottom + 1)
      out.push(`SVG text clipped by its <svg> box: "${t.textContent.trim().slice(0, 40)}"`);
  }
  for (const el of s.querySelectorAll('.title,.cap,.node,.core,.lv,.bar,.stat,.num,.v,.mo,.ph-l,.h3,.h4,.big,.sec-num,.sec-title,.cv-title,.tbl th,.tbl td')) {
    const b = el.getBoundingClientRect(), r = document.createRange(); r.selectNodeContents(el);
    const t = r.getBoundingClientRect(), tol = parseFloat(getComputedStyle(el).fontSize) * .2 * k + 1;
    if (!t.width) continue;
    const txt = el.textContent.trim().slice(0, 40);
    if (t.left < b.left - 2 || t.right > b.right + 2) out.push(`text wider than its box: "${txt}"`);
    else if (t.top < b.top - tol || t.bottom > b.bottom + tol) out.push(`text taller than its box (too many lines): "${txt}"`);
  }
  return [...new Set(out)];
}
"""
HIDE_HUD = '.hud{display:none!important}'
WIDE = ".slide,.slide *{font-family:Verdana,'DejaVu Sans',sans-serif!important}"


def find_browser():
    for c in ['chrome', 'google-chrome', 'chromium', 'chromium-browser', 'msedge', 'microsoft-edge',
              r'C:\Program Files\Google\Chrome\Application\chrome.exe',
              r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
              str(pathlib.Path.home() / 'AppData/Local/Google/Chrome/Application/chrome.exe'),
              r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
              r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
              '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
              '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge']:
        p = shutil.which(c) or (c if pathlib.Path(c).is_file() else None)
        if p:
            return p
    return None


def render_playwright(path, out, wide):
    from playwright.sync_api import sync_playwright
    errs = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 960, 'height': 540})
        pg.goto(pathlib.Path(path).resolve().as_uri())
        if wide:
            pg.add_style_tag(content=WIDE)
        pg.evaluate('document.fonts.ready')
        pg.wait_for_timeout(600)
        pg.add_style_tag(content=HIDE_HUD)
        n = pg.evaluate("document.querySelectorAll('.slide').length")
        for i in range(n):
            pg.evaluate(f"document.querySelectorAll('.slide').forEach((s,k)=>s.classList.toggle('active',k=={i}))")
            pg.screenshot(path=str(out / f'slide-{i+1:02d}.png'))
            errs += [f'slide {i+1}: {m}' for m in pg.evaluate(JS_CHECK, i)]
        b.close()
    return errs


def render_browser(path, out, wide, exe):
    """No-dependency fallback: headless Chrome / Edge on a temporary copy next to the deck (so relative images resolve)."""
    src = pathlib.Path(path).resolve()
    html = src.read_text(encoding='utf-8')
    style = f'<style>{HIDE_HUD}{WIDE if wide else ""}</style>'
    probe = ('<script>addEventListener("load",()=>document.fonts.ready.then(()=>setTimeout(()=>{'
             'document.querySelector(".deck").style.transform="none";const f=' + JS_CHECK.strip() + ';'
             'const S=document.querySelectorAll(".slide"),r=[];for(let i=0;i<S.length;i++){S.forEach((s,k)=>s.classList.toggle("active",k==i));r.push(f(i))}'
             'const p=document.createElement("pre");p.id="__check";p.textContent=JSON.stringify(r);document.body.appendChild(p)},300)))</script>')
    shot = src.with_name(f'.{src.stem}.shot.html')
    tmp = src.with_name(f'.{src.stem}.check.html')
    gate = ('<style>body{visibility:hidden}</style><script>addEventListener("load",()=>document.fonts.ready'
            '.then(()=>document.body.style.visibility="visible"))</script>')
    shot.write_text(html.replace('</head>', style + gate + '</head>', 1), encoding='utf-8')
    tmp.write_text(html.replace('</head>', style + '</head>', 1).replace('</body>', probe + '</body>', 1), encoding='utf-8')
    base = [exe, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run', '--window-size=960,540']
    errs = []
    try:
        with tempfile.TemporaryDirectory() as prof:
            dom = subprocess.run(base + [f'--user-data-dir={prof}', '--virtual-time-budget=15000', '--dump-dom', tmp.as_uri()],
                                 capture_output=True, text=True, encoding='utf-8', timeout=120).stdout
            m = re.search(r'<pre id="__check">(.*?)</pre>', dom, re.S)
            if not m:
                return ['render: the headless browser did not report layout results (timeout?)']
            for i, msgs in enumerate(json.loads(htmllib.unescape(m.group(1)))):
                errs += [f'slide {i+1}: {x}' for x in msgs]
            n = len(re.findall(r'<section\s+class="slide\b', html))
            for i in range(n):
                subprocess.run(base + [f'--user-data-dir={prof}', '--virtual-time-budget=4000',
                                       f'--screenshot={(out / f"slide-{i+1:02d}.png").resolve()}', shot.as_uri() + f'#{i+1}'],
                               capture_output=True, timeout=120)
    finally:
        tmp.unlink(missing_ok=True)
        shot.unlink(missing_ok=True)
    return errs


def render_checks(path, outdir, wide):
    out = pathlib.Path(outdir); out.mkdir(parents=True, exist_ok=True)
    try:
        import playwright  # noqa: F401
        errs = render_playwright(path, out, wide)
    except ImportError:
        exe = find_browser()
        if not exe:
            print('! neither playwright nor Chrome/Edge found — skipped render checks (pip install playwright)')
            return []
        print(f'  rendering with {pathlib.Path(exe).name} (playwright not installed)')
        errs = render_browser(path, out, wide, exe)
    try:  # contact sheet
        from PIL import Image
        files = sorted(out.glob('slide-*.png'))
        cols, w, h = 3, 480, 270
        sheet = Image.new('RGB', (cols * (w + 8), ((len(files) + cols - 1) // cols) * (h + 8)), '#555')
        for k, f in enumerate(files):
            sheet.paste(Image.open(f).convert('RGB').resize((w, h)), ((k % cols) * (w + 8), (k // cols) * (h + 8)))
        sheet.save(out / 'contact-sheet.png')
        print(f'  contact sheet: {out / "contact-sheet.png"}')
    except ImportError:
        print(f'  screenshots: {out} (pip install pillow for a contact sheet)')
    return errs


def main():
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    ap = argparse.ArgumentParser()
    ap.add_argument('deck'); ap.add_argument('--render'); ap.add_argument('--wide-font', action='store_true')
    a = ap.parse_args()
    html = pathlib.Path(a.deck).read_text(encoding='utf-8')
    slides, errs, warns = static_checks(html)
    if a.render:
        errs += render_checks(a.deck, a.render, a.wide_font)
    print(f'{len(slides)} slides checked')
    for w in warns: print('  WARN ', w)
    for e in errs: print('  ERROR', e)
    print('OK' if not errs else f'{len(errs)} error(s)')
    sys.exit(1 if errs else 0)


if __name__ == '__main__':
    main()
