# -*- coding: utf-8 -*-
"""Générateur statique de architecte-commerce.fr (FIXIA Architecte).

Usage : python3 -I build.py      (dépendance : jinja2)
Sortie : dist/ (servie telle quelle par Vercel, adresses sans extension grâce à cleanUrls) et vercel.json.
"""
import json, pathlib, shutil, sys, hashlib, html, re, unicodedata

ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from jinja2 import Environment, FileSystemLoader, ChainableUndefined
from content import site as S, home as HOME, drawings as D, legal as LEGAL
from content import pages as P, guides as G, core as C

DIST = ROOT / 'dist'
STATIC = ROOT / 'src/static'
SITE = S.SITE
URL = SITE['url']

env = Environment(loader=FileSystemLoader(str(ROOT / 'src/templates')), autoescape=True, undefined=ChainableUndefined)

EDITORIAL = P.PAGES + G.PAGES
ALL = {p['path']: p for p in EDITORIAL + C.PAGES}
KIND_LABEL = {'situation': 'Projet', 'activite': 'Activité', 'guide': 'Guide', 'zone': 'Zone', 'outil': 'Outil', 'core': 'FIXIA'}
SECTION_OF = {'situation': 'projets', 'activite': 'activites', 'guide': '/guides', 'zone': None, 'outil': 'outils'}


def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')[:60]


def strip(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s or '')).strip()


def label_of(path):
    p = ALL.get(path)
    if p:
        return p.get('short') or p['h1']
    return {'/': 'Accueil', '/guides': 'Guides', '/votre-projet': 'Projets', '/outils': 'Outils',
            '/etudier-mon-projet': 'Étudier mon projet', '/mentions-legales': 'Mentions légales',
            '/confidentialite': 'Confidentialité', '/plan-du-site': 'Plan du site'}.get(path, path)


def teaser_of(path):
    p = ALL.get(path)
    return (p.get('teaser') or strip(p.get('description'))) if p else ''


def crumbs_for(path):
    items = [('/', 'Accueil')]
    p = ALL.get(path)
    k = p['kind'] if p else None
    if path.startswith('/guides/'):
        items.append(('/guides', 'Guides'))
    elif k in ('situation', 'activite'):
        items.append(('/votre-projet', 'Projets'))
    elif k == 'outil':
        items.append(('/outils', 'Outils'))
    if path != '/':
        items.append((path, label_of(path)))
    return items


def related_items(paths):
    out = []
    for h in paths:
        if h.startswith('http'):
            for k, (n, u, d) in S.ERP_SITES.items():
                if h.startswith(u.rstrip('/')):
                    out.append((h, n, d.split(':')[0])); break
            else:
                out.append((h, h, ''))
        else:
            out.append((h, label_of(h), teaser_of(h)))
    return out


# ---------------------------------------------------------------- données structurées
ORG_ID, PERSON_ID, SITE_ID = URL + '/#fixia', URL + '/#quentin-piepszownik', URL + '/#site'
AREA = [{"@type": "City", "name": "Paris"}, {"@type": "AdministrativeArea", "name": "Île-de-France"}]


def base_graph():
    return [
        {"@type": ["ProfessionalService", "LocalBusiness"], "@id": ORG_ID, "name": SITE['brand'],
         "alternateName": ["FIXIA", "Architecte Commerce"], "url": URL + '/',
         "logo": {"@type": "ImageObject", "url": URL + "/icon-512.png", "width": 512, "height": 512},
         "image": URL + "/og/architecte-commerce.png", "telephone": "+33 9 70 70 17 99", "email": SITE['email'],
         "address": {"@type": "PostalAddress", "streetAddress": SITE['street'], "postalCode": SITE['postal'], "addressLocality": SITE['city'], "addressCountry": "FR"},
         "areaServed": AREA, "founder": {"@id": PERSON_ID}, "priceRange": "Sur devis",
         "knowsAbout": ["architecture commerciale", "aménagement de local commercial", "création de boutique", "restaurant", "devanture et enseigne",
                        "établissements recevant du public", "autorisation de travaux", "accessibilité", "bail commercial", "PLU de Paris"],
         "sameAs": [], "description": "Architecte de commerces à Paris et en Île-de-France : boutiques, restaurants, instituts, showrooms et enseignes, de la vérification du local avant le bail à l'ouverture."},
        {"@type": "Person", "@id": PERSON_ID, "name": SITE['person'], "jobTitle": "Architecte", "worksFor": {"@id": ORG_ID},
         "image": URL + "/img/portrait-800.jpg",
         "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "Inscription au tableau de l'Ordre des architectes d'Île-de-France", "identifier": SITE['ordre']}},
        {"@type": "WebSite", "@id": SITE_ID, "url": URL + '/', "name": "Architecte Commerce — FIXIA", "inLanguage": "fr-FR", "publisher": {"@id": ORG_ID}},
    ]


def page_graph(path, page, kind='WebPage', faq=None, article=None, service=None, extra=None):
    g = base_graph()
    wp = {"@type": kind, "@id": URL + path + '#page', "url": URL + path, "name": page['title'], "description": page['description'],
          "inLanguage": "fr-FR", "isPartOf": {"@id": SITE_ID}, "about": {"@id": ORG_ID}, "dateModified": S.VERIFIED_ISO}
    if path != '/':
        g.append({"@type": "BreadcrumbList", "@id": URL + path + '#ariane', "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": URL + h} for i, (h, n) in enumerate(crumbs_for(path))]})
        wp["breadcrumb"] = {"@id": URL + path + '#ariane'}
    g.append(wp)
    if faq:
        g.append({"@type": "FAQPage", "@id": URL + path + '#faq', "mainEntity": [
            {"@type": "Question", "name": f['q'], "acceptedAnswer": {"@type": "Answer", "text": strip(f['a'])}} for f in faq]})
    if article:
        g.append({"@type": "Article", "@id": URL + path + '#article', "headline": article['h1'], "description": article['description'],
                  "author": {"@id": PERSON_ID}, "publisher": {"@id": ORG_ID}, "datePublished": S.VERIFIED_ISO, "dateModified": S.VERIFIED_ISO,
                  "mainEntityOfPage": {"@id": URL + path + '#page'}, "inLanguage": "fr-FR",
                  "citation": [S.SOURCES[k][1] for k in article.get('sources', [])]})
    if service:
        g.append({"@type": "Service", "@id": URL + path + '#service', "name": service.get('short') or service['h1'],
                  "serviceType": service.get('service_type', 'Architecture commerciale'), "provider": {"@id": ORG_ID},
                  "description": service['description'], "areaServed": AREA})
    if extra:
        g.extend(extra)
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')


# ---------------------------------------------------------------- rendu
PAGES_OUT = []
_SPLIT = re.compile(r'(<script\b[^>]*>.*?</script>|<style\b[^>]*>.*?</style>|<[^>]+>)', re.S)


def typo(doc):
    """Typographie française : espace insécable avant : ; ? ! et dans les guillemets, hors balises et scripts."""
    out = []
    for part in _SPLIT.split(doc):
        if not part or part.startswith('<'):
            out.append(part); continue
        part = re.sub(r' ([:;?!])(?=\s|$|<|[^/\w])', ' \\1', part)
        part = part.replace('« ', '« ').replace(' »', ' »')
        out.append(part)
    return ''.join(out)


MINIS = [D.devanture(k, 'nav-' + k) for k in ('boutique', 'restaurant', 'bouche', 'beaute', 'showroom')]


def common(path, page):
    v = hashlib.md5(b''.join((STATIC / f).read_bytes() for f in ('css/site.css', 'js/site.js', 'js/outils.js'))).hexdigest()[:8]
    return dict(site=SITE, sources=S.SOURCES, situations=S.SITUATIONS, activites=S.ACTIVITES, outils=S.OUTILS, nav=S.NAV, zones=S.ZONES,
                erp=S.ERP_SITES, guides_nav=G.PAGES, verified=S.VERIFIED, verified_iso=S.VERIFIED_ISO, v=v, page=page,
                crumbs=crumbs_for(path), minis=MINIS)


def write(path, tpl, page, jsonld, indexable=True, **kw):
    page = dict(page)
    page['path'] = path
    page.setdefault('noindex', not indexable)
    ctx = common(path, page)
    ctx.update(kw)
    ctx['jsonld'] = jsonld
    out = typo(env.get_template(tpl).render(**ctx))
    f = DIST / ('index.html' if path == '/' else path.lstrip('/') + '.html')
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(out, encoding='utf-8')
    PAGES_OUT.append((path, indexable, page.get('title', ''), page.get('description', '')))


def prep(p):
    """Normalise une page éditoriale : identifiants de section, valeurs par défaut."""
    p = dict(p)
    secs = []
    for s in p.get('sections', []):
        s = dict(s) if isinstance(s, dict) else {'h': s[0], 'html': s[1]}
        s.setdefault('id', slug(s['h']))
        secs.append(s)
    p['sections'] = secs
    p.setdefault('sources', [])
    for k in p['sources']:
        assert k in S.SOURCES, (p['path'], k)
    return p


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(STATIC, DIST)

    # Accueil
    home = {"title": "Architecte commerce à Paris : boutique, restaurant, enseigne | FIXIA",
            "description": "Architecte de commerces à Paris et en Île-de-France : local vérifié avant le bail, plans conformes ERP, autorisations (devanture, enseigne, travaux), chantier jusqu'à l'ouverture.",
            "section": "/"}
    write('/', 'home.html', home, page_graph('/', home, faq=HOME.FAQ, service={"h1": "Architecture de commerces", "short": "Architecture de commerces à Paris", "description": home['description']}),
          acts=D.ACTS, elevation=D.elevation('boutique', 'hero'), plan=D.plan_local('plan'), legend=HOME.LEGEND, checks=HOME.CHECKS,
          vac=HOME.VACANCY, steps=HOME.STEPS, gantt=HOME.GANTT, deliverables=HOME.DELIVERABLES, faq=HOME.FAQ)

    # Pages éditoriales
    for raw in EDITORIAL:
        p = prep(raw)
        kind = p['kind']
        page = {"title": p['title'], "description": p['description'], "section": SECTION_OF.get(kind), "og": p.get('og')}
        jl = page_graph(p['path'], p, faq=p.get('faq') or None, article=p if kind == 'guide' else None,
                        service=p if kind in ('situation', 'activite', 'zone') else None, extra=p.get('jsonld_extra'))
        mini = D.devanture(p['mini'], 'pg') if p.get('mini') else None
        write(p['path'], p.get('tpl', 'page.html'), page, jl, p=p, mini=mini, kind_label=KIND_LABEL.get(kind, 'Page'),
              related=related_items(p.get('related', [])), **p.get('ctx', {}))

    # Pages du noyau (méthode, références, à propos, hubs, outils, contact)
    for raw in C.PAGES:
        p = prep(raw)
        page = {"title": p['title'], "description": p['description'], "section": p.get('section'), "og": p.get('og')}
        ctx = dict(p.get('ctx', {}))
        if p.get('needs_plan'):
            ctx['plan'] = D.plan_local('plan')
        jl = page_graph(p['path'], p, kind=p.get('schema', 'WebPage'), faq=p.get('faq') or None,
                        service=p if p.get('as_service') else None, extra=p.get('jsonld_extra'))
        write(p['path'], p['tpl'], page, jl, indexable=p.get('indexable', True), p=p, kind_label=KIND_LABEL.get(p['kind'], 'FIXIA'),
              related=related_items(p.get('related', [])), home=HOME, guides=G.PAGES, all_pages=ALL, tools=C.TOOLS_INTRO, **ctx)

    # Mentions légales et confidentialité
    fmt = dict(SITE)
    ml = {"title": "Mentions légales | FIXIA Architecte", "description": "Mentions légales de architecte-commerce.fr : éditeur, titre professionnel, assurance, hébergement.",
          "h1": "Mentions légales", "lede": "Éditeur, titre professionnel, assurance et hébergement du site architecte-commerce.fr."}
    write('/mentions-legales', 'legal.html', ml, page_graph('/mentions-legales', ml), p=ml, body=LEGAL.LEGAL_BODY.format(**fmt))
    cf = {"title": "Politique de confidentialité | FIXIA Architecte", "description": "Données traitées par les formulaires et les outils du site, finalités, destinataires, durées de conservation et droits.",
          "h1": "Politique de confidentialité", "lede": "Ce que devient votre demande : données traitées, destinataires, durées de conservation et droits."}
    write('/confidentialite', 'legal.html', cf, page_graph('/confidentialite', cf), p=cf, body=LEGAL.PRIVACY_BODY.format(**fmt))

    # Plan du site
    groups = [
        ("FIXIA", [('/', 'Accueil'), ('/mission', 'Méthode'), ('/references', 'Références'), ('/a-propos', "L'architecte"), ('/etudier-mon-projet', 'Étudier mon projet')]),
        ("Projets", [('/votre-projet', 'Tous les projets')] + [(h, l) for h, l, _ in S.SITUATIONS]),
        ("Activités", [(h, l) for h, l, _ in S.ACTIVITES]),
        ("Outils", [('/outils', 'Tous les outils')] + [(h, l) for h, l, _ in S.OUTILS]),
        ("Guides", [('/guides', 'Tous les guides')] + [(g['path'], g['short']) for g in G.PAGES]),
        ("Paris et Île-de-France", S.ZONES),
        ("Informations", [('/mentions-legales', 'Mentions légales'), ('/confidentialite', 'Confidentialité')]),
    ]
    pl = {"title": "Plan du site | FIXIA Architecte", "description": "Toutes les pages de architecte-commerce.fr : projets, activités, outils, guides, zones et informations légales."}
    write('/plan-du-site', 'plan.html', pl, page_graph('/plan-du-site', pl), groups=groups)
    nf = {"title": "Page introuvable | FIXIA Architecte", "description": "Cette page n'existe pas ou plus."}
    write('/404', 'notfound.html', nf, page_graph('/404', nf), indexable=False)

    # ---------------------------------------------------------------- fichiers techniques
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, idx, _, _ in PAGES_OUT:
        if idx:
            sm.append(f'<url><loc>{URL}{path}</loc><lastmod>{S.VERIFIED_ISO}</lastmod></url>')
    sm.append('</urlset>')
    (DIST / 'sitemap.xml').write_text('\n'.join(sm) + '\n', encoding='utf-8')
    (DIST / 'robots.txt').write_text(f"User-agent: *\nAllow: /\n\nSitemap: {URL}/sitemap.xml\n", encoding='utf-8')

    llms = ["# FIXIA Architecte — architecte-commerce.fr", "",
            "> Architecte de commerces à Paris et en Île-de-France : boutiques, restaurants et bars, instituts et salons, boulangeries et métiers de bouche, showrooms, enseignes en réseau. "
            "Vérification du local avant la signature du bail, conception, dossiers d'autorisation (déclaration préalable, autorisation de travaux ERP, enseigne, permis de construire), consultation des entreprises, suivi de chantier, ouverture. "
            f"FIXIA Architecte est le nom commercial de Quentin Piepszownik, architecte inscrit à l'Ordre des architectes d'Île-de-France (n° {SITE['ordre']}). Adresse : {SITE['address']}. Téléphone : {SITE['phone']}. Courriel : {SITE['email']}.", "",
            f"Les règles citées sur ce site renvoient à leurs textes (règlement de sécurité ERP, code de la construction, code de l'urbanisme, PLU bioclimatique de Paris, code de l'environnement, règlement sanitaire de Paris, code de commerce) et ont été vérifiées le {S.VERIFIED}.", "",
            "Sites spécialisés du même architecte : dossier-erp-paris.fr (dossier ERP à Paris, par Kalya Architecte) ; architecte-erp.fr (établissements recevant du public).", ""]
    for title, items in [("Projets", [(h, l) for h, l, _ in S.SITUATIONS]), ("Activités", [(h, l) for h, l, _ in S.ACTIVITES]),
                         ("Outils", [(h, l) for h, l, _ in S.OUTILS]), ("Guides", [(g['path'], g['h1']) for g in G.PAGES]),
                         ("Zones", S.ZONES), ("FIXIA", [('/mission', 'Méthode'), ('/references', 'Références'), ('/a-propos', "L'architecte"), ('/etudier-mon-projet', 'Contact')])]:
        llms.append(f"## {title}")
        seen = set()
        for h, l in items:
            if h in seen:
                continue
            seen.add(h)
            d = ALL[h]['description'] if h in ALL else ''
            llms.append(f"- [{l}]({URL}{h}){': ' + d if d else ''}")
        llms.append('')
    llms.append("## Questions fréquentes")
    for f in HOME.FAQ:
        llms.append(f"- {f['q']} {strip(f['a'])}")
    llms.append('')
    (DIST / 'llms.txt').write_text('\n'.join(llms), encoding='utf-8')

    (DIST / 'site.webmanifest').write_text(json.dumps({"name": "FIXIA Architecte — commerces", "short_name": "FIXIA", "start_url": "/", "display": "standalone",
        "background_color": "#133A63", "theme_color": "#133A63", "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, ensure_ascii=False), encoding='utf-8')

    vercel = {
        "$schema": "https://openapi.vercel.sh/vercel.json", "framework": None, "buildCommand": "", "installCommand": "", "outputDirectory": "dist",
        "cleanUrls": True, "trailingSlash": False,
        "redirects": [{"source": "/(.*)", "has": [{"type": "host", "value": "www.architecte-commerce.fr"}], "destination": "https://architecte-commerce.fr/$1", "permanent": True}] +
                     [{"source": s, "destination": d, "permanent": True} for s, d in S.REDIRECTS] +
                     [{"source": s + '/', "destination": d, "permanent": True} for s, d in S.REDIRECTS],
        "headers": [
            {"source": "/(.*)", "headers": [
                {"key": "X-Content-Type-Options", "value": "nosniff"},
                {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                {"key": "X-Frame-Options", "value": "DENY"},
                {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=(), interest-cohort=()"},
                {"key": "Strict-Transport-Security", "value": "max-age=63072000; includeSubDomains"},
                {"key": "Content-Security-Policy", "value": "default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; script-src 'self'; font-src 'self'; connect-src 'self'; form-action 'self' https://architecte-erp.app.n8n.cloud; frame-ancestors 'none'; base-uri 'self'; object-src 'none'; upgrade-insecure-requests"}]},
            {"source": "/fonts/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
            {"source": "/(img|brand|og)/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=2592000"}]},
            {"source": "/(css|js)/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
            {"source": "/sitemap.xml", "headers": [{"key": "Content-Type", "value": "application/xml; charset=utf-8"}, {"key": "Cache-Control", "value": "public, max-age=0, must-revalidate"}]},
            {"source": "/robots.txt", "headers": [{"key": "Content-Type", "value": "text/plain; charset=utf-8"}]},
            {"source": "/llms.txt", "headers": [{"key": "Content-Type", "value": "text/plain; charset=utf-8"}]},
        ],
    }
    (ROOT / 'vercel.json').write_text(json.dumps(vercel, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"{len(PAGES_OUT)} pages, {sum(1 for x in PAGES_OUT if x[1])} indexables")


if __name__ == '__main__':
    main()
