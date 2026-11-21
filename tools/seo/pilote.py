# -*- coding: utf-8 -*-
"""Outils d'analyse du pilote SEO / GEO / GEA d'architecte-commerce.fr. Lecture seule : rien n'est publié.

    python3 -I tools/seo/pilote.py sc ENTREE.json SORTIE.csv
        Convertit les lignes Search Console renvoyées par Windsor.ai (tableau « data » de get_data, copié tel quel dans
        ENTREE.json) au format des relevés : requete;page;clics;impressions;ctr;position (requête × page),
        page;clics;impressions;ctr;position (page seule) ou date;clics;impressions (série quotidienne).
    python3 -I tools/seo/pilote.py opportunites RELEVE.csv [--min 5]
        Classe les requêtes : positions 4 à 20 (score = impressions × (21 − position) / 17), mauvaise page classée
        (page différente de la page cible de QUERY_UNIVERSE.csv), cannibalisation (une requête, plusieurs pages),
        requêtes d'un autre site de Quentin (à signaler à son pilote), requêtes sans groupe (à classer).
    python3 -I tools/seo/pilote.py positions
        Compare les deux derniers relevés data/positions/ : gagnées, perdues, top 3 / 10 / 20.
    python3 -I tools/seo/pilote.py geo
        Résume le dernier relevé data/geo/ (cité, mentionné, absent) et l'écart avec le précédent.
    python3 -I tools/seo/pilote.py registre [--date AAAA-MM-JJ]
        Lignes de CHANGE_LEDGER.csv dont la relecture à 7, 28 ou 90 jours est due et non renseignée.

Le score d'opportunité est un ordre de travail interne, pas une prévision de clics.
"""
import csv, datetime, json, pathlib, re, sys, unicodedata
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[2]
SYS = ROOT / 'SEO_GEO_GEA_SYSTEM'
HOST = 'architecte-commerce.fr'


def norm(s):
    s = unicodedata.normalize('NFKD', s.lower().replace('’', "'")).encode('ascii', 'ignore').decode()
    return re.sub(r"[^a-z0-9' ]+", ' ', s).split()


def read_csv(path):
    with open(path, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter=';'))


def univers():
    rows = read_csv(SYS / 'QUERY_UNIVERSE.csv')
    for r in rows:
        r['_ex'] = [norm(e) for e in r['exemples'].split('|') if e.strip()]
    return rows


def groupe(q, rows):
    """Groupe de la requête : exemple identique, sinon exemple dont tous les mots sont dans la requête (le plus long)."""
    w = norm(q)
    best, size = None, 0
    for r in rows:
        for ex in r['_ex']:
            if ex == w:
                return r
            if ex and set(ex) <= set(w) and len(ex) > size:
                best, size = r, len(ex)
    return best


COLS = [('query', 'requete'), ('date', 'date'), ('page', 'page'), ('clicks', 'clics'), ('impressions', 'impressions'),
        ('ctr', 'ctr'), ('position', 'position')]


def cmd_sc(src, dst):
    """Lignes Windsor (requête × page, page seule ou jour) → CSV des relevés, colonnes dans l'ordre de COLS."""
    data = json.loads(pathlib.Path(src).read_text(encoding='utf-8'))
    data = data.get('data', data) if isinstance(data, dict) else data
    cols = [(k, nom) for k, nom in COLS if data and k in data[0]]
    with open(dst, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter=';', lineterminator='\n')
        w.writerow([nom for _, nom in cols])
        for r in data:
            ligne = []
            for k, _ in cols:
                v = r.get(k)
                if k == 'page':
                    v = re.sub(r'^https?://(www\.)?' + re.escape(HOST), '', v or '') or '/'
                elif k in ('clicks', 'impressions'):
                    v = int(v or 0)
                elif k == 'ctr':
                    v = round(float(v or 0), 4)
                elif k == 'position':
                    v = round(float(v or 0), 2)
                ligne.append(v)
            w.writerow(ligne)
    print(f"{len(data)} lignes écrites dans {dst}")


def cmd_opportunites(path, mini):
    rows, U = read_csv(path), univers()
    for r in rows:
        r['impressions'], r['position'], r['clics'] = int(r['impressions']), float(r['position']), int(r['clics'])
        r['page'] = r['page'].replace(' (http)', '')
    par_requete = defaultdict(list)
    for r in rows:
        par_requete[r['requete']].append(r)
    print(f"# Opportunités — {pathlib.Path(path).name}\n")
    print("## Positions 4 à 20 (score = impressions × (21 − position) / 17)")
    pos = sorted([r for r in rows if 4 <= r['position'] <= 20 and r['impressions'] >= mini],
                 key=lambda r: -r['impressions'] * (21 - r['position']) / 17)
    for r in pos[:15]:
        print(f"- {r['requete']} → {r['page']} : position {r['position']:.1f}, {r['impressions']} impressions, "
              f"{r['clics']} clic(s), score {r['impressions'] * (21 - r['position']) / 17:.0f}")
    if not pos:
        print("- aucune")
    print("\n## Mauvaise page classée, autre site, sans groupe")
    autres, sans, mauvaises = [], [], []
    for q, rs in par_requete.items():
        imp = sum(r['impressions'] for r in rs)
        if imp < mini:
            continue
        g = groupe(q, U)
        if not g:
            sans.append((q, imp))
            continue
        if g.get('decision', '').startswith('IGNORER') or g.get('site') in ('', '—'):
            continue
        if g['site'] != HOST:
            autres.append((q, imp, g['site'], g['cluster']))
            continue
        cible = g['page_cible'].split()[0] if g['page_cible'] else ''
        top = max(rs, key=lambda r: r['impressions'])
        if cible.startswith('/') and top['page'] != cible:
            mauvaises.append((q, imp, top['page'], cible, g['cluster']))
    for q, imp, p, c, cl in sorted(mauvaises, key=lambda x: -x[1]):
        print(f"- MAUVAISE PAGE : « {q} » ({imp} impr.) classe {p}, page cible {c} [{cl}]")
    for q, imp, site, cl in sorted(autres, key=lambda x: -x[1]):
        print(f"- AUTRE SITE : « {q} » ({imp} impr.) relève de {site} [{cl}] : à signaler, ne pas créer de contenu ici")
    for q, imp in sorted(sans, key=lambda x: -x[1]):
        print(f"- SANS GROUPE : « {q} » ({imp} impr.) : à classer dans QUERY_UNIVERSE.csv (ou à ignorer si hors sujet)")
    print("\n## Cannibalisation (une requête, plusieurs pages avec impressions)")
    can = [(q, rs) for q, rs in par_requete.items() if len(rs) > 1 and sum(r['impressions'] for r in rs) >= mini]
    for q, rs in sorted(can, key=lambda x: -sum(r['impressions'] for r in x[1])):
        print(f"- « {q} » : " + ' ; '.join(f"{r['page']} ({r['impressions']} impr., pos. {r['position']:.1f})" for r in sorted(rs, key=lambda r: -r['impressions'])))
    if not can:
        print("- aucune")


def releves(dossier):
    return sorted((SYS / 'data' / dossier).glob('2*.csv'))


def rang(v):
    try:
        return int(v)
    except ValueError:
        return 99


def cmd_positions():
    fs = releves('positions')
    if not fs:
        return print("aucun relevé")
    cur = {r['id']: r for r in read_csv(fs[-1])}
    prev = {r['id']: r for r in read_csv(fs[-2])} if len(fs) > 1 else {}
    ranks = [rang(r['position']) for r in cur.values()]
    print(f"Relevé {fs[-1].stem} ({len(cur)} requêtes) : top 3 {sum(x <= 3 for x in ranks)}, top 10 {sum(x <= 10 for x in ranks)}, top 20 {sum(x <= 20 for x in ranks)}")
    if prev:
        print(f"Comparaison avec {fs[-2].stem} :")
        for i, r in cur.items():
            a, b = rang(prev.get(i, {}).get('position', '> 20')), rang(r['position'])
            if a != b:
                sens = 'gagnée' if b < a else 'perdue'
                print(f"- {sens} : {r['requete']} : {prev.get(i, {}).get('position', '—')} → {r['position']} {r.get('url', '')}")


def cmd_geo():
    fs = releves('geo')
    if not fs:
        return print("aucun relevé")
    def bilan(f):
        c = defaultdict(int)
        for r in read_csv(f):
            c[r['statut']] += 1
        return c
    cur = bilan(fs[-1])
    print(f"Relevé {fs[-1].stem} : cité {cur['cité']}, mentionné {cur['mentionné']}, absent {cur['absent']}, non mesurable {cur['non mesurable']}")
    if len(fs) > 1:
        p = bilan(fs[-2])
        print(f"Précédent {fs[-2].stem} : cité {p['cité']}, mentionné {p['mentionné']}, absent {p['absent']}")


def cmd_registre(date):
    d = datetime.date.fromisoformat(date)
    for r in read_csv(SYS / 'CHANGE_LEDGER.csv'):
        if not r.get('publie'):
            continue
        try:
            pub = datetime.date.fromisoformat(r['publie'][:10])
        except ValueError:
            continue
        for n, col in ((7, 'resultat_7j'), (28, 'resultat_28j'), (90, 'resultat_90j')):
            if (d - pub).days >= n and not r.get(col):
                print(f"- {r['id']} ({r['url']}) : relecture à {n} jours due depuis le {(pub + datetime.timedelta(days=n)).isoformat()} — {r['changement'][:90]}")


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit(0)
    if a[0] == 'sc':
        cmd_sc(a[1], a[2])
    elif a[0] == 'opportunites':
        cmd_opportunites(a[1], int(a[a.index('--min') + 1]) if '--min' in a else 5)
    elif a[0] == 'positions':
        cmd_positions()
    elif a[0] == 'geo':
        cmd_geo()
    elif a[0] == 'registre':
        cmd_registre(a[a.index('--date') + 1] if '--date' in a else datetime.date.today().isoformat())
    else:
        print(__doc__); sys.exit(1)
