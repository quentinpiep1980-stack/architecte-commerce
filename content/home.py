# -*- coding: utf-8 -*-
"""Contenus de l'accueil. Chaque fait réglementaire renvoie à une clé de content.site.SOURCES."""

# Légende du dessin : trois faits par activité (titre, texte, référence courte) + page liée
LEGEND = {
    "boutique": {
        "label": "une boutique", "href": "/architecte-boutique", "go": "Créer une boutique",
        "facts": [
            ("ERP de type M, 5e catégorie sous 200 personnes", "Moins de 100 personnes au sous-sol, 100 aux étages et 200 au total.", "Règlement de sécurité, art. PE 2"),
            ("1 personne pour 3 m² de surface de vente", "Au sous-sol, au rez-de-chaussée et au 1er étage ; 1 pour 6 m² au 2e étage.", "Règlement de sécurité, art. M 2"),
            ("Enseigne soumise à autorisation à Paris", "Demande en ligne à la Ville ; sans réponse sous deux mois, l'autorisation est acquise.", "Code de l'environnement, art. L581-18 et R581-13"),
        ],
    },
    "restaurant": {
        "label": "un restaurant", "href": "/architecte-restaurant", "go": "Ouvrir un restaurant",
        "facts": [
            ("ERP de type N, 5e catégorie sous 200 personnes", "Moins de 100 personnes au sous-sol, 200 aux étages et 200 au total.", "Règlement de sécurité, art. PE 2"),
            ("Places assises : 1 personne pour 2 m² au plus", "Sur déclaration du nombre de places ; à défaut, 1 personne par m². Debout : 2 par m².", "Règlement de sécurité, art. N 2"),
            ("Air de cuisine rejeté à 8 m de toute fenêtre", "Hotte débordante, conduit propre, filtres nettoyés au moins une fois par mois.", "Règlement sanitaire de Paris, art. 63-1 et 130-3"),
        ],
    },
    "beaute": {
        "label": "un institut ou un salon", "href": "/architecte-institut-beaute-coiffure", "go": "Aménager un institut",
        "facts": [
            ("Un salon qui reçoit des clients est un ERP", "Le type se qualifie selon l'exploitation réelle, puis la catégorie selon l'effectif.", "Règlement de sécurité, art. GN 1"),
            ("Registre public d'accessibilité obligatoire", "Il s'applique à tous les ERP, 5e catégorie comprise, et se tient à la disposition du public.", "Code de la construction, art. R164-6"),
            ("Devanture dans le plan de la façade", "En applique, ou en feuillure avec un retrait limité de 10 à 20 cm ; grilles à l'intérieur.", "PLU de Paris, art. UG.2.1.4"),
        ],
    },
    "bouche": {
        "label": "une boulangerie", "href": "/architecte-metiers-de-bouche", "go": "Concevoir un commerce de bouche",
        "facts": [
            ("Laboratoire : prévenir les contaminations", "Un agencement qui sépare les opérations ; la « marche en avant » en est la méthode, pas un article.", "Règlement (CE) n° 852/2004, annexe II"),
            ("Déclaration de l'établissement", "Avant l'ouverture, déclaration d'activité alimentaire (Cerfa n° 13984).", "Code rural, art. R233-4"),
            ("Graisses : prétraitement obligatoire à Paris", "Restaurants et métiers de bouche équipés d'un dispositif de prétraitement.", "Règlement d'assainissement de Paris, art. 17.1"),
        ],
    },
    "showroom": {
        "label": "un showroom", "href": "/architecte-showroom", "go": "Concevoir un showroom",
        "facts": [
            ("Recevoir des clients, c'est être un ERP", "Le type suit l'exploitation réelle : exposition, vente, prise de commande.", "Règlement de sécurité, art. GN 1"),
            ("Faible densité : 1 personne pour 9 m²", "Pour un magasin de vente à faible densité de public, à justifier.", "Règlement de sécurité, art. M 2"),
            ("Au-delà de 1 000 m² de vente : autorisation commerciale", "Autorisation d'exploitation commerciale, délivrée après avis de la CDAC.", "Code de commerce, art. L752-1"),
        ],
    },
}

# Avant de signer : neuf points, repérés sur le plan
CHECKS = [
    (1, "Destination et bail", "La clause de destination autorise-t-elle votre activité ? En changer en cours de bail passe par l'accord du bailleur ou par une procédure de déspécialisation.", "Code de commerce, art. L145-47 et L145-48"),
    (2, "Linéaire protégé", "Sur les rues protégées du PLU de Paris, un rez-de-chaussée commercial ne peut pas devenir un bureau ou une agence ; sur certaines, l'artisanat ou le commerce culturel est lui-même protégé.", "PLU de Paris, art. UG.1.4.2"),
    (3, "Extraction", "Pour cuisiner : hotte, conduit propre à la cuisine, air rejeté à 8 m au moins de toute fenêtre. Sans conduit réalisable, le projet de cuisine est à revoir.", "Règlement sanitaire de Paris, art. 63-1 et 130-3"),
    (4, "Puissance électrique", "Fours, froid, climatisation, éclairage : la puissance disponible et la possibilité de l'augmenter se vérifient avant de s'engager.", "Point technique à faire relever sur place"),
    (5, "Entrée accessible", "Une marche à l'entrée ne dispense pas de l'accessibilité : adaptation de l'entrée ou dérogation motivée, à intégrer au dossier.", "Code de la construction, art. R164-1 et R164-3"),
    (6, "Sous-sol et sorties", "Ouvrir le sous-sol ou l'étage au public change l'effectif, donc parfois la catégorie et le nombre de sorties exigées.", "Règlement de sécurité, art. PE 2 et PE 11"),
    (7, "Réserve et livraisons", "Où livrer, où stocker, où sortir les déchets : un local mal desservi coûte du temps chaque jour d'exploitation.", "Point d'exploitation à vérifier sur place"),
    (8, "Façade et enseigne", "Devanture modifiée : déclaration préalable, un mois, deux en site patrimonial ou aux abords d'un monument. Enseigne : autorisation, deux mois.", "Code de l'urbanisme, art. R*421-17 et R423-24 ; Code de l'environnement, art. R581-13"),
    (9, "Copropriété", "Conduit en façade, travaux sur les parties communes : vote de l'assemblée générale. Le règlement de copropriété peut encadrer l'activité.", "Loi du 10 juillet 1965, art. 25 b"),
]

STEPS = [
    ("Avant le bail", "Lire le local", "Visite, relevé des contraintes, faisabilité de votre activité.", "Note de faisabilité : go, go sous conditions ou non"),
    ("Esquisse", "Concevoir", "Parcours client, zones de vente, réserve, caisse, lumière, mobilier.", "Plans et estimation par lots"),
    ("Dossiers", "Autoriser", "Déclaration préalable, autorisation de travaux ERP, enseigne, permis si nécessaire.", "Dossiers déposés et suivis"),
    ("Entreprises", "Consulter", "Cahier des charges, consultation, comparaison poste à poste.", "Tableau comparatif et marchés"),
    ("Chantier", "Construire", "Visites, comptes rendus, contrôle des situations de travaux.", "Comptes rendus de chantier"),
    ("Réception", "Ouvrir", "Réception, levée des réserves, attestations, registres.", "Dossier d'ouverture"),
]

# Délais d'instruction (mois) : libellé, précision, durée, extension, référence
GANTT = [
    ("Déclaration préalable", "devanture, aspect extérieur", 1, 1, "R*423-23 et R423-24 (+1 mois en site patrimonial ou abords)"),
    ("Enseigne", "autorisation du maire", 2, 0, "R581-13, Code de l'environnement"),
    ("Autorisation de travaux ERP", "accessibilité et sécurité", 4, 0, "R122-16, Code de la construction"),
    ("Permis de construire ERP", "façade ou structure et changement de destination", 5, 0, "R*423-28, Code de l'urbanisme"),
]

DELIVERABLES = [
    ("Une réponse avant de signer", "Le local tient-il votre activité, à quelles conditions, pour quels travaux ? Une note claire avant l'engagement."),
    ("Des plans qui tiennent la règle", "Effectif, sorties, accessibilité, sécurité : le plan de vente est dessiné avec le règlement, pas corrigé après."),
    ("Des dossiers complets", "Déclaration préalable, autorisation de travaux, enseigne : préparés, déposés et suivis jusqu'à la décision."),
    ("Des devis comparables", "Un même cahier des charges pour toutes les entreprises : vous comparez des prix, pas des interprétations."),
    ("Un chantier tenu", "Visites, comptes rendus, contrôle des situations avant paiement, réserves levées."),
    ("Une ouverture préparée", "Attestations, registre d'accessibilité, registre de sécurité, commission quand elle est requise."),
]

FAQ = [
    {"q": "Faut-il un architecte pour aménager un commerce à Paris ?",
     "a": "<p>Pas toujours. Le recours à un architecte est obligatoire pour un permis de construire, sauf exceptions prévues par la loi (code de l'urbanisme, article L431-1). Beaucoup d'aménagements de boutique relèvent d'une déclaration préalable et d'une autorisation de travaux au titre des ERP. L'architecte vous apporte surtout trois choses : la vérification du local avant le bail, des plans conformes aux règles de sécurité et d'accessibilité, et des dossiers complets.</p>"},
    {"q": "Combien de temps faut-il pour obtenir les autorisations d'un commerce ?",
     "a": "<p>Comptez, à partir d'un dossier complet : un mois pour une déclaration préalable de devanture (deux en site patrimonial remarquable ou aux abords d'un monument historique), deux mois pour une enseigne, quatre mois pour une autorisation de travaux ERP, cinq mois pour un permis de construire portant sur un ERP. Déposés ensemble, ces dossiers s'instruisent en parallèle. Voir le <a href=\"/guides/calendrier-ouverture-magasin\">calendrier d'ouverture</a>.</p>"},
    {"q": "Mon commerce est-il un ERP de 5e catégorie ?",
     "a": "<p>Cela dépend de l'effectif du public, calculé selon les règles de votre type d'établissement. Un magasin (type M) reste en 5e catégorie sous 100 personnes au sous-sol, 100 aux étages et 200 au total ; un restaurant (type N) sous 100 au sous-sol, 200 aux étages et 200 au total (règlement de sécurité, PE 2). Faites le calcul avec le <a href=\"/calcul-effectif-erp-commerce\">calculateur d'effectif</a>.</p>"},
    {"q": "Faut-il une autorisation pour changer une devanture ou une enseigne ?",
     "a": "<p>Oui. Des travaux qui modifient l'aspect extérieur demandent une déclaration préalable (code de l'urbanisme, R*421-17 a). À Paris, le PLU encadre les devantures : intégration à la façade, retrait limité à 10 à 20 cm pour une devanture en feuillure, grilles posées à l'intérieur (UG.2.1.4). L'enseigne relève d'une autorisation distincte du maire, demandée en ligne (code de l'environnement, L581-18).</p>"},
    {"q": "Peut-on transformer une boutique en restaurant ?",
     "a": "<p>Souvent, mais quatre régimes se croisent. Urbanisme : passer du commerce de détail à la restauration reste dans la même destination ; sans travaux, aucune déclaration n'est due à ce titre (R*421-17 b), mais des travaux sur la façade ou la structure imposent un permis (R*421-14 c). ERP : le type passe de M à N, donc une autorisation de travaux. Bail : l'activité doit être autorisée ou faire l'objet d'une déspécialisation. Technique : l'extraction doit être réalisable.</p>"},
    {"q": "Que vérifier avant de signer un bail commercial ?",
     "a": "<p>La destination prévue au bail, les protections du PLU sur la rue, l'extraction si vous cuisinez, la puissance électrique, l'accessibilité de l'entrée, l'effectif et les sorties, la réserve et les livraisons, la façade et l'enseigne, la copropriété. Le <a href=\"/diagnostic-local-commercial\">diagnostic en 12 questions</a> vous donne une première réponse.</p>"},
    {"q": "Quels documents le bailleur doit-il fournir ?",
     "a": "<p>Le diagnostic de performance énergétique est joint au bail (code de la construction, L126-29) et l'état des risques y est annexé (code de l'environnement, L125-5). Le bail comporte un inventaire des charges et un état des travaux (code de commerce, L145-40-2) ; un état des lieux est établi à l'entrée (L145-40-1).</p>"},
    {"q": "Où intervient FIXIA ?",
     "a": "<p>À Paris et en Île-de-France. Hors de Paris, les règles de fond sont les mêmes, mais l'autorisation de travaux est délivrée par le maire et les avis sont rendus par les sous-commissions départementales. Rendez-vous au 71 rue du Cherche-Midi, Paris 6e, ou au 09 70 70 17 99.</p>"},
]

# Marché parisien (Apur, PLU, BNP Paribas Real Estate)
VACANCY = {"commerces": 73, "vacants": 11, "autres": 16}
