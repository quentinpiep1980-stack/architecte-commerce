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

  /* Accueil : la devanture change avec l'activité choisie */
  var elev = d.querySelector('.hero .elev');
  var sets = d.querySelectorAll('.legend-set');
  d.querySelectorAll('.plates input').forEach(function (r) {
    r.addEventListener('change', function () {
      if (!r.checked) return;
      if (elev) elev.setAttribute('data-act', r.value);
      sets.forEach(function (s) { s.hidden = s.dataset.act !== r.value; });
    });
  });

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
