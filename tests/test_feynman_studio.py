"""
End-to-end tests of Feynman Studio.

They open index.html in a real browser (Chromium, through Playwright), draw and edit diagrams the way a
person does, and check what the app holds and what it exports.

    pip install -r tests/requirements.txt
    python -m playwright install chromium
    pytest tests

The LaTeX and PDF libraries are loaded from their CDN, so the tests need an internet connection
(set FS_LIBS to a folder holding katex/, mathjax/ and jspdf/ to run them offline).
The TikZ compilation test runs only when pdflatex is installed.
"""
import functools, http.server, io, json, os, re, shutil, subprocess, threading, zipfile
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / 'examples' / 'showcase.json'
LIBS = os.environ.get('FS_LIBS')


@pytest.fixture(scope='session')
def server():
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
    handler.log_message = lambda *a: None
    httpd = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    yield f'http://127.0.0.1:{httpd.server_address[1]}/index.html'
    httpd.shutdown()


def _route(route):
    url = route.request.url
    if LIBS:
        for key, sub in (('KaTeX/0.16.9/', 'katex/dist/'), ('mathjax@3.2.2/', 'mathjax/')):
            if key in url:
                return route.fulfill(path=os.path.join(LIBS, sub + url.split(key)[1]))
        if 'jspdf' in url:
            return route.fulfill(path=os.path.join(LIBS, 'jspdf/dist/jspdf.umd.min.js'))
    return route.continue_()


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        b = p.chromium.launch()
        yield b
        b.close()


@pytest.fixture
def app(browser, server):
    ctx = browser.new_context(viewport={'width': 1440, 'height': 900}, accept_downloads=True)
    ctx.add_init_script("try{localStorage.setItem('feynmanStudio.checkBeforeExport','false')}catch(e){}")
    ctx.route('**/*', _route)
    page = ctx.new_page()
    errors = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.goto(server)
    page.wait_for_function("!!(window.MathJax && typeof window.MathJax.tex2svg==='function')", timeout=60000)
    page.wait_for_timeout(1200)
    page.errors = errors
    yield page
    ctx.close()


def state(page):
    return page.evaluate("JSON.parse(JSON.stringify(window.__fsV21.state()))")


def load_example(page):
    page.set_input_files('#loadProjectInput', str(EXAMPLE))
    page.wait_for_timeout(1200)
    page.evaluate("window.__fsSetPinned && window.__fsSetPinned(false)")


def download(page, action):
    with page.expect_download(timeout=60000) as d:
        page.evaluate(action) if isinstance(action, str) else action()
    return Path(d.value.path()).read_bytes()


# ---------------------------------------------------------------------------------------------- drawing

def test_opens_blank_without_errors(app):
    s = state(app)
    assert not (s['vertices'] or s['lines'] or s['symbols'])
    assert not app.errors


def test_click_places_vertices_and_joins_them(app):
    box = app.locator('.canvas-wrap').bounding_box()
    a = (box['x'] + box['width'] * 0.4, box['y'] + box['height'] * 0.5)
    b = (box['x'] + box['width'] * 0.6, box['y'] + box['height'] * 0.5)
    app.mouse.click(*a); app.wait_for_timeout(250)
    app.mouse.click(*b); app.wait_for_timeout(250)
    assert len(state(app)['vertices']) == 2
    for v in app.evaluate("[...document.querySelectorAll('#content-layer [data-kind=vertex]')].map(e=>{const r=e.getBoundingClientRect(); return [r.left+r.width/2, r.top+r.height/2]})"):
        app.mouse.click(*v); app.wait_for_timeout(250)
    s = state(app)
    assert len(s['lines']) == 1 and {s['lines'][0]['from'], s['lines'][0]['to']} == {v['id'] for v in s['vertices']}
    app.keyboard.press('Control+z'); app.wait_for_timeout(200)
    assert len(state(app)['lines']) == 0


def test_library_inserts_ready_made_diagrams_without_labels(app):
    app.evaluate("window.__fsOpenDrawer('diagrams')"); app.wait_for_timeout(600)
    tiles = app.locator('#fsDrwRow .fs-tile')
    assert tiles.count() == 12
    tiles.nth(3).click(); app.wait_for_timeout(500)  # GW self-energy
    s = state(app)
    assert len(s['lines']) == 2 and all(not (l['text'] if isinstance(l, dict) else '') for v in s['vertices'] for l in v['labels'])


# ---------------------------------------------------------------------------------------------- editing

def test_momentum_arrow_follows_its_line(app):
    load_example(app)
    app.evaluate("window.__fsV21.select('line','L1')"); app.keyboard.press('p'); app.wait_for_timeout(300)
    arrow = [a for a in state(app)['annotations'] if a.get('att', {}).get('line') == 'L1'][0]
    app.evaluate("(()=>{const s=window.__fsV21.state(); s.vertices.find(v=>v.id==='V1').y += 72; s.vertices.find(v=>v.id==='V2').y += 72; window.__feynmanRender();})()")
    moved = [a for a in state(app)['annotations'] if a['id'] == arrow['id']][0]
    assert abs(moved['P0']['y'] - arrow['P0']['y'] - 72) < 0.01


def test_copy_paste_style_lines_and_kernel_legs(app):
    load_example(app)
    app.evaluate("window.__fsV21.select('line','L6')"); app.keyboard.press('Control+Alt+c')
    app.evaluate("window.__fsV21.selectMany([{type:'line',id:'L7'},{type:'kernelunit',id:'K1'}])"); app.keyboard.press('Control+Alt+v'); app.wait_for_timeout(200)
    s = state(app)
    l6, l7 = [next(l for l in s['lines'] if l['id'] == i) for i in ('L6', 'L7')]
    k1 = next(k for k in s['kernelUnits'] if k['id'] == 'K1')
    assert l7['style'] == l6['style'] and l7['color'] == l6['color'] and l7['from'] == 'V9'
    assert k1['lineStyle'] == l6['style']


def test_groups_move_together_and_locked_elements_stay(app):
    load_example(app)
    app.evaluate("window.__fsV21.selectMany([{type:'vertex',id:'V1'},{type:'vertex',id:'V2'}])"); app.keyboard.press('Control+g'); app.wait_for_timeout(200)
    app.evaluate("window.__fsV21.selectMany([])")
    x, y = app.evaluate("(()=>{const r=document.querySelector('#content-layer [data-kind=vertex][data-id=V1]').getBoundingClientRect(); return [r.left+r.width/2, r.top+r.height/2]})()")
    before = {v['id']: (v['x'], v['y']) for v in state(app)['vertices']}
    app.mouse.move(x, y); app.mouse.down(); app.mouse.move(x + 30, y + 70, steps=10); app.mouse.up(); app.wait_for_timeout(300)
    after = {v['id']: (v['x'], v['y']) for v in state(app)['vertices']}
    d1 = (after['V1'][0] - before['V1'][0], after['V1'][1] - before['V1'][1])
    assert d1 != (0, 0) and d1 == (after['V2'][0] - before['V2'][0], after['V2'][1] - before['V2'][1])
    app.evaluate("window.__fsV21.select('kernelunit','K1')"); app.keyboard.press('Control+Shift+l'); app.wait_for_timeout(200)
    k0 = next(k for k in state(app)['kernelUnits'] if k['id'] == 'K1')
    app.keyboard.press('r'); app.keyboard.press('Delete'); app.wait_for_timeout(200)
    k1 = next(k for k in state(app)['kernelUnits'] if k['id'] == 'K1')
    assert (k1['cx'], k1['cy'], k1.get('angle', 0)) == (k0['cx'], k0['cy'], k0.get('angle', 0))


def test_check_diagram_flags_unbalanced_fermion_arrows(app):
    load_example(app)
    app.evaluate("(()=>{const l=window.__fsV21.state().lines.find(l=>l.id==='L8'); l.reverseArrow=true; window.__feynmanRender();})()")
    app.evaluate("window.__fsOpenExport()"); app.wait_for_timeout(400)
    app.click('#checkDiagramBtn'); app.wait_for_timeout(400)
    assert 'Fermion arrows do not balance' in app.inner_text('.check-box')


# ---------------------------------------------------------------------------------------------- export

def test_svg_and_tikz_exports(app):
    load_example(app)
    svg = download(app, "document.getElementById('exportSvgBtn').click()").decode()
    assert svg.startswith('<svg') and 'viewBox' in svg and svg.count('<path') > 20
    tex = download(app, "document.getElementById('exportTikzBtn').click()").decode()
    assert '\\begin{tikzpicture}' in tex and '\\end{tikzpicture}' in tex and '$G_0$' in tex


def test_png_and_pdf_exports(app):
    load_example(app)
    png = download(app, "document.getElementById('exportPngBtn').click()")
    assert png[:8] == b'\x89PNG\r\n\x1a\n'
    pdf = download(app, "document.getElementById('exportPdfBtn').click()")
    assert pdf[:5] == b'%PDF-'


def test_export_selection_only(app):
    load_example(app)
    full = download(app, "document.getElementById('exportTikzBtn').click()").decode()
    app.evaluate("window.__fsV21.selectMany([{type:'line',id:'L1'}])"); app.wait_for_timeout(200)
    app.evaluate("window.__fsOpenExport()"); app.wait_for_timeout(300)
    app.evaluate("window.__fsExportSel.set(true)")
    part = download(app, "document.getElementById('exportTikzBtn').click()").decode()
    assert part.count('\\draw') < full.count('\\draw') / 3


def test_export_all_diagrams_as_zip_and_pdf(app):
    load_example(app)
    app.evaluate("window.__fsDuplicateTab()"); app.wait_for_timeout(500)
    z = zipfile.ZipFile(io.BytesIO(download(app, "window.__fsExportAll.run('tikz')")))
    assert len(z.namelist()) == 2 and z.testzip() is None
    pdf = download(app, "window.__fsExportAll.run('pdf')")
    assert len(re.findall(rb'/Type\s*/Page[^s]', pdf)) == 2


@pytest.mark.skipif(not shutil.which('pdflatex'), reason='pdflatex not installed')
def test_tikz_compiles_with_pdflatex(app, tmp_path):
    load_example(app)
    for line in ('L1', 'L6'):
        app.evaluate(f"window.__fsV21.select('line','{line}')"); app.keyboard.press('p'); app.wait_for_timeout(150)
    tex = download(app, "document.getElementById('exportTikzBtn').click()").decode()
    (tmp_path / 'fig.tex').write_text(tex)
    (tmp_path / 'doc.tex').write_text('\\documentclass{standalone}\n\\usepackage{tikz}\\usepackage{amsmath}\n'
        '\\usetikzlibrary{arrows.meta, decorations.pathmorphing, decorations.markings, calc, shadings, svg.path}\n'
        '\\begin{document}\n\\input{fig.tex}\n\\end{document}\n')
    r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'doc.tex'], cwd=tmp_path, capture_output=True, text=True, timeout=180)
    assert r.returncode == 0, r.stdout[-3000:]
    assert (tmp_path / 'doc.pdf').exists()


# ---------------------------------------------------------------------------------------------- projects

def test_project_round_trip_with_versions(app, tmp_path):
    load_example(app)
    app.evaluate("window.__fsVersions.save('first')")
    data = json.loads(download(app, "document.getElementById('saveProjectBtn').click()"))
    assert data['versions'][0]['name'] == 'first' and len(data['lines']) == len(state(app)['lines'])
    f = tmp_path / 'project.json'; f.write_text(json.dumps(data))
    app.set_input_files('#loadProjectInput', str(f)); app.wait_for_timeout(800)
    assert app.evaluate("window.__fsVersions.list().length") == 1
    assert not app.errors
