# -*- coding: utf-8 -*-
"""Pages du noyau : hubs, méthode, références, l'architecte, contact, outils."""

PAGES = [
    {
        "path": "/votre-projet", "kind": "core", "tpl": "hub.html", "section": "projets", "schema": "CollectionPage",
        "title": "Projets de commerce : situations et activités | FIXIA Architecte",
        "description": "Avant le bail, création de boutique, aménagement, rénovation, travaux sans fermer, devanture, déploiement d'enseigne ; restaurants, métiers de bouche, instituts, showrooms.",
        "h1": "Votre projet de commerce, par situation et par activité",
        "lede": "Choisissez votre point de départ : chaque page dit ce qui compte, ce qui s'autorise et dans quels délais, textes à l'appui.",
        "cta": "Faire étudier mon projet",
    },
    {
        "path": "/outils", "kind": "core", "tpl": "hub.html", "section": "outils", "schema": "CollectionPage",
        "title": "Outils commerce : diagnostic, effectif ERP, calendrier | FIXIA",
        "description": "Trois outils gratuits, sans inscription : diagnostic d'un local avant le bail, calcul d'effectif et de catégorie ERP, calendrier des autorisations.",
        "h1": "Trois outils pour décider plus vite",
        "lede": "Gratuits, sans inscription, calculés dans votre navigateur. Ils donnent une première lecture ; la visite et l'étude la confirment.",
    },
    {
        "path": "/guides", "kind": "core", "tpl": "hub.html", "section": "/guides", "schema": "CollectionPage",
        "title": "Guides pour ouvrir un commerce à Paris : ERP, PLU, bail | FIXIA",
        "description": "Guides sourcés pour un commerce : autorisations, calendrier, budget, classement ERP, accessibilité, enseigne, extraction, bail, destination, PLU de Paris.",
        "h1": "Guides pour un projet de commerce, texte à l'appui",
        "lede": "Chaque guide répond d'abord en quelques lignes, puis détaille. Les règles citées renvoient à leurs textes, consultés le 9 octobre 2026.",
    },
    {
        "path": "/mission", "kind": "core", "tpl": "mission.html", "section": "/mission", "as_service": True,
        "title": "Méthode : la mission d'architecte, du bail à l'ouverture | FIXIA",
        "description": "La mission d'architecte pour un commerce en six étapes : lire le local, concevoir, autoriser, consulter, construire, ouvrir. Un livrable à chaque étape, des délais sourcés.",
        "h1": "Méthode : six étapes, un livrable à chacune",
        "short": "Méthode", "teaser": "Six étapes, un livrable à chacune.",
        "lede": "Du local repéré à la vitrine allumée, une seule personne responsable du projet : l'architecte qui l'a dessiné. Chaque étape se conclut par un document que vous gardez.",
        "service_type": "Mission d'architecture commerciale",
        "sources": ["r42323", "r42324", "r58113", "r12216", "r42328", "l4311"],
    },
    {
        "path": "/references", "kind": "core", "tpl": "references.html", "section": "/references", "schema": "CollectionPage",
        "title": "Références : projets conduits par Quentin Piepszownik, architecte | FIXIA",
        "description": "Projets réellement conduits par l'architecte de FIXIA : aménagement de 700 m² livré pour CGE, dossiers ERP à Paris et en Île-de-France. Photos du projet livré.",
        "h1": "Références : des projets réellement conduits",
        "lede": "Ne sont publiés ici que des projets conduits par l'architecte, avec leur périmètre réel et les photos du projet livré.",
    },
    {
        "path": "/a-propos", "kind": "core", "tpl": "about.html", "section": "/a-propos", "schema": "AboutPage",
        "title": "L'architecte : Quentin Piepszownik, FIXIA Architecte, Paris | FIXIA",
        "description": "Quentin Piepszownik, architecte inscrit à l'Ordre d'Île-de-France (n° 077297), FIXIA Architecte : commerces, ERP et autorisations à Paris et en Île-de-France.",
        "h1": "L'architecte : un interlocuteur, du bail à l'ouverture",
        "lede": "FIXIA Architecte est le nom sous lequel Quentin Piepszownik, architecte, conduit ses missions. Il est aussi l'auteur de dossier-erp-paris.fr, consacré aux dossiers ERP à Paris.",
    },
    {
        "path": "/etudier-mon-projet", "kind": "core", "tpl": "contact.html", "schema": "ContactPage",
        "title": "Faire étudier mon projet de commerce | FIXIA Architecte, Paris",
        "description": "Décrivez votre projet de commerce : activité, adresse ou quartier, surface, avancement, échéance. Réponse d'un architecte. 71 rue du Cherche-Midi, Paris 6e. 09 70 70 17 99.",
        "h1": "Faire étudier mon projet",
        "lede": "Cinq minutes pour décrire votre projet ; une réponse d'architecte, avec les premières questions à se poser sur votre local.",
    },
    {
        "path": "/etudier-mon-projet/merci", "kind": "core", "tpl": "merci.html", "indexable": False,
        "title": "Demande envoyée | FIXIA Architecte", "description": "Votre demande a bien été envoyée.",
        "h1": "Demande envoyée.", "lede": "Merci. Un accusé de réception vient de partir vers votre adresse ; l'architecte revient vers vous avec les premières questions sur votre local.",
    },
    {
        "path": "/diagnostic-local-commercial", "kind": "outil", "tpl": "tool_diag.html", "section": "outils", "needs_plan": True,
        "title": "Ce local commercial est-il bon ? Diagnostic en 12 questions | FIXIA",
        "description": "Diagnostic gratuit d'un local commercial avant le bail : activité, PLU de Paris, extraction, accessibilité, devanture, copropriété. Verdict et points à vérifier.",
        "h1": "Ce local est-il bon ? Le diagnostic avant de signer",
        "short": "Diagnostic de local", "teaser": "Douze questions avant de signer : verdict et points à vérifier.",
        "answer": "Douze questions, deux minutes : vous obtenez un premier verdict (oui, oui sous conditions, risque élevé, ou non pour ce format) et la liste des points à faire vérifier avant de signer le bail, avec leurs textes. Rien n'est enregistré : le calcul se fait dans votre navigateur.",
        "sources": ["l14547", "plubreg", "rsd631", "rsd1303", "r1641", "r1643", "pe2", "pe11", "r42117", "r42324", "l58118", "copro25", "l1223", "r42114"],
        "faq": [
            {"q": "Le diagnostic remplace-t-il une visite ?", "a": "<p>Non. Il signale les points qui peuvent rendre un local impropre à votre activité et ceux qui conditionnent le projet. La visite d'un architecte les vérifie sur place, plans et documents en main.</p>"},
            {"q": "Mes réponses sont-elles enregistrées ?", "a": "<p>Non. Le calcul se fait dans votre navigateur. Si vous choisissez d'envoyer le diagnostic à l'architecte, seul le résumé et vos coordonnées sont transmis, par le formulaire.</p>"},
        ],
    },
    {
        "path": "/calcul-effectif-erp-commerce", "kind": "outil", "tpl": "tool_eff.html", "section": "outils",
        "title": "Calcul de l'effectif ERP d'un magasin ou d'un restaurant | FIXIA",
        "description": "Calculez l'effectif d'une boutique (type M) ou d'un restaurant (type N), sa catégorie ERP et ses sorties, selon les articles M 2, N 2, PE 2, PE 11 et R143-19.",
        "h1": "Calcul d'effectif et de catégorie ERP, magasin ou restaurant",
        "short": "Calcul d'effectif ERP", "teaser": "Effectif, catégorie et sorties, magasin ou restaurant.",
        "answer": "Indiquez vos surfaces par niveau : le calculateur applique les densités du règlement de sécurité (M 2 pour un magasin, N 2 pour un restaurant), compare l'effectif aux seuils de la 5e catégorie (PE 2), donne la catégorie (R143-19) et les sorties exigées (PE 11). Résultat indicatif : la notice de sécurité du projet fait foi.",
        "sources": ["m2", "n2", "pe2", "pe3", "r14319", "gn1", "pe11"],
        "faq": [
            {"q": "Quelle surface saisir pour un magasin ?", "a": "<p>L'article M 2 calcule l'effectif sur la surface de vente. Le règlement n'en donne pas de définition opposable : on y retient en pratique les zones où le public circule et achète, hors réserves et locaux de personnel. En cas de doute, l'hypothèse se justifie dans la notice de sécurité.</p>"},
            {"q": "Le personnel compte-t-il ?", "a": "<p>Pas pour classer un établissement en 5e catégorie. Il compte pour la catégorie au-delà, et pour les sorties, lorsqu'il ne dispose pas de dégagements propres (GN 1, PE 3, PE 11).</p>"},
        ],
    },
]

TOOLS_INTRO = [
    ("/diagnostic-local-commercial", "Ce local est-il bon ?", "Douze questions avant de signer le bail : un verdict et la liste des points à vérifier, avec leurs textes."),
    ("/calcul-effectif-erp-commerce", "Calcul d'effectif et de catégorie", "Magasin ou restaurant : effectif du public par niveau, catégorie ERP, sorties exigées."),
    ("/guides/calendrier-ouverture-magasin", "Calendrier d'ouverture", "Cochez ce que comporte votre projet : le délai d'instruction le plus long s'affiche."),
]
