# Consignes d'écriture — architecte-commerce.fr

## 1. Ton
- Celui d'un architecte qui connaît le commerce parisien et ses textes : précis, concret, sûr de lui sans se vanter. Le lecteur est un commerçant, un restaurateur ou un responsable de réseau pressé, qui engage de l'argent : il veut savoir ce qui est permis, ce qui bloque, combien de temps et combien.
- Le site parle de « l'architecte » et de « Kalya Architecte » ; il s'adresse au lecteur par « vous ». Jamais « je », sauf citation de Quentin ; « nous » reste rare.
- Aucun superlatif promotionnel (« meilleur », « leader », « n° 1 »), aucune promesse de résultat, de délai ou de position, aucune gratuité qui ne soit déjà publiée, aucun point d'exclamation, aucun emoji.
- Chaque paragraphe apporte une règle, un chiffre sourcé, une méthode ou une décision. Les exemples sont présentés comme des exemples, les hypothèses comme des hypothèses.

## 2. Typographie française
`build.py` pose les espaces insécables (avant « : ; ? ! », dans « 10 % », « 2 200 € HT », « n° 077297 », « art. 25 b », « M 2 », « PE 2 ») : écrire avec des espaces ordinaires. Guillemets « » ; apostrophe ’ ou ' ; « 5e catégorie » ; dates « 21 novembre 2026 » ; « HT » après les honoraires Kalya ; articles cités sous leur forme officielle (« R*423-23 », « L145-40 », « GN 1 »).

## 3. Faits
- Chaque fait réglementaire : article et texte, source officielle ouverte pendant la session, ajoutée à `SOURCES` (`content/site.py`) avec un intitulé précis, l'URL et la version en vigueur ou la date de consultation, puis citée dans `sources` de la page.
- Chaque chiffre : source et date (« Apur, avril 2023 »). Un prix de marché est attribué à sa source (« fourchettes publiées par … ») et suivi de « ce n'est pas un devis » ; il est inscrit dans `faits_controles.json` (`type` « marche »).
- Inconnu = « se vérifie au cas par cas, documents en main », jamais inventé.
- Faits sur Kalya Architecte et sur Quentin : uniquement ceux de `BUSINESS_SOURCE_OF_TRUTH.md`.
- La réforme de l'autorisation de travaux (loi n° 2026-403 du 26 mai 2026, déclaration de conformité pour certains ERP de moins de 300 m²) se décrit telle qu'elle est : prévue, applicable après un décret. Tant que ce décret n'est pas publié et lu, aucune page ne dit qu'elle s'applique.

## 4. Interdits (contrôlés par `tools/check.py` et `tools/seo/audit.py`)
Montant (quelle que soit son écriture), téléphone ou courriel hors `faits_controles.json`, ou montant admis ailleurs mais pas sur cette page ; prix du JSON-LD hors honoraires ; phrase nouvelle ou réécrite qui contient une garantie, une gratuité ou un délai ; superlatifs ; « résultat / délai / prix garanti » ; visite, étude ou faisabilité « offerte » ou « gratuite » ; prestation « avant achat » ; avis ou notes balisés ; FAQ balisée absente de la page ; emoji ; noms des autres marques de Quentin (FIXIA, WorkRepublik) ; « TODO », « lorem », « À FOURNIR », « NON VÉRIFIÉ » ; Montmorency hors mentions légales. Hors contrôle automatique : nom d'un client privé, page par ville ou par arrondissement, guide ERP générique (domaine d'architecte-erp.fr), photo d'ambiance présentée comme réalisation.

## 5. Grille de la relecture indépendante (sous-agent)
Le relecteur n'a pas écrit la page. Il lit la page construite (`dist/…html`) et ses sources, puis rend une liste « à corriger / à retirer / OK » :
1. Chaque affirmation réglementaire : l'article cité dit-il exactement cela, dans sa version en vigueur ? (ouvrir la source ; Légifrance de préférence)
2. Chaque chiffre : présent dans la source citée, à la date indiquée ?
3. Chaque fait sur Kalya Architecte : présent dans `BUSINESS_SOURCE_OF_TRUTH.md` ?
4. Une phrase peut-elle se lire comme une promesse, un prix Kalya non publié, une gratuité, un délai, une prestation avant achat ?
5. La réponse courte répond-elle à la question du titre, en moins de 90 mots ?
6. La page recoupe-t-elle une page existante ou un autre site de Quentin (`QUERY_UNIVERSE.csv`) ?
7. Typographie, ton, niveau (§1, §2) ; title ≤ 60 signes, description 70 à 155.
Tout point « à corriger » ou « à retirer » est traité avant publication ; un doute persistant = pas de publication.
