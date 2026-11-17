# -*- coding: utf-8 -*-
"""Pages du noyau : hubs, méthode, références, l'architecte, contact, outils."""

PAGES = [
    {
        "path": "/votre-projet", "kind": "core", "tpl": "hub.html", "section": "projets", "schema": "CollectionPage",
        "title": "Projets de commerce : situations et activités | Kalya Architecte",
        "description": "Avant le bail, création de boutique, aménagement, rénovation, travaux sans fermer, devanture, déploiement d'enseigne ; restaurants, métiers de bouche, instituts, showrooms.",
        "h1": "Votre projet de commerce, par situation et par activité",
        "lede": "Choisissez votre point de départ : chaque page dit ce qui compte, ce qui s'autorise et dans quels délais, textes à l'appui.",
        "cta": "Faire étudier mon projet",
    },
    {
        "path": "/outils", "kind": "core", "tpl": "hub.html", "section": "outils", "schema": "CollectionPage",
        "title": "Outils commerce : diagnostic, effectif ERP, calendrier | Kalya",
        "description": "Trois outils gratuits, sans inscription : diagnostic d'un local avant le bail, calcul d'effectif et de catégorie ERP, calendrier des autorisations.",
        "h1": "Trois outils pour décider plus vite",
        "lede": "Gratuits, sans inscription, calculés dans votre navigateur. Ils donnent une première lecture ; la faisabilité d'architecte la confirme, documents en main.",
    },
    {
        "path": "/guides", "kind": "core", "tpl": "hub.html", "section": "/guides", "schema": "CollectionPage",
        "title": "Guides pour ouvrir un commerce à Paris : ERP, PLU, bail | Kalya",
        "description": "Guides sourcés pour un commerce : autorisations, calendrier, budget, classement ERP, accessibilité, enseigne, extraction, bail, destination, PLU de Paris.",
        "h1": "Guides pour un projet de commerce, texte à l'appui",
        "lede": "Chaque guide répond d'abord en quelques lignes, puis détaille. Les règles citées renvoient à leurs textes, consultés le 9 octobre 2026.",
    },
    {
        "path": "/mission", "kind": "core", "tpl": "mission.html", "section": "/mission", "as_service": True,
        "title": "Méthode : la mission d'architecte, du bail à l'ouverture | Kalya",
        "description": "La mission d'architecte pour un commerce en six étapes : lire le local, concevoir, autoriser, consulter, construire, ouvrir. Un livrable à chaque étape, des délais sourcés.",
        "h1": "Méthode : six étapes, un livrable à chacune",
        "short": "Méthode", "teaser": "Six étapes, un livrable à chacune.",
        "lede": "Du local repéré à la vitrine allumée, une seule personne responsable du projet : l'architecte qui l'a dessiné. Chaque étape se conclut par un document que vous gardez.",
        "service_type": "Mission d'architecture commerciale",
        "sources": ["r42323", "r42324", "r58113", "r12216", "r42328", "l4311"],
    },
    {
        "path": "/honoraires", "kind": "core", "tpl": "page.html", "section": "/honoraires", "verified": "new",
        "title": "Honoraires d'architecte pour un commerce : prix publiés | Kalya",
        "description": "Prix d'architecte pour un commerce à Paris : faisabilité 790 € HT, autorisation de travaux ERP 2 200 € HT jusqu'à 100 m² puis 7 € HT/m². Le reste sur devis gratuit.",
        "h1": "Honoraires : des prix publiés, écrits dans le devis",
        "short": "Honoraires", "teaser": "Faisabilité 790 € HT, autorisation de travaux dès 2 200 € HT.",
        "answer": "Faisabilité avant signature : 790 € HT. Autorisation de travaux ERP : forfait de 2 200 € HT jusqu'à 100 m², puis 7 € HT par m² supplémentaire jusqu'à 400 m², pour un établissement de 5e catégorie sans hébergement à Paris et en petite couronne. Déclaration préalable de devanture, enseigne, permis de construire, conception complète de l'aménagement et suivi de chantier : sur devis. Le devis est gratuit ; rien n'est à payer avant sa signature.",
        "cta": "Demander un devis", "cta_href": "/etudier-mon-projet",
        "plate": [("790 € HT", "Faisabilité avant signature, jusqu'à 100 m²"), ("2 200 € HT", "Autorisation de travaux ERP jusqu'à 100 m², puis 7 € HT par m²")],
        "bullets": [
            "Faisabilité avant signature : 790 € HT (948 € TTC), note avec croquis et avis : faisable, faisable sous conditions ou bloquant.",
            "Autorisation de travaux ERP : 2 200 € HT jusqu'à 100 m², puis 7 € HT par m² supplémentaire, jusqu'à 400 m².",
            "Dossier prêt en une semaine, une fois toutes les pièces nécessaires réunies (délai indicatif).",
            "Réponse sous 24 heures ; devis gratuit ; échéancier : 50 % à la signature du devis, 50 % à la remise du dossier.",
            "Les mêmes prix sont publiés sur architecte-erp.fr, par le même architecte.",
        ],
        "sections": [
            ("Faisabilité avant signature : 790 € HT", """<p>L'architecte analyse la destination du local, le classement de l'établissement, l'accessibilité, la sécurité incendie et les autorisations nécessaires, puis vous remet une note avec croquis et son avis : faisable, faisable sous conditions ou bloquant. 790 € HT, soit 948 € TTC, pour un établissement de 5e catégorie sans hébergement jusqu'à 100 m², à Paris et en petite couronne ; au-delà, sur devis.</p>
<p>C'est une mission distincte, en plus du forfait d'autorisation de travaux, qui ne comprend pas la conception de l'aménagement. Voir <a href="/avant-signature-bail-commercial">avant de signer le bail</a>.</p>"""),
            ("Autorisation de travaux ERP : le forfait", """<div class="table-wrap"><table>
<caption class="sr">Forfait d'autorisation de travaux selon la surface totale du local</caption>
<thead><tr><th scope="col">Surface totale du local (réserves, sous-sol et locaux du personnel compris)</th><th scope="col">Prix HT</th><th scope="col">Prix TTC</th></tr></thead>
<tbody>
<tr><td>Jusqu'à 100 m²</td><td>2 200 €</td><td>2 640 €</td></tr>
<tr><td>150 m²</td><td>2 550 €</td><td>3 060 €</td></tr>
<tr><td>200 m²</td><td>2 900 €</td><td>3 480 €</td></tr>
<tr><td>250 m²</td><td>3 250 €</td><td>3 900 €</td></tr>
<tr><td>300 m²</td><td>3 600 €</td><td>4 320 €</td></tr>
<tr><td>400 m²</td><td>4 300 €</td><td>5 160 €</td></tr>
</tbody></table></div>
<p>Pour un établissement de 5e catégorie sans hébergement, à Paris et en petite couronne. Au-delà de 400 m², dans une autre catégorie ou ailleurs en Île-de-France : sur devis.</p>
<h3>Ce qui est inclus</h3>
<ul>
<li>Un échange par téléphone pour cadrer le projet, puis le devis écrit, gratuit.</li>
<li>Une visite du local par l'architecte, si elle est nécessaire.</li>
<li>Les plans du projet, établis à partir de vos plans existants cotés et de l'aménagement que vous décrivez, avec une série de corrections avant votre validation, dont les plans cotés en trois dimensions du volet accessibilité (code de la construction et de l'habitation, D122-12).</li>
<li>La notice d'accessibilité (D122-12) et le volet sécurité : description succincte des travaux pour un établissement de 5e catégorie sans hébergement (R122-7, II).</li>
<li>Le formulaire de demande (Cerfa n° 13824) et les exemplaires exigés (R122-11).</li>
<li>Le dépôt de la demande, présentée par vous en qualité de demandeur (R122-10).</li>
<li>La réponse à la demande de pièces manquantes (R122-16), pour les pièces établies par l'architecte et sans modification du projet.</li>
</ul>
<h3>Ce qui n'est pas inclus</h3>
<ul>
<li>Le permis de construire, la déclaration préalable (façade, vitrine), l'autorisation d'enseigne et le changement de destination : sur devis.</li>
<li>Le relevé du local, si vos plans cotés ne sont pas exploitables (vous le savez avant le devis) : en option.</li>
<li>Les études techniques (désenfumage, structure, acoustique) et les diagnostics.</li>
<li>La conception complète de l'aménagement et le suivi des travaux : sur devis.</li>
<li>Une nouvelle demande après un refus : sur devis.</li>
</ul>"""),
            ("Options, seulement si vous les demandez", """<div class="table-wrap"><table>
<caption class="sr">Options et prix</caption>
<thead><tr><th scope="col">Option</th><th scope="col">Prix HT</th><th scope="col">Prix TTC</th></tr></thead>
<tbody>
<tr><td>Relevé du local par un géomètre missionné : plans cotés de chaque niveau ouvert au public, niveaux de l'accès, hauteurs sous plafond</td><td>900 € jusqu'à 100 m², puis 4 € par m²</td><td>1 080 €, puis 4,80 € par m²</td></tr>
<tr><td>Demande de dérogation aux règles d'accessibilité (R164-3), par règle, hors justificatifs, qui restent à votre charge</td><td>450 €</td><td>540 €</td></tr>
<tr><td>Visite supplémentaire du local</td><td>250 €</td><td>300 €</td></tr>
<tr><td>Modification de l'aménagement après validation des plans, sur estimation écrite acceptée avant exécution</td><td>110 € de l'heure</td><td>132 € de l'heure</td></tr>
</tbody></table></div>"""),
            ("Conception, devanture, chantier : sur devis", """<p>Créer une boutique ou un restaurant demande souvent davantage que l'autorisation de travaux : conception de l'aménagement, déclaration préalable de la devanture, autorisation d'enseigne, consultation des entreprises et, si vous le demandez, suivi du chantier jusqu'à la réception. Ces missions font l'objet d'un devis écrit, après un premier échange : leur contenu dépend du local, de l'activité et de ce que vous confiez à l'architecte.</p>"""),
            ("Ce qui est écrit avant de commencer", """<ul>
<li>Le prix ferme et ce qu'il comprend.</li>
<li>La liste des pièces nécessaires : adresse du local, bail, plans existants cotés avec les niveaux de l'accès, ou à défaut le relevé en option, description de l'activité et de l'aménagement, effectif prévu.</li>
<li>L'échéancier : 50 % à la signature du devis, 50 % à la remise du dossier, avant son dépôt.</li>
</ul>
<p>Aucun travail n'est engagé avant la signature du devis. Les missions sont signées par Quentin Piepszownik, architecte inscrit à l'Ordre, entrepreneur individuel assuré à la Mutuelle des Architectes Français.</p>"""),
        ],
        "faq": [
            {"q": "Combien coûte un dossier d'autorisation de travaux pour un commerce ?", "a": "<p>Chez Kalya Architecte, 2 200 € HT pour un local jusqu'à 100 m², puis 7 € HT par m² supplémentaire jusqu'à 400 m², pour un établissement de 5e catégorie sans hébergement à Paris et en petite couronne. Le prix comprend les plans, la notice d'accessibilité, le volet sécurité, le formulaire et le dépôt.</p>"},
            {"q": "La faisabilité est-elle déduite du forfait ?", "a": "<p>Non. La faisabilité avant signature (790 € HT) est une mission distincte, en plus du forfait d'autorisation de travaux.</p>"},
            {"q": "Le délai d'une semaine est-il garanti ?", "a": "<p>C'est un délai indicatif de préparation du dossier, qui ne court qu'une fois toutes les pièces nécessaires réunies. L'instruction par l'administration dure ensuite quatre mois à compter d'un dossier complet (R122-16).</p>"},
        ],
        "sources": ["aerp_tarifs", "r12216", "r1227", "cerfa13824", "r1643"],
        "related": ["/avant-signature-bail-commercial", "/guides/architecte-obligatoire-commerce", "/guides/autorisations-travaux-commerce"],
        "jsonld_offers": [
            ("Faisabilité avant signature d'un bail commercial", 790, "Établissement de 5e catégorie sans hébergement jusqu'à 100 m², Paris et petite couronne"),
            ("Autorisation de travaux ERP, local jusqu'à 100 m²", 2200, "Puis 7 € HT par m² supplémentaire jusqu'à 400 m² ; 5e catégorie sans hébergement, Paris et petite couronne"),
        ],
    },
    {
        "path": "/references", "kind": "core", "tpl": "references.html", "section": "/references", "schema": "CollectionPage", "short": "Références",
        "title": "Références : projets conduits par Quentin Piepszownik, architecte | Kalya",
        "description": "Projets réellement conduits par Quentin Piepszownik, architecte : aménagement de 700 m² livré pour CGE, dossiers ERP à Paris et en Île-de-France. Photos du projet livré.",
        "h1": "Références : des projets réellement conduits",
        "lede": "Ne sont publiés ici que des projets conduits par l'architecte, avec leur périmètre réel et les photos du projet livré.",
    },
    {
        "path": "/a-propos", "kind": "core", "tpl": "about.html", "section": "/a-propos", "schema": "AboutPage", "short": "L'architecte",
        "title": "L'architecte : Quentin Piepszownik, Kalya Architecte, Paris",
        "description": "Quentin Piepszownik, architecte inscrit à l'Ordre d'Île-de-France (n° 077297), Kalya Architecte : commerces, ERP et autorisations à Paris et en Île-de-France.",
        "h1": "L'architecte : un interlocuteur, du bail à l'ouverture",
        "lede": "Kalya Architecte est le nom sous lequel Quentin Piepszownik, architecte, conduit ses missions. Il est aussi l'auteur de dossier-erp-paris.fr, consacré aux dossiers ERP à Paris.",
    },
    {
        "path": "/etudier-mon-projet", "kind": "core", "tpl": "contact.html", "schema": "ContactPage", "short": "Présenter mon projet",
        "title": "Présenter mon projet de commerce : devis gratuit | Kalya Architecte",
        "description": "Décrivez votre projet de boutique, de restaurant ou d'institut : activité, adresse, surface, avancement, échéance. Réponse sous 24 heures, devis gratuit. 07 56 83 24 28.",
        "h1": "Présenter mon projet",
        "lede": "Cinq minutes pour décrire votre projet. Réponse sous 24 heures, devis gratuit, rien à payer avant sa signature.",
    },
    {
        "path": "/etudier-mon-projet/merci", "kind": "core", "tpl": "merci.html", "indexable": False,
        "title": "Demande envoyée | Kalya Architecte", "description": "Votre demande a bien été envoyée.",
        "h1": "Demande envoyée.", "lede": "Merci. Un accusé de réception vient de partir vers votre adresse ; l'architecte revient vers vous avec les premières questions sur votre local.",
    },
    {
        "path": "/diagnostic-local-commercial", "kind": "outil", "tpl": "tool_diag.html", "section": "outils", "needs_plan": True,
        "title": "Ce local commercial est-il bon ? Diagnostic en 12 questions | Kalya",
        "description": "Diagnostic gratuit d'un local commercial avant le bail : activité, PLU de Paris, extraction, accessibilité, devanture, copropriété. Verdict et points à vérifier.",
        "h1": "Ce local est-il bon ? Le diagnostic avant de signer",
        "short": "Diagnostic de local", "teaser": "Douze questions avant de signer : verdict et points à vérifier.",
        "answer": "Douze questions, deux minutes : vous obtenez un premier verdict (oui, oui sous conditions, risque élevé, ou non pour ce format) et la liste des points à faire vérifier avant de signer le bail, avec leurs textes. Rien n'est enregistré : le calcul se fait dans votre navigateur.",
        "sources": ["l14547", "l14548", "r15128", "a2016", "plubreg", "rsd631", "rsd1303", "r1642", "r1643", "terrasses", "m2", "n2", "pe2", "pe11", "pe14", "r42117", "r42114", "r42323", "r42324", "r4251", "r4252", "l58118", "r58113", "l1223", "r12216", "copro25", "copro3", "copro8", "copro9"],
        "faq": [
            {"q": "Le diagnostic remplace-t-il une étude ?", "a": "<p>Non. Il signale les points qui peuvent rendre un local impropre à votre activité et ceux qui conditionnent le projet. La <a href=\"/avant-signature-bail-commercial\">faisabilité avant signature</a> (790 € HT) les vérifie, plans et documents en main.</p>"},
            {"q": "Mes réponses sont-elles enregistrées ?", "a": "<p>Non. Le calcul se fait dans votre navigateur. Si vous choisissez d'envoyer le diagnostic à l'architecte, seul le résumé et vos coordonnées sont transmis, par le formulaire.</p>"},
        ],
    },
]

TOOLS_INTRO = [
    ("/diagnostic-local-commercial", "Ce local est-il bon ?", "Douze questions avant de signer le bail : un verdict et la liste des points à vérifier, avec leurs textes."),
    ("/guides/erp-commerce-categorie-effectif#calcul", "Calcul d'effectif et de catégorie", "Magasin ou restaurant : effectif du public par niveau, catégorie ERP, sorties exigées."),
    ("/guides/calendrier-ouverture-magasin", "Calendrier d'ouverture", "Cochez ce que comporte votre projet : le délai d'instruction le plus long s'affiche."),
]
