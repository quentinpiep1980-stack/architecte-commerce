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
CSS = (STATIC / 'css/site.css').read_text().replace('url("/fonts/archivo.woff2")', 'url("' + (STATIC / 'fonts/archivo.woff2').as_uri() + '")')

def page(body, w, h):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS} html,body{{margin:0;width:{w}px;height:{h}px;overflow:hidden;background:var(--plan)}}</style></head><body>{body}</body></html>'

ICON = '<div style="width:512px;height:512px;background:#133A63;display:grid;place-items:center"><div style="width:380px;color:#fff">' + B.symbol('', '#FFFFFF') + '</div><div style="position:absolute;left:66px;right:66px;bottom:70px;height:22px;background:#FFB52E"></div></div>'

def og(title, sub, act):
    el = D.elevation(act, 'og').replace('class="elev"', 'class="elev" style="width:1400px;max-width:none;margin-left:-100px"')
    return page(f'''<div class="draw" style="position:relative;width:1200px;height:630px;overflow:hidden;background:var(--plan)">
<div style="position:absolute;left:0;right:0;bottom:-60px">{el}</div>
<div style="position:absolute;left:0;right:0;top:0;height:330px;background:linear-gradient(var(--plan) 62%, rgba(19,58,99,0))"></div>
<div style="position:absolute;left:64px;top:52px;right:64px;color:#fff">
<img src="{(STATIC / 'brand/kalya-blanc.svg').as_uri()}" style="height:38px;margin-bottom:34px">
<div style="font-family:Archivo;font-stretch:125%;font-weight:830;font-size:76px;line-height:.95;letter-spacing:-.02em">{title}</div>
<div style="font-family:Archivo;font-size:26px;color:#D3E3F5;margin-top:18px">{sub}</div></div></div>''', 1200, 630)

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
        ('architecte-commerce', 'Architecte commerce<br>à Paris', 'Du local vide à la vitrine allumée, autorisations comprises.', 'boutique'),
        ('restaurant', 'Architecte restaurant<br>à Paris', 'Cuisine, extraction, ERP type N, terrasse.', 'restaurant'),
    ]:
        load(pg, og(title, sub, act)); pg.wait_for_timeout(800)
        Image.open(io.BytesIO(pg.screenshot())).convert('RGB').save(STATIC / 'og' / f'{name}.png', optimize=True)
    b.close()
print('ok')
