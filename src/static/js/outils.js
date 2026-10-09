/* architecte-commerce.fr — outils : diagnostic de local, calcul d'effectif ERP.
   Tout est calculé dans le navigateur ; rien n'est enregistré ni transmis sans action de l'utilisateur. */
(function () {
  'use strict';
  var d = document;

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  /* ================================================================ Diagnostic de local */
  var diag = d.getElementById('diag');
  if (diag) {
    var LV = { nogo: 4, risk: 3, cond: 2, ok: 1 };
    var TAG = { nogo: ['tag-nogo', 'Bloquant'], risk: ['tag-risk', 'Risque'], cond: ['tag-cond', 'Condition'], ok: ['tag-ok', 'OK'] };
    var VERDICT = {
      nogo: ['Non pour ce format, en l\'état', 'Un point bloque l\'activité telle que décrite. Le local peut convenir à une autre activité : faites-le vérifier avant d\'abandonner, et surtout avant de signer.'],
      risk: ['Risque élevé : à faire vérifier avant de signer', 'Un ou plusieurs points peuvent faire échouer le projet ou le retarder fortement. Ne signez pas sans réponse écrite sur ces points.'],
      cond: ['Oui, sous conditions', 'Le projet paraît faisable si les démarches et les travaux listés sont menés. Intégrez-les au budget et au calendrier, et négociez-les avec le bailleur.'],
      ok: ['Oui, a priori', 'Rien de bloquant dans vos réponses. La visite du local le confirme, plans et documents en main.']
    };
    var ACT_LABEL = { boutique: 'Boutique ou concept store', resto: 'Restaurant, bar, café', froid: 'Restaurant, bar, café', beaute: 'Institut ou salon de coiffure', bouche: 'Boulangerie ou métier de bouche', showroom: 'Showroom' };
    var LABELS = {};
    diag.querySelectorAll('fieldset.q').forEach(function (fs) {
      LABELS[fs.dataset.q] = fs.querySelector('legend').textContent.replace(/^\d+\.\s*/, '');
    });

    function val(n) { var r = diag.querySelector('input[name="' + n + '"]:checked'); return r ? r.value : null; }

    function toggleOnly() {
      var act = val('act');
      diag.querySelectorAll('[data-only]').forEach(function (fs) {
        var show = !act || fs.dataset.only.split(' ').indexOf(act) >= 0;
        fs.hidden = !show;
      });
    }

    function evaluate() {
      var a = {};
      ['act', 'bail', 'avant', 'plu', 'extr', 'entree', 'niveaux', 'surface', 'facade', 'copro', 'elec', 'livr'].forEach(function (k) { a[k] = val(k); });
      var cook = a.act === 'resto' || a.act === 'bouche';
      var items = [];
      function add(lv, t, x, src) { items.push({ lv: lv, t: t, x: x, src: src }); }

      // Bail
      if (a.bail === 'non') add('risk', 'Bail : activité non autorisée', 'La clause de destination ne prévoit pas votre activité. Il faut l\'accord du bailleur (activité connexe, deux mois pour contester) ou une déspécialisation. À régler avant de signer.', 'Code de commerce, L145-47 et L145-48');
      else if (a.bail === 'nsp') add('cond', 'Bail : clause de destination à lire', 'Faites vérifier que la destination autorise votre activité, et les clauses de travaux et de remise en état.', 'Code de commerce, L145-47');
      else if (a.bail === 'oui') add('ok', 'Bail compatible', 'La destination prévue couvre votre activité.', '');

      // Usage et destination
      if (a.avant === 'logement') add('risk', 'Ancien logement : changement d\'usage', 'À Paris, transformer un logement en local commercial demande une autorisation de changement d\'usage de la Ville, en plus des démarches d\'urbanisme. Délai et faisabilité à vérifier en premier.', 'Ville de Paris, changement d\'usage');
      else if (a.avant === 'bureau' || a.avant === 'entrepot') add('cond', 'Changement de destination', 'Passer d\'un bureau ou d\'un entrepôt à un commerce change de destination : déclaration préalable, ou permis de construire si la façade ou la structure est modifiée.', 'Code de l\'urbanisme, R*421-17 b et R*421-14 c');
      else if (a.avant === 'nsp') add('cond', 'Destination actuelle à établir', 'La destination du local (commerce, bureau, logement) décide des démarches d\'urbanisme et d\'usage.', 'Code de l\'urbanisme, R151-27');

      // PLU Paris
      if (a.plu === 'part') add('risk', 'Rue à protection particulière', 'Sur ces linéaires, un local affecté au commerce artisanal de proximité ou au commerce culturel ne peut pas changer d\'activité. Vérifiez l\'activité actuelle du local et la vôtre.', 'PLU de Paris, UG.1.4.2');
      else if (a.plu === 'ca' && (a.act === 'beaute')) add('risk', 'Rue protégée et activité de service', 'Sur ces voies, un local de commerce ne peut pas devenir une activité de services hors des sous-destinations protégées. La qualification de votre activité (artisanat ou service) est à établir avant de signer.', 'PLU de Paris, UG.1.4.2');
      else if (a.plu === 'ca') add('ok', 'Rue protégée, activité compatible', 'La protection impose de rester en commerce, restauration ou artisanat : votre activité y entre.', 'PLU de Paris, UG.1.4.2');
      else if (a.plu === 'nsp') add('cond', 'Protection de la rue à vérifier', 'Consultez la carte des protections du commerce (sans valeur réglementaire), puis le règlement graphique du PLU.', 'PLU de Paris, UG.1.4.2');

      // Extraction
      if (cook) {
        if (a.extr === 'non') add('nogo', 'Cuisine sans extraction possible', 'À Paris, l\'air de cuisine est rejeté sans recyclage à 8 m au moins de toute fenêtre, par une hotte et un conduit propre. Sans tracé possible, la cuisson n\'est pas faisable en l\'état.', 'Règlement sanitaire de Paris, art. 63-1 et 130-3');
        else if (a.extr === 'trace') add('cond', 'Tracé d\'extraction à confirmer', 'Le tracé du conduit jusqu\'au point de rejet se vérifie sur place, avec la copropriété s\'il emprunte des parties communes.', 'RSD de Paris, art. 63-1 ; loi du 10 juillet 1965, art. 25 b');
        else if (a.extr === 'nsp') add('risk', 'Extraction inconnue', 'C\'est le premier point à vérifier pour une cuisine : sans conduit réalisable, pas de cuisson.', 'Règlement sanitaire de Paris, art. 63-1');
        else if (a.extr === 'oui') add('cond', 'Conduit existant à contrôler', 'Section, état, point de rejet et nettoyage : un conduit existant se contrôle avant d\'être réutilisé.', 'RSD de Paris, art. 130-3');
      }

      // Accessibilité
      if (a.entree === 'marche') add('cond', 'Ressaut à l\'entrée', 'L\'accessibilité reste due : adaptation de l\'entrée, solution d\'effet équivalent ou dérogation motivée, à intégrer au dossier.', 'Code de la construction, R164-1 et R164-3');
      else if (a.entree === 'marches') add('risk', 'Plusieurs marches à l\'entrée', 'Une solution d\'accès ou une dérogation motivée est à établir avant de signer ; une rampe sur le trottoir relève d\'une autorisation de la Ville.', 'Code de la construction, R164-1 et R164-3');
      else if (a.entree === 'nsp') add('cond', 'Entrée à relever', 'Hauteur du seuil, largeur de passage : à relever pendant la visite.', 'Code de la construction, R164-1');

      // Effectif, niveaux
      if (a.niveaux === 'oui') add('cond', 'Public à l\'étage ou au sous-sol', 'L\'effectif augmente, parfois la catégorie, et chaque niveau demande ses sorties. Calculez l\'effectif avant de signer.', 'Règlement de sécurité, PE 2 et PE 11');
      if (a.surface === 's4') add('cond', 'Grande surface ouverte au public', 'Au-delà de 300 m² en rez-de-chaussée ou en étage, une salle doit être désenfumée ; l\'effectif peut dépasser la 5e catégorie.', 'Règlement de sécurité, PE 14 et PE 2');

      // Façade
      if (a.facade === 'oui') add('cond', 'Devanture modifiée', 'Déclaration préalable, instruite en un mois ; la devanture suit les règles du PLU de Paris.', 'Code de l\'urbanisme, R*421-17 a ; PLU de Paris, UG.2.1.4');
      else if (a.facade === 'abf') add('cond', 'Devanture en secteur protégé', 'Déclaration préalable instruite en deux mois, avec l\'accord de l\'architecte des Bâtiments de France.', 'Code de l\'urbanisme, R423-24 et R*425-1');
      add('cond', 'Enseigne et autorisation de travaux', 'L\'enseigne demande une autorisation du maire (deux mois) ; l\'aménagement d\'un ERP, une autorisation de travaux (quatre mois).', 'Code de l\'environnement, L581-18 ; code de la construction, L122-3');

      // Copropriété
      if (a.copro === 'oui') add('cond', 'Vote de la copropriété', 'Travaux sur les parties communes ou l\'aspect extérieur : autorisation de l\'assemblée générale. Le calendrier dépend de la date de l\'assemblée.', 'Loi du 10 juillet 1965, art. 25 b');
      else if (a.copro === 'nsp') add('cond', 'Copropriété à interroger', 'Lisez le règlement de copropriété (clauses d\'activité) et les derniers procès-verbaux.', 'Loi du 10 juillet 1965, art. 8 et 9');

      // Réseaux, logistique
      if (a.elec === 'aug' || a.elec === 'nsp') add('cond', 'Puissance électrique', a.elec === 'aug' ? 'Une augmentation de puissance a un coût et un délai : à chiffrer avant de signer.' : 'À faire relever : froid, cuisson et climatisation en dépendent.', '');
      if (a.livr === 'non') add('risk', 'Livraisons et réserve', 'Un local mal desservi pèse chaque jour sur l\'exploitation. À arbitrer avant de signer.', '');
      else if (a.livr === 'lim') add('cond', 'Logistique limitée', 'Organisez livraisons, stockage et déchets dès le plan.', '');

      var worst = 'ok';
      items.forEach(function (i) { if (LV[i.lv] > LV[worst]) worst = i.lv; });
      items.sort(function (x, y) { return LV[y.lv] - LV[x.lv]; });
      return { a: a, items: items, worst: worst };
    }

    function render() {
      var r = evaluate();
      var missing = [];
      diag.querySelectorAll('fieldset.q').forEach(function (fs) {
        if (fs.hidden) return;
        if (!diag.querySelector('input[name="' + fs.dataset.q + '"]:checked')) missing.push(fs.dataset.q);
      });
      d.getElementById('diag-miss').textContent = missing.length ? (missing.length + ' question' + (missing.length > 1 ? 's' : '') + ' sans réponse : le verdict en tient compte comme « je ne sais pas ».') : '';
      var v = d.getElementById('verdict');
      var V = VERDICT[r.worst];
      var html = '<h3>' + esc(V[0]) + '</h3><p>' + esc(V[1]) + '</p><ul>';
      r.items.forEach(function (i) {
        html += '<li><span class="tag ' + TAG[i.lv][0] + '">' + TAG[i.lv][1] + '</span><b style="display:inline">' + esc(i.t) + '</b><br>' + esc(i.x) + (i.src ? '<br><span class="small muted">' + esc(i.src) + '</span>' : '') + '</li>';
      });
      html += '</ul><p class="small muted">Première lecture à partir de vos réponses : elle ne remplace pas la visite du local ni la lecture des documents.</p>';
      v.innerHTML = html;
      v.dataset.v = r.worst === 'ok' ? 'go' : r.worst;
      v.hidden = false;
      // résumé pour l'envoi
      var lines = ['Diagnostic de local (architecte-commerce.fr)', 'Verdict : ' + V[0], ''];
      Object.keys(LABELS).forEach(function (k) {
        var inp = diag.querySelector('input[name="' + k + '"]:checked');
        if (inp) lines.push(LABELS[k] + (/[?]$/.test(LABELS[k]) ? ' ' : ' : ') + inp.nextElementSibling.textContent);
      });
      lines.push('');
      r.items.forEach(function (i) { if (i.lv !== 'ok') lines.push('- [' + TAG[i.lv][1] + '] ' + i.t); });
      var send = d.getElementById('diag-send');
      if (send) {
        send.hidden = false;
        d.getElementById('f-diag').value = lines.join('\n');
        d.getElementById('f-act-h').value = ACT_LABEL[r.a.act] || 'Autre activité recevant du public';
      }
      return v;
    }

    var shown = false;
    diag.addEventListener('change', function () { toggleOnly(); if (shown) render(); });
    d.getElementById('diag-go').addEventListener('click', function () { shown = true; render().focus(); });
    toggleOnly();
  }

  /* ================================================================ Calcul d'effectif */
  var eff = d.getElementById('eff');
  if (eff) {
    function num(n) { var el = eff.querySelector('[name="' + n + '"]'); if (!el) return 0; var x = parseFloat(String(el.value).replace(',', '.').replace(/\s/g, '')); return isFinite(x) && x > 0 ? x : 0; }
    function up(x) { return Math.ceil(x - 1e-9); }
    function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ' '); }
    function degag(n) {
      if (n < 20) return '1 dégagement de 0,90 m';
      if (n <= 50) return '1 dégagement de 1,40 m sur l\'extérieur (parcours de 25 m au plus), ou 2 dégagements (0,90 m et 0,60 m)';
      if (n <= 100) return '2 dégagements de 0,90 m, ou 1 de 1,40 m et 1 de 0,60 m';
      if (n <= 200) return '1 dégagement de 1,40 m et 1 de 0,90 m';
      if (n <= 300) return '2 dégagements de 1,40 m';
      return 'au-delà de 300 personnes : règles des catégories 1 à 4';
    }
    function calc() {
      var type = eff.querySelector('input[name="type"]:checked').value;
      eff.querySelectorAll('[data-type]').forEach(function (b) { b.hidden = b.dataset.type !== type; });
      var cas = eff.querySelector('[name="mcas"]').value;
      eff.querySelector('[data-pro]').hidden = !(type === 'M' && cas === 'pro');
      var ss = 0, rdc = 0, et = 0, note = '';
      if (type === 'M') {
        var s = { ss: num('m_ss'), rdc: num('m_rdc'), e1: num('m_e1'), e2: num('m_e2'), e3: num('m_e3') };
        if (cas === 'std') { ss = s.ss / 3; rdc = s.rdc / 3; et = s.e1 / 3 + s.e2 / 6 + s.e3 / 15; }
        else if (cas === 'cc300') { ss = s.ss / 6; rdc = s.rdc / 6; et = (s.e1 + s.e2 + s.e3) / 6; }
        else if (cas === 'faible') { ss = s.ss / 9; rdc = s.rdc / 9; et = (s.e1 + s.e2 + s.e3) / 9; }
        else { rdc = num('m_decl'); note = 'Magasin réservé aux professionnels : l\'effectif déclaré est contrôlé par la commission ; il est compté ici au rez-de-chaussée.'; }
      } else {
        ['ss', 'rdc', 'et'].forEach(function (k) {
          var a = num('n_' + k + '_a'), p = num('n_' + k + '_p'), st = num('n_' + k + '_d'), f = num('n_' + k + '_f');
          var assis = p > 0 ? Math.min(p, a / 2) : a;
          var tot = assis + st * 2 + f * 3;
          if (k === 'ss') ss = tot; else if (k === 'rdc') rdc = tot; else et = tot;
          if (p > 0 && p > a / 2 && a > 0) note = 'Places déclarées plafonnées à 1 personne pour 2 m² de zone assise.';
        });
      }
      ss = up(ss); rdc = up(rdc); et = up(et);
      var pub = ss + rdc + et;
      var pers = up(num('pers'));
      var lim = type === 'M' ? [100, 100, 200] : [100, 200, 200];
      var cinq = ss < lim[0] && et < lim[1] && pub < lim[2];
      var cat, catTxt;
      if (cinq) { cat = '5e'; catTxt = '5e catégorie'; }
      else {
        var t = pub + pers;
        cat = t > 1500 ? '1re' : t > 700 ? '2e' : t > 300 ? '3e' : '4e';
        catTxt = cat + ' catégorie (public et personnel : ' + fmt(t) + ')';
      }
      var res = d.getElementById('eff-res');
      res.innerHTML =
        '<div><b>' + fmt(pub) + '</b><span>personnes, effectif du public</span></div>' +
        '<div><b>Type ' + type + ', ' + cat + '</b><span>' + catTxt + '</span></div>' +
        '<div><b>' + fmt(ss) + ' / ' + fmt(rdc) + ' / ' + fmt(et) + '</b><span>sous-sol / rez-de-chaussée / étages</span></div>';
      var why = cinq ? 'Sous les seuils de la 5e catégorie : moins de ' + lim[0] + ' au sous-sol, ' + lim[1] + ' aux étages et ' + lim[2] + ' au total (PE 2).'
        : 'Au moins un seuil de la 5e catégorie est atteint (' + lim[0] + ' au sous-sol, ' + lim[1] + ' aux étages, ' + lim[2] + ' au total) : la catégorie se lit sur l\'effectif total, personnel sans sortie propre compris (R143-19, GN 1).';
      var sorties = cinq ? '<p><strong>Sorties exigées (PE 11)</strong>, pour ' + fmt(pub + pers) + ' personnes avec le personnel : ' + degag(pub + pers) + '.</p>' : '';
      d.getElementById('eff-note').innerHTML = '<p>' + why + '</p>' + sorties + (note ? '<p class="muted">' + esc(note) + '</p>' : '') + '<p class="muted small">Résultat indicatif, arrondi à l\'unité supérieure. La notice de sécurité du projet fait foi.</p>';
    }
    eff.addEventListener('input', calc);
    eff.addEventListener('change', calc);
    calc();
  }
})();
