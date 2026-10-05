/* Menu do celular e contagem regressiva do lançamento. Sem dependências. */
(function () {
  var b = document.querySelector('.menu-btn'), n = document.getElementById('nav');
  if (b && n) b.addEventListener('click', function () {
    var o = n.classList.toggle('is-open'); b.setAttribute('aria-expanded', o);
  });
  var alvo = new Date('2026-10-23T00:00:00-03:00').getTime();
  function pad(x) { return String(x).padStart(2, '0'); }
  function tick() {
    var s = Math.floor(Math.max(0, alvo - Date.now()) / 1000);
    var D = Math.floor(s / 86400), H = Math.floor(s % 86400 / 3600), M = Math.floor(s % 3600 / 60), S = s % 60;
    document.querySelectorAll('[data-cont]').forEach(function (c) {
      c.querySelector('[data-d]').textContent = D; c.querySelector('[data-h]').textContent = pad(H);
      c.querySelector('[data-m]').textContent = pad(M); c.querySelector('[data-s]').textContent = pad(S);
    });
    document.querySelectorAll('[data-dias]').forEach(function (e) { e.textContent = D; });
  }
  if (document.querySelector('[data-cont],[data-dias]')) { tick(); setInterval(tick, 1000); }
})();
