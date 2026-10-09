# architecte-commerce.fr — FIXIA Architecte

Site de FIXIA Architecte (Quentin Piepszownik, architecte, Ordre des architectes d'Île-de-France n° 077297) consacré aux commerces à Paris et en Île-de-France : boutiques, restaurants, métiers de bouche, instituts, showrooms, enseignes.
HTML entièrement pré-rendu (contenu, liens, JSON-LD et canoniques lisibles sans JavaScript), sans cookie ni script tiers. Direction artistique : tirage de plan (bleu cyanotype #133A63, traits #A9C6E8) et lumière de vitrine (ambre #FFB52E) ; police Archivo variable auto-hébergée (OFL), sous-ensemble latin.

## Structure
- `content/site.py` — identité, navigation, redirections, **sources datées** (`SOURCES`, lues le 9 octobre 2026).
- `content/home.py` — accueil : légende par activité, neuf points avant le bail, méthode, délais, FAQ.
- `content/pages.py` — projets (situations), activités, zones ; `content/guides.py` — onze guides ; `content/core.py` — hubs, méthode, références, l'architecte, contact, outils.
- `content/drawings.py` — dessins SVG générés : élévation de rue (la devanture change avec l'activité), vignettes de devantures, plan de local. Annotations = règles sourcées uniquement.
- `content/brand.py` — logo FIXIA (symbole et mot-symbole vectorisés) ; `content/legal.py` — mentions légales, confidentialité.
- `src/templates/` — gabarits Jinja2 ; `src/static/` — CSS, JS (`site.js` : menus, dessin, sommaire ; `outils.js` : diagnostic de local, calcul d'effectif), police, logos, icônes, images de partage.
- `tools/check.py` — contrôles (liens, ancres, H1, JSON-LD, sitemap) ; `tools/assets.py` — icônes et images de partage ; `tools/serve.py` — serveur local ; `tools/n8n/formulaire.js` — workflow du formulaire.
- `build.py` — génère `dist/` (pages, sitemap.xml, robots.txt, llms.txt, site.webmanifest) et `vercel.json` (cleanUrls, redirections, en-têtes de sécurité).

## Publier une modification
```
python3 -I build.py          # dépendance : jinja2
python3 -I tools/check.py
git add -A && git commit -m "…" && git push
```
Vercel sert `dist/` tel quel (pas d'étape de construction). Auteur des commits : `327586153+quentinpiep1980-stack@users.noreply.github.com`.

## Formulaire
Workflow n8n « ARCHITECTE COMMERCE (FIXIA) — formulaire de contact (production) » (su50ih0Q6dvATejB, projet FIXIA) : webhook `architecte-commerce-demande-5d8e2a71c4f9b036`, courriel vers analyse@fixia.fr, accusé de réception, redirection vers `/etudier-mon-projet/merci`. Données d'exécution non conservées. Le diagnostic de local envoie son résumé par le même webhook.

## Liens éditoriaux
dossier-erp-paris.fr (Kalya Architecte, même architecte) et architecte-erp.fr : liens contextuels dans les pages ERP, bloc dédié sur l'accueil et le pied de page.
