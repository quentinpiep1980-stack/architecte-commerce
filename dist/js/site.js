/* architecte-commerce.fr — interactions légères, sans dépendance ni cookie. */
(function () {
  'use strict';
  var d = document;

  /* Panneaux de navigation (Projets, Activités, Outils) */
  var tops = d.querySelectorAll('.nav [data-panel]');
  function closeAll(except) {
    tops.forEach(function (a) {
      if (a === except) return;
      a.setAttribute('aria-expanded', 'false');
      var p = d.getElementById(a.dataset.panel);
      if (p) p.classList.remove('open');
    });
  }
  tops.forEach(function (a) {
    a.setAttribute('aria-expanded', 'false');
    a.setAttribute('aria-controls', a.dataset.panel);
    a.setAttribute('role', 'button');
    a.addEventListener('click', function (e) {
      e.preventDefault();
      var p = d.getElementById(a.dataset.panel);
      var open = a.getAttribute('aria-expanded') !== 'true';
      closeAll(a);
      a.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (p) p.classList.toggle('open', open);
    });
  });
  d.addEventListener('click', function (e) {
    if (!e.target.closest('.site-head')) closeAll();
  });
  d.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      var opened = d.querySelector('.nav [aria-expanded="true"]');
      closeAll();
      if (opened) opened.focus();
      if (burger && burger.getAttribute('aria-expanded') === 'true') toggleMenu(false);
    }
  });

  /* Menu mobile */
  var burger = d.querySelector('.burger');
  var mnav = d.getElementById('mnav');
  function toggleMenu(open) {
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    mnav.classList.toggle('open', open);
    d.body.style.overflow = open ? 'hidden' : '';
  }
  if (burger && mnav) {
    burger.addEventListener('click', function () {
      toggleMenu(burger.getAttribute('aria-expanded') !== 'true');
    });
  }

  /* Accueil : le rideau descend, l'enseigne change, le rideau remonte */
  var scene = d.getElementById('scene');
  var still = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var timer;
  if (scene) {
    var rid = scene.querySelector('.rideau');
    if (rid) rid.addEventListener('animationend', function () { scene.classList.add('leve'); });
    if (still) scene.classList.add('leve');
  }
  function show(act) {
    d.querySelectorAll('.soub-g [data-act]').forEach(function (el) { el.hidden = el.dataset.act !== act; });
  }
  d.querySelectorAll('.enseignes-sw input').forEach(function (r) {
    r.addEventListener('change', function () {
      if (!r.checked || !scene) return;
      var act = r.value;
      var desc = scene.querySelector('desc');
      clearTimeout(timer);
      scene.classList.add('leve');
      show(act);
      if (still) {
        scene.setAttribute('data-act', act);
      } else {
        scene.classList.add('ferme');
        timer = setTimeout(function () {
          scene.setAttribute('data-act', act);
          scene.classList.remove('ferme');
        }, 460);
      }
      if (desc && r.dataset.desc) desc.textContent = "Dessin d'illustration : une devanture en applique, avec deux vitrines, une porte vitrée et un rideau métallique. À travers le vitrage, on voit " + r.dataset.desc + '.';
    });
  });

  /* Calendrier d'ouverture : décision la plus tardive */
  var cal = d.querySelector('[data-cal]');
  if (cal) {
    var din = cal.querySelector('input[type=date]');
    var t0 = new Date(); t0.setDate(t0.getDate() + 7);
    var iso = function (x) { return x.getFullYear() + '-' + ('0' + (x.getMonth() + 1)).slice(-2) + '-' + ('0' + x.getDate()).slice(-2); };
    if (din && !din.value) din.value = iso(t0);
    var MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'];
    var rowsC = cal.querySelectorAll('[data-row]');
    var outD = cal.querySelector('[data-cal-date]'), outL = cal.querySelector('[data-cal-l]');
    var outM = cal.querySelector('[data-cal-max]'), outW = cal.querySelector('[data-cal-w]');
    var calc = function () {
      var spr = cal.querySelector('input[name=spr]').checked;
      var max = 0, who = '';
      rowsC.forEach(function (row) {
        var on = cal.querySelector('input[name=k][value="' + row.dataset.row + '"]').checked;
        var m = parseFloat(row.dataset.m) + (spr ? parseFloat(row.dataset.e || 0) : 0);
        row.classList.toggle('off', !on);
        var ext = row.querySelector('[data-ext]');
        if (ext) ext.hidden = !spr;
        if (on && m > max) { max = m; who = row.querySelector('.lab').firstChild.textContent.trim(); }
      });
      if (!max) {
        outD.textContent = '—'; outL.textContent = 'cochez au moins un dossier';
        outM.textContent = '—'; outW.textContent = '';
        return;
      }
      outM.textContent = max + ' mois';
      outW.textContent = 'délai le plus long : ' + who.charAt(0).toLowerCase() + who.slice(1);
      var v = din && din.value ? din.value.split('-') : null;
      if (v && v.length === 3) {
        var x = new Date(+v[0], +v[1] - 1, +v[2]);
        var day = x.getDate();
        x.setMonth(x.getMonth() + max);
        if (x.getDate() !== day) x.setDate(0);
        outD.textContent = x.getDate() + (x.getDate() === 1 ? 'er' : '') + ' ' + MOIS[x.getMonth()] + ' ' + x.getFullYear();
        outL.textContent = 'dernière décision attendue, sans demande de pièces';
      } else {
        outD.textContent = max + ' mois'; outL.textContent = 'après le dépôt d\'un dossier complet';
      }
    };
    cal.addEventListener('change', calc);
    cal.addEventListener('input', calc);
    calc();
  }

  /* Mobile : barre d'appel après la devanture */
  var dock = d.querySelector('.dock');
  var hero = d.querySelector('.devanture, .planche');
  if (dock && hero && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (en) { dock.classList.toggle('on', !en[0].isIntersecting); }).observe(hero);
  } else if (dock) { dock.classList.add('on'); }

  /* Accueil : liste « avant de signer » reliée aux repères du plan */
  var pins = {};
  d.querySelectorAll('.plan .pin').forEach(function (p) { pins[p.dataset.pin] = p; });
  d.querySelectorAll('#checks li').forEach(function (li) {
    var n = li.dataset.pin;
    function on() { li.classList.add('on'); if (pins[n]) pins[n].classList.add('on'); }
    function off() { li.classList.remove('on'); if (pins[n]) pins[n].classList.remove('on'); }
    li.addEventListener('mouseenter', on);
    li.addEventListener('mouseleave', off);
    var b = li.querySelector('button');
    if (b) { b.addEventListener('focus', on); b.addEventListener('blur', off); }
  });

  /* Sommaire : section en cours */
  var toc = d.querySelectorAll('.toc a');
  if (toc.length && 'IntersectionObserver' in window) {
    var map = {};
    toc.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting && map[en.target.id]) {
          toc.forEach(function (a) { a.classList.remove('on'); });
          map[en.target.id].classList.add('on');
        }
      });
    }, { rootMargin: '-20% 0px -70% 0px' });
    Object.keys(map).forEach(function (id) { var h = d.getElementById(id); if (h) io.observe(h); });
  }

  /* Calendrier : scénarios */
  d.querySelectorAll('[data-scenarios]').forEach(function (box) {
    var rows = box.querySelectorAll('[data-in]');
    function apply() {
      var on = {};
      box.querySelectorAll('input[type=checkbox]').forEach(function (c) { on[c.value] = c.checked; });
      var max = 0;
      rows.forEach(function (r) {
        var need = r.dataset.in.split(' ').some(function (k) { return on[k]; });
        r.hidden = !need;
        if (need) max = Math.max(max, parseFloat(r.dataset.m || 0));
      });
      var out = box.querySelector('[data-total]');
      if (out) out.textContent = max ? max + ' mois' : '—';
    }
    box.addEventListener('change', apply);
    apply();
  });
})();
