/* AULÃO UNIVERSAL — contagem regressiva até o fim da promoção (30/11, 23h59) e carrossel de fotos. */
(function () {
  "use strict";
  var root = document.documentElement;
  root.classList.add("am-js");
  var END = new Date("2026-11-30T23:59:59-03:00").getTime();     // fim da venda
  var els = document.querySelectorAll("[data-count]"), ended = false;

  function pad(n) { return n < 10 ? "0" + n : "" + n; }
  function paint(el, ms) {
    var s = Math.max(0, Math.floor(ms / 1000));
    var d = Math.floor(s / 86400), h = Math.floor((s % 86400) / 3600), m = Math.floor((s % 3600) / 60), x = s % 60;
    el.innerHTML = '<span>' + d + '<small>d</small></span><span>' + pad(h) + '<small>h</small></span><span>' + pad(m) + '<small>min</small></span><span>' + pad(x) + '<small>s</small></span>';
  }
  function tick() {
    var now = Date.now(), i;
    for (i = 0; i < els.length; i++) {
      paint(els[i], END - now);
    }
    if (now >= END && !ended) {
      ended = true;
      // Depois de 30/11 23h59: some tudo o que é da promoção (contagem, bônus, preço de Black Friday). O preço novo vem do modelo "pós-promoção".
      var pr = document.querySelectorAll("[data-promo]"), k;
      for (k = 0; k < pr.length; k++) { pr[k].hidden = true; }
      var det = document.querySelector(".am-reveal");
      if (det) { det.open = true; }
    }
  }
  tick();
  setInterval(tick, 1000);

  // Carrossel de fotos: setas, arraste no celular e rolagem automática lenta (pausa ao tocar e com movimento reduzido).
  var car = document.querySelector("[data-carousel]");
  if (car) {
    var track = car.querySelector(".am-track"), btns = car.querySelectorAll(".am-arrow");
    var step = function () { var s = track.querySelector(".am-slide"); return s ? s.getBoundingClientRect().width + 14 : 280; };
    var go = function (d) {
      var max = track.scrollWidth - track.clientWidth;
      if (d > 0 && track.scrollLeft >= max - 4) { track.scrollTo({ left: 0 }); return; }
      if (d < 0 && track.scrollLeft <= 4) { track.scrollTo({ left: max }); return; }
      track.scrollBy({ left: d * step() });
    };
    for (var b = 0; b < btns.length; b++) {
      btns[b].addEventListener("click", function () { paused = true; go(parseInt(this.getAttribute("data-dir"), 10)); });
    }
    var paused = false, reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    ["mouseenter", "touchstart", "focusin"].forEach(function (e) { car.addEventListener(e, function () { paused = true; }, { passive: true }); });
    if (!reduce) { setInterval(function () { if (!paused && !document.hidden) { go(1); } }, 3500); }
  }
})();
