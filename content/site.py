# -*- coding: utf-8 -*-
"""Identité, navigation et sources de architecte-commerce.fr (FIXIA Architecte).

Règle éditoriale : un fait juridique, réglementaire ou chiffré n'est publié qu'avec sa source (SOURCES),
lue dans sa version en vigueur. Textes relus le 9 octobre 2026 (Légifrance, EUR-Lex, paris.fr, service-public, Apur).
Les hypothèses et les exemples sont présentés comme tels ; aucun chiffre de coût n'est publié sans source.
"""

VERIFIED = "9 octobre 2026"
VERIFIED_ISO = "2026-10-09"

SITE = {
    "domain": "architecte-commerce.fr",
    "url": "https://architecte-commerce.fr",
    "brand": "FIXIA Architecte",
    "short": "FIXIA",
    "descriptor": "Architecte de commerces à Paris",
    "person": "Quentin Piepszownik",
    "person_title": "Architecte DE-HMONP",
    "phone": "09 70 70 17 99",
    "phone_intl": "+33970701799",
    "email": "analyse@fixia.fr",
    "street": "71 rue du Cherche-Midi",
    "postal": "75006",
    "city": "Paris",
    "address": "71 rue du Cherche-Midi, 75006 Paris",
    "maps_url": "https://www.google.com/maps/search/?api=1&query=71%20rue%20du%20Cherche-Midi%2C%2075006%20Paris",
    "legal_name": "Quentin Piepszownik",
    "siren": "513 794 768",
    "tva": "FR93513794768",
    "siege": "1 bis rue Gallieni, 95160 Montmorency",
    "ordre": "077297",
    "ordre_region": "Île-de-France",
    # Formulaire : webhook n8n « ARCHITECTE COMMERCE (FIXIA) — formulaire de contact (production) », envoi vers analyse@fixia.fr
    "form_action": "https://architecte-erp.app.n8n.cloud/webhook/architecte-commerce-demande-5d8e2a71c4f9b036",
}

# Sites du même architecte (liens éditoriaux)
ERP_SITES = {
    "dep": ("dossier-erp-paris.fr", "https://dossier-erp-paris.fr/", "Les guides sourcés du dossier ERP à Paris : autorisation de travaux, pièces, commission de sécurité, ouverture. Par Kalya Architecte, marque du même architecte."),
    "aerp": ("architecte-erp.fr", "https://www.architecte-erp.fr/", "L'architecte des établissements recevant du public : faisabilité, conception, autorisations de travaux, accessibilité et sécurité incendie."),
}
DEP = "https://dossier-erp-paris.fr"

# Projets (situations) : chemin, libellé, accroche
SITUATIONS = [
    ("/avant-signature-bail-commercial", "Avant de signer le bail", "Le local tient-il votre activité ? Réponse avant l'engagement."),
    ("/architecte-boutique", "Créer une boutique", "Du concept à l'ouverture, autorisations comprises."),
    ("/amenagement-local-commercial", "Aménager un local commercial", "Plan, réserve, caisse, réseaux : un local qui tourne."),
    ("/renovation-magasin", "Rénover un magasin", "Remettre à niveau sans perdre la clientèle."),
    ("/renovation-commerce-site-occupe", "Travaux sans fermer", "Phasage, nuit, week-end : rester ouvert."),
    ("/vitrine-et-devanture-commerce", "Vitrine et devanture", "Façade, enseigne, store : ce que Paris autorise."),
    ("/concept-et-deploiement-enseigne", "Déployer une enseigne", "Un concept, des locaux tous différents."),
]
# Activités : chemin, libellé, accroche
ACTIVITES = [
    ("/architecte-boutique", "Boutique et concept store", "Magasin de vente : type M."),
    ("/architecte-restaurant", "Restaurant, bar, café", "Type N, cuisine, extraction, terrasse."),
    ("/architecte-metiers-de-bouche", "Boulangerie et métiers de bouche", "Laboratoire, hygiène, vente."),
    ("/architecte-institut-beaute-coiffure", "Institut, salon de coiffure", "Cabines, réseaux, accueil."),
    ("/architecte-showroom", "Showroom", "Montrer, conseiller, commander."),
]
OUTILS = [
    ("/diagnostic-local-commercial", "Ce local est-il bon ?", "Diagnostic en 12 questions avant de signer."),
    ("/calcul-effectif-erp-commerce", "Calcul d'effectif et catégorie", "Magasin ou restaurant : effectif, catégorie, sorties."),
    ("/guides/calendrier-ouverture-magasin", "Calendrier d'ouverture", "Les délais d'autorisation, scénario par scénario."),
]
NAV = [
    ("/mission", "Méthode"),
    ("/guides", "Guides"),
    ("/references", "Références"),
    ("/a-propos", "L'architecte"),
]
ZONES = [
    ("/architecte-commerce-paris", "Architecte commerce Paris"),
    ("/architecte-commerce-ile-de-france", "Architecte commerce Île-de-France"),
]

# Redirections permanentes (anciennes adresses du site)
REDIRECTS = [
    ("/fixia", "/a-propos"),
    ("/contact", "/etudier-mon-projet"),
    ("/guides/preparer-projet-commerce", "/guides/preparer-projet-commerce"),
]
REDIRECTS = [r for r in REDIRECTS if r[0] != r[1]]

LF = "https://www.legifrance.gouv.fr/codes/article_lc/"
LL = "https://www.legifrance.gouv.fr/loda/article_lc/"

# Sources : clé -> (intitulé, URL, précision de version ou de date)
SOURCES = {
    # --- ERP : classement, effectif, sécurité
    "gn1": ("Règlement de sécurité du 25 juin 1980, article GN 1 (classement, effectif du personnel)", LL + "LEGIARTI000045143487", "version en vigueur depuis le 10 février 2022"),
    "r14319": ("Code de la construction et de l'habitation, article R143-19 (catégories 1 à 4)", LF + "LEGIARTI000043818977", "version en vigueur depuis le 1er juillet 2021"),
    "pe2": ("Règlement de sécurité, livre III, article PE 2 (seuils de la 5e catégorie)", LL + "LEGIARTI000024770569", "version en vigueur depuis le 1er janvier 2026"),
    "pe3": ("Règlement de sécurité, article PE 3 (calcul de l'effectif en 5e catégorie)", LF + "LEGIARTI000024751105", "version en vigueur depuis le 27 août 1990"),
    "pe11": ("Règlement de sécurité, article PE 11 (dégagements en 5e catégorie)", LL + "LEGIARTI000024751142", "version en vigueur depuis le 1er juillet 2004"),
    "m2": ("Règlement de sécurité, article M 2 (effectif des magasins de vente)", LF + "LEGIARTI000036117441", "version en vigueur depuis le 1er décembre 2017"),
    "n2": ("Règlement de sécurité, article N 2 (effectif des restaurants et débits de boissons)", LF + "LEGIARTI000024751045", "version en vigueur depuis le 10 février 2022"),
    # --- Autorisation de travaux ERP
    "l1223": ("Code de la construction et de l'habitation, article L122-3 (autorisation de travaux ; régime déclaratif de la loi du 26 mai 2026)", LF + "LEGIARTI000054142549", "version en vigueur depuis le 28 mai 2026"),
    "r12216": ("Code de la construction et de l'habitation, article R122-16 (instruction : quatre mois)", LF + "LEGIARTI000043818451", "version en vigueur depuis le 1er juillet 2021"),
    "r12221": ("Code de la construction et de l'habitation, article R122-21 (accord implicite)", LF + "LEGIARTI000043818463", "version en vigueur depuis le 1er juillet 2021"),
    "r42328": ("Code de l'urbanisme, article R*423-28 (permis de construire portant sur un ERP : cinq mois)", LF + "LEGIARTI000043841115", "version en vigueur"),
    "r42515": ("Code de l'urbanisme, article R*425-15 (le permis de construire vaut autorisation de travaux)", LF + "LEGIARTI000043841073", "version en vigueur depuis le 1er juillet 2021"),
    "cerfa13824": ("Formulaire Cerfa n° 13824*04, demande d'autorisation de travaux (service-public, fiche R10190)", "https://entreprendre.service-public.gouv.fr/vosdroits/R10190", "consulté le 7 octobre 2026"),
    "ppol": ("Préfecture de police, sécurité incendie des ERP à Paris", "https://www.prefecturedepolice.interieur.gouv.fr/demarches/securite-incendie-des-erp-dont-hebergement-et-des-igh", "consulté le 7 octobre 2026"),
    # --- Accessibilité
    "r1641": ("Code de la construction et de l'habitation, article R164-1 (ERP existants)", LF + "LEGIARTI000043819295", "version en vigueur depuis le 1er juillet 2021"),
    "r1643": ("Code de la construction et de l'habitation, article R164-3 (demandes de dérogation)", LF + "LEGIARTI000043819299", "version en vigueur depuis le 1er juillet 2021"),
    "r1646": ("Code de la construction et de l'habitation, article R164-6 (registre public d'accessibilité)", LF + "LEGIARTI000043819305", "version en vigueur depuis le 1er juillet 2021"),
    "a2014": ("Arrêté du 8 décembre 2014 (accessibilité des ERP situés dans un cadre bâti existant)", LL + "LEGIARTI000034797402", "article 1"),
    "a2017reg": ("Arrêté du 19 avril 2017 (registre public d'accessibilité)", LL + "LEGIARTI000034480997", "articles 1 et 3"),
    # --- Urbanisme
    "r15127": ("Code de l'urbanisme, article R151-27 (destinations)", LF + "LEGIARTI000047337112", "version en vigueur depuis le 1er juillet 2023"),
    "r15128": ("Code de l'urbanisme, article R151-28 (sous-destinations)", LF + "LEGIARTI000047337108", "version en vigueur depuis le 1er juillet 2023"),
    "a2016": ("Arrêté du 10 novembre 2016 modifié, article 3 (définition des sous-destinations)", LL + "LEGIARTI000047336587", "version en vigueur depuis le 25 mars 2023"),
    "r42114": ("Code de l'urbanisme, article R*421-14 c (permis : structures porteuses ou façade avec changement de destination)", LF + "LEGIARTI000031764577", "version en vigueur depuis le 1er janvier 2016"),
    "r42117": ("Code de l'urbanisme, article R*421-17 (déclaration préalable : aspect extérieur, changement de destination)", LF + "LEGIARTI000053561259", "version en vigueur depuis le 22 février 2026"),
    "l4218": ("Code de l'urbanisme, article L421-8 (travaux dispensés de formalité : respect du PLU)", LF + "LEGIARTI000049398814", "version en vigueur depuis le 11 avril 2024"),
    "r42323": ("Code de l'urbanisme, article R*423-23 (délai : un mois pour une déclaration préalable)", LF + "LEGIARTI000006819920", "version en vigueur depuis le 1er octobre 2007"),
    "r42324": ("Code de l'urbanisme, article R423-24 (majoration d'un mois : site patrimonial remarquable, abords)", LF + "LEGIARTI000053903312", "version en vigueur depuis le 17 avril 2026"),
    "r4251": ("Code de l'urbanisme, articles R*425-1 et R*425-2 (accord de l'architecte des Bâtiments de France)", LF + "LEGIARTI000038682307", "versions en vigueur depuis le 23 juin 2019"),
    "plub": ("Ville de Paris, PLU bioclimatique approuvé le 20 novembre 2024", "https://www.paris.fr/pages/plan-local-d-urbanisme-bioclimatique-vers-un-paris-plus-vert-et-plus-solidaire-23805", "page consultée le 9 octobre 2026"),
    "plubreg": ("PLU bioclimatique de Paris, règlement, tome 1, zone UG (UG.1.3.1, UG.1.3.5, UG.1.4.2, UG.2.1.4)", "https://regles-urbanisme.paris.fr/plu-bioclimatique/jsp/site/Portal.jsp?document_id=198&portlet_id=45", "texte consulté le 9 octobre 2026"),
    "plubcarte": ("Paris Data, « PLU bioclimatique : protections du commerce et de l'artisanat » (carte sans valeur réglementaire)", "https://opendata.paris.fr/explore/dataset/plub_protcom/", "jeu mis à jour le 5 juin 2025"),
    "spr": ("Ville de Paris, sites patrimoniaux remarquables (Marais, 7e arrondissement)", "https://www.paris.fr/pages/secteurs-sauvegardes-psmv-2351", "page consultée le 9 octobre 2026"),
    "l7521": ("Code de commerce, article L752-1 (autorisation d'exploitation commerciale au-delà de 1 000 m² de surface de vente)", LF + "LEGIARTI000037671151", "version en vigueur depuis le 25 novembre 2018"),
    # --- Enseignes et terrasses
    "l58118": ("Code de l'environnement, article L581-18 (enseignes soumises à autorisation)", LF + "LEGIARTI000043974793", "version en vigueur depuis le 1er janvier 2024"),
    "r58113": ("Code de l'environnement, article R581-13 (délai : deux mois, accord tacite)", LF + "LEGIARTI000053219839", "version en vigueur depuis le 1er juillet 2026"),
    "r58159": ("Code de l'environnement, article R581-59 (extinction des enseignes lumineuses)", LF + "LEGIARTI000048869649", "version en vigueur depuis le 1er janvier 2024"),
    "cerfa16308": ("Formulaire Cerfa n° 16308*01, autorisation préalable d'une enseigne (service-public, fiche R77838)", "https://entreprendre.service-public.gouv.fr/vosdroits/R77838", "fiche vérifiée le 25 septembre 2026"),
    "parisenseignes": ("Ville de Paris, enseignes et publicités (demande en ligne)", "https://www.paris.fr/pages/enseignes-et-publicites-3514", "page consultée le 9 octobre 2026"),
    "terrasses": ("Ville de Paris, terrasses et étalages (règlement du 18 juin 2021)", "https://www.paris.fr/pages/terrasses-et-etalages-3516", "page consultée le 9 octobre 2026"),
    # --- Copropriété
    "copro25": ("Loi n° 65-557 du 10 juillet 1965, article 25 b (travaux affectant les parties communes ou l'aspect extérieur)", LL + "LEGIARTI000051749507", "version en vigueur depuis le 18 juin 2025"),
    # --- Restaurant, hygiène
    "rsd631": ("Règlement sanitaire départemental de Paris, article 63-1 (air des locaux à pollution spécifique, rejet à 8 m des fenêtres)", "https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000006363928", "consolidation Légifrance"),
    "rsd1303": ("Règlement sanitaire départemental de Paris, article 130-3 (hottes, conduits, nettoyage mensuel), applicable aux restaurants par l'article 152-2", "https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000006364019", "consolidation Légifrance"),
    "ce852": ("Règlement (CE) n° 852/2004 relatif à l'hygiène des denrées alimentaires, annexe II", "https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:02004R0852-20210324", "version consolidée du 24 mars 2021"),
    "a2009": ("Arrêté du 21 décembre 2009 (règles sanitaires du commerce de détail)", "https://www.legifrance.gouv.fr/loda/id/LEGITEXT000021676844/", "version en vigueur"),
    "ddpp": ("Déclaration d'activité alimentaire, Cerfa n° 13984 (service-public, fiche R17520)", "https://entreprendre.service-public.gouv.fr/vosdroits/R17520", "consultée le 9 octobre 2026"),
    "r2334": ("Code rural, article R233-4 (déclaration des établissements manipulant des denrées)", LF + "LEGIARTI000044116307", "version en vigueur depuis le 30 septembre 2021"),
    "l2334": ("Code rural, article L233-4 (formation à l'hygiène alimentaire en restauration commerciale)", LF + "LEGIARTI000022657498", "version en vigueur"),
    "f32189": ("Service-public, « Règles d'hygiène dans les restaurants » (fiche F32189)", "https://entreprendre.service-public.gouv.fr/vosdroits/F32189", "fiche vérifiée le 12 mars 2024"),
    "assainissement": ("Ville de Paris, règlement d'assainissement en vigueur au 1er janvier 2026 (articles 15 et 17.1)", "https://www.paris.fr/pages/evacuation-des-eaux-usees-non-domestiques-3547", "page mise à jour le 5 octobre 2026"),
    "licences": ("Code de la santé publique, articles L3331-1 et L3331-2 (licences de débit de boissons et de restaurant)", LF + "LEGIARTI000031643392", "version en vigueur"),
    "r13361": ("Code de la santé publique, article R1336-1 (lieux diffusant des sons amplifiés)", LF + "LEGIARTI000035425898", "version en vigueur"),
    # --- Bail commercial
    "l1454": ("Code de commerce, article L145-4 (durée du bail : neuf ans au moins, résiliation triennale)", LF + "LEGIARTI000037667139", "version en vigueur"),
    "l1455": ("Code de commerce, article L145-5 (bail dérogatoire : trois ans au plus)", LF + "LEGIARTI000029108698", "version en vigueur"),
    "l14547": ("Code de commerce, articles L145-47 et L145-48 (activités connexes ou différentes)", LF + "LEGIARTI000039280354", "version en vigueur"),
    "l145401": ("Code de commerce, article L145-40-1 (état des lieux)", LF + "LEGIARTI000029103499", "version en vigueur"),
    "l145402": ("Code de commerce, article L145-40-2 (inventaire des charges, état des travaux)", LF + "LEGIARTI000029103688", "version en vigueur"),
    "r14535": ("Code de commerce, article R145-35 (charges et travaux non imputables au locataire)", LF + "LEGIARTI000029704677", "version en vigueur"),
    "l12629": ("Code de la construction et de l'habitation, article L126-29 (diagnostic de performance énergétique joint au bail)", LF + "LEGIARTI000043977041", "version en vigueur"),
    "l1255": ("Code de l'environnement, article L125-5 (état des risques annexé au bail)", LF + "LEGIARTI000006832938", "version en vigueur"),
    # --- Marché
    "apur2023": ("Apur, « L'évolution des commerces à Paris : inventaire des commerces 2023 », note n° 236", "https://www.apur.org/sites/default/files/8p236_bdcom_2023.pdf", "septembre 2023, relevé d'avril 2023"),
    "apurbdcom": ("Apur, observatoire des commerces parisiens (BDCOM)", "https://www.apur.org/en/open-data-maps/observatory/observatory-businesses-and-shops-paris-bdcom", "consulté le 9 octobre 2026"),
    "bnpre": ("BNP Paribas Real Estate, marché des commerces en France, 2e trimestre 2026", "https://www.realestate.bnpparibas.fr/media/france/2026-08/REVIEW%20COMMERCE%20-%20T2%202026_FR.pdf", "loyers prime du 1er semestre 2026"),
    "insee2111": ("Insee Première n° 2111, « Le compte du commerce en 2025 »", "https://www.insee.fr/fr/statistiques/9008999", "publié le 18 juin 2026"),
    # --- Profession
    "loi77": ("Loi n° 77-2 du 3 janvier 1977 sur l'architecture, article 9 (inscription au tableau)", LL + "LEGIARTI000006847402", "version en vigueur"),
    "l4311": ("Code de l'urbanisme, article L431-1 (recours à un architecte pour le permis de construire)", LF + "LEGIARTI000006815974", "version en vigueur depuis le 1er octobre 2007"),
    # --- Ajouts : bail 2026, sons, licences, amiante, Paris, autorité ERP, accessibilité, sécurité 5e catégorie
    "l145321": ("Code de commerce, article L145-32-1 (paiement mensuel du loyer de droit, loi n° 2026-403 du 26 mai 2026)", LF + "LEGIARTI000054137998", "en vigueur depuis le 28 mai 2026"),
    "l14540": ("Code de commerce, article L145-40 (garanties limitées à un trimestre de loyer, loi n° 2026-403 du 26 mai 2026)", LF + "LEGIARTI000054142450", "version issue de la loi du 26 mai 2026"),
    "r57127": ("Code de l'environnement, article R571-27 (étude de l'impact des nuisances sonores)", LF + "LEGIARTI000035426072", "version en vigueur"),
    "l333211": ("Code de la santé publique, article L3332-1-1 (permis d'exploitation, valable dix ans)", LF + "LEGIARTI000041510405", "version en vigueur"),
    "r133429": ("Code de la santé publique, article R1334-29-5 (dossier technique amiante tenu à disposition)", LF + "LEGIARTI000043841389", "version en vigueur depuis le 1er juillet 2021"),
    "preemption": ("Ville de Paris, diversité commerciale (droit de préemption commercial dans les 5e, 6e et une partie du 7e)", "https://www.paris.fr/pages/diversite-commerciale-3553", "page mise à jour le 7 août 2024"),
    "cci2023": ("CCI Paris Île-de-France, recensement 2023 de l'équipement commercial francilien", "https://www.cci-paris-idf.fr/fr/newsroom/presse/cp/recensement-2023-equipement-commercial-francilien", "communiqué du 25 janvier 2024"),
    "r1227": ("Code de la construction et de l'habitation, article R122-7 (autorité compétente ; 5e catégorie sans locaux à sommeil)", "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074096/LEGISCTA000043818421/", "version en vigueur depuis le 21 novembre 2025"),
    "r1653": ("Code de la construction et de l'habitation, article R165-3 (attestation d'accessibilité)", LF + "LEGIARTI000043819317", "version en vigueur depuis le 1er juillet 2021"),
    "adap": ("Ministère de la transition écologique, agenda d'accessibilité programmée (Ad'AP)", "https://www.ecologie.gouv.fr/politiques-publiques/ladap-agenda-daccessibilite-programmee", "page relue le 7 octobre 2026"),
    "pe14": ("Règlement de sécurité, livre III, article PE 14 (désenfumage), texte reproduit avec ses modifications", "https://sitesecurite.com/contenu/_erp/erppe/pe14.php?id=PE14", "consulté le 7 octobre 2026"),
    "pe24": ("Règlement de sécurité, livre III, article PE 24 (éclairage de sécurité), texte reproduit avec ses modifications", "https://sitesecurite.com/contenu/_erp/erppe/pe24.php?id=PE24", "consulté le 7 octobre 2026"),
    "pe26": ("Règlement de sécurité, livre III, articles PE 26 et PE 27 (extincteurs, alarme, consignes), texte reproduit avec ses modifications", "https://sitesecurite.com/contenu/_erp/erppe/pe26a27.php?id=PE26", "consulté le 7 octobre 2026"),
    "pe4": ("Règlement de sécurité, livre III, article PE 4 (vérifications techniques), texte reproduit avec ses modifications", "https://sitesecurite.com/contenu/_erp/erppe/pe01a04.php", "consulté le 7 octobre 2026"),
    "dep_reforme": ("Dossier ERP Paris, « Réforme 2026 : la déclaration de conformité remplace-t-elle l'autorisation de travaux ? »", "https://dossier-erp-paris.fr/reforme-2026-autorisation-travaux-erp/", "page du 7 octobre 2026, sources Légifrance et ministère"),
    "r42114b": ("Code de l'urbanisme, article R*421-13 (changements de destination ou de sous-destination)", LF + "LEGIARTI000053561283", "version en vigueur depuis le 22 février 2026"),
    "l4254": ("Code de l'urbanisme, article L425-4 (le permis tient lieu d'autorisation d'exploitation commerciale)", LF + "LEGIARTI000031008816", "version en vigueur"),
    "copro3": ("Loi n° 65-557 du 10 juillet 1965, articles 3, 8 et 9 (parties communes, destination de l'immeuble)", LL + "LEGIARTI000037671848", "versions en vigueur"),
    "a2016e": ("Arrêté du 10 novembre 2016 modifié, article 5 (entrepôt ; cuisine dédiée à la vente en ligne)", LL + "LEGIARTI000047336582", "version en vigueur depuis le 25 mars 2023"),
    "l1259": ("Code de l'environnement, article L125-9 (annexe environnementale au-delà de 2 000 m²)", LF + "LEGIARTI000025118427", "version en vigueur"),
}
