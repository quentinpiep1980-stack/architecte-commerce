# -*- coding: utf-8 -*-
"""Génère les icônes (favicon.ico, apple-touch-icon, icon-192/512) et l'image de partage (og/*.png)
à partir du logo vectoriel et du dessin d'élévation. Usage : python3 -I tools/assets.py (dépendances : playwright, Pillow)."""
import pathlib, sys, io
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from content import drawings as D, brand as B
from playwright.sync_api import sync_playwright
from PIL import Image

STATIC = ROOT / 'src/static'
CSS = (STATIC / 'css/site.css').read_text()
for _f in ('archivo', 'bodoni', 'bodoni-italic'):
    CSS = CSS.replace(f'url("/fonts/{_f}.woff2")', 'url("' + (STATIC / f'fonts/{_f}.woff2').as_uri() + '")')

def page(body, w, h):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS} html,body{{margin:0;width:{w}px;height:{h}px;overflow:hidden;background:var(--laque)}}</style></head><body>{body}</body></html>'

ICON = '<div style="width:512px;height:512px;background:#0F201B;display:grid;place-items:center;position:relative"><div style="width:360px">' + B.symbol('', '#C49A5A') + '</div><div style="position:absolute;left:66px;right:66px;bottom:72px;height:14px;background:#C49A5A"></div></div>'

def og(title, sub, act):
    sc = D.scene(act, 'og').replace('<svg ', '<svg style="width:1040px;height:auto;display:block" ', 1)
    return page(f'''<div style="position:relative;width:1200px;height:630px;overflow:hidden;background:var(--laque)">
<div class="scene" data-act="{act}" style="position:absolute;left:80px;width:1040px;bottom:-4px;max-width:none">{sc}</div>
<div style="position:absolute;left:64px;top:46px;right:64px;color:var(--craie)">
<img src="{(STATIC / 'brand/kalya-laiton.svg').as_uri()}" style="height:34px;margin-bottom:26px">
<div style="font-family:Bodoni;font-weight:500;font-size:62px;line-height:1;letter-spacing:-.01em">{title}</div>
<div style="font-family:Archivo;font-size:25px;color:var(--laiton-2);margin-top:14px">{sub}</div></div></div>''', 1200, 630)

import tempfile
TMP = pathlib.Path(tempfile.mkdtemp())
def load(pg, html):
    f = TMP / 'p.html'; f.write_text(html, encoding='utf-8'); pg.goto(f.as_uri())

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 512, 'height': 512})
    load(pg, page(ICON, 512, 512)); pg.wait_for_timeout(300)
    png = pg.screenshot()
    im = Image.open(io.BytesIO(png)).convert('RGB')
    im.save(STATIC / 'icon-512.png')
    im.resize((192, 192), Image.LANCZOS).save(STATIC / 'icon-192.png')
    im.resize((180, 180), Image.LANCZOS).save(STATIC / 'apple-touch-icon.png')
    im.resize((48, 48), Image.LANCZOS).save(STATIC / 'favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
    pg = b.new_page(viewport={'width': 1200, 'height': 630})
    (STATIC / 'og').mkdir(exist_ok=True)
    for name, title, sub, act in [
        ('architecte-commerce', 'Architecte de commerces à Paris', 'Faisabilité avant bail, autorisations, chantier. Réponse sous 24 heures.', 'boutique'),
        ('restaurant', 'Architecte restaurant à Paris', 'Cuisine, extraction, ERP de type N, terrasse.', 'restaurant'),
    ]:
        load(pg, og(title, sub, act)); pg.wait_for_timeout(800)
        Image.open(io.BytesIO(pg.screenshot())).convert('RGB').save(STATIC / 'og' / f'{name}.png', optimize=True)
    b.close()
print('ok')
