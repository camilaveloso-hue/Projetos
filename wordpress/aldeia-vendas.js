/* Aldeia Literária — Página de vendas: comportamentos leves (sem dependências).
   Elementor: cole dentro de um widget HTML (envolvido por uma tag script) no rodapé da página,
   ou use Elementor Pro > Custom Code. Os widgets nativos (Tabs, Counter, Accordion) dispensam as partes correspondentes. */
(function(){
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.documentElement.classList.add('av-js');

  /* Revelação ao rolar: adicione a classe av-reveal em qualquer bloco */
  var rv=document.querySelectorAll('.av-reveal');
  if('IntersectionObserver' in window){
    var ro=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('is-in');ro.unobserve(e.target)}})},{threshold:.12,rootMargin:'0px 0px -40px 0px'});
    rv.forEach(function(e){ro.observe(e)});
  } else rv.forEach(function(e){e.classList.add('is-in')});

  /* Tabs no desktop / acordeão no celular */
  document.querySelectorAll('[data-av-tabs]').forEach(function(w){
    var tabs=[].slice.call(w.querySelectorAll('.av-tab')), panels=[].slice.call(w.querySelectorAll('.av-panel'));
    function set(i){
      var mobile=matchMedia('(max-width:767px)').matches, wasOn=tabs[i].classList.contains('is-active');
      tabs.forEach(function(t,j){var on=j===i&&!(mobile&&wasOn);t.classList.toggle('is-active',on);t.setAttribute('aria-selected',on);panels[j].classList.toggle('is-active',on)});
    }
    tabs.forEach(function(t,i){t.addEventListener('click',function(){set(i)})});
  });

  /* Contadores animados (data-count="50" data-prefix="~" data-suffix="") */
  var els=document.querySelectorAll('[data-count]');
  function run(el){
    var end=+el.dataset.count,p=el.dataset.prefix||'',s=el.dataset.suffix||'';
    if(reduce){el.textContent=p+end+s;return}
    var t0=null;(function f(t){t0=t0||t;var k=Math.min((t-t0)/1200,1);el.textContent=p+Math.round(end*(1-Math.pow(1-k,3)))+s;if(k<1)requestAnimationFrame(f)})(performance.now());
  }
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){run(e.target);io.unobserve(e.target)}})},{threshold:.6});
    els.forEach(function(e){io.observe(e)});
  } else els.forEach(run);

  /* Barra fixa de compra (celular): aparece depois do hero */
  var hero=document.querySelector('.av-hero'),bar=document.querySelector('.av-sticky');
  if(hero&&bar&&'IntersectionObserver' in window){
    new IntersectionObserver(function(es){bar.classList.toggle('is-on',!es[0].isIntersecting)}).observe(hero);
  }
})();
