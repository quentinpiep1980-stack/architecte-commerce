# -*- coding: utf-8 -*-
"""Pages éditoriales : projets (situations), activités, zones.

Règle : chaque règle citée renvoie à une clé de SOURCES (content/site.py), lue le 9 octobre 2026.
Les conseils de méthode (parcours client, phasage, budget) sont présentés comme tels, sans chiffre inventé.
"""
DEP = "https://dossier-erp-paris.fr"


def erp_link(path, title, text):
    return f'<a class="ext-link" href="{DEP}{path}" rel="noopener"><b>{title}</b><span>{text}</span></a>'


DEGAGEMENTS = """<div class="table-wrap"><table>
<caption class="sr">Dégagements exigés en 5e catégorie selon l'effectif</caption>
<thead><tr><th scope="col">Effectif (public et personnel sans sortie propre)</th><th scope="col">Dégagements exigés</th></tr></thead>
<tbody>
<tr><td>Moins de 20 personnes</td><td>1 dégagement de 0,90 m</td></tr>
<tr><td>De 20 à 50 personnes</td><td>Soit 1 dégagement de 1,40 m débouchant directement sur l'extérieur, le public n'ayant jamais plus de 25 m à parcourir ; soit 2 dégagements (0,90 m et 0,60 m, ou dégagement accessoire) débouchant directement sur l'extérieur ou sur des locaux différents non en cul-de-sac</td></tr>
<tr><td>De 51 à 100 personnes</td><td>2 dégagements de 0,90 m, ou 1 de 1,40 m et 1 de 0,60 m (ou dégagement accessoire)</td></tr>
<tr><td>De 101 à 200 personnes</td><td>1 dégagement de 1,40 m et 1 de 0,90 m</td></tr>
<tr><td>De 201 à 300 personnes</td><td>2 dégagements de 1,40 m</td></tr>
</tbody></table></div>
<p class="small muted">Règlement de sécurité, article PE 11. Chaque local, niveau et établissement se vérifie sur son propre effectif. Dans un bâtiment existant, une largeur de 0,90 m peut être ramenée à 0,80 m.</p>"""

M2_TABLE = """<div class="table-wrap"><table>
<caption class="sr">Densité d'occupation des magasins de vente (article M 2)</caption>
<thead><tr><th scope="col">Niveau ou cas</th><th scope="col">Effectif théorique du public</th></tr></thead>
<tbody>
<tr><td>Sous-sol, rez-de-chaussée, 1er étage</td><td>1 personne pour 3 m² de surface de vente</td></tr>
<tr><td>2e étage</td><td>1 personne pour 6 m²</td></tr>
<tr><td>Étages supérieurs</td><td>1 personne pour 15 m²</td></tr>
<tr><td>Boutique de moins de 300 m² dans un centre commercial</td><td>1 personne pour 6 m², quel que soit le niveau</td></tr>
<tr><td>Mails d'un centre commercial</td><td>1 personne pour 5 m² de leur surface totale</td></tr>
<tr><td>Magasin à faible densité de public</td><td>1 personne pour 9 m², quel que soit le niveau</td></tr>
<tr><td>Magasin réservé aux professionnels</td><td>Déclaration contrôlée du chef d'établissement</td></tr>
</tbody></table></div>
<p class="small muted">Règlement de sécurité, article M 2, version en vigueur depuis le 1er décembre 2017. L'ancienne règle « 2 personnes par m² sur le tiers de la surface » est abrogée.</p>"""

AUTOS_TABLE = """<div class="table-wrap"><table>
<caption class="sr">Autorisations d'un commerce à Paris et délais d'instruction</caption>
<thead><tr><th scope="col">Ce que vous faites</th><th scope="col">Autorisation</th><th scope="col">Délai</th></tr></thead>
<tbody>
<tr><td>Aménager, cloisonner, modifier un ERP</td><td>Autorisation de travaux (Cerfa n° 13824*04) ; en 5e catégorie sans hébergement, volet accessibilité seul et description succincte à l'autorité de police</td><td>4 mois ; silence vaut accord, sauf dérogation refusée</td></tr>
<tr><td>Modifier la devanture, l'aspect extérieur</td><td>Déclaration préalable</td><td>1 mois ; 2 mois en site patrimonial remarquable ou aux abords d'un monument</td></tr>
<tr><td>Poser ou changer une enseigne</td><td>Autorisation du maire (Cerfa n° 16308*01, en ligne à Paris)</td><td>2 mois ; silence vaut accord</td></tr>
<tr><td>Toucher la façade ou la structure en changeant de destination</td><td>Permis de construire, qui vaut autorisation de travaux</td><td>5 mois pour un ERP</td></tr>
<tr><td>Créer plus de 1 000 m² de surface de vente</td><td>Autorisation d'exploitation commerciale</td><td>Si un permis est nécessaire, il en tient lieu après avis favorable de la CDAC (L425-4)</td></tr>
</tbody></table></div>"""

PAGES = [
    # ================================================================ SITUATIONS
    {
        "path": "/avant-signature-bail-commercial", "kind": "situation", "short": "Avant de signer le bail",
        "teaser": "Le local tient-il votre activité ? Réponse avant l'engagement.",
        "title": "Avant de signer un bail commercial : faire vérifier le local | Kalya",
        "description": "Avant de signer un bail commercial à Paris : destination, PLU, extraction, accessibilité, effectif ERP, façade, copropriété. Ce qu'un architecte vérifie, texte à l'appui.",
        "h1": "Avant de signer un bail commercial, faites lire le local par un architecte",
        "answer": "Un bail commercial est conclu pour neuf ans au moins, avec une faculté de congé du locataire à chaque période triennale, sauf exceptions. Avant de signer, vérifiez que le local tient votre activité : destination prévue au bail, protections du PLU sur la rue, extraction si vous cuisinez, accessibilité de l'entrée, effectif et sorties, façade, enseigne, copropriété. La réponse tient en trois mots : oui, oui sous conditions, ou non.",
        "cta2": ("/diagnostic-local-commercial", "Tester le local en 12 questions"),
        "bullets": [
            "Durée : neuf ans au moins, avec faculté de résiliation à chaque période triennale, sauf exceptions (code de commerce, L145-4).",
            "Activité : la clause de destination fixe ce que vous pouvez exercer ; en changer passe par l'article L145-47 ou L145-48.",
            "Paris : sur les rues protégées du PLU, un rez-de-chaussée commercial ne peut pas devenir un bureau ou une agence (UG.1.4.2).",
            "Restaurant : l'air de cuisine est rejeté à 8 m au moins de toute fenêtre, sauf aménagement empêchant toute reprise d'air pollué (règlement sanitaire de Paris, art. 63-1).",
            "Baux conclus ou renouvelés depuis la loi n° 2026-403 du 26 mai 2026 : dépôt de garantie et autres garanties limités aux loyers d'un trimestre (L145-40).",
        ],
        "sections": [
            ("Ce que la visite doit établir", """<p>Un local se juge sur ce qu'il permet, pas sur ce qu'il montre. La visite d'un architecte vise un verdict : <strong>oui</strong>, <strong>oui sous conditions</strong> (travaux, autorisations, accord du bailleur ou de la copropriété) ou <strong>non pour cette activité</strong>. Neuf points le fondent.</p>
<ol>
<li><strong>Destination et bail.</strong> La clause de destination autorise-t-elle votre activité ? Une activité connexe ou complémentaire se notifie au bailleur, qui a deux mois pour en contester le caractère connexe ou complémentaire (L145-47) ; une activité différente suit la procédure de l'article L145-48.</li>
<li><strong>Protections du PLU.</strong> À Paris, 329 km de linéaires protégés imposent de garder les rez-de-chaussée en commerce, artisanat, restauration ou commerce de gros (ou en activités médicales et paramédicales de proximité). Sur certaines, l'artisanat de proximité ou le commerce culturel est lui-même protégé (voir le <a href="/guides/plu-paris-commerce">guide du PLU de Paris</a>).</li>
<li><strong>Extraction.</strong> Pour cuisiner : hotte débordante, conduit de ventilation unique, indépendant des conduits de fumée, rejet de l'air à 8 m au moins de toute fenêtre ou prise d'air neuf, sauf aménagement empêchant toute reprise d'air pollué (RSD de Paris, art. 63-1 et 130-3). Si aucun tracé n'est réalisable, la cuisine n'est pas faisable en l'état (voir le <a href="/guides/extraction-restaurant-paris">guide de l'extraction</a>).</li>
<li><strong>Puissance électrique et fluides.</strong> Froid, cuisson, climatisation, éclairage : la puissance disponible et la possibilité de l'augmenter se vérifient avant de s'engager, comme les arrivées d'eau et les évacuations.</li>
<li><strong>Accessibilité.</strong> Une marche à l'entrée ne dispense de rien : un ERP de 5e catégorie dans l'existant doit rendre accessible une partie du local donnant accès à l'ensemble des prestations ; une dérogation se motive point par point (code de la construction, R164-2 et R164-3).</li>
<li><strong>Effectif et sorties.</strong> Ouvrir un sous-sol ou un étage au public change l'effectif, donc parfois la catégorie et le nombre de dégagements exigés (règlement de sécurité, PE 2 et PE 11).</li>
<li><strong>Réserve, livraisons, déchets.</strong> Le back-office se dessine aussi : où livrer, où stocker, où sortir les déchets, par où passe le personnel.</li>
<li><strong>Façade et enseigne.</strong> Modifier la devanture demande une déclaration préalable ; poser une enseigne, une autorisation du maire. En site patrimonial remarquable ou aux abords d'un monument historique, l'architecte des Bâtiments de France donne son accord.</li>
<li><strong>Copropriété.</strong> Un conduit en façade ou des travaux sur les parties communes demandent un vote de l'assemblée générale (loi du 10 juillet 1965, art. 25 b) ; le règlement de copropriété peut encadrer l'activité.</li>
</ol>
<p>Le <a href="/diagnostic-local-commercial">diagnostic en 12 questions</a> vous donne une première lecture en deux minutes ; la visite la confirme.</p>"""),
            ("Les documents à demander au bailleur", """<ul>
<li><strong>Le diagnostic de performance énergétique</strong>, joint au bail (code de la construction, L126-29).</li>
<li><strong>L'état des risques</strong>, annexé aux baux commerciaux (code de l'environnement, L125-5).</li>
<li><strong>L'inventaire précis et limitatif des catégories de charges, impôts, taxes et redevances</strong>, que le bail doit comporter, et l'état prévisionnel des travaux des trois années suivantes ainsi que l'état récapitulatif des trois années précédentes, que le bailleur communique à la conclusion du bail puis tous les trois ans (code de commerce, L145-40-2).</li>
<li><strong>L'état des lieux d'entrée</strong>, établi contradictoirement (L145-40-1).</li>
<li><strong>Le dossier technique amiante</strong> pour un immeuble dont le permis est antérieur au 1er juillet 1997 : le propriétaire le tient à la disposition des occupants (code de la santé publique, R1334-29-5).</li>
<li><strong>Le règlement de copropriété</strong> et les derniers procès-verbaux d'assemblée générale, pour lire les clauses d'activité et les travaux votés.</li>
<li><strong>Les plans et les autorisations antérieures</strong> du local, s'ils existent : ils disent ce qui a déjà été accordé.</li>
</ul>"""),
            ("Les clauses qui touchent aux travaux", """<p>La loi fixe quelques bornes ; le reste dépend du bail. Ne peuvent pas être imputées au locataire les grosses réparations de l'article 606 du code civil, ni les dépenses de mise en conformité lorsqu'elles relèvent de ces grosses réparations (code de commerce, R145-35). L'autorisation des travaux du preneur, leur sort en fin de bail et la remise en état se lisent dans les clauses.</p>
<p>Deux nouveautés de la loi n° 2026-403 du 26 mai 2026 : le paiement mensuel du loyer est de droit à la demande du preneur, en l'absence d'arriérés (L145-32-1) ; pour les baux conclus ou renouvelés depuis cette loi, le dépôt de garantie et les autres garanties ne peuvent excéder le montant des loyers dus au titre d'un trimestre (L145-40).</p>
<div class="callout"><strong>Ce que l'architecte apporte à la négociation</strong><p>Les conditions relevées pendant la visite (travaux lourds, autorisations à obtenir, accord de la copropriété) peuvent nourrir la négociation : franchise de loyer, travaux à la charge du bailleur, délai pour obtenir les autorisations. Leur rédaction relève de votre avocat ou de votre notaire.</p></div>"""),
            ("Ce que vous recevez", """<p>Une note de faisabilité, datée et sourcée : votre activité est-elle possible dans ce local, à quelles conditions, avec quels travaux et quelles autorisations, dans quel ordre de délais. Elle se lit en dix minutes et sert de base à la négociation, au budget et au calendrier.</p>
<p>Pour comparer plusieurs locaux, la même grille s'applique à chacun : vous choisissez sur des critères identiques, pas sur un coup de cœur.</p>"""),
        ],
        "faq": [
            {"q": "Combien de temps engage un bail commercial ?", "a": "<p>Neuf ans au moins (code de commerce, L145-4). Le preneur peut en principe donner congé à l'expiration de chaque période triennale, sauf exceptions prévues par la loi (bail de plus de neuf ans, locaux monovalents, bureaux, stockage). Un bail dérogatoire ne peut dépasser trois ans (L145-5).</p>"},
            {"q": "Puis-je ouvrir un restaurant dans une ancienne boutique ?", "a": "<p>Souvent, si le bail l'autorise, si l'extraction est réalisable et si le PLU le permet. En urbanisme, passer de l'artisanat et commerce de détail à la restauration ne change pas de destination ; des travaux sur la façade ou la structure imposent toutefois un permis de construire (R*421-14 c). Le type d'ERP passe de M à N : les travaux d'aménagement relèvent de l'autorisation de travaux (L122-3).</p>"},
            {"q": "Le bailleur doit-il fournir des diagnostics ?", "a": "<p>Oui : le diagnostic de performance énergétique est joint au bail et l'état des risques y est annexé. Le bail comporte aussi un inventaire des charges, et le bailleur communique un état des travaux prévus et réalisés.</p>"},
        ],
        "sources": ["l1454", "l1455", "l14547", "l14548", "plub", "plubreg", "rsd631", "rsd1303", "r1641", "r1642", "r1643", "pe2", "pe11", "r42117", "l58118", "copro25", "l12629", "l1255", "l145401", "l145402", "r133429", "r14535", "l145321", "l14540", "r42114"],
        "related": ["/diagnostic-local-commercial", "/guides/bail-commercial-travaux", "/guides/plu-paris-commerce", "/guides/extraction-restaurant-paris"],
        "service_type": "Vérification de local commercial avant bail",
    },
    {
        "path": "/architecte-boutique", "kind": "activite", "mini": "boutique", "short": "Créer une boutique",
        "teaser": "Du concept à l'ouverture, autorisations comprises.",
        "title": "Architecte boutique à Paris : créer et aménager votre magasin | Kalya",
        "description": "Créer une boutique à Paris : concept, plan de vente, classement ERP type M, devanture conforme au PLU, enseigne, autorisation de travaux. Un architecte du local à l'ouverture.",
        "h1": "Créer une boutique à Paris, du concept à la vitrine allumée",
        "answer": "Une boutique est un ERP de type M. Son effectif se calcule à 1 personne pour 3 m² de surface de vente au rez-de-chaussée, et elle reste en 5e catégorie sous 100 personnes au sous-sol, 100 aux étages et 200 au total. À Paris, la devanture suit le PLU, l'enseigne demande une autorisation et les travaux intérieurs une autorisation de travaux ERP.",
        "cta2": ("/calcul-effectif-erp-commerce", "Calculer l'effectif"),
        "bullets": [
            "Type M : 5e catégorie sous 100 personnes au sous-sol, 100 aux étages et 200 au total (règlement de sécurité, PE 2).",
            "Effectif : 1 personne pour 3 m² de surface de vente au sous-sol, au rez-de-chaussée et au 1er étage (M 2).",
            "Boutique à rez-de-chaussée de moins de 500 m² ne comportant que des circulations principales d'au moins 1,80 m : 1 personne par m² sur le tiers de la surface accessible au public (PE 3).",
            "Devanture de préférence en applique, ou en feuillure avec un retrait limité de 10 à 20 cm ; grilles et coffres à l'intérieur sauf impossibilité (PLU de Paris, UG.2.1.4).",
            "Enseigne : autorisation du maire, demandée en ligne à Paris ; sans réponse sous deux mois, elle est acquise (R581-13).",
        ],
        "sections": [
            ("Du concept au plan de vente", """<p>Une boutique ne se dessine pas d'abord : elle se comprend. Qui entre, pour quelle mission d'achat (découvrir, comparer, être conseillé, retirer une commande), avec quelle offre et quel panier ? Le plan découle de ces réponses.</p>
<ul>
<li><strong>Le seuil.</strong> Les premiers mètres après la porte servent à ralentir et à s'orienter : les surcharger fait fuir.</li>
<li><strong>Les lignes de vue.</strong> Depuis l'entrée, on doit comprendre ce qui est vendu, pour qui et à quel prix.</li>
<li><strong>La circulation.</strong> Intuitive, accessible, commerciale, et compatible avec les dégagements exigés par le règlement.</li>
<li><strong>La caisse et le service.</strong> Visibles sans encombrer, dimensionnées pour les pics, reliées au retrait des commandes en ligne si vous en faites.</li>
<li><strong>Le back-office.</strong> Réserve, réception, personnel, déchets : un arrière mal pensé dégrade la vente chaque jour.</li>
</ul>
<p>Le concept se traduit ensuite en matériaux, lumière, mobilier et signalétique, choisis aussi pour leur entretien et leur remplacement : qui nettoie, qui répare, à quel coût.</p>"""),
            ("Le classement ERP d'une boutique", f"""<p>Dès qu'elle reçoit du public, une boutique est un établissement recevant du public de <strong>type M</strong> (magasins de vente, centres commerciaux). Sa catégorie dépend de l'effectif du public, calculé selon l'article M 2 :</p>
{M2_TABLE}
<p>Elle reste en <strong>5e catégorie</strong> tant que l'effectif est inférieur à 100 personnes au sous-sol, 100 aux étages et 200 pour l'ensemble (PE 2). Pour une boutique en rez-de-chaussée de moins de 500 m² ne comportant que des circulations principales d'au moins 1,80 m, l'effectif se calcule à 1 personne par m² sur le tiers de la surface accessible au public (PE 3). Le personnel ne compte pas pour classer en 5e catégorie.</p>
<p>Faites le calcul avec le <a href="/calcul-effectif-erp-commerce">calculateur d'effectif</a>.</p>
{erp_link('/erp-boutique-commerce-paris/', 'Boutique ou magasin à Paris : classement ERP et dossier', 'Le détail du type M, des boutiques voisines non isolées et des stockages, sur dossier-erp-paris.fr.')}"""),
            ("Les autorisations, dossier par dossier", f"""{AUTOS_TABLE}
<p>Ces dossiers sont distincts : une déclaration préalable ne vaut pas autorisation de travaux, alors qu'un permis de construire en tient lieu lorsque l'autorité compétente a donné son accord (code de l'urbanisme, R*425-15). Déposés ensemble, ils s'instruisent en parallèle. Le détail figure dans le <a href="/guides/autorisations-travaux-commerce">guide des autorisations</a>.</p>"""),
            ("La devanture selon le PLU de Paris", """<p>Le règlement du PLU bioclimatique consacre un article aux devantures commerciales (UG.2.1.4). Il demande notamment :</p>
<ul>
<li>une devanture intégrée « de façon harmonieuse au cadre bâti et à la composition architecturale des façades » ;</li>
<li>pas de comptoir ouvert directement sur la voie sans devanture ;</li>
<li>une devanture de préférence dans le plan de la façade : en applique, ou en feuillure avec un retrait limité de 10 à 20 cm ;</li>
<li>un vitrage « le plus clair possible et non réfléchissant » ;</li>
<li>des coffres et grilles de fermeture à l'intérieur, en retrait des vitrines, sauf impossibilité ;</li>
<li>le maintien ou la restitution d'une devanture d'intérêt historique ou architectural, qui peuvent être exigés.</li>
</ul>
<p>Voir la page <a href="/vitrine-et-devanture-commerce">vitrine et devanture</a>.</p>"""),
            ("Le budget, structuré avant d'être chiffré", """<p>Un budget de boutique se construit par enveloppes : travaux, mobilier et agencement, enseigne et signalétique, éclairage, sécurité et accessibilité, informatique et caisse, honoraires et autorisations, préouverture, aléas. Chaque enveloppe a sa maturité : un ordre de grandeur avant le bail, une estimation détaillée sur plans, un prix consulté auprès des entreprises, un prix contracté.</p>
<p>Ce site ne publie pas de prix au mètre carré : ils dépendent trop du local, de l'état existant et du concept pour être honnêtes hors étude. Le <a href="/guides/budget-renovation-commerce">guide du budget</a> détaille la méthode.</p>"""),
        ],
        "faq": [
            {"q": "Ma boutique fait moins de 300 m² : est-elle en 5e catégorie ?", "a": "<p>On ne peut pas le conclure à la surface seule. La catégorie dépend de l'effectif du public calculé selon l'article M 2, comparé aux seuils de PE 2 : moins de 100 personnes au sous-sol, 100 aux étages, 200 au total.</p>"},
            {"q": "Faut-il un permis de construire pour ouvrir une boutique ?", "a": "<p>Pas en général. Un permis est exigé notamment lorsque des travaux modifient les structures porteuses ou la façade et s'accompagnent d'un changement de destination (R*421-14 c). Les aménagements intérieurs relèvent de l'autorisation de travaux ERP ; la devanture, d'une déclaration préalable.</p>"},
            {"q": "Peut-on poser une grille de fermeture à l'extérieur ?", "a": "<p>À Paris, le PLU demande que coffres et grilles soient implantés à l'intérieur, en retrait des vitrines, sauf impossibilité technique ou architecturale, et que la protection maintienne les transparences (UG.2.1.4).</p>"},
        ],
        "sources": ["m2", "pe2", "pe3", "gn1", "l1223", "r12216", "cerfa13824", "r42117", "r42323", "r42324", "r42114", "r42515", "r42328", "l58118", "r58113", "cerfa16308", "parisenseignes", "plubreg", "l7521"],
        "related": ["/calcul-effectif-erp-commerce", "/vitrine-et-devanture-commerce", "/guides/autorisations-travaux-commerce", DEP + "/erp-boutique-commerce-paris/"],
        "service_type": "Conception et aménagement de boutique",
    },
    {
        "path": "/amenagement-local-commercial", "kind": "situation", "short": "Aménager un local commercial",
        "teaser": "Plan, réserve, caisse, réseaux : un local qui tourne.",
        "title": "Aménagement de local commercial à Paris : plan, ERP, accessibilité | Kalya",
        "description": "Aménager un local commercial : relevé de l'existant, zones de vente et réserve, dégagements selon l'effectif, accessibilité dans le bâti existant, autorisation de travaux ERP.",
        "h1": "Aménager un local commercial : faire tenir l'activité dans des murs existants",
        "answer": "Aménager un local commercial, c'est faire entrer un parcours client, une réserve, des réseaux et des règles dans des murs qui existent déjà. Le plan se dessine avec l'effectif, les sorties et l'accessibilité dès l'esquisse. Les travaux qui aménagent ou modifient un ERP demandent une autorisation de travaux, instruite en quatre mois.",
        "bullets": [
            "Les sorties dépendent de l'effectif : un dégagement de 0,90 m sous 20 personnes, deux de 1,40 m de 201 à 300 (PE 11).",
            "Un commerce ouvert dans un bâtiment existant relève des règles d'accessibilité des ERP existants (R164-1 et R164-2, arrêté du 8 décembre 2014).",
            "Une dérogation d'accessibilité se motive point par point ; la petite surface ne figure pas parmi les motifs prévus (L164-3, R164-3).",
            "Autorisation de travaux : quatre mois d'instruction ; sans réponse, elle est en principe accordée (R122-16, R122-21).",
            "Tout ERP, 5e catégorie comprise, tient un registre public d'accessibilité (R164-6).",
        ],
        "sections": [
            ("Partir d'un relevé, pas d'une intuition", """<p>Le projet commence par un relevé précis du local : surfaces, hauteurs sous plafond et sous poutres, niveaux et marches, structure apparente, état des sols et des murs, arrivées d'eau, évacuations, tableau électrique, ventilation, gaines, accès de service. C'est ce relevé qui dit ce qui coûte cher (déplacer une évacuation, créer une gaine) et ce qui est gratuit (profiter d'une hauteur, d'une vitrine d'angle).</p>"""),
            ("Le zoning : la vente devant, le service derrière", """<p>Un local commercial fonctionne en deux mondes reliés :</p>
<ul>
<li><strong>La salle</strong> : seuil, présentation, essayage ou dégustation, conseil, caisse, retrait de commande.</li>
<li><strong>L'arrière</strong> : réserve, réception des livraisons, préparation, vestiaire et sanitaires du personnel, déchets, local technique.</li>
</ul>
<p>La distance entre la réserve et la vente, la largeur des passages de réassort et la place de la caisse se décident sur plan, avec l'exploitant : c'est lui qui vivra le local tous les jours.</p>"""),
            ("Dégagements : l'effectif décide", f"""<p>En 5e catégorie, le nombre et la largeur des sorties découlent de l'effectif, en comptant le personnel qui ne dispose pas de sorties propres :</p>
{DEGAGEMENTS}
<p>L'effectif lui-même se calcule selon le type d'activité : voir le <a href="/calcul-effectif-erp-commerce">calculateur</a> et le <a href="/guides/erp-commerce-categorie-effectif">guide du classement ERP</a>.</p>"""),
            ("Accessibilité dans le bâti existant", """<p>Un commerce qui s'installe dans un bâtiment existant n'est pas, pour ce seul motif, une construction neuve : il relève des articles R164-1 à R164-6 du code de la construction et de l'arrêté du 8 décembre 2014. En 5e catégorie, l'obligation porte sur une partie du local, la plus proche possible de l'entrée principale, qui doit donner accès à l'ensemble des prestations (R164-2) ; certaines prestations peuvent être délivrées par des mesures de substitution.</p>
<p>Une dérogation est possible pour un point identifié, dans des cas prévus par les textes : impossibilité technique, conservation du patrimoine, disproportion manifeste, refus de la copropriété dans les conditions fixées. Elle se motive et se justifie dans le dossier. Le <a href="/guides/accessibilite-commerce">guide de l'accessibilité</a> détaille la démarche.</p>"""),
            ("L'autorisation de travaux", """<p>Les travaux qui conduisent à créer, aménager ou modifier un ERP ne peuvent être exécutés qu'après autorisation (code de la construction, L122-3). La demande se fait sur le Cerfa n° 13824*04, avec plans, notice d'accessibilité et, lorsque le volet incendie est demandé, notice de sécurité. Le délai d'instruction est de quatre mois à compter d'un dossier complet ; à défaut de décision notifiée, l'autorisation est en principe accordée (R122-16, R122-21).</p>
<p>Pour un ERP de 5e catégorie sans locaux d'hébergement du public, la demande d'autorisation n'est pas exigée au titre de l'incendie : une description succincte des travaux envisagés est communiquée, pour information, à l'autorité de police, et les règles de sécurité restent applicables ; l'accessibilité, elle, est instruite (R122-7, II).</p>"""),
        ],
        "faq": [
            {"q": "Faut-il une autorisation pour aménager l'intérieur d'une boutique ?", "a": "<p>En principe oui, dès lors que les travaux aménagent ou modifient un établissement recevant du public : c'est l'autorisation de travaux de l'article L122-3 du code de la construction, instruite en quatre mois. Elle vérifie l'accessibilité lorsque les travaux y touchent ; en 5e catégorie sans hébergement du public, elle ne porte pas sur l'incendie, et une description succincte des travaux est communiquée à l'autorité de police (R122-7, II).</p>"},
            {"q": "Mon local a une marche à l'entrée : est-ce rédhibitoire ?", "a": "<p>Non, mais c'est un point à traiter dans le dossier : adaptation de l'entrée, solution d'effet équivalent ou dérogation motivée. Une rampe sur le trottoir relève en principe d'une autorisation d'occupation du domaine public.</p>"},
        ],
        "sources": ["pe11", "pe2", "pe3", "m2", "r1641", "r1642", "a2014", "r1643", "r1646", "a2017reg", "l1223", "r12216", "r12221", "r1227", "cerfa13824"],
        "related": ["/calcul-effectif-erp-commerce", "/guides/accessibilite-commerce", "/guides/erp-commerce-categorie-effectif", DEP + "/autorisation-travaux-erp-paris/"],
        "service_type": "Aménagement de local commercial",
    },
    {
        "path": "/renovation-magasin", "kind": "situation", "short": "Rénover un magasin",
        "teaser": "Remettre à niveau sans perdre la clientèle.",
        "title": "Rénovation de magasin à Paris : diagnostic, autorisations, phasage | Kalya",
        "description": "Rénover un magasin : diagnostiquer avant de changer, ce que la rénovation déclenche (autorisation de travaux, devanture, enseigne, accessibilité), phaser pour rester ouvert.",
        "h1": "Rénover un magasin : décider ce qui reste, ce qui change, et pourquoi",
        "answer": "Rénover un magasin commence par un diagnostic : une baisse des ventes vient rarement du seul décor. Ensuite, toute modification d'un ERP existant relève d'une autorisation de travaux ; la devanture, d'une déclaration préalable ; une nouvelle enseigne, d'une autorisation du maire. La rénovation est aussi le moment de remettre l'accessibilité à niveau.",
        "bullets": [
            "Diagnostiquer d'abord : fréquentation, transformation, panier, ruptures, effectifs aux heures de pointe.",
            "Modifier un ERP existant : autorisation de travaux, quatre mois (code de la construction, L122-3 et R122-16).",
            "Changer la devanture : déclaration préalable, un mois ou deux selon le secteur (R*421-17, R423-24).",
            "Nouvelle enseigne : nouvelle autorisation du maire (code de l'environnement, L581-18).",
            "Accessibilité : registre public à mettre à jour (R164-6).",
        ],
        "sections": [
            ("Diagnostiquer avant de rénover", """<p>Un magasin qui vend moins peut souffrir d'une baisse de fréquentation, d'une moins bonne transformation, d'un panier plus faible, de ruptures, d'un effectif insuffisant aux heures de pointe, d'un assortiment mal lu, ou d'un marché local qui a changé. Le décor n'est qu'une cause parmi d'autres. Avant de dessiner, on regarde les chiffres de l'exploitant et le magasin en fonctionnement.</p>
<p>La rénovation se décide ensuite en trois colonnes : <strong>ce qui reste</strong> (ce qui marche et fait l'identité), <strong>ce qui change</strong> (ce qui freine la vente ou l'exploitation), et <strong>l'effet attendu</strong> de chaque changement.</p>"""),
            ("Ce que la rénovation déclenche", f"""{AUTOS_TABLE}
<p>Une rénovation qui modifie le cloisonnement, les sorties ou les sanitaires ouverts au public touche l'ERP : elle passe par l'autorisation de travaux pour l'accessibilité et, hors 5e catégorie sans hébergement du public, pour la sécurité incendie. En 5e catégorie sans hébergement, une description succincte des travaux est communiquée à l'autorité de police et les règles de sécurité restent applicables (R122-7, II). Un simple rafraîchissement (peinture, mobilier libre) n'a pas cet effet, mais les règles du règlement de sécurité sur les matériaux d'aménagement restent à respecter.</p>"""),
            ("L'occasion de remettre l'accessibilité à niveau", """<p>Les travaux sont le bon moment pour traiter l'accessibilité : entrée, circulation, caisse, cabines, sanitaires ouverts au public. Les règles applicables sont celles des ERP existants (R164-1, arrêté du 8 décembre 2014). Le registre public d'accessibilité, obligatoire pour tout ERP, se met à jour à la fin du chantier (R164-6).</p>"""),
            ("Rester ouvert pendant les travaux", """<p>Une rénovation peut se mener magasin ouvert, par zones, avec les travaux bruyants hors des heures d'ouverture et des sorties maintenues à chaque phase. Voir la page <a href="/renovation-commerce-site-occupe">travaux sans fermer</a>.</p>"""),
        ],
        "faq": [
            {"q": "Repeindre et changer le mobilier demande-t-il une autorisation ?", "a": "<p>En général non au titre de l'autorisation de travaux, tant que l'aménagement n'a d'incidence ni sur l'accessibilité ni sur la sécurité incendie (cloisons, sorties, sanitaires, installations de sécurité) ; en 5e catégorie sans hébergement, une modification des installations de sécurité donne lieu à une description succincte communiquée à l'autorité de police (R122-7, II). Les matériaux posés restent soumis aux règles du règlement de sécurité.</p>"},
            {"q": "Changer seulement l'enseigne suffit-il à déclencher une démarche ?", "a": "<p>Oui : à Paris, toute enseigne est soumise à autorisation du maire, y compris son remplacement (code de l'environnement, L581-18).</p>"},
        ],
        "sources": ["l1223", "r12216", "cerfa13824", "r42117", "r42323", "r42324", "l58118", "r58113", "r1641", "r1642", "a2014", "r1646"],
        "related": ["/renovation-commerce-site-occupe", "/vitrine-et-devanture-commerce", "/guides/budget-renovation-commerce", "/guides/accessibilite-commerce"],
        "service_type": "Rénovation de magasin",
    },
    {
        "path": "/renovation-commerce-site-occupe", "kind": "situation", "short": "Travaux sans fermer",
        "teaser": "Phasage, nuit, week-end : rester ouvert.",
        "title": "Travaux dans un commerce ouvert : phasage et sécurité du public | Kalya",
        "description": "Rénover un commerce sans fermer : phasage par zones, travaux hors horaires, sorties maintenues, protection du public, coordination avec l'exploitant et la copropriété.",
        "h1": "Travaux sans fermer : rénover un commerce qui reste ouvert",
        "answer": "Rester ouvert pendant les travaux est possible si le chantier est conçu pour : phasage par zones, travaux bruyants hors des heures d'ouverture, cheminements et sorties maintenus à chaque phase, protections, nettoyage. Dans un ERP, les dégagements exigés pour l'effectif admis doivent rester disponibles pendant tout le chantier.",
        "bullets": [
            "Les dégagements exigés par l'effectif admis (règlement de sécurité, PE 11) doivent rester disponibles à chaque phase : sinon, l'effectif admis baisse.",
            "Réduire temporairement la surface ouverte réduit l'effectif admissible : à intégrer au phasage.",
            "Les travaux qui modifient l'ERP restent soumis à autorisation, même phasés (L122-3).",
            "Le planning se construit avec l'exploitant : jours forts, livraisons, inventaires, soldes.",
        ],
        "sections": [
            ("Concevoir le chantier autour de la vente", """<p>Le phasage se dessine sur plan, avant de consulter les entreprises : quelles zones ferment, dans quel ordre, combien de temps, par où passent le public, le personnel et les ouvriers. Chaque phase a son plan : surfaces ouvertes, cloisons provisoires, sorties, protections, stockage du chantier.</p>
<ul>
<li><strong>Travaux bruyants et poussiéreux</strong> : hors des heures d'ouverture, la nuit ou le jour de fermeture, dans le respect du voisinage et du règlement de copropriété.</li>
<li><strong>Livraisons du chantier</strong> : à des heures qui ne croisent pas celles du magasin.</li>
<li><strong>Nettoyage</strong> : chaque matin avant l'ouverture, compris dans les marchés.</li>
</ul>"""),
            ("La sécurité du public pendant les travaux", f"""<p>Le public admis doit toujours disposer des dégagements que son effectif exige :</p>
{DEGAGEMENTS}
<p>Si une sortie est neutralisée par une phase, l'effectif admis doit baisser en conséquence, ou la phase être réorganisée. Les installations de sécurité (éclairage de sécurité, alarme, extincteurs) restent en service.</p>"""),
            ("Coordonner les acteurs", """<p>L'exploitant, le bailleur, le syndic, les entreprises et, le cas échéant, le coordonnateur de sécurité et de protection de la santé se mettent d'accord sur un planning commun. L'architecte tient ce planning, prépare les marchés en conséquence (clauses d'horaires, de nettoyage, de pénalités) et vérifie leur respect en visite de chantier.</p>"""),
        ],
        "sources": ["pe11", "pe2", "l1223"],
        "related": ["/renovation-magasin", "/amenagement-local-commercial", "/guides/calendrier-ouverture-magasin"],
        "service_type": "Travaux en site occupé",
    },
    {
        "path": "/vitrine-et-devanture-commerce", "kind": "situation", "short": "Vitrine et devanture",
        "teaser": "Façade, enseigne, store : ce que Paris autorise.",
        "title": "Devanture, vitrine et enseigne à Paris : règles et autorisations | Kalya",
        "description": "Devanture de commerce à Paris : règles du PLU (UG.2.1.4), déclaration préalable, accord de l'ABF, enseigne (autorisation, Cerfa 16308, 2 mois), extinction nocturne, terrasses.",
        "h1": "Vitrine et devanture à Paris : ce que la ville autorise, et comment",
        "answer": "À Paris, une devanture s'intègre à la façade : de préférence en applique, ou en feuillure avec un retrait limité de 10 à 20 cm, vitrage le plus clair possible, grilles à l'intérieur sauf impossibilité (PLU, UG.2.1.4). La modifier demande une déclaration préalable, instruite en un mois, deux en site patrimonial remarquable ou aux abords d'un monument. L'enseigne demande une autorisation du maire, accordée tacitement après deux mois.",
        "bullets": [
            "PLU de Paris : pas de comptoir ouvert sur la voie sans devanture ; vitrage clair et non réfléchissant (UG.2.1.4).",
            "Déclaration préalable : 1 mois ; 2 mois en site patrimonial remarquable ou aux abords d'un monument historique (R*423-23, R423-24).",
            "Abords et sites patrimoniaux : la décision vaut autorisation patrimoniale si l'architecte des Bâtiments de France a donné son accord (R*425-1, R*425-2).",
            "Enseigne : Cerfa n° 16308*01, demande en ligne à Paris depuis le 1er octobre 2025, deux mois (R581-13).",
            "Enseignes lumineuses éteintes entre 1 h et 6 h lorsque l'activité a cessé ; clignotement interdit sauf pharmacie et urgences (R581-59).",
        ],
        "sections": [
            ("Ce que demande le PLU de Paris", """<p>L'article UG.2.1.4 du règlement du PLU bioclimatique fixe les principes des devantures commerciales :</p>
<ul>
<li>« Les devantures participent à l'animation visuelle et commerciale de la ville. Elles doivent s'intégrer de façon harmonieuse au cadre bâti et à la composition architecturale des façades. »</li>
<li>Les locaux ouverts directement sur la voie, de type comptoir sans devanture, sont proscrits.</li>
<li>Les devantures se placent préférentiellement dans le plan de la façade : en saillie pour une devanture en applique, en retrait limité de 10 à 20 cm pour une devanture en feuillure.</li>
<li>Une devanture d'intérêt historique ou architectural peut devoir être maintenue, restituée ou refaite.</li>
<li>Le vitrage est le plus clair possible et non réfléchissant.</li>
<li>Les devantures ne masquent ni baies, ni porches, ni moulurations, ni consoles de balcons.</li>
<li>Coffres et grilles de fermeture s'implantent à l'intérieur, en retrait des vitrines, sauf impossibilité ; la protection maintient les transparences.</li>
</ul>
<p>L'article UG.2.1.3 ajoute que les rez-de-chaussée sur rue présentent des façades ouvertes, en évitant les locaux aveugles en bordure de voie.</p>"""),
            ("La déclaration préalable", """<p>Les travaux qui modifient l'aspect extérieur d'un bâtiment existant sont soumis à déclaration préalable (code de l'urbanisme, R*421-17 a). Le délai d'instruction est d'un mois (R*423-23), majoré d'un mois en site patrimonial remarquable ou aux abords d'un monument historique (R423-24). Dans ces secteurs, la décision vaut autorisation au titre du patrimoine si l'architecte des Bâtiments de France a donné son accord, le cas échéant avec prescriptions (R*425-1, R*425-2).</p>
<p>Paris compte deux sites patrimoniaux remarquables : le Marais et une partie du 7e arrondissement. Dans le périmètre d'un plan de sauvegarde, une déclaration préalable vise aussi les travaux qui modifient les éléments d'architecture et de décoration protégés, extérieurs ou intérieurs (R*421-17 c).</p>"""),
            ("L'enseigne, une autorisation à part", """<p>Paris est couverte par un règlement local de publicité : l'installation de toute enseigne y est soumise à autorisation (code de l'environnement, L581-18). Depuis le 1er juillet 2026, la procédure est réécrite :</p>
<ul>
<li>la demande est présentée par l'exploitant de l'activité signalée, sur le Cerfa n° 16308*01 ;</li>
<li>à Paris, elle se dépose uniquement en ligne, sur le téléservice de la Ville, depuis le 1er octobre 2025 ;</li>
<li>le dossier montre l'enseigne en situation, avec et sans le dispositif ;</li>
<li>l'autorité statue dans les deux mois suivant la réception d'un dossier complet ; sans notification, l'autorisation est réputée accordée (R581-13) ; lorsque l'accord de l'architecte des Bâtiments de France est requis (R581-16-1), ce texte ne prévoit pas de délai plus long.</li>
</ul>
<p>Les enseignes lumineuses sont éteintes entre 1 heure et 6 heures lorsque l'activité a cessé ; les enseignes clignotantes sont interdites, sauf pour les pharmacies et les services d'urgence (R581-59). Le <a href="/guides/enseigne-paris">guide de l'enseigne</a> détaille le dossier.</p>"""),
            ("Store, terrasse, étalage", """<p>Un store banne ou une marquise modifie l'aspect extérieur : il relève en principe de la déclaration préalable de la devanture. Une terrasse ou un étalage sur le trottoir relève d'une autorisation d'occupation du domaine public, précaire et révocable, délivrée par la Ville selon le règlement des étalages et terrasses applicable depuis le 1er juillet 2021 ; les terrasses estivales vont du 1er avril au 31 octobre.</p>"""),
        ],
        "faq": [
            {"q": "Puis-je repeindre ma devanture sans démarche ?", "a": "<p>Changer la couleur modifie l'aspect extérieur : c'est en principe une déclaration préalable (R*421-17 a). En site patrimonial remarquable ou aux abords d'un monument, l'accord de l'architecte des Bâtiments de France est requis.</p>"},
            {"q": "Combien de temps pour une enseigne à Paris ?", "a": "<p>Deux mois à compter d'un dossier complet ; sans réponse, l'autorisation est acquise (R581-13). La demande se fait en ligne sur le téléservice de la Ville.</p>"},
            {"q": "Mon enseigne peut-elle rester allumée la nuit ?", "a": "<p>Non, si l'activité a cessé : les enseignes lumineuses sont éteintes entre 1 h et 6 h (R581-59). Si l'activité cesse ou commence entre minuit et 7 h, l'enseigne s'éteint au plus tard une heure après la fermeture et peut s'allumer une heure avant l'ouverture.</p>"},
        ],
        "sources": ["plubreg", "r42117", "r42323", "r42324", "r4251", "r4252", "spr", "l58118", "r58113", "cerfa16308", "parisenseignes", "r58159", "terrasses"],
        "related": ["/guides/enseigne-paris", "/guides/plu-paris-commerce", "/architecte-boutique", "/guides/autorisations-travaux-commerce"],
        "service_type": "Conception de devanture et dossiers de façade",
    },
    {
        "path": "/concept-et-deploiement-enseigne", "kind": "situation", "short": "Déployer une enseigne",
        "teaser": "Un concept, des locaux tous différents.",
        "title": "Déploiement d'enseigne et concept retail : architecte réseau | Kalya",
        "description": "Déployer une enseigne en Île-de-France : traduire le concept en manuel, adapter chaque local sans copier-coller, vérifier PLU, ERP, copropriété et façade adresse par adresse.",
        "h1": "Déployer une enseigne : un concept reconnaissable, des locaux tous différents",
        "answer": "Déployer une enseigne, c'est écrire des règles assez fermes pour être reconnues et assez souples pour entrer dans des locaux tous différents. Le concept se traduit en manuel : codes fixes, éléments adaptables, variantes de format. Chaque local reste un projet : PLU, ERP, copropriété, façade et enseigne se vérifient adresse par adresse.",
        "bullets": [
            "Le concept n'est pas un décor : offre, parcours, service, stock, opérations et économie du point de vente.",
            "Un manuel de déploiement fixe ce qui est imposé, ce qui s'adapte et qui valide les écarts.",
            "À Paris, le délai de déclaration préalable passe de 1 à 2 mois en site patrimonial ou aux abords (R423-24).",
            "Chaque commune dotée d'un règlement local de publicité soumet l'enseigne à autorisation (L581-18).",
            "Au-delà de 1 000 m² de surface de vente : autorisation d'exploitation commerciale (L752-1).",
        ],
        "sections": [
            ("Le concept n'est pas un décor", """<p>Un concept de magasin traduit une promesse : quel client, quelle mission d'achat, quelle offre, quel service, quel modèle d'exploitation, quelle économie. Les matériaux et la lumière viennent après. Un concept qui ne tient pas l'exploitation (réassort, caisse, réserve, nettoyage) ne se déploie pas : il se répare à chaque ouverture.</p>"""),
            ("Le manuel de déploiement", """<p>Le manuel est l'outil qui permet d'ouvrir vite sans tout redessiner :</p>
<ul>
<li><strong>codes fixes</strong> : ce qui fait reconnaître l'enseigne partout ;</li>
<li><strong>éléments adaptables</strong> : modules de mobilier, gammes de matériaux, variantes d'éclairage ;</li>
<li><strong>variantes de format</strong> : grand format, format compact, corner ;</li>
<li><strong>plans-types et détails</strong>, avec leurs tolérances et les alternatives approuvées ;</li>
<li><strong>règles techniques</strong> : réseaux, back-office, sécurité, accessibilité ;</li>
<li><strong>gouvernance</strong> : qui valide le site, le plan, la façade, le budget, les écarts, l'ouverture.</li>
</ul>"""),
            ("Chaque local reste un projet", """<p>Le copier-coller échoue sur les murs réels : une façade d'immeuble ancien, un linéaire protégé, une copropriété restrictive, une extraction impossible, un sous-sol ouvert au public qui change la catégorie. Chaque adresse fait donc l'objet d'une vérification avant engagement, avec la même grille, puis d'une adaptation du concept sans perte d'identité.</p>
<p>À Paris, ce qui varie d'une adresse à l'autre tient en quatre questions : la rue est-elle protégée au PLU ? le bâtiment est-il en site patrimonial remarquable ou aux abords d'un monument ? que dit le règlement de copropriété ? que permet la devanture existante ?</p>"""),
            ("Grandes surfaces et centres commerciaux", """<p>La création d'un magasin de plus de 1 000 m² de surface de vente est soumise à autorisation d'exploitation commerciale (code de commerce, L752-1) ; lorsqu'un permis de construire est nécessaire, il en tient lieu après avis favorable de la commission départementale d'aménagement commercial (code de l'urbanisme, L425-4). Dans un centre commercial, une boutique de moins de 300 m² compte 1 personne pour 6 m² quel que soit le niveau, et les mails 1 personne pour 5 m² (règlement de sécurité, M 2).</p>"""),
        ],
        "sources": ["plubreg", "r42324", "spr", "l58118", "l7521", "l4254", "m2", "copro25"],
        "related": ["/architecte-commerce-ile-de-france", "/avant-signature-bail-commercial", "/guides/plu-paris-commerce", "/architecte-showroom"],
        "service_type": "Conception et déploiement de concept retail",
    },

    # ================================================================ ACTIVITÉS
    {
        "path": "/architecte-restaurant", "kind": "activite", "mini": "restaurant", "short": "Restaurant, bar, café",
        "teaser": "Type N, cuisine, extraction, terrasse.",
        "title": "Architecte restaurant à Paris : cuisine, extraction, ERP type N | Kalya",
        "description": "Ouvrir un restaurant, un bar ou un café à Paris : effectif ERP type N, extraction (RSD de Paris), hygiène de la cuisine, bac à graisses, licences, sons amplifiés, terrasse.",
        "h1": "Architecte restaurant à Paris : la salle se voit, la cuisine décide",
        "answer": "Un restaurant est un ERP de type N : il reste en 5e catégorie sous 100 personnes au sous-sol, 200 aux étages et 200 au total. Le projet se joue sur ce que la salle ne montre pas : l'extraction (à Paris, air de cuisine rejeté à 8 m au moins de toute fenêtre, sauf aménagement empêchant toute reprise d'air pollué), l'organisation hygiénique de la cuisine et le prétraitement des graisses.",
        "cta2": ("/calcul-effectif-erp-commerce", "Calculer l'effectif"),
        "bullets": [
            "Places assises : nombre déclaré, dans la limite d'1 personne pour 2 m² ; sans déclaration, 1 par m² ; debout, 2 par m² ; files d'attente, 3 par m² (N 2).",
            "Cuisine : hotte débordante, conduit unique indépendant des conduits de fumée, filtres et conduits nettoyés au moins une fois par mois (RSD de Paris, art. 130-3).",
            "Air extrait rejeté à 8 m au moins de toute fenêtre ou prise d'air neuf, sauf aménagement empêchant toute reprise d'air pollué (RSD de Paris, art. 63-1).",
            "Eaux grasses : dispositif de prétraitement obligatoire pour les restaurants à Paris (règlement d'assainissement, art. 17.1).",
            "Au moins une personne formée à l'hygiène alimentaire en restauration commerciale, ou justifiant de trois ans d'expérience comme gestionnaire ou exploitant (code rural, L233-4 et D233-11).",
        ],
        "sections": [
            ("Effectif et catégorie", f"""<p>L'effectif d'un restaurant se calcule zone par zone, sur la surface diminuée des estrades et des aménagements fixes autres que les tables et les sièges (règlement de sécurité, N 2) :</p>
<div class="table-wrap"><table><caption class="sr">Densité d'occupation des restaurants (article N 2)</caption>
<thead><tr><th scope="col">Zone</th><th scope="col">Effectif théorique</th></tr></thead>
<tbody>
<tr><td>Restauration assise, sur déclaration</td><td>Nombre de places déclaré, dans la limite d'1 personne pour 2 m²</td></tr>
<tr><td>Restauration assise, sans déclaration</td><td>1 personne par m²</td></tr>
<tr><td>Restauration debout</td><td>2 personnes par m²</td></tr>
<tr><td>Files d'attente</td><td>3 personnes par m²</td></tr>
</tbody></table></div>
<p>Le restaurant reste en 5e catégorie sous 100 personnes au sous-sol, 200 aux étages et 200 au total (PE 2). Aucune densité propre à la restauration rapide n'existe : on applique la règle de chaque zone.</p>
{erp_link('/erp-restaurant-bar-paris/', 'Restaurant ou bar à Paris : classement ERP et dossier (type N)', 'Cuisine, gaz, ventilation et vérifications périodiques, sur dossier-erp-paris.fr.')}"""),
            ("Extraction : la question à trancher avant le bail", """<p>Le règlement sanitaire départemental de Paris classe les cuisines parmi les locaux à pollution spécifique : l'air extrait est rejeté sans recyclage, « à au moins huit mètres de toute fenêtre, de toute prise d'air neuf », de tout débouché de conduit de fumée et de tout conduit de ventilation, « sauf aménagements tels qu'une reprise d'air pollué ne soit pas possible » (art. 63-1). Les fourneaux sont équipés d'une hotte débordante, raccordée à un conduit de ventilation unique, indépendant des conduits de fumée ; conduits et filtres à graisse sont nettoyés au moins une fois par mois (art. 130-3, applicable aux restaurants par l'art. 152-2).</p>
<p>Les articles du RSD consultés ne fixent pas de hauteur de rejet en toiture : ils imposent la distance aux ouvertures et l'absence de gêne pour le voisinage. Le tracé du conduit (cour, gaine, façade arrière, toiture) se vérifie avant de signer, avec la copropriété : un conduit sur les parties communes demande un vote de l'assemblée générale (loi du 10 juillet 1965, art. 25 b). Le <a href="/guides/extraction-restaurant-paris">guide de l'extraction</a> détaille la démarche.</p>"""),
            ("Une cuisine qui sépare les opérations", """<p>Le règlement (CE) n° 852/2004 impose des locaux conçus pour prévenir la contamination « entre et durant les opérations » (annexe II). La « marche en avant » n'est pas un article : c'est la méthode d'organisation qui répond à cette exigence. Concrètement : réception et stockage, préparation, cuisson, dressage, plonge et déchets s'enchaînent sans croiser le propre et le sale.</p>
<ul>
<li>Déclaration de l'établissement avant l'ouverture (code rural, R233-4 ; Cerfa n° 13984).</li>
<li>Au moins une personne justifiant d'une formation en hygiène alimentaire adaptée à la restauration commerciale, ou de trois ans d'expérience comme gestionnaire ou exploitant (code rural, L233-4 et D233-11).</li>
<li>Prétraitement des eaux grasses et déclaration de déversement à Paris (règlement d'assainissement, art. 17.1 et 15).</li>
</ul>"""),
            ("Licences, musique, terrasse", """<p><strong>Boissons.</strong> Les débits de boissons relèvent de la licence III ou IV (code de la santé publique, L3331-1) ; un restaurant peut se contenter de la petite licence restaurant ou de la licence restaurant, qui ne permettent de servir qu'à l'occasion des repas (L3331-2). Le permis d'exploitation, obtenu après formation, vaut dix ans (L3332-1-1).</p>
<p><strong>Sons amplifiés.</strong> Au-delà d'un niveau moyen de 80 dB(A) sur huit heures, les limites de 102 dB(A) et 118 dB(C) sur 15 minutes s'appliquent (code de la santé publique, R1336-1) ; une étude de l'impact des nuisances sonores est obligatoire pour une diffusion habituelle (code de l'environnement, R571-27).</p>
<p><strong>Terrasse.</strong> Autorisation d'occupation du domaine public, délivrée par la Ville selon le règlement des étalages et terrasses.</p>"""),
            ("Transformer une boutique en restaurant", """<p>Quatre régimes se croisent. <strong>Urbanisme</strong> : la restauration et le commerce de détail sont deux sous-destinations de la même destination ; sans travaux, aucune déclaration n'est due au titre du changement (R*421-17 b), mais des travaux sur la façade ou la structure imposent un permis (R*421-14 c), et le PLU s'applique même sans formalité (L421-8). <strong>ERP</strong> : le type passe de M à N ; les travaux d'aménagement (cuisine, extraction, salle) relèvent de l'autorisation de travaux (L122-3), et le classement est à refaire. <strong>Bail</strong> : l'activité doit être autorisée par la clause de destination ou faire l'objet d'une déspécialisation. <strong>Technique</strong> : l'extraction doit être réalisable. À Paris, la transformation d'un rez-de-chaussée sur rue en cuisine dédiée à la vente en ligne est interdite (PLU, UG.1.3.5).</p>"""),
        ],
        "faq": [
            {"q": "Combien de couverts dans 80 m² de salle ?", "a": "<p>Le règlement ne fixe pas un nombre de couverts mais un effectif : le nombre de places assises que vous déclarez, dans la limite d'1 personne pour 2 m² (N 2). Sur 80 m² de zone assise, la déclaration ne peut donc dépasser 40 places ; sans déclaration, l'effectif retenu est de 80 personnes. Le confort de service conduit souvent à moins.</p>"},
            {"q": "Peut-on ouvrir un restaurant sans conduit d'extraction ?", "a": "<p>Une cuisine qui cuit doit évacuer son air selon le RSD de Paris : hotte, conduit de ventilation unique, rejet à 8 m au moins de toute fenêtre, sauf aménagement empêchant toute reprise d'air pollué. Sans tracé possible, le projet de cuisson n'est pas faisable en l'état ; une offre sans cuisson ou avec des équipements adaptés se discute au cas par cas.</p>"},
            {"q": "Un restaurant de 5e catégorie passe-t-il en commission de sécurité ?", "a": "<p>Pas systématiquement : un ERP de 5e catégorie sans locaux à sommeil n'a ni avis préalable ni visite périodique systématiques, mais il doit respecter les règles, et l'autorité de police (à Paris, le préfet de police) peut faire procéder à une visite. Voir <a href=\"https://dossier-erp-paris.fr/commission-securite-erp-paris/\" rel=\"noopener\">la commission de sécurité à Paris</a>.</p>"},
        ],
        "sources": ["n2", "pe2", "gn1", "rsd631", "rsd1303", "copro25", "ce852", "f32189", "r2334", "ddpp", "l2334", "assainissement", "d23311", "licences", "l33312", "l333211", "r13361", "r57127", "terrasses", "r42117", "r42114", "l4218", "plubreg", "l1223"],
        "related": ["/guides/extraction-restaurant-paris", "/calcul-effectif-erp-commerce", "/avant-signature-bail-commercial", DEP + "/erp-restaurant-bar-paris/"],
        "service_type": "Conception de restaurant, bar et café", "og": "restaurant",
    },
    {
        "path": "/architecte-metiers-de-bouche", "kind": "activite", "mini": "bouche", "short": "Boulangerie et métiers de bouche",
        "teaser": "Laboratoire, hygiène, vente.",
        "title": "Architecte boulangerie et métiers de bouche à Paris | Kalya",
        "description": "Boulangerie, pâtisserie, boucherie, fromagerie, traiteur à Paris : laboratoire conforme au règlement 852/2004, extraction, froid, prétraitement des graisses, vente type M.",
        "h1": "Boulangerie, boucherie, traiteur : un laboratoire derrière la vitrine",
        "answer": "Un commerce de bouche associe une vente, qui reçoit du public, et un laboratoire, qui produit. Le laboratoire doit prévenir les contaminations entre les opérations (règlement CE n° 852/2004), avec hotte et conduit nettoyés chaque mois (RSD de Paris, art. 130-3). À Paris, les métiers de bouche équipent leurs évacuations d'un prétraitement des graisses.",
        "bullets": [
            "Laboratoire : agencement qui sépare les opérations, surfaces faciles à nettoyer, lave-mains (règlement (CE) n° 852/2004, annexe II).",
            "Ateliers et laboratoires de préparation : hotte, conduit unique, nettoyage mensuel des conduits et filtres (RSD de Paris, art. 130-3).",
            "Déclaration de l'établissement avant l'ouverture (code rural, R233-4 ; Cerfa n° 13984).",
            "Prétraitement des graisses : restaurants et métiers de bouche (règlement d'assainissement de Paris, art. 17.1).",
            "La partie vente reste un ERP : type, catégorie et accessibilité à établir (GN 1, R164-2).",
        ],
        "sections": [
            ("Deux mondes dans un même local", """<p>La vente demande de la visibilité, un comptoir lisible, une file d'attente qui ne bloque pas l'entrée, une vitrine réfrigérée accessible au service. Le laboratoire demande de la surface utile, des flux propres, du froid, de l'extraction, des évacuations et de la puissance. Le plan se joue à la frontière : passe-plats, réassort de la vitrine, livraisons qui ne traversent pas la boutique.</p>"""),
            ("Le laboratoire selon le règlement 852/2004", """<p>L'annexe II du règlement (CE) n° 852/2004 fixe les exigences des locaux : conception permettant un nettoyage adéquat, prévention de la contamination « entre et durant les opérations », lave-mains en nombre suffisant, ventilation adaptée, surfaces faciles à nettoyer. L'arrêté du 21 décembre 2009 complète ces règles pour le commerce de détail. La « marche en avant » est la manière d'organiser ces exigences : du sale vers le propre, sans retour en arrière.</p>
<p>Avant l'ouverture, l'établissement est déclaré (code rural, R233-4 ; Cerfa n° 13984 adressé à la direction départementale de la protection des populations).</p>"""),
            ("Fours, froid, extraction, évacuations", """<p>Le règlement sanitaire de Paris consacre son titre VII aux ateliers et laboratoires de préparation des aliments : hotte débordante à captage total, conduit de ventilation unique et indépendant des conduits de fumée, nettoyage des conduits et filtres au moins une fois par mois (art. 130-3). L'air des locaux à pollution spécifique est rejeté à 8 m au moins de toute fenêtre ou prise d'air neuf, sauf aménagement empêchant toute reprise d'air pollué (art. 63-1).</p>
<p>Le règlement d'assainissement de Paris, en vigueur depuis le 1er janvier 2026, impose aux restaurants, à la restauration collective et aux métiers de bouche un dispositif de prétraitement des effluents gras (art. 17.1) et une déclaration de déversement (art. 15). Puissance électrique, gaz éventuel et groupes froids se vérifient avant de signer : voir <a href="/avant-signature-bail-commercial">avant de signer le bail</a>.</p>"""),
            ("La vente : un ERP à part entière", """<p>La partie ouverte au public est un établissement recevant du public : son type se qualifie selon l'exploitation réelle et sa catégorie selon l'effectif. Pour un magasin de vente, l'effectif se calcule à 1 personne pour 3 m² de surface de vente au rez-de-chaussée (M 2). L'accessibilité porte sur l'entrée, la circulation jusqu'au comptoir et la caisse (R164-2, arrêté du 8 décembre 2014). Sur les rues de Paris protégées pour le commerce artisanal de proximité, un local affecté à ce commerce, au sens du lexique du PLU, ne peut pas devenir une autre activité (PLU, UG.1.4.2).</p>"""),
        ],
        "sources": ["ce852", "a2009", "rsd1303", "rsd631", "r2334", "ddpp", "assainissement", "gn1", "m2", "r1641", "r1642", "a2014", "plubreg"],
        "related": ["/architecte-restaurant", "/guides/extraction-restaurant-paris", "/avant-signature-bail-commercial", "/guides/plu-paris-commerce"],
        "service_type": "Conception de commerce de bouche et laboratoire",
    },
    {
        "path": "/architecte-institut-beaute-coiffure", "kind": "activite", "mini": "beaute", "short": "Institut, salon de coiffure",
        "teaser": "Cabines, réseaux, accueil.",
        "title": "Architecte institut de beauté et salon de coiffure à Paris | Kalya",
        "description": "Aménager un institut de beauté, un spa urbain ou un salon de coiffure à Paris : qualification ERP, PLU et linéaires protégés, réseaux d'eau, ventilation, cabines, accessibilité.",
        "h1": "Institut de beauté, salon de coiffure : des cabines, des réseaux, un accueil",
        "answer": "Un institut ou un salon qui reçoit des clients est un ERP : son type se qualifie selon l'exploitation réelle (soins, prestations, vente de produits), puis sa catégorie selon l'effectif. À Paris, la qualification compte aussi pour le PLU : sur les rues protégées, un rez-de-chaussée commercial ne peut pas devenir une activité de services hors des sous-destinations autorisées.",
        "bullets": [
            "Recevoir des clients fait du salon un ERP ; le type se qualifie selon l'exploitation réelle (règlement de sécurité, GN 1).",
            "Urbanisme : « artisanat et commerce de détail » couvre la prestation de services artisanale ; « activités de services où s'effectue l'accueil d'une clientèle » est une autre sous-destination (R151-28, arrêté du 10 novembre 2016).",
            "Sur un linéaire « protection du commerce et de l'artisanat », un local de commerce ne peut pas devenir une activité de services (PLU de Paris, UG.1.4.2).",
            "Accessibilité : accueil, circulation, et les cabines ou postes nécessaires pour délivrer l'ensemble des prestations (R164-2).",
            "Registre public d'accessibilité obligatoire (R164-6).",
        ],
        "sections": [
            ("Qualifier l'activité avant de signer", """<p>Deux qualifications se font en parallèle, et elles ne se recoupent pas forcément. En <strong>urbanisme</strong>, l'arrêté du 10 novembre 2016 rattache à « artisanat et commerce de détail » les activités artisanales de production, de transformation, de réparation ou de prestation de services, et à « activités de services où s'effectue l'accueil d'une clientèle » la conclusion directe de contrats de prestation de services, « notamment médicaux ». En <strong>sécurité</strong>, le type d'ERP suit l'exploitation réelle.</p>
<p>Cette qualification compte à Paris : sur les rues soumises à la protection du commerce et de l'artisanat, un local d'artisanat et commerce de détail, de restauration ou de commerce de gros ne peut pas changer pour une autre sous-destination, sauf activités médicales et paramédicales de proximité (UG.1.4.2). Une reprise de boutique par un institut se vérifie donc sur le plan des protections et sur la nature exacte des prestations.</p>"""),
            ("Cabines, bacs, réseaux", """<p>Un institut se dessine autour de ses réseaux : arrivées d'eau et évacuations pour les bacs à shampoing et les cabines, eau chaude en quantité, ventilation pour les produits, électricité pour les appareils. Le local doit permettre ces tracés sans casser la structure : c'est un point de visite avant le bail.</p>
<ul>
<li><strong>Accueil</strong> : visible depuis l'entrée, avec une attente qui n'expose pas les clients en soin.</li>
<li><strong>Cabines</strong> : intimité visuelle et acoustique, rangements, lavabo, ventilation.</li>
<li><strong>Postes de coiffage</strong> : miroirs, prises, lumière sans ombre portée, circulation derrière les fauteuils.</li>
<li><strong>Arrière</strong> : linge, stock de produits, pause du personnel.</li>
</ul>"""),
            ("Accessibilité des soins", """<p>Dans un ERP existant de 5e catégorie, l'obligation porte sur une partie du local donnant accès à l'ensemble des prestations, au plus près de l'entrée (R164-2, arrêté du 8 décembre 2014). Pour un institut, cela concerne l'accueil, le cheminement et les cabines ou postes nécessaires pour délivrer l'ensemble des prestations ; les mesures de substitution et les dérogations se motivent. Le <a href="/guides/accessibilite-commerce">guide de l'accessibilité</a> détaille la démarche.</p>"""),
        ],
        "sources": ["gn1", "r15128", "a2016", "plubreg", "r1641", "r1642", "a2014", "r1643", "r1646"],
        "related": ["/guides/plu-paris-commerce", "/guides/accessibilite-commerce", "/avant-signature-bail-commercial", "/guides/changement-destination-local-commercial"],
        "service_type": "Conception d'institut de beauté et de salon de coiffure",
    },
    {
        "path": "/architecte-showroom", "kind": "activite", "mini": "showroom", "short": "Showroom",
        "teaser": "Montrer, conseiller, commander.",
        "title": "Architecte showroom à Paris : exposition, vente, B2B | Kalya",
        "description": "Concevoir un showroom à Paris : exposition, conseil, configuration, commande ; effectif ERP (faible densité, professionnels), commerce de gros ou de détail, grandes surfaces.",
        "h1": "Showroom : montrer, conseiller, faire commander",
        "answer": "Un showroom se dimensionne par ce qu'il montre et ce qu'il fait vivre, pas par le stock. S'il reçoit des clients, c'est un ERP : un magasin à faible densité de public compte 1 personne pour 9 m² de surface de vente, et un magasin réservé aux professionnels peut retenir l'effectif déclaré par le chef d'établissement (règlement de sécurité, M 2).",
        "bullets": [
            "Magasin à faible densité de public : 1 personne pour 9 m², quel que soit le niveau, à justifier (M 2).",
            "Magasin exclusivement réservé aux professionnels : effectif sur déclaration contrôlée (M 2).",
            "Un showroom pour clientèle professionnelle relève de la sous-destination « commerce de gros » (arrêté du 10 novembre 2016).",
            "Au-delà de 1 000 m² de surface de vente au détail : autorisation d'exploitation commerciale (L752-1).",
        ],
        "sections": [
            ("Un parcours en six temps", """<p>Un showroom ne vend pas toujours sur place : il fait comprendre, désirer et commander. Le plan suit six temps : <strong>exposition</strong> (mise en scène des produits), <strong>conseil</strong> (tables, écrans, échantillons), <strong>configuration</strong> (matières, finitions, options), <strong>commande</strong>, <strong>livraison</strong> et <strong>après-vente</strong>. La surface n'est pas dimensionnée par le stock, mais par la place que chaque temps demande.</p>"""),
            ("Effectif et classement", f"""<p>L'article M 2 prévoit deux cas utiles aux showrooms : le magasin de vente à faible densité de public, compté à 1 personne pour 9 m² de surface de vente quel que soit le niveau, et le magasin exclusivement réservé aux professionnels, dont l'effectif peut être déterminé sur déclaration contrôlée du chef d'établissement. Ces cas se justifient dans la notice de sécurité.</p>
{M2_TABLE}"""),
            ("Commerce de gros ou de détail ?", """<p>En urbanisme, la sous-destination « commerce de gros » recouvre la présentation et la vente de biens pour une clientèle professionnelle ; « artisanat et commerce de détail » vise la vente au détail à une clientèle (arrêté du 10 novembre 2016, art. 3). Le choix compte pour le PLU, notamment à Paris où certains changements depuis le commerce de gros sont encadrés (UG.1.3.4).</p>
<p>Au-delà de 1 000 m² de surface de vente au détail, la création d'un magasin est soumise à autorisation d'exploitation commerciale (code de commerce, L752-1).</p>"""),
        ],
        "sources": ["m2", "gn1", "a2016", "r15128", "plubreg", "l7521", "l4254"],
        "related": ["/concept-et-deploiement-enseigne", "/calcul-effectif-erp-commerce", "/architecte-commerce-ile-de-france"],
        "service_type": "Conception de showroom",
    },

    # ================================================================ ZONES
    {
        "path": "/architecte-commerce-paris", "kind": "zone", "short": "Paris", "lieu": "Paris, 20 arrondissements",
        "teaser": "PLU, linéaires, devantures, marché.",
        "title": "Architecte commerce Paris : PLU, devantures, ERP, marché | Kalya",
        "description": "Architecte de commerces à Paris : linéaires protégés du PLU, devantures, sites patrimoniaux, enseignes, extraction, préemption commerciale, chiffres de l'Apur.",
        "h1": "Architecte commerce à Paris : ce qui change quand le local est parisien",
        "answer": "À Paris, un projet de commerce passe par des règles que l'on ne trouve pas ailleurs : 329 km de linéaires où le rez-de-chaussée commercial est protégé, un article du PLU dédié aux devantures, deux sites patrimoniaux remarquables, des enseignes demandées en ligne, un règlement sanitaire qui fixe l'extraction des cuisines. Kalya Architecte, dont l'adresse parisienne est rue du Cherche-Midi (6e), intervient dans tous les arrondissements.",
        "bullets": [
            "PLU bioclimatique approuvé le 20 novembre 2024 : protection du commerce et de l'artisanat sur 329 km de voies, plus 29 km pour l'artisanat de proximité et 9 km pour le commerce culturel.",
            "Dark stores et dark kitchens : changement interdit pour les rez-de-chaussée sur rue (UG.1.3.1 et UG.1.3.5).",
            "Sites patrimoniaux remarquables du Marais et du 7e : déclaration préalable en deux mois.",
            "Droit de préemption commercial depuis le 7 août 2024 dans les 5e, 6e et une partie du 7e arrondissement.",
            "60 846 commerces et services commerciaux en rez-de-chaussée et 10,9 % de locaux vacants en avril 2023 (Apur).",
        ],
        "sections": [
            ("Le PLU bioclimatique et les rez-de-chaussée", """<p>Le PLU bioclimatique de Paris, approuvé le 20 novembre 2024 et modifié depuis, protège les rez-de-chaussée commerciaux le long des voies repérées (UG.1.4.2) :</p>
<ul>
<li><strong>protection du commerce et de l'artisanat</strong> : un local d'artisanat et commerce de détail, de restauration ou de commerce de gros ne peut pas changer pour une autre sous-destination, sauf activités médicales et paramédicales de proximité ;</li>
<li><strong>protection particulière du commerce artisanal de proximité</strong> et <strong>du commerce culturel</strong> : l'activité elle-même est protégée ;</li>
<li><strong>sites de protection des grands magasins</strong> : la part de commerce et de restauration ne peut pas diminuer.</li>
</ul>
<p>Le règlement interdit aussi de transformer un rez-de-chaussée sur rue en entrepôt (hors logistique urbaine) ou en cuisine dédiée à la vente en ligne (UG.1.3.1, UG.1.3.5). La carte des protections est publiée en données ouvertes, sans valeur réglementaire : le règlement graphique fait foi. Voir le <a href="/guides/plu-paris-commerce">guide du PLU de Paris</a>.</p>"""),
            ("Devantures, patrimoine, enseignes", """<p>L'article UG.2.1.4 encadre les devantures : intégration à la façade, devanture de préférence en applique ou en feuillure avec un retrait limité de 10 à 20 cm, vitrage le plus clair possible, grilles intérieures sauf impossibilité technique ou architecturale. Dans les deux sites patrimoniaux remarquables (Marais, 7e) et aux abords des monuments historiques, la déclaration préalable est instruite en deux mois et suppose l'accord de l'architecte des Bâtiments de France. Les enseignes se demandent en ligne à la Ville depuis le 1er octobre 2025 ; l'autorisation est acquise après deux mois de silence. Voir <a href="/vitrine-et-devanture-commerce">vitrine et devanture</a>.</p>"""),
            ("Restaurants : règles sanitaires parisiennes", """<p>Le règlement sanitaire départemental de Paris fixe le rejet de l'air des cuisines à 8 m au moins de toute fenêtre ou prise d'air neuf, sauf aménagement empêchant toute reprise d'air pollué (art. 63-1) et le nettoyage mensuel des conduits et filtres (art. 130-3). Le règlement d'assainissement, en vigueur depuis le 1er janvier 2026, impose le prétraitement des graisses aux restaurants et métiers de bouche (art. 17.1). Voir <a href="/architecte-restaurant">architecte restaurant</a>.</p>"""),
            ("Le marché parisien en quelques repères", """<p>L'Apur a recensé en avril 2023 83 154 locaux en rez-de-chaussée, dont 60 846 commerces, bars-restaurants et services commerciaux, soit 28 pour 1 000 habitants, et 9 059 locaux vacants : 10,9 %, contre 10,2 % en 2020. Entre 2020 et 2023, la restauration rapide progresse de 10 %, l'alimentaire de 4 % ; l'équipement de la personne recule de 8 % selon la Ville de Paris. Le relevé d'avril 2026 doit être publié fin 2026.</p>
<p>Sur les grands axes, BNP Paribas Real Estate relève au 1er semestre 2026 des loyers prime de 18 000 €/m²/an sur les Champs-Élysées, 14 000 € avenue Montaigne et rue Saint-Honoré, 5 500 € rue des Francs-Bourgeois et 5 000 € boulevard Haussmann. Depuis le 7 août 2024, la Ville dispose d'un droit de préemption commercial dans les 5e et 6e arrondissements et sur certaines rues du 7e.</p>"""),
            ("Où et comment Kalya Architecte intervient", """<p>L'adresse parisienne de Kalya Architecte est au 71 rue du Cherche-Midi, dans le 6e arrondissement. L'architecte se déplace dans tout Paris pour visiter les locaux, de préférence avant la signature du bail. Les dossiers ERP parisiens suivent un circuit propre, décrit sur <a href="https://dossier-erp-paris.fr/autorisation-travaux-erp-paris/" rel="noopener">dossier-erp-paris.fr</a>.</p>"""),
        ],
        "sources": ["plub", "plubreg", "plubcarte", "spr", "r42324", "r4251", "r4252", "parisenseignes", "r58113", "rsd631", "rsd1303", "assainissement", "preemption", "apur2023", "paris28", "bnpre"],
        "related": ["/guides/plu-paris-commerce", "/vitrine-et-devanture-commerce", "/architecte-commerce-ile-de-france", DEP + "/"],
        "service_type": "Architecture de commerces à Paris",
    },
    {
        "path": "/architecte-commerce-ile-de-france", "kind": "zone", "short": "Île-de-France", "lieu": "Île-de-France",
        "teaser": "Centres commerciaux, retail parks, centres-villes.",
        "title": "Architecte commerce Île-de-France : centres-villes, malls | Kalya",
        "description": "Architecte de commerces en Île-de-France : mêmes règles ERP, procédures propres à chaque commune, centres commerciaux, retail parks, autorisation commerciale.",
        "h1": "Architecte commerce en Île-de-France : mêmes règles, autres guichets",
        "answer": "Hors de Paris, les règles de fond d'un commerce sont les mêmes : classement ERP, sécurité, accessibilité. Ce qui change, c'est la procédure (autorisation de travaux délivrée par le maire, sauf compétence du préfet, avis des commissions compétentes) et le droit local : chaque commune a son PLU ; l'enseigne est soumise à autorisation si la commune a un règlement local de publicité et, partout, dans les secteurs protégés (L581-18).",
        "bullets": [
            "157 205 commerces actifs en Île-de-France en 2023, +2,1 % par rapport à 2021 (CCI Paris Île-de-France).",
            "Centre commercial : mails à 1 personne pour 5 m², boutiques de moins de 300 m² à 1 personne pour 6 m² (M 2).",
            "Enseigne soumise à autorisation dans les communes dotées d'un règlement local de publicité et dans les secteurs protégés (L581-18).",
            "Plus de 1 000 m² de surface de vente : autorisation d'exploitation commerciale (L752-1).",
        ],
        "sections": [
            ("Les règles de fond ne changent pas", """<p>Le règlement de sécurité, le classement des ERP, les règles d'accessibilité et le code de l'urbanisme sont nationaux. Ce qui change à la sortie de Paris : l'autorité qui délivre l'autorisation de travaux (le maire, sauf compétence du préfet), le service qui instruit, les sous-commissions départementales qui rendent les avis, et le droit local (PLU ou PLU intercommunal, règlement local de publicité, protections patrimoniales).</p>"""),
            ("Centres commerciaux et retail parks", """<p>Dans un centre commercial, l'effectif des mails se compte à 1 personne pour 5 m² de leur surface totale ; les boutiques de moins de 300 m² comptent 1 personne pour 6 m², quel que soit le niveau (règlement de sécurité, M 2). Le bailleur impose en général son cahier des charges preneur : il s'ajoute aux règles, sans les remplacer.</p>
<p>En retail park, le projet se joue sur la visibilité depuis la route, le stationnement, la livraison et la façade. Au-delà de 1 000 m² de surface de vente, la création d'un magasin est soumise à autorisation d'exploitation commerciale ; le permis de construire en tient lieu après avis favorable de la commission départementale (L752-1, L425-4).</p>"""),
            ("Centres-villes de petite et grande couronne", """<p>Dans les centres-villes, les sujets parisiens se retrouvent à une autre échelle : devantures en immeuble ancien, copropriétés, abords de monuments historiques, linéaires commerciaux protégés par certains PLU. La vérification avant bail suit la même grille qu'à Paris, avec les documents de la commune.</p>
<p>La CCI Paris Île-de-France recensait 157 205 commerces actifs dans la région en 2023, contre 153 990 en 2021 ; l'alimentaire progresse de 5 % et la restauration rapide de 9 % sur la période.</p>"""),
            ("Où intervient Kalya Architecte", """<p>Dans toute l'Île-de-France, depuis Paris. Pour la procédure ERP hors de Paris, voir aussi <a href="https://dossier-erp-paris.fr/erp-hors-paris-ile-de-france/" rel="noopener">ERP hors de Paris</a> sur dossier-erp-paris.fr.</p>"""),
        ],
        "sources": ["r1227", "m2", "l58118", "l7521", "l4254", "cci2023"],
        "related": ["/architecte-commerce-paris", "/concept-et-deploiement-enseigne", "/architecte-showroom", DEP + "/erp-hors-paris-ile-de-france/"],
        "service_type": "Architecture de commerces en Île-de-France",
    },
]
