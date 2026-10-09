# -*- coding: utf-8 -*-
"""Contrôles avant publication : liens internes et ancres, un H1 par page, titres et descriptions,
JSON-LD lisible, sitemap cohérent, mots interdits. Usage : python3 -I tools/check.py"""
import pathlib, re, json, html, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
DIST = ROOT / 'dist'
pages = {}
for f in DIST.rglob('*.html'):
    rel = '/' + str(f.relative_to(DIST))[:-5]
    rel = '/' if rel == '/index' else rel
    pages[rel] = f.read_text(encoding='utf-8')
errs, warns = [], []
titles = {}
static = {('/' + str(p.relative_to(DIST))) for p in DIST.rglob('*') if p.is_file()}
redirects = {r['source'] for r in json.loads((ROOT / 'vercel.json').read_text())['redirects']}
for path, doc in pages.items():
    ids = set(re.findall(r'\sid="([^"]+)"', doc))
    h1 = re.findall(r'<h1[\s>]', doc)
    if len(h1) != 1: errs.append(f'{path}: {len(h1)} h1')
    t = re.search(r'<title>(.*?)</title>', doc, re.S).group(1)
    d = re.search(r'<meta name="description" content="([^"]*)"', doc).group(1)
    if path not in ('/404',) and 'noindex' not in doc:
        titles.setdefault(t, []).append(path)
        if not (30 <= len(html.unescape(t)) <= 70): warns.append(f'{path}: titre {len(html.unescape(t))} car.')
        if not (90 <= len(html.unescape(d)) <= 175): warns.append(f'{path}: description {len(html.unescape(d))} car.')
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
        try: json.loads(m.replace('<\\/', '</'))
        except Exception as e: errs.append(f'{path}: JSON-LD {e}')
    for href in re.findall(r'href="([^"]+)"', doc):
        if href.startswith(('http', 'mailto:', 'tel:')): continue
        base, _, frag = href.partition('#')
        base = base.split('?')[0]
        if base == '':
            if frag and frag not in ids and frag != 'erreur': errs.append(f'{path}: ancre #{frag} absente')
            continue
        if base in pages:
            if frag and frag not in set(re.findall(r'\sid="([^"]+)"', pages[base])): errs.append(f'{path}: {href} ancre absente')
        elif base not in static and base not in redirects:
            errs.append(f'{path}: lien cassé {href}')
    for bad in ('WorkRepublik', 'TODO', 'À FOURNIR', 'lorem', 'NON VÉRIFIÉ'):
        if bad.lower() in doc.lower(): errs.append(f'{path}: mot interdit {bad}')
for t, ps in titles.items():
    if len(ps) > 1: errs.append(f'titre dupliqué {t} : {ps}')
sm = (DIST / 'sitemap.xml').read_text()
for loc in re.findall(r'<loc>https://architecte-commerce.fr(.*?)</loc>', sm):
    if loc not in pages: errs.append(f'sitemap : {loc} absent')
print(f'{len(pages)} pages contrôlées')
for w in warns: print('AVERTISSEMENT', w)
for e in errs: print('ERREUR', e)
sys.exit(1 if errs else 0)
