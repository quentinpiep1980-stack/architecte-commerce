# -*- coding: utf-8 -*-
"""Guides : chaque guide répond d'abord en quelques lignes (réponse directe), puis détaille, texte à l'appui.
Sources : clés de content/site.py, consultées le 9 octobre 2026."""
from content.pages import DEGAGEMENTS, M2_TABLE, AUTOS_TABLE, erp_link

DEP = "https://dossier-erp-paris.fr"

CAL_WIDGET = """<div class="tool" data-scenarios>
<fieldset class="q"><legend>Cochez ce que comporte votre projet</legend>
<p class="qh">Les dossiers déposés ensemble s'instruisent en parallèle : le délai d'instruction le plus long fixe le chemin critique administratif.</p>
<div class="chips">
<label class="chip"><input type="checkbox" value="at" checked><span>Aménagement intérieur d'un ERP</span></label>
<label class="chip"><input type="checkbox" value="devanture" checked><span>Devanture modifiée</span></label>
<label class="chip"><input type="checkbox" value="abf"><span>Site patrimonial ou abords d'un monument</span></label>
<label class="chip"><input type="checkbox" value="enseigne" checked><span>Nouvelle enseigne</span></label>
<label class="chip"><input type="checkbox" value="pc"><span>Façade ou structure, avec changement de destination</span></label>
</div></fieldset>
<div class="gantt" style="margin-top:20px">
<div class="gantt-scale" aria-hidden="true"><span class="lab"></span><div class="ticks"><span>0</span><span>1 mois</span><span>2</span><span>3</span><span>4</span><span>5 mois</span></div></div>
<div class="gantt-row" data-in="devanture" data-m="1"><div class="lab">Déclaration préalable<small>R*423-23</small></div><div class="bar-track"><span class="bar" style="left:0;width:16.67%">1 mois</span></div></div>
<div class="gantt-row" data-in="abf" data-m="2"><div class="lab">Déclaration préalable en secteur protégé<small>R423-24, accord de l'ABF</small></div><div class="bar-track"><span class="bar ext" style="left:0;width:33.33%">2 mois</span></div></div>
<div class="gantt-row" data-in="enseigne" data-m="2"><div class="lab">Enseigne<small>R581-13</small></div><div class="bar-track"><span class="bar" style="left:0;width:33.33%">2 mois</span></div></div>
<div class="gantt-row" data-in="at" data-m="4"><div class="lab">Autorisation de travaux ERP<small>R122-16</small></div><div class="bar-track"><span class="bar" style="left:0;width:66.67%">4 mois</span></div></div>
<div class="gantt-row" data-in="pc" data-m="5"><div class="lab">Permis de construire ERP<small>R*423-28, hors majorations ; vaut autorisation de travaux</small></div><div class="bar-track"><span class="bar" style="left:0;width:83.33%">5 mois</span></div></div>
</div>
<p class="res-note" aria-live="polite">Délai d'instruction le plus long : <strong data-total>4 mois</strong>, à compter de dossiers complets. Ajoutez la conception avant le dépôt, la consultation des entreprises et le chantier.</p>
</div>"""

PAGES = [
    {
        "path": "/guides/autorisations-travaux-commerce", "kind": "guide", "short": "Autorisations de travaux",
        "teaser": "Déclaration préalable, autorisation ERP, enseigne, permis : qui fait quoi.",
        "title": "Autorisations de travaux d'un commerce : DP, AT, enseigne, permis | Kalya",
        "description": "Autorisations des travaux d'un commerce à Paris : autorisation ERP (4 mois), déclaration préalable (1 ou 2 mois), enseigne (2 mois), permis (5 mois), réforme 2026.",
        "h1": "Les autorisations de travaux d'un commerce, dossier par dossier",
        "answer": "Un commerce cumule souvent trois dossiers : l'autorisation de travaux au titre des ERP pour l'intérieur (4 mois), la déclaration préalable pour la devanture (1 mois, 2 en secteur protégé) et l'autorisation d'enseigne (2 mois). Un permis de construire, exigé si la façade ou la structure change avec la destination, vaut autorisation de travaux (5 mois).",
        "bullets": [
            "Autorisation de travaux : pour créer, aménager ou modifier un ERP (code de la construction, L122-3) ; Cerfa n° 13824*04 ; 4 mois (R122-16).",
            "Déclaration préalable : travaux modifiant l'aspect extérieur (R*421-17 a) ; 1 mois, 2 en site patrimonial ou abords (R*423-23, R423-24).",
            "Enseigne : autorisation du maire là où un règlement local de publicité s'applique, donc partout à Paris (L581-18) ; 2 mois (R581-13).",
            "Permis de construire : structure ou façade modifiée avec changement de destination (R*421-14 c) ; 5 mois pour un ERP (R*423-28), hors majorations éventuelles.",
            "Loi du 26 mai 2026 : déclaration de conformité prévue pour certains ERP de moins de 300 m², applicable après un décret.",
        ],
        "sections": [
            ("Le tableau des autorisations", AUTOS_TABLE),
            ("L'autorisation de travaux ERP", """<p>Les travaux qui conduisent à la création, l'aménagement ou la modification d'un établissement recevant du public ne peuvent être exécutés qu'après autorisation (code de la construction, L122-3). La demande se fait sur le Cerfa n° 13824*04, avec plans, notice d'accessibilité et, sauf en 5e catégorie sans locaux d'hébergement du public (R122-7, II : une description succincte des travaux est alors communiquée à l'autorité de police), notice de sécurité. L'instruction dure quatre mois à compter d'un dossier complet ; sans décision notifiée, l'autorisation est en principe acquise (R122-16, R122-21), sauf refus d'une dérogation.</p>
<p>Elle ne vaut pas autorisation d'ouvrir : pour les ERP soumis à visite, l'ouverture passe par la commission de sécurité. Voir <a href="https://dossier-erp-paris.fr/autorisation-ouverture-erp-paris/" rel="noopener">fin de travaux et ouverture</a>.</p>"""),
            ("Déclaration préalable ou permis de construire ?", """<p>L'urbanisme et l'ERP s'examinent séparément. Ce sont les travaux et la destination qui orientent l'urbanisme :</p>
<ul>
<li>modifier l'aspect extérieur (devanture, store, menuiseries) : <strong>déclaration préalable</strong> (R*421-17 a) ;</li>
<li>changer de destination sans toucher la structure ni la façade : déclaration préalable, mais pas entre sous-destinations d'une même destination (R*421-17 b) ;</li>
<li>modifier la structure porteuse ou la façade en changeant de destination ou de sous-destination : <strong>permis de construire</strong> (R*421-14 c).</li>
</ul>
<p>Un permis de construire tient lieu d'autorisation de travaux lorsque l'autorité compétente a donné son accord (code de l'urbanisme, R*425-15) ; une déclaration préalable n'a pas cet effet.</p>"""),
            ("L'enseigne", """<p>À Paris, couverte par un règlement local de publicité, toute enseigne est soumise à autorisation du maire (code de l'environnement, L581-18). La demande se fait sur le Cerfa n° 16308*01, en ligne sur le téléservice de la Ville ; l'autorité statue dans les deux mois d'un dossier complet, et son silence vaut accord (R581-13). Voir le <a href="/guides/enseigne-paris">guide de l'enseigne</a>.</p>"""),
            ("Réforme 2026 : ce qui est prévu, ce qui ne l'est pas encore", """<p>La loi n° 2026-403 du 26 mai 2026 a modifié l'article L122-3 du code de la construction : pour certains ERP de moins de 300 m², une déclaration de conformité certifiée par un tiers pourra remplacer l'autorisation de travaux, sous conditions cumulatives (surface, système d'extinction adapté ou situation en gare, maintien de la même activité). Le ministère subordonne son application à un décret, que nous n'avons pas identifié au 9 octobre 2026. En attendant, l'autorisation de travaux reste la règle.</p>"""
             + erp_link('/reforme-2026-autorisation-travaux-erp/', 'Réforme 2026 de l\'autorisation de travaux ERP', 'Ce que dit la loi, ce qui attend un décret : l\'analyse détaillée sur dossier-erp-paris.fr.')),
        ],
        "faq": [
            {"q": "Mon dossier de déclaration préalable vaut-il autorisation de travaux ERP ?", "a": "<p>Non. Seul le permis de construire tient lieu d'autorisation de travaux, lorsque l'autorité compétente a donné son accord (R*425-15). Avec une déclaration préalable, l'autorisation de travaux se demande à part.</p>"},
            {"q": "Que se passe-t-il si l'administration ne répond pas ?", "a": "<p>Pour l'autorisation de travaux, le silence au terme de quatre mois vaut en principe accord (R122-21), sauf refus d'une dérogation. Pour l'enseigne, le silence au terme de deux mois vaut accord (R581-13). Encore faut-il que le dossier ait été complet.</p>"},
        ],
        "sources": ["l1223", "r12216", "r12221", "cerfa13824", "r1227", "r42117", "r42323", "r42324", "r42114", "r42328", "r42515", "l58118", "r58113", "cerfa16308", "l7521", "l4254", "dep_reforme"],
        "related": ["/guides/calendrier-ouverture-magasin", "/guides/enseigne-paris", "/guides/changement-destination-local-commercial", DEP + "/pc-dp-ou-at-erp/"],
    },
    {
        "path": "/guides/calendrier-ouverture-magasin", "kind": "guide", "short": "Calendrier d'ouverture",
        "teaser": "Les délais d'autorisation, scénario par scénario.",
        "title": "Calendrier d'ouverture d'un magasin : délais d'autorisation | Kalya",
        "description": "Construire le calendrier d'ouverture d'un commerce : chemin critique du bail à l'ouverture, délais d'instruction (1, 2, 4, 5 mois), saisine de la commission, simulateur de scénarios.",
        "h1": "Calendrier d'ouverture : le chemin critique, du bail à la vitrine allumée",
        "answer": "Le calendrier d'un commerce se lit comme un chemin critique : bail, conception, dossiers, consultation, chantier, réception, ouverture. Côté administration, les délais d'instruction courent en parallèle : un mois pour une déclaration préalable (deux en secteur protégé), deux pour une enseigne, quatre pour une autorisation de travaux ERP, cinq pour un permis de construire ERP.",
        "bullets": [
            "Les délais courent à compter d'un dossier complet ; une demande de pièces suspend le départ.",
            "Déposés ensemble, les dossiers s'instruisent en parallèle : le plus long fixe le chemin critique administratif.",
            "Quand une visite est requise, les services de l'État demandent de saisir la commission au moins un mois avant la date d'ouverture prévue.",
            "Le délai d'instruction n'est ni la durée du projet, ni un résultat garanti.",
        ],
        "sections": [
            ("Simuler votre calendrier administratif", CAL_WIDGET),
            ("Le chemin critique d'une ouverture", """<ol>
<li><strong>Maîtrise du local</strong> : vérification avant bail, négociation, signature.</li>
<li><strong>Conception</strong> : relevé, esquisse, plans, notices de sécurité et d'accessibilité.</li>
<li><strong>Dossiers</strong> : dépôt simultané de la déclaration préalable, de l'autorisation de travaux, de l'enseigne.</li>
<li><strong>Consultation des entreprises</strong> pendant l'instruction, pour signer dès l'accord.</li>
<li><strong>Commandes longues</strong> : mobilier sur mesure, enseigne, froid, cuisine, à lancer tôt.</li>
<li><strong>Chantier</strong>, puis réception et levée des réserves.</li>
<li><strong>Préouverture</strong> : recrutement, formation, stock, caisse, nettoyage, registres.</li>
<li><strong>Ouverture</strong>, et commission de sécurité si l'établissement y est soumis.</li>
</ol>
<p>Le gain de temps vient surtout du recouvrement : consulter les entreprises pendant l'instruction, commander les éléments longs dès que le dessin est figé.</p>"""),
            ("Pièces manquantes, silence, commission", """<p>Si le dossier d'autorisation de travaux est incomplet, l'autorité demande les pièces manquantes dans le mois ; le délai de quatre mois ne court qu'à leur réception (R122-16). Au terme du délai, le silence vaut en principe accord (R122-21). Pour l'enseigne, le dossier est réputé complet faute de demande de pièces dans le mois, et le silence au terme de deux mois vaut accord (R581-13).</p>
<p>Pour les établissements soumis à visite avant ouverture (1re à 4e catégorie, 5e avec locaux à sommeil), les services de l'État demandent de saisir la commission au moins un mois avant la date prévue. Un ERP de 5e catégorie sans locaux à sommeil n'a pas de visite systématique.</p>"""
             + erp_link('/autorisation-ouverture-erp-paris/', 'Fin de travaux et autorisation d\'ouverture à Paris', 'Déclaration d\'achèvement, attestations, commission : les trois formalités à ne pas confondre.')),
        ],
        "sources": ["r42323", "r42324", "r58113", "r12216", "r12221", "r42328", "r42515", "r1227", "pe4", "vie_erp"],
        "related": ["/guides/autorisations-travaux-commerce", "/guides/preparer-projet-commerce", "/renovation-commerce-site-occupe"],
    },
    {
        "path": "/guides/budget-renovation-commerce", "kind": "guide", "short": "Budget d'un commerce",
        "teaser": "Enveloppes, maturité, qui paie quoi.",
        "title": "Budget de création ou de rénovation d'un commerce : la méthode | Kalya",
        "description": "Construire le budget d'un commerce : enveloppes (travaux, agencement, enseigne, sécurité, honoraires, préouverture), maturité de l'estimation, charges du bailleur et du preneur (R145-35).",
        "h1": "Le budget d'un commerce : des enveloppes, une maturité, des responsabilités",
        "answer": "Un budget de commerce fiable se construit par enveloppes (travaux, agencement, enseigne, sécurité et accessibilité, informatique, honoraires et autorisations, préouverture, aléas) et affiche sa maturité : ordre de grandeur, estimation sur plans, prix consultés, prix contractés. Il distingue aussi ce que le bail met à la charge du bailleur et du preneur.",
        "bullets": [
            "Pas de prix au mètre carré hors étude : l'état du local et le concept font varier les coûts du simple au multiple.",
            "Chaque estimation affiche sa maturité : ordre de grandeur, préliminaire, détaillée, consultée, contractée.",
            "Les grosses réparations de l'article 606 du code civil ne peuvent pas être imputées au locataire (code de commerce, R145-35).",
            "Une provision pour aléas se justifie d'autant plus que le local est ancien et mal connu.",
        ],
        "sections": [
            ("Les enveloppes d'un budget de commerce", """<div class="table-wrap"><table><caption class="sr">Enveloppes d'un budget de commerce</caption>
<thead><tr><th scope="col">Enveloppe</th><th scope="col">Ce qu'elle couvre</th></tr></thead>
<tbody>
<tr><td>Travaux</td><td>Démolition, cloisons, sols, plafonds, électricité, plomberie, ventilation, chauffage et climatisation, menuiseries</td></tr>
<tr><td>Agencement et mobilier</td><td>Comptoirs, présentoirs, cabines, mobilier sur mesure ou de série</td></tr>
<tr><td>Façade et enseigne</td><td>Devanture, store, enseigne, éclairage de vitrine</td></tr>
<tr><td>Sécurité et accessibilité</td><td>Éclairage de sécurité, alarme, extincteurs, adaptations d'accès</td></tr>
<tr><td>Équipements d'activité</td><td>Cuisine, froid, fours, bacs, matériel spécifique</td></tr>
<tr><td>Informatique et caisse</td><td>Caisse, réseau, écrans, comptage, vidéoprotection éventuelle</td></tr>
<tr><td>Honoraires et autorisations</td><td>Architecte, bureau de contrôle si requis, diagnostics, frais de dossiers</td></tr>
<tr><td>Préouverture</td><td>Recrutement, formation, stock initial, nettoyage, communication</td></tr>
<tr><td>Aléas</td><td>Provision pour les découvertes de chantier et les décisions tardives</td></tr>
</tbody></table></div>"""),
            ("La maturité d'une estimation", """<p>Un chiffre ne vaut que par sa maturité. Avant le bail, on parle d'<strong>ordre de grandeur</strong> : il sert à décider si le local est jouable. Sur esquisse, l'estimation devient <strong>préliminaire</strong> ; sur plans, <strong>détaillée</strong> par lots ; après consultation, <strong>consultée</strong> ; à la signature des marchés, <strong>contractée</strong>. Présenter un ordre de grandeur comme un prix ferme est la première cause de dérapage.</p>"""),
            ("Ce que paie le bailleur, ce que paie le preneur", """<p>La loi fixe quelques limites ; le bail fait le reste. Ne peuvent pas être imputées au locataire les dépenses relatives aux grosses réparations de l'article 606 du code civil, ni celles de mise en conformité lorsqu'elles relèvent de ces grosses réparations (code de commerce, R145-35). L'inventaire des charges et l'état des travaux figurent dans le bail (L145-40-2). La répartition des travaux d'aménagement, elle, se négocie : d'où l'intérêt de connaître leur coût avant de signer.</p>"""),
            ("Où se cachent les dépassements", """<ul>
<li>Un réseau à reprendre découvert au curage (évacuations, électricité ancienne).</li>
<li>Une extraction plus longue ou plus complexe que prévu.</li>
<li>Une sortie supplémentaire rendue nécessaire par l'effectif.</li>
<li>Des choix de finition arrêtés après la consultation des entreprises.</li>
<li>Des délais de livraison qui repoussent l'ouverture et font courir le loyer.</li>
</ul>
<p>La vérification avant bail et un cahier des charges complet avant consultation sont les deux meilleures assurances contre ces écarts.</p>"""),
        ],
        "sources": ["r14535", "l145402", "l145401"],
        "related": ["/avant-signature-bail-commercial", "/guides/bail-commercial-travaux", "/guides/calendrier-ouverture-magasin"],
    },
    {
        "path": "/guides/preparer-projet-commerce", "kind": "guide", "short": "Préparer son projet",
        "teaser": "Ce qu'il faut réunir avant le premier échange.",
        "title": "Préparer son projet de commerce avant le premier rendez-vous | Kalya",
        "description": "Préparer un projet de boutique ou de restaurant : activité, client, surface, budget, échéance, locaux repérés, bail, documents. La liste à réunir avant d'appeler un architecte.",
        "h1": "Préparer son projet de commerce : ce qu'il faut réunir avant d'appeler",
        "answer": "Un premier échange utile tient en six réponses : votre activité et votre client, la surface et le format visés, le budget global, l'échéance d'ouverture, les locaux repérés (adresses, photos, plans) et l'état du bail (projet, signé, à renouveler). Avec cela, un architecte peut déjà dire ce qui est jouable.",
        "bullets": [
            "L'activité exacte : vente, restauration, service, production sur place.",
            "Le client et sa mission d'achat : urgence, découverte, conseil, retrait de commande.",
            "La surface visée, le budget global, l'échéance d'ouverture.",
            "Les locaux repérés : adresse, photos, plans, annonce, projet de bail.",
        ],
        "sections": [
            ("Les six réponses à préparer", """<ol>
<li><strong>Activité</strong> : que vend-on, que prépare-t-on sur place, combien de personnes travaillent ?</li>
<li><strong>Client</strong> : qui entre, pourquoi, combien de temps reste-t-il, combien dépense-t-il ?</li>
<li><strong>Format</strong> : surface de vente, réserve, laboratoire ou cuisine, places assises.</li>
<li><strong>Budget</strong> : l'enveloppe globale, y compris préouverture.</li>
<li><strong>Échéance</strong> : date d'ouverture souhaitée, date à laquelle le loyer commence à courir.</li>
<li><strong>Local</strong> : adresse, photos, plans, annonce, projet de bail ou bail signé.</li>
</ol>"""),
            ("Les documents utiles", """<ul>
<li>Le projet de bail et ses annexes : diagnostic de performance énergétique, état des risques, inventaire des charges.</li>
<li>Les plans du local et ceux de l'immeuble, s'ils existent.</li>
<li>Le règlement de copropriété et les derniers procès-verbaux d'assemblée.</li>
<li>Les autorisations obtenues par l'exploitant précédent, s'il y en a.</li>
<li>Votre concept : planche d'ambiance, références, charte de marque.</li>
</ul>"""),
            ("Ensuite", """<p>Envoyez ces éléments par le <a href="/etudier-mon-projet">formulaire</a> ou appelez le 09 70 70 17 99. Si le bail n'est pas signé, la priorité est la visite du local : le <a href="/diagnostic-local-commercial">diagnostic en 12 questions</a> vous prépare à cette visite.</p>"""),
        ],
        "sources": ["l12629", "l1255", "l145402"],
        "related": ["/diagnostic-local-commercial", "/avant-signature-bail-commercial", "/guides/budget-renovation-commerce"],
    },
    {
        "path": "/guides/erp-commerce-categorie-effectif", "kind": "guide", "short": "Classement ERP d'un commerce",
        "teaser": "Type M ou N, effectif, catégorie, sorties.",
        "title": "Classement ERP d'un commerce : type M, type N, effectif, catégorie | Kalya",
        "description": "Classer un commerce en ERP : type M ou N, calcul de l'effectif (M 2, N 2), seuils de la 5e catégorie (PE 2), catégories 1 à 4, sorties (PE 11), obligations.",
        "h1": "Classement ERP d'un commerce : type, effectif, catégorie",
        "answer": "Un commerce ouvert au public est un ERP. Son type dépend de l'activité (M pour un magasin, N pour un restaurant ou un bar) et sa catégorie de l'effectif (public seul pour la 5e catégorie ; public et personnel sans dégagements propres pour les catégories 1 à 4). Un magasin reste en 5e catégorie sous 100 personnes au sous-sol, 100 aux étages et 200 au total ; un restaurant sous 100, 200 et 200 (règlement de sécurité, PE 2).",
        "cta": "Calculer mon effectif", "cta_href": "/calcul-effectif-erp-commerce",
        "bullets": [
            "Catégories : 1re au-delà de 1 500 personnes, 2e de 701 à 1 500, 3e de 301 à 700, 4e 300 et moins hors 5e (code de la construction, R143-19).",
            "Magasin : 1 personne pour 3 m² de surface de vente au sous-sol, au rez-de-chaussée et au 1er étage (M 2).",
            "Restaurant : places assises déclarées dans la limite d'1 personne pour 2 m² ; debout 2 par m² (N 2).",
            "Le personnel ne compte pas pour classer en 5e catégorie (GN 1, PE 3) ; il compte pour les catégories 1 à 4 (R143-19) et pour les sorties s'il n'a pas les siennes (PE 11 § 5).",
        ],
        "sections": [
            ("Type et catégorie", """<p>Le classement d'un ERP se lit en deux dimensions : une lettre pour le <strong>type</strong>, selon la nature réelle de l'exploitation, et un chiffre pour la <strong>catégorie</strong>, selon l'effectif. Les magasins de vente et centres commerciaux relèvent du type M ; les restaurants et débits de boissons du type N. La catégorie suit l'effectif total (R143-19) : 1re au-delà de 1 500 personnes, 2e de 701 à 1 500, 3e de 301 à 700, 4e jusqu'à 300 lorsque l'établissement n'est pas en 5e catégorie.</p>"""),
            ("Calculer l'effectif d'un magasin (type M)", M2_TABLE + """<p>En 5e catégorie, pour les boutiques à rez-de-chaussée de moins de 500 m² ne comportant que des circulations principales d'au moins 1,80 m, l'effectif se calcule à 1 personne par m² sur le tiers de la surface des locaux accessibles au public (PE 3).</p>"""),
            ("Calculer l'effectif d'un restaurant (type N)", """<div class="table-wrap"><table><caption class="sr">Densité d'occupation des restaurants (article N 2)</caption>
<thead><tr><th scope="col">Zone</th><th scope="col">Effectif théorique</th></tr></thead>
<tbody>
<tr><td>Assise, avec déclaration contrôlée du nombre de places</td><td>Nombre déclaré, dans la limite d'1 personne pour 2 m²</td></tr>
<tr><td>Assise, sans déclaration</td><td>1 personne par m²</td></tr>
<tr><td>Debout</td><td>2 personnes par m²</td></tr>
<tr><td>Files d'attente</td><td>3 personnes par m²</td></tr>
</tbody></table></div>
<p>La surface est diminuée des estrades des musiciens et des aménagements fixes autres que les tables et les sièges (N 2). La déclaration précise la capacité maximale par niveau.</p>"""),
            ("Les seuils de la 5e catégorie", """<div class="table-wrap"><table><caption class="sr">Seuils de la 5e catégorie (article PE 2)</caption>
<thead><tr><th scope="col">Type</th><th scope="col">Sous-sol</th><th scope="col">Étages</th><th scope="col">Ensemble des niveaux</th></tr></thead>
<tbody>
<tr><td>M, magasins de vente</td><td>moins de 100</td><td>moins de 100</td><td>moins de 200</td></tr>
<tr><td>N, restaurants et débits de boissons</td><td>moins de 100</td><td>moins de 200</td><td>moins de 200</td></tr>
</tbody></table></div>
<p>L'établissement reste en 5e catégorie tant que l'effectif du public est inférieur à chacun de ces nombres.</p>"""),
            ("Sorties et obligations de base en 5e catégorie", DEGAGEMENTS + """<p>Autres exigences du règlement pour les petits établissements : désenfumage des salles de plus de 300 m² en rez-de-chaussée ou en étage et de plus de 100 m² en sous-sol (PE 14) ; éclairage de sécurité dans les escaliers, les circulations de plus de 10 m ou compliquées et les salles de plus de 100 m² (PE 24) ; au moins un extincteur par niveau, avec un appareil pour 300 m² au minimum, une alarme, des consignes affichées (PE 26 et PE 27) ; installations vérifiées au moins tous les trois ans (PE 4).</p>"""
             + erp_link('/securite-incendie-erp/', 'Sécurité incendie d\'un ERP de 5e catégorie', 'Le règlement PE article par article, sur dossier-erp-paris.fr.')),
        ],
        "sources": ["gn1", "r14319", "pe2", "pe3", "m2", "n2", "pe11", "pe14", "pe24", "pe26", "pe4"],
        "related": ["/calcul-effectif-erp-commerce", "/architecte-boutique", "/architecte-restaurant", DEP + "/classement-erp-types-categories/"],
    },
    {
        "path": "/guides/accessibilite-commerce", "kind": "guide", "short": "Accessibilité d'un commerce",
        "teaser": "Bâti existant, 5e catégorie, dérogations, registre.",
        "title": "Accessibilité d'un commerce : règles, dérogations, registre public | Kalya",
        "description": "Accessibilité d'une boutique ou d'un restaurant dans un bâtiment existant : règles applicables, 5e catégorie, dérogations motivées, attestation, registre public.",
        "h1": "Accessibilité d'un commerce : ce que la petite taille ne dispense pas",
        "answer": "Un commerce qui s'installe dans un bâtiment existant relève des règles des ERP existants (code de la construction, R164-1 ; arrêté du 8 décembre 2014). En 5e catégorie, une partie du local, au plus près de l'entrée, doit donner accès à l'ensemble des prestations (R164-2). Une dérogation se motive point par point, et tout ERP tient un registre public d'accessibilité.",
        "bullets": [
            "Bâti existant : articles R164-1 à R164-6 et arrêté du 8 décembre 2014 ; construction neuve : arrêté du 20 avril 2017.",
            "5e catégorie : une partie du bâtiment donnant accès à l'ensemble des prestations, mesures de substitution possibles.",
            "Dérogations : impossibilité technique, patrimoine, disproportion manifeste, refus de la copropriété dans les conditions du texte (R164-3).",
            "Nouveaux Ad'AP : plus de dépôt depuis le 31 mars 2019.",
            "Registre public d'accessibilité pour tout ERP, 5e catégorie comprise (R164-6).",
        ],
        "sections": [
            ("Quel texte pour quel local ?", """<p>Un commerce nouvellement ouvert dans un bâtiment existant n'est pas, pour ce seul motif, une construction neuve : il relève des articles R164-1 à R164-6 du code de la construction et de l'arrêté du 8 décembre 2014. La construction d'un ERP relève, elle, des articles R162-8 et suivants et de l'arrêté du 20 avril 2017. Une opération mixte se qualifie partie par partie.</p>"""),
            ("Ce qu'on examine dans un commerce", """<ol>
<li>le cheminement depuis le trottoir jusqu'à l'entrée ;</li>
<li>l'entrée, la porte, le seuil, l'accueil ;</li>
<li>les circulations, les changements de niveau ;</li>
<li>les équipements utilisés par le public : caisse, cabines, présentoirs ;</li>
<li>les sanitaires, lorsqu'ils sont ouverts au public ;</li>
<li>l'information, l'éclairage, l'acoustique.</li>
</ol>
<p>Les cotes précises figurent dans l'arrêté applicable : elles ne se devinent pas.</p>"""),
            ("La 5e catégorie n'est pas une dispense", """<p>Dans un ERP existant de 5e catégorie, l'obligation porte sur une partie du bâtiment qui permet d'accéder à l'ensemble des prestations, située le plus près possible de l'entrée principale et desservie par le cheminement usuel ; certaines prestations peuvent être délivrées par des mesures de substitution. Une petite surface ne suffit ni à justifier une dérogation ni à écarter l'obligation.</p>"""),
            ("Dérogations, attestation, registre", """<p>Une dérogation se demande pour un point identifié, dans l'un des cas prévus : impossibilité technique, conservation du patrimoine architectural, disproportion manifeste entre les améliorations et leurs conséquences, refus de l'assemblée générale des copropriétaires dans les conditions du texte (R164-3). Elle se justifie dans le dossier d'autorisation de travaux, avec les mesures de substitution proposées.</p>
<p>Un ERP conforme le déclare par une attestation d'accessibilité (R165-3) ; en 5e catégorie, elle peut prendre la forme d'une déclaration sur l'honneur. Les nouveaux agendas d'accessibilité programmée ne se déposent plus depuis le 31 mars 2019. Enfin, tout ERP met à disposition du public un registre public d'accessibilité, mis à jour, au principal point d'accueil (R164-6, arrêté du 19 avril 2017).</p>"""
             + erp_link('/accessibilite-erp-paris/', 'Accessibilité des ERP à Paris', 'Règles, dérogations, attestations et registre, en détail, sur dossier-erp-paris.fr.')),
        ],
        "sources": ["r1641", "r1642", "a2014", "r1643", "r1653", "adap", "r1646", "a2017reg"],
        "related": ["/amenagement-local-commercial", "/architecte-institut-beaute-coiffure", DEP + "/accessibilite-erp-paris/"],
    },
    {
        "path": "/guides/enseigne-paris", "kind": "guide", "short": "Enseigne à Paris",
        "teaser": "Autorisation, Cerfa 16308, deux mois, extinction.",
        "title": "Enseigne de commerce à Paris : autorisation, dossier, délai | Kalya",
        "description": "Enseigne à Paris : autorisation du maire (L581-18), Cerfa 16308*01 en ligne, dossier, accord de l'ABF, deux mois (R581-13), extinction de 1 h à 6 h.",
        "h1": "Enseigne à Paris : l'autorisation, le dossier, le délai",
        "answer": "À Paris, toute enseigne est soumise à autorisation du maire, parce que la ville est couverte par un règlement local de publicité (code de l'environnement, L581-18). La demande se fait en ligne sur le Cerfa n° 16308*01. L'autorité statue dans les deux mois d'un dossier complet ; son silence vaut accord (R581-13). Les enseignes lumineuses s'éteignent entre 1 h et 6 h quand l'activité a cessé.",
        "bullets": [
            "Autorisation obligatoire dans les communes dotées d'un règlement local de publicité et dans les secteurs protégés (L581-18).",
            "Procédure réécrite au 1er juillet 2026 (décret n° 2025-1354) : demande présentée par la personne ou l'entreprise qui exerce l'activité signalée (R581-9) ; formulaire en vigueur : Cerfa n° 16308*01.",
            "À Paris, dépôt uniquement en ligne depuis le 1er octobre 2025.",
            "Deux mois, silence valant accord (R581-13) ; ce texte ne prévoit pas de majoration lorsque l'accord de l'architecte des Bâtiments de France est requis (R581-16-1).",
            "Extinction de 1 h à 6 h si l'activité a cessé ; clignotement interdit sauf pharmacie et services d'urgence (R581-59).",
        ],
        "sections": [
            ("Pourquoi une autorisation à Paris", """<p>L'installation d'une enseigne est soumise à autorisation sur les immeubles et dans les lieux protégés, ainsi que dans le cadre d'un règlement local de publicité (code de l'environnement, L581-18). Paris étant couverte par un tel règlement, toute enseigne y est soumise à autorisation, y compris le remplacement d'une enseigne existante. Le règlement local peut être plus restrictif que le règlement national.</p>"""),
            ("Le dossier", """<p>Depuis le 1er juillet 2026 (décret n° 2025-1354), la demande est présentée par la personne ou l'entreprise qui exerce l'activité signalée (R581-9) ; le formulaire en vigueur est le Cerfa n° 16308*01. Le dossier montre l'enseigne dans son environnement : mise en situation, vues avec et sans le dispositif, document graphique d'intégration à la façade. À Paris, il se dépose sur le téléservice de la Ville « Terrasses, étalages, enseignes ».</p>
<p>Sur un immeuble protégé, aux abords d'un monument historique ou en site patrimonial remarquable, l'autorisation est délivrée après accord de l'architecte des Bâtiments de France.</p>"""),
            ("Le délai", """<p>L'autorité statue dans les deux mois suivant la réception d'un dossier complet. Le dossier est réputé complet si aucune pièce n'est demandée dans le mois. À défaut de notification dans le délai, l'autorisation est réputée accordée (R581-13). Nous n'avons trouvé aucune majoration à quatre mois en cas d'accord de l'architecte des Bâtiments de France dans la version en vigueur.</p>"""),
            ("L'enseigne allumée", """<p>Les enseignes lumineuses sont éteintes entre 1 heure et 6 heures lorsque l'activité signalée a cessé. Si l'activité cesse ou commence entre minuit et 7 heures, l'enseigne s'éteint au plus tard une heure après la fermeture et peut s'allumer une heure avant l'ouverture. Les enseignes clignotantes sont interdites, sauf pour les pharmacies et les services d'urgence (R581-59).</p>"""),
        ],
        "faq": [
            {"q": "Faut-il une autorisation pour remplacer une enseigne existante ?", "a": "<p>Oui à Paris : l'installation de toute enseigne est soumise à autorisation (L581-18). Une nouvelle enseigne, même à l'emplacement de l'ancienne, fait l'objet d'une demande d'autorisation.</p>"},
            {"q": "Le Cerfa 14798 est-il encore valable ?", "a": "<p>La fiche officielle indique désormais le Cerfa n° 16308*01 pour la demande d'autorisation préalable d'une enseigne. À Paris, la demande se fait en ligne.</p>"},
        ],
        "sources": ["l58118", "r5819", "r58113", "r581161", "cerfa16308", "parisenseignes", "r58159", "spr"],
        "related": ["/vitrine-et-devanture-commerce", "/guides/autorisations-travaux-commerce", "/guides/plu-paris-commerce"],
    },
    {
        "path": "/guides/extraction-restaurant-paris", "kind": "guide", "short": "Extraction d'un restaurant",
        "teaser": "RSD de Paris, conduit, copropriété.",
        "title": "Extraction d'un restaurant à Paris : RSD, conduit, copropriété | Kalya",
        "description": "Extraction d'un restaurant à Paris : rejet à 8 m de toute fenêtre (RSD, art. 63-1), hotte et conduit unique, nettoyage mensuel, vote de la copropriété.",
        "h1": "Extraction d'un restaurant à Paris : la question à régler avant le bail",
        "answer": "À Paris, le règlement sanitaire départemental impose de rejeter l'air des cuisines sans recyclage, à au moins 8 m de toute fenêtre ou prise d'air neuf, sauf aménagements empêchant toute reprise d'air pollué (art. 63-1), par une hotte débordante raccordée à un conduit unique, indépendant des conduits de fumée, nettoyé avec ses filtres au moins une fois par mois (art. 130-3). Le tracé du conduit se vérifie avant de signer.",
        "bullets": [
            "Cuisines : locaux à pollution spécifique, air extrait sans recyclage (RSD de Paris, art. 63-1).",
            "Rejet à au moins 8 m de toute fenêtre, de toute prise d'air neuf, de tout débouché de conduit de fumée et de tout conduit de ventilation, sauf aménagements empêchant toute reprise d'air pollué (art. 63-1).",
            "Hotte débordante, conduit unique indépendant des conduits de fumée, sans gêne pour le voisinage (art. 130-3).",
            "Conduits et filtres à graisse nettoyés au moins une fois par mois (art. 130-3).",
            "Conduit sur les parties communes : vote de l'assemblée générale (loi du 10 juillet 1965, art. 25 b).",
        ],
        "sections": [
            ("Ce que dit le règlement sanitaire de Paris", """<p>Le règlement sanitaire départemental de Paris range les cuisines parmi les locaux à pollution spécifique : l'air extrait ne peut pas être recyclé et doit être rejeté « à au moins huit mètres de toute fenêtre, de toute prise d'air neuf », de tout débouché de conduit de fumée et de tout conduit de ventilation, « sauf aménagements tels qu'une reprise d'air pollué ne soit pas possible » (art. 63-1). Les fourneaux sont équipés d'une hotte débordante à captage total, raccordée à un conduit de ventilation unique, indépendant des conduits de fumée ; l'installation ne doit pas gêner le voisinage, et conduits et filtres à graisse sont nettoyés au moins une fois par mois (art. 130-3). Ces règles s'appliquent aux cuisines des restaurants (art. 152-2) comme aux laboratoires de préparation.</p>
<p>Les articles consultés ne fixent pas de hauteur de rejet en toiture. La règle souvent citée des 40 cm vient de l'arrêté du 22 octobre 1969 (art. 18), qui vise les orifices des conduits de fumée à tirage naturel desservant des logements. Les textes consultés n'établissent pas qu'elle s'applique à l'extraction mécanique d'une cuisine professionnelle.</p>"""),
            ("Trouver le tracé", """<p>La faisabilité tient au tracé du conduit, de la hotte au point de rejet :</p>
<ul>
<li>une gaine existante, réutilisable, d'une section suffisante ;</li>
<li>une cour intérieure, avec un rejet qui respecte la distance aux fenêtres ;</li>
<li>une façade arrière ou une toiture accessibles, avec l'accord de la copropriété ;</li>
<li>des traversées de planchers et de logements, souvent impossibles en pratique.</li>
</ul>
<p>Un relevé du local et de l'immeuble, avant le bail, dit si l'un de ces tracés existe. Sans tracé, le projet de cuisson n'est pas faisable en l'état.</p>"""),
            ("Copropriété et bail", """<p>La façade (gros œuvre) et les gaines sont présumées parties communes ; y faire passer un conduit demande l'autorisation de l'assemblée générale, à la majorité de l'article 25 b de la loi du 10 juillet 1965. Le règlement de copropriété peut aussi encadrer l'activité exercée dans les lots. Côté bail, la destination doit autoriser la restauration ; l'autorisation des travaux d'extraction, le sort des ouvrages et la remise en état se lisent dans les clauses du bail. C'est le bailleur, copropriétaire, qui porte la demande à l'assemblée générale.</p>"""),
        ],
        "sources": ["rsd631", "rsd1303", "copro25", "copro3", "copro8", "copro9"],
        "related": ["/architecte-restaurant", "/avant-signature-bail-commercial", "/architecte-metiers-de-bouche"],
    },
    {
        "path": "/guides/bail-commercial-travaux", "kind": "guide", "short": "Bail commercial et travaux",
        "teaser": "Destination, charges, état des lieux, loi de 2026.",
        "title": "Bail commercial et travaux : charges, annexes, loi 2026 | Kalya",
        "description": "Bail commercial et travaux : durée, destination et déspécialisation, charges non imputables (R145-35), état des lieux, annexes, loi du 26 mai 2026.",
        "h1": "Bail commercial et travaux : ce que la loi fixe, ce que le bail décide",
        "answer": "Le bail commercial est conclu pour neuf ans au moins, avec une faculté de congé du locataire à chaque période triennale, sauf exceptions (code de commerce, L145-4). Sa clause de destination fixe l'activité autorisée. La loi interdit d'imputer au locataire les grosses réparations de l'article 606 du code civil (R145-35) et impose un état des lieux, un inventaire des charges, le DPE et l'état des risques. Pour les baux conclus ou renouvelés depuis la loi du 26 mai 2026, les garanties sont limitées à un trimestre de loyer.",
        "bullets": [
            "Durée : neuf ans au moins ; bail dérogatoire : trois ans au plus (L145-4, L145-5).",
            "Activité connexe : notification au bailleur, qui a deux mois pour en contester le caractère connexe ou complémentaire (L145-47) ; activité différente : L145-48.",
            "Non imputables au locataire : grosses réparations de l'article 606 et mise en conformité qui en relève (R145-35).",
            "État des lieux d'entrée, inventaire des charges et état des travaux obligatoires (L145-40-1, L145-40-2).",
            "Loi du 26 mai 2026 : loyer mensuel de droit à la demande du preneur (L145-32-1) ; garanties plafonnées à un trimestre pour les baux conclus ou renouvelés depuis la loi (L145-40).",
        ],
        "sections": [
            ("Durée et destination", """<p>La durée du bail commercial ne peut être inférieure à neuf ans ; le preneur peut en principe donner congé à l'expiration de chaque période triennale, sauf exceptions (bail de plus de neuf ans, locaux monovalents, bureaux, stockage) (L145-4). Un bail dérogatoire ne peut excéder trois ans (L145-5).</p>
<p>La clause de destination fixe les activités autorisées. Pour adjoindre une activité connexe ou complémentaire, le preneur en informe le bailleur, qui dispose de deux mois pour contester ce caractère (L145-47). Pour exercer une activité différente, la déspécialisation plénière suit l'article L145-48 et les suivants.</p>"""),
            ("Charges et travaux : la ligne de partage", """<p>Ne peuvent pas être imputées au locataire les dépenses relatives aux grosses réparations de l'article 606 du code civil (gros murs, voûtes, poutres, couvertures entières), ni celles de mise en conformité lorsqu'elles relèvent de ces grosses réparations (R145-35). Le bail comporte un inventaire précis et limitatif des catégories de charges, impôts, taxes et redevances ; le bailleur communique à la conclusion du bail, puis tous les trois ans, l'état prévisionnel des travaux des trois années suivantes et l'état récapitulatif des trois années précédentes (L145-40-2).</p>
<p>Pour les travaux du preneur, la loi pose surtout la restitution des lieux conforme à l'état des lieux (code civil, art. 1730 et suivants). L'autorisation des travaux, leur sort en fin de bail et la remise en état se lisent dans les clauses : à négocier avant de signer, chiffrage à l'appui.</p>"""),
            ("Annexes et documents obligatoires", """<ul>
<li><strong>État des lieux</strong> d'entrée, établi contradictoirement (L145-40-1).</li>
<li><strong>Diagnostic de performance énergétique</strong>, joint au contrat de location (code de la construction, L126-29).</li>
<li><strong>État des risques</strong>, annexé aux baux commerciaux (code de l'environnement, L125-5).</li>
<li><strong>Annexe environnementale</strong> pour les locaux de plus de 2 000 m² de bureaux ou de commerces.</li>
<li><strong>Dossier technique amiante</strong> tenu à la disposition des occupants pour les immeubles dont le permis est antérieur au 1er juillet 1997 (code de la santé publique, R1334-29-5) ; il n'a pas à être annexé au bail.</li>
</ul>"""),
            ("Ce qui change avec la loi du 26 mai 2026", """<p>La loi n° 2026-403 du 26 mai 2026 a modifié le chapitre du code de commerce consacré au bail commercial. Le paiement mensuel du loyer est de droit lorsque le preneur le demande, en l'absence d'arriérés (L145-32-1). Le dépôt de garantie et les autres garanties ne peuvent excéder le montant des loyers d'un trimestre ; le dépôt est restitué dans un délai de trois mois au plus après la remise des clés (L145-40). Le paiement mensuel vaut aussi pour les baux en cours ; le plafond des garanties vise les baux conclus ou renouvelés à compter de la promulgation de la loi (la fiche service-public F23927 retient le 28 mai 2026).</p>"""),
        ],
        "sources": ["l1454", "l1455", "l14547", "l14548", "r14535", "l145401", "l145402", "l12629", "l1255", "l1259", "r133429", "l145321", "l14540"],
        "related": ["/avant-signature-bail-commercial", "/guides/budget-renovation-commerce", "/guides/changement-destination-local-commercial"],
    },
    {
        "path": "/guides/changement-destination-local-commercial", "kind": "guide", "short": "Changement de destination",
        "teaser": "Destination, sous-destination, usage, ERP.",
        "title": "Changement de destination d'un local commercial : DP, PC, PLU, ERP | Kalya",
        "description": "Changer la destination d'un local : destinations et sous-destinations, déclaration préalable ou permis, PLU de Paris, changement d'usage, type d'ERP.",
        "h1": "Changement de destination d'un local commercial : trois régimes à ne pas confondre",
        "answer": "Changer d'activité dans un local fait jouer trois régimes : la destination d'urbanisme (déclaration préalable entre destinations, permis si la façade ou la structure change en même temps), le classement ERP (le type change avec l'activité) et, pour un logement à Paris, le changement d'usage. Entre sous-destinations d'une même destination, comme boutique et restaurant, aucune déclaration n'est due sans travaux.",
        "bullets": [
            "Cinq destinations, dont « commerce et activités de service » et « autres activités des secteurs primaire, secondaire ou tertiaire » (R151-27).",
            "Sous-destinations du commerce : artisanat et commerce de détail, restauration, commerce de gros, services avec accueil d'une clientèle, cinéma, hôtels, autres hébergements touristiques (R151-28).",
            "Déclaration préalable entre destinations ; pas de contrôle entre sous-destinations d'une même destination (R*421-17 b).",
            "Permis si la structure porteuse ou la façade change avec la destination ou la sous-destination (R*421-14 c).",
            "Même sans formalité, le PLU s'applique (L421-8) : à Paris, les linéaires protégés (UG.1.4.2).",
        ],
        "sections": [
            ("Destinations et sous-destinations", """<p>Le code de l'urbanisme compte cinq destinations : exploitation agricole et forestière ; habitation ; commerce et activités de service ; équipements d'intérêt collectif et services publics ; autres activités des secteurs primaire, secondaire ou tertiaire (R151-27). La destination « commerce et activités de service » se divise en artisanat et commerce de détail, restauration, commerce de gros, activités de services où s'effectue l'accueil d'une clientèle, cinéma, hôtels et autres hébergements touristiques (R151-28). Le bureau, l'entrepôt et la cuisine dédiée à la vente en ligne appartiennent à la cinquième destination.</p>"""),
            ("Quelle formalité ?", """<div class="table-wrap"><table><caption class="sr">Formalités d'urbanisme selon le changement</caption>
<thead><tr><th scope="col">Situation</th><th scope="col">Formalité</th></tr></thead>
<tbody>
<tr><td>Bureau devenant boutique, sans travaux sur la façade ou la structure</td><td>Déclaration préalable (R*421-17 b)</td></tr>
<tr><td>Boutique devenant restaurant, sans travaux</td><td>Aucune au titre du changement (même destination), PLU applicable</td></tr>
<tr><td>Changement avec travaux sur la façade ou la structure porteuse</td><td>Permis de construire (R*421-14 c)</td></tr>
<tr><td>Changement avec seulement une devanture refaite</td><td>Déclaration préalable au titre de l'aspect extérieur (R*421-17 a)</td></tr>
</tbody></table></div>
<p>La frontière entre « modifier l'aspect extérieur » et « modifier la façade » s'apprécie projet par projet ; dans le doute, elle se tranche avant le dépôt.</p>"""),
            ("Paris : ce que le PLU interdit", """<p>Sur les voies protégées du PLU bioclimatique, un rez-de-chaussée sur rue en artisanat et commerce de détail, restauration ou commerce de gros ne peut pas changer pour une autre sous-destination, sauf activités médicales et paramédicales de proximité ; sur les linéaires d'artisanat de proximité ou de commerce culturel, l'activité elle-même est protégée (UG.1.4.2). En zone UG, le changement de destination ou de sous-destination en entrepôt d'un local existant en rez-de-chaussée sur rue est interdit, sauf équipements de logistique urbaine (UG.1.3.1) ; le changement en cuisine dédiée à la vente en ligne l'est aussi (UG.1.3.5). Ces règles s'appliquent même sans formalité (L421-8).</p>"""),
            ("ERP et usage : deux autres régimes", """<p>Changer d'activité change souvent le type d'ERP (boutique en type M, restaurant en type N, agence en type W) : les travaux d'aménagement relèvent de l'autorisation de travaux (L122-3), même si l'urbanisme n'exige rien ; sans travaux, l'utilisation du local pour une autre destination peut exiger une nouvelle autorisation d'ouverture. Transformer un logement en local commercial à Paris relève en plus du changement d'usage, soumis à autorisation de la Ville.</p>"""
             + erp_link('/changement-destination-erp-paris/', 'Changement de destination et ERP à Paris', 'Comment s\'articulent urbanisme, ERP et usage, sur dossier-erp-paris.fr.')
             + erp_link('/changement-usage-paris-erp/', 'Changement d\'usage à Paris', 'Le régime propre aux logements, à ne pas confondre avec la destination.')),
        ],
        "sources": ["r15127", "r15128", "a2016", "r42117", "r42114", "r42114b", "l4218", "plubreg", "l1223"],
        "related": ["/guides/plu-paris-commerce", "/architecte-restaurant", DEP + "/changement-destination-erp-paris/", DEP + "/changement-usage-paris-erp/"],
    },
    {
        "path": "/guides/plu-paris-commerce", "kind": "guide", "short": "PLU de Paris et commerce",
        "teaser": "Linéaires protégés, devantures, dark stores.",
        "title": "PLU bioclimatique de Paris et commerces : linéaires, devantures | Kalya",
        "description": "Le PLU bioclimatique de Paris et les commerces : rez-de-chaussée protégés (UG.1.4.2), devantures (UG.2.1.4), dark stores et dark kitchens interdits sur rue.",
        "h1": "PLU de Paris et commerce : les rez-de-chaussée sous protection",
        "answer": "Le PLU bioclimatique de Paris, approuvé le 20 novembre 2024, protège 329 km de linéaires où un rez-de-chaussée commercial doit rester commerce, artisanat, restauration ou commerce de gros (ou activité médicale et paramédicale de proximité), plus 29 km pour l'artisanat de proximité et 9 km pour le commerce culturel. Il encadre aussi les devantures et interdit les dark stores et dark kitchens en rez-de-chaussée sur rue.",
        "bullets": [
            "Trois protections des rez-de-chaussée : commerce et artisanat ; commerce artisanal de proximité ; commerce culturel (UG.1.4.2).",
            "Les locaux d'angle sont protégés en totalité, même si l'une des voies ne l'est pas.",
            "Devantures : de préférence dans le plan de la façade, en applique ou en feuillure avec un retrait limité de 10 à 20 cm ; vitrage le plus clair possible et non réfléchissant ; coffres et grilles à l'intérieur, sauf impossibilité technique ou architecturale (UG.2.1.4).",
            "Pas de changement vers entrepôt ni vers cuisine dédiée à la vente en ligne en rez-de-chaussée sur rue (UG.1.3.1, UG.1.3.5).",
            "Une carte en données ouvertes situe les linéaires ; elle n'a pas de valeur réglementaire.",
        ],
        "sections": [
            ("Les protections des rez-de-chaussée", """<p>L'article UG.1.4.2 s'applique aux locaux à rez-de-chaussée situés en bordure des voies repérées sur les documents graphiques, et à la totalité des locaux d'angle :</p>
<ul>
<li><strong>Protection du commerce et de l'artisanat</strong> : le changement de sous-destination d'un local en artisanat et commerce de détail, restauration ou commerce de gros, ou affecté à des activités médicales et paramédicales de proximité, vers une sous-destination ou une activité autre que celles-ci est interdit. Une boutique peut devenir un restaurant ; elle ne peut pas devenir une agence ou un bureau.</li>
<li><strong>Protection particulière du commerce artisanal de proximité</strong> : même règle, et un local affecté au commerce artisanal de proximité ne peut pas devenir une autre activité.</li>
<li><strong>Protection particulière du commerce culturel</strong> : même règle pour le commerce culturel (établissements commerciaux destinés principalement à la vente de biens culturels, selon le lexique du PLU).</li>
<li><strong>Sites de protection des grands magasins</strong> : la part de commerce et de restauration ne peut pas diminuer.</li>
</ul>
<p>Selon la Ville de Paris, ces protections couvrent 329 km de voies, auxquels s'ajoutent 29 km pour les commerces artisanaux et 9 km pour les commerces culturels.</p>"""),
            ("Devantures et rez-de-chaussée ouverts", """<p>L'article UG.2.1.4 demande des devantures intégrées à la composition de la façade, interdit les comptoirs ouverts sur la voie sans devanture, place les devantures de préférence dans le plan de la façade, suivant ses caractéristiques (en applique, ou en feuillure avec un retrait limité de 10 à 20 cm), demande un vitrage le plus clair possible et non réfléchissant, et des coffres et grilles à l'intérieur, sauf impossibilité technique ou architecturale. L'article UG.2.1.3 demande des rez-de-chaussée ouverts sur l'espace public, sans locaux aveugles en bordure de voie. Voir <a href="/vitrine-et-devanture-commerce">vitrine et devanture</a>.</p>"""),
            ("Dark stores et dark kitchens", """<p>Le changement de destination ou de sous-destination en entrepôt des locaux existants en rez-de-chaussée sur rue est interdit, sauf équipements de logistique urbaine (UG.1.3.1). Le changement en cuisine dédiée à la vente en ligne est également interdit pour ces locaux (UG.1.3.5). Les points permanents de livraison, ou de livraison et de retrait, d'achats au détail commandés en ligne relèvent de la sous-destination entrepôt (arrêté du 10 novembre 2016, art. 5) ; les locaux où les clients retirent exclusivement des produits stockés sur place et commandés en ligne relèvent de l'artisanat et du commerce de détail (art. 3).</p>"""),
            ("Vérifier une adresse", """<p>La Ville publie en données ouvertes une carte des protections du commerce et de l'artisanat. Elle aide à repérer une rue, mais n'a pas de valeur réglementaire : seul le règlement graphique du PLU fait foi. Le PLU approuvé le 20 novembre 2024 a fait l'objet de modifications simplifiées en décembre 2025 et en juin 2026 : la version en vigueur se vérifie à la date du projet.</p>"""),
        ],
        "sources": ["plub", "plubreg", "plubcarte", "a2016", "a2016e", "l4218", "spr"],
        "related": ["/architecte-commerce-paris", "/guides/changement-destination-local-commercial", "/vitrine-et-devanture-commerce", "/avant-signature-bail-commercial"],
    },
]
