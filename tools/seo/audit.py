# -*- coding: utf-8 -*-
"""Audit SEO / GEO / GEA d'architecte-commerce.fr, bloquant avant toute publication.

Usage (après python3 -I build.py) :
    python3 -I tools/seo/audit.py               contrôle ; code de sortie 1 s'il reste une erreur
    python3 -I tools/seo/audit.py --inventaire  contrôle + URL_INVENTORY.csv, SOURCES_MAP.csv, data/audit/AAAA-MM-JJ.json
    python3 -I tools/seo/audit.py --releve      écrit data/audit/faits_releves.json : montants par page et phrases
                                                « à surveiller » observés (à n'utiliser que dans une session validée par Quentin)

Complète tools/check.py (liens, ancres, h1, JSON-LD lisible, mots interdits). Ici :
- faits contrôlés (SEO_GEO_GEA_SYSTEM/faits_controles.json) : tout montant en euros (« 1 500 € », « 1500€ », « 1.500 € »,
  « 3 000 EUR », « € 900 ») doit y figurer pour la page où il apparaît ; prix du JSON-LD = honoraires publiés ;
  téléphones et courriels fermés ;
- la partie « kalya » de ce fichier (honoraires, téléphones, courriels, phrases publiées) doit avoir l'empreinte KALYA_EMPREINTE,
  également inscrite dans la consigne de la tâche programmée : le pilote ne peut pas l'élargir lui-même ;
- promesses : superlatifs, « résultat / délai / prix garanti », gratuités et prestations non publiées interdits ;
  toute phrase contenant « garanti… », « gratuit… », « offert… » ou un délai (« sous 48 heures », « en 5 jours ») doit
  être une phrase déjà publiée et validée (liste « phrases_publiees ») ;
- entité, FAQ balisée = FAQ visible, canonique, sitemap et dates réelles (content/lastmod.json), titres et descriptions
  (stricts pour les pages créées après le 21/11/2026), maillage éditorial, réponse courte, sources, fraîcheur,
  couverture de llms.txt et llms-full.txt, clé IndexNow, robots.txt.
"""
import csv, datetime, hashlib, html, json, pathlib, re, sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from content import site as S, pages as P, guides as G, core as C  # noqa: E402

DIST = ROOT / 'dist'
SYS = ROOT / 'SEO_GEO_GEA_SYSTEM'
URL = S.SITE['url']
TODAY = datetime.date.today()
INDEXNOW_KEY = '12457e08790f31ac0fc9c51152218be1'
FRAICHEUR_JOURS = 120
# Empreinte de la partie Kalya de faits_controles.json validée par Quentin (21/11/2026). Ne jamais la changer seul.
KALYA_EMPREINTE = 'eda634c372c242b7'

errs, warns = [], []
def E(m): errs.append(m)
def W(m): warns.append(m)

FAITS_PATH = SYS / 'faits_controles.json'
faits = json.loads(FAITS_PATH.read_text(encoding='utf-8'))
SRC = {p['path']: p for p in P.PAGES + G.PAGES + C.PAGES}
MOIS = {m: i + 1 for i, m in enumerate('janvier février mars avril mai juin juillet août septembre octobre novembre décembre'.split())}

# ------------------------------------------------------------------ expressions
SP = r'[   ]'
NUM = r'\d{1,3}(?:[   .]\d{3})+(?:,\d+)?|\d+(?:,\d+)?'
RE_EURO = re.compile(r'(?<![\d,.])(' + NUM + r')' + SP + r'?(?:€|euros?\b|eur\b)', re.I)
RE_EURO_AVANT = re.compile(r'(?:€|\beur\b)' + SP + r'?\d', re.I)
RE_TEL = re.compile(r'(?<!\d)(?:\+33[ .]?|0)[1-9](?:[ . ]?\d{2}){4}(?!\d)')
RE_MAIL = re.compile(r'[\w.+-]+@[\w-]+(?:\.[\w-]+)+')
NEGATION = re.compile(r"\b(ni|pas|aucun|aucune|jamais|non|sans)\b", re.I)
PROMESSES = [  # interdits absolus (CONSIGNES.md §4)
    (r"\b(?:le |la |les )?meilleur(?:e|s|es)? (?:architecte|agence|cabinet|prix)", 'superlatif'),
    (r"\bleader\b", 'superlatif'), (r"\bn[°º] ?1\b|\bnuméro 1\b|\bnumber one\b", 'superlatif'),
    (r"\b(?:résultats?|délais?|positions?|classements?|prix|tarifs?) garanti", 'promesse garantie'),
    (r"\bgarantie de résultat|\bnous garantissons\b|\bje garantis\b", 'promesse garantie'),
    (r"\b(?:visite|déplacement|étude|faisabilité|diagnostic sur place|relevé) (?:offert|gratuit)e?s?\b", 'prestation gratuite non publiée'),
    (r"\bavant (?:l'|d')?ach(?:at|eter)\b", 'prestation avant achat'),
    (r"[\U0001F300-\U0001FAFF☀-➿]", 'emoji'),
    (r"\b(?:avis|note) (?:\d|cinq) étoiles", 'avis non publié'),
]
VEILLE = [  # admis seulement dans une phrase déjà publiée et validée
    r"\bgaranti\w*", r"\b(?:gratuit\w*|offert(?:e|s|es)?|sans frais)\b",
    r"\b(?:sous|en|dans les|d'ici|en moins de) (?:\d+|un|une|deux|trois|quatre|cinq|six|sept|huit|dix|quinze|vingt-quatre|quarante-huit|soixante-douze)"
    + SP + r"?(?:h|heures?|jours?|semaines?)\b",
    r"\b(?:nous|kalya|l'architecte|votre (?:dossier|commerce|boutique|restaurant|projet)|ouvr\w*|livr\w*|déposée?s?|obtenue?s?)\b[^.;]{0,50}\b(?:en|sous|dans|d'ici) (?:\d+|un|une|deux|trois|quatre|cinq|six)" + SP + r"?mois\b",
    r"\b(?:accord|autorisation|obtention|permis|dossier|acceptation)s?\b[^.;:]{0,40}\b(?:assurée?s?|certaine?s?|acquise?s? d'avance)\b",
]


def norm_amount(a):
    return re.sub(r'[   .]', '', a)


def norm_phrase(s):
    return re.sub(r'\s+', ' ', s.replace(' ', ' ').replace(' ', ' ')).strip()


def visible(doc):
    doc = re.sub(r'<(script|style|svg|noscript)\b.*?</\1>', ' ', doc, flags=re.S)
    return re.sub(r'[\s  ]+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', doc)))


BLOCS = re.compile(r'</?(?:p|li|h[1-6]|div|td|th|tr|br|dt|dd|caption|figcaption|blockquote|section|header|footer|nav|main|aside|ul|ol|table|summary|details|button|label|option|legend|fieldset|form)\b[^>]*>', re.I)


def blocs(doc):
    """Texte visible découpé par blocs (paragraphes, cellules, éléments de liste) : des phrases stables d'une construction à l'autre."""
    doc = re.sub(r'<(script|style|svg|noscript)\b.*?</\1>', ' ', doc, flags=re.S)
    t = html.unescape(re.sub(r'<[^>]+>', ' ', BLOCS.sub('\n', doc)))
    return '\n'.join(norm_phrase(l) for l in t.split('\n') if l.strip())


def phrases(texte):
    return [norm_phrase(p) for p in re.split(r'(?<=[.!?])\s+|\n+', texte) if p.strip()]


def main_of(doc):
    m = re.search(r'<main id="contenu">(.*?)</main>', doc, re.S)
    return m.group(1) if m else ''


def date_fr(s):
    m = re.match(r'(\d{1,2})(?:er)? (\w+) (\d{4})', s or '')
    return datetime.date(int(m.group(3)), MOIS[m.group(2)], int(m.group(1))) if m and m.group(2) in MOIS else None


# ------------------------------------------------------------------ faits contrôlés et empreinte de la partie Kalya
def partie_kalya(f):
    return {'montants': sorted((m['montant'], tuple(sorted(m.get('pages', [])))) for m in f.get('montants', []) if m.get('type') == 'kalya'),
            'telephones': sorted(f.get('telephones', [])), 'courriels': sorted(f.get('courriels', [])),
            'phrases_publiees': sorted(f.get('phrases_publiees', []))}


def empreinte_kalya(f):
    return hashlib.sha256(json.dumps(partie_kalya(f), ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:16]


EMPREINTE = empreinte_kalya(faits)
if EMPREINTE != KALYA_EMPREINTE and '--releve' not in sys.argv:
    E(f"faits_controles.json : honoraires, téléphones, courriels ou phrases publiées modifiés (empreinte {EMPREINTE}, attendue {KALYA_EMPREINTE}). "
      "Seul Quentin les change : une session qu'il valide met à jour le fichier, KALYA_EMPREINTE et la consigne de la tâche programmée.")

AUTORISE_KALYA, AUTORISE_MARCHE = defaultdict(set), defaultdict(set)  # montant normalisé -> pages où il est admis
KALYA = set()
for m in faits['montants']:
    a = norm_amount(m['montant'])
    if m.get('type') == 'kalya':
        KALYA.add(a)
        AUTORISE_KALYA[a] |= set(m.get('pages', []))
    elif m.get('type') == 'marche':
        if not (m.get('source') in S.SOURCES and m.get('page') and m.get('lu_le')):
            E(f"faits_controles.json : montant de marché « {m['montant']} » sans clé de source valide, page ou date de lecture")
            continue
        if m['source'] not in SRC.get(m['page'], {}).get('sources', []):
            E(f"faits_controles.json : la source « {m['source']} » du montant « {m['montant']} » n'est pas citée par {m['page']}")
        AUTORISE_MARCHE[a] |= {m['page'], 'llms-full.txt'}
TELS = {re.sub(r'\D', '', x) for x in faits['telephones']}
MAILS = set(faits['courriels'])
PHRASES_OK = set(faits.get('phrases_publiees', []))
INITIALES = set(faits['pages_initiales'])
releve_montants, releve_phrases = defaultdict(set), set()


def controle_faits(nom, texte):
    for t in RE_TEL.findall(texte):
        if re.sub(r'\D', '', t.replace('+33', '0')) not in TELS:
            E(f"{nom} : téléphone « {t} » non autorisé")
    texte = RE_TEL.sub(' [tél] ', texte)
    for bloc in texte.split('\n'):
        for a in RE_EURO.findall(bloc):
            n = norm_amount(a)
            releve_montants[n].add(nom)
            kalya_ici = n in KALYA and (nom in AUTORISE_KALYA.get(n, ()) or '*' in AUTORISE_KALYA.get(n, ()))
            marche_ici = nom in AUTORISE_MARCHE.get(n, ())
            if not (kalya_ici or marche_ici):
                E(f"{nom} : montant « {a} € » non autorisé sur cette page (faits_controles.json : prix Kalya = Quentin seul ; "
                  "chiffre de marché = entrée « marche » avec source, page et date)")
            elif marche_ici and not kalya_ici and (not re.search(r"pas un devis", bloc, re.I)
                                                    or re.search(r"\bKalya\b|honoraire|forfait|nous facturons|l'architecte facture", bloc, re.I)):
                E(f"{nom} : chiffre de marché « {a} € » sans « ce n'est pas un devis » dans le même paragraphe, ou présenté comme un prix Kalya")
    for m in RE_EURO_AVANT.finditer(texte):
        E(f"{nom} : montant écrit « {m.group(0)}… » (écrire le nombre puis « € »)")
    for m in RE_MAIL.findall(texte):
        if m.rstrip('.') not in MAILS:
            E(f"{nom} : courriel « {m} » non autorisé")
    for ph in phrases(texte):
        for pat in VEILLE:
            if re.search(pat, ph, re.I):
                releve_phrases.add(ph)
                if ph not in PHRASES_OK:
                    E(f"{nom} : formulation à valider (garantie, gratuité ou délai) : « {ph[:160]} »")
                break


def controle_promesses(nom, txt):
    for pat, lab in PROMESSES:
        for m in re.finditer(pat, txt, re.I):
            seg = re.split(r'[.,;:!?()—–]', txt[max(0, m.start() - 40):m.start()])[-1]
            if NEGATION.search(seg):
                continue  # même membre de phrase : « ni un résultat garanti »
            E(f"{nom} : {lab} « {m.group(0)} » (CONSIGNES.md §4)")


# ------------------------------------------------------------------ lecture du site
pages = {}
for f in DIST.rglob('*.html'):
    rel = '/' + str(f.relative_to(DIST))[:-5]
    pages['/' if rel == '/index' else rel] = f.read_text(encoding='utf-8')
sm = (DIST / 'sitemap.xml').read_text(encoding='utf-8')
sitemap = dict(re.findall(r'<loc>' + re.escape(URL) + r'(.*?)</loc><lastmod>(.*?)</lastmod>', sm))
lastmod = json.loads((ROOT / 'content/lastmod.json').read_text(encoding='utf-8'))
llms = (DIST / 'llms.txt').read_text(encoding='utf-8')
llms_full = (DIST / 'llms-full.txt').read_text(encoding='utf-8') if (DIST / 'llms-full.txt').exists() else ''

inbound = defaultdict(set)
for path, doc in pages.items():
    for h in re.findall(r'href="(/[^"#?]*)', main_of(doc)):
        h = h.rstrip('/') or '/'
        if h != path:
            inbound[h].add(path)


def prix_jsonld(path, n):
    if isinstance(n, dict):
        for k, v in n.items():
            if k == 'price':
                if norm_amount(str(v)) not in KALYA:
                    E(f"{path} : prix JSON-LD « {v} » absent des honoraires publiés")
            elif k == 'priceRange':
                for a in RE_EURO.findall(str(v)):
                    if norm_amount(a) not in KALYA:
                        E(f"{path} : priceRange JSON-LD « {a} € » absent des honoraires publiés")
            else:
                prix_jsonld(path, v)
    elif isinstance(n, list):
        for x in n:
            prix_jsonld(path, x)


# ------------------------------------------------------------------ contrôles par page
inv, descs = [], defaultdict(list)
for path, doc in sorted(pages.items()):
    noindex = bool(re.search(r'<meta name="robots" content="noindex', doc))
    title = html.unescape(re.search(r'<title>(.*?)</title>', doc, re.S).group(1))
    desc = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', doc).group(1))
    txt = visible(doc)
    controle_faits(path, blocs(doc) + '\n' + norm_phrase(desc))
    controle_promesses(path, txt + ' ' + desc)
    if 'aggregateRating' in doc or '"Review"' in doc:
        E(f"{path} : avis ou note balisés (interdit sans avis publiés et vérifiés)")
    for tag in re.findall(r'<img\b[^>]*>', doc):
        if ' alt=' not in tag:
            E(f"{path} : image sans attribut alt")
    graph = []
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
        try:
            graph += json.loads(m.replace('<\\/', '</')).get('@graph', [])
        except Exception as e:
            E(f"{path} : JSON-LD illisible ({e})")
    prix_jsonld(path, graph)
    for n in graph:
        if 'LocalBusiness' in (n.get('@type') or []):
            if n.get('telephone') != '+33 7 56 83 24 28' or n.get('address', {}).get('streetAddress') != S.SITE['street'] \
                    or n.get('identifier', {}).get('value') != S.SITE['siren'].replace(' ', ''):
                E(f"{path} : entité JSON-LD différente de content/site.py (téléphone, adresse ou SIREN)")
        if n.get('@type') == 'FAQPage':
            for q in n.get('mainEntity', []):
                if norm_phrase(q['name']) not in norm_phrase(txt):
                    E(f"{path} : question balisée absente de la page : « {q['name'][:60]} »")
    if noindex:
        if path in sitemap:
            E(f"{path} : noindex mais présent au sitemap")
    else:
        can = re.search(r'<link rel="canonical" href="([^"]+)"', doc)
        if not can or can.group(1) != URL + (path if path != '/' else '/'):
            E(f"{path} : canonique absente ou différente de l'adresse")
        if path not in sitemap:
            E(f"{path} : indexable mais absent du sitemap")
        elif lastmod.get(path, {}).get('lastmod') != sitemap[path]:
            E(f"{path} : date du sitemap différente de content/lastmod.json")
        descs[desc].append(path)
        strict = path not in INITIALES
        if len(title) > 60:
            (E if strict else W)(f"{path} : titre de {len(title)} signes (60 au plus)")
        if not 70 <= len(desc) <= 155:
            (E if strict else W)(f"{path} : description de {len(desc)} signes (70 à 155)")
        if path != '/' and len(inbound.get(path, ())) < 2:
            W(f"{path} : {len(inbound.get(path, ()))} lien(s) entrant(s) depuis le texte d'autres pages (2 au moins)")
    src = SRC.get(path, {})
    kind = src.get('kind') or {'/': 'accueil', '/mentions-legales': 'legal', '/confidentialite': 'legal', '/plan-du-site': 'plan'}.get(path, 'technique')
    if kind in ('situation', 'activite', 'guide', 'zone', 'outil') and not src.get('answer'):
        W(f"{path} : pas de réponse courte (answer)")
    if kind == 'guide' and len(src.get('sources', [])) < 3:
        W(f"{path} : guide avec moins de 3 sources")
    v = src.get('verified')
    if not src:
        vdate = None
    elif v and re.fullmatch(r'\d{4}-\d{2}-\d{2}', v):
        vdate = datetime.date.fromisoformat(v)
    else:
        vdate = date_fr(S.VERIFIED_NEW if v == 'new' else S.VERIFIED)
    if vdate and kind in ('situation', 'activite', 'guide', 'zone', 'outil') and (TODAY - vdate).days > FRAICHEUR_JOURS:
        W(f"{path} : vérifiée le {vdate.isoformat()}, il y a plus de {FRAICHEUR_JOURS} jours : à revérifier (une page par mois)")
    if not noindex and kind in ('situation', 'activite', 'guide', 'zone', 'outil') and (URL + path) not in llms:
        W(f"{path} : absente de llms.txt")
    if not noindex and src.get('sections') and llms_full and (URL + path + '\n') not in llms_full:
        W(f"{path} : absente de llms-full.txt")
    inv.append({'url': URL + path, 'type': kind, 'title': title, 'title_len': len(title), 'description_len': len(desc),
                'indexable': 'non' if noindex else 'oui', 'lastmod': lastmod.get(path, {}).get('lastmod', ''),
                'verifie': vdate.isoformat() if vdate else '', 'mots': len(visible(main_of(doc)).split()),
                'liens_entrants': len(inbound.get(path, ())), 'sources': len(src.get('sources', [])),
                'faq': len(src.get('faq') or []), 'reponse_courte': 'oui' if src.get('answer') else 'non'})

for d, ps in descs.items():
    if len(ps) > 1:
        E(f"description dupliquée : {ps}")

# ------------------------------------------------------------------ fichiers techniques
controle_faits('llms.txt', llms)
controle_promesses('llms.txt', llms)
if llms_full:
    controle_faits('llms-full.txt', llms_full)
    controle_promesses('llms-full.txt', llms_full)
for k, lab in (('077297', "n° d'Ordre"), (S.SITE['siren'], 'SIREN'), (S.SITE['address'], 'adresse'), (S.SITE['phone'], 'téléphone')):
    for nom, t in (('llms.txt', llms), ('/mentions-legales', visible(pages.get('/mentions-legales', ''))), ('/a-propos', visible(pages.get('/a-propos', '')))):
        if norm_phrase(k) not in norm_phrase(t):
            E(f"{nom} : {lab} absent ou différent ({k})")
key = DIST / f'{INDEXNOW_KEY}.txt'
if not key.exists() or key.read_text().strip() != INDEXNOW_KEY:
    E("clé IndexNow absente de dist/ ou contenu différent (ne jamais la changer)")
robots = (DIST / 'robots.txt').read_text(encoding='utf-8')
if re.search(r'^Disallow:\s*/\s*$', robots, re.M) or f'Sitemap: {URL}/sitemap.xml' not in robots:
    E("robots.txt : blocage général ou ligne Sitemap absente")
for path in sitemap:
    if path not in pages:
        E(f"sitemap : {path} ne correspond à aucune page")

# ------------------------------------------------------------------ sorties
(SYS / 'data/audit').mkdir(parents=True, exist_ok=True)
if '--releve' in sys.argv:
    (SYS / 'data/audit/faits_releves.json').write_text(json.dumps(
        {'montants': {k: sorted(v) for k, v in sorted(releve_montants.items())}, 'phrases': sorted(releve_phrases)},
        ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
if '--inventaire' in sys.argv:
    with open(SYS / 'URL_INVENTORY.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(inv[0].keys()), delimiter=';', lineterminator='\n')
        w.writeheader(); w.writerows(inv)
    usage = defaultdict(list)
    for p in P.PAGES + G.PAGES + C.PAGES:
        for k in p.get('sources', []):
            usage[k].append(p['path'])
    with open(SYS / 'SOURCES_MAP.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, delimiter=';', lineterminator='\n')
        w.writerow(['cle', 'intitule', 'url', 'version', 'pages'])
        for k, (lab, u, ver) in S.SOURCES.items():
            w.writerow([k, lab.replace(';', ','), u, ver.replace(';', ','), ' '.join(sorted(usage.get(k, []))) or 'NON UTILISÉE'])
    (SYS / 'data/audit' / f'{TODAY.isoformat()}.json').write_text(json.dumps(
        {'date': TODAY.isoformat(), 'pages': len(pages), 'indexables': sum(1 for r in inv if r['indexable'] == 'oui'),
         'erreurs': errs, 'avertissements': warns}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

print(f"{len(pages)} pages, {len(sitemap)} au sitemap, {len(errs)} erreur(s), {len(warns)} avertissement(s) ; empreinte des faits Kalya : {EMPREINTE}")
for w_ in warns:
    print('AVERTISSEMENT', w_)
for e in errs:
    print('ERREUR', e)
sys.exit(1 if errs else 0)
