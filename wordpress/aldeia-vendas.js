/* Aldeia Literária — Página de vendas: comportamentos leves (sem dependências).
   - Revelação ao rolar (classe av-reveal)
   - Carrossel dos problemas (.av-problems > .av-problems__stage > .av-problem)
   - Faixa de capas em loop (.av-marquee__track)
   - Barra fixa de compra no celular (.av-sticky) depois do hero (.av-hero)
   Não faz nada dentro do editor do Elementor (para você editar com tudo visível). */
(function(){
  if(document.body.classList.contains('elementor-editor-active'))return;
  if(window.__avInit)return;window.__avInit=1; /* evita rodar duas vezes (plugin + código embutido na página) */
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.documentElement.classList.add('av-js');

  /* Revelação ao rolar */
  var rv=document.querySelectorAll('.av-reveal');
  if('IntersectionObserver' in window){
    var ro=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('is-in');ro.unobserve(e.target)}})},{threshold:.12,rootMargin:'0px 0px -40px 0px'});
    rv.forEach(function(e){ro.observe(e)});
  } else rv.forEach(function(e){e.classList.add('is-in')});

  /* Tabs próprias (só na prévia HTML; no Elementor o widget Abas cuida disso) */
  document.querySelectorAll('[data-av-tabset]').forEach(function(w){
    if(w.dataset.avInit)return;w.dataset.avInit='1';
    var tabs=[].slice.call(w.querySelectorAll('.av-tab')), panels=[].slice.call(w.querySelectorAll('.av-panel'));
    function set(i){
      var mobile=matchMedia('(max-width:767px)').matches, wasOn=tabs[i].classList.contains('is-active');
      tabs.forEach(function(t,j){var on=j===i&&!(mobile&&wasOn);t.classList.toggle('is-active',on);t.setAttribute('aria-selected',on);panels[j].classList.toggle('is-active',on)});
    }
    tabs.forEach(function(t,i){t.addEventListener('click',function(){set(i)})});
  });

  /* Contadores próprios (só na prévia HTML; no Elementor use o widget Contador) */
  var els=document.querySelectorAll('[data-count],[data-minutes]');
  function hm(m){var h=Math.floor(m/60),r=m%60;return h+'h'+(r?('0'+r).slice(-2):'')}
  function run(el){
    var mins=el.dataset.minutes!==undefined,end=+(mins?el.dataset.minutes:el.dataset.count),p=el.dataset.prefix||'',s=el.dataset.suffix||'';
    function show(v){el.textContent=mins?hm(v):p+v+s}
    if(reduce){show(end);return}
    var t0=null;(function f(t){t0=t0||t;var k=Math.min((t-t0)/1200,1);show(Math.round(end*(1-Math.pow(1-k,3))));if(k<1)requestAnimationFrame(f)})(performance.now());
  }
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){run(e.target);io.unobserve(e.target)}})},{threshold:.6});
    els.forEach(function(e){io.observe(e)});
  } else els.forEach(run);

  /* Carrossel dos problemas: automático, pausa ao passar o mouse, setas, pontos e deslize no celular.
     Os controles e a numeração são criados aqui, então basta ter os cartões .av-problem. */
  document.querySelectorAll('.av-problems').forEach(function(c){
    if(c.dataset.avInit)return;c.dataset.avInit='1';
    var slides=[].slice.call(c.querySelectorAll('.av-problem'));
    if(slides.length<2)return;
    slides.forEach(function(s,k){
      if(!s.querySelector('.av-problem__n')){var n=document.createElement('span');n.className='av-problem__n';n.textContent='0'+(k+1)+' / 0'+slides.length;s.insertBefore(n,s.firstChild)}
    });
    var ctrl=c.querySelector('.av-problems__ctrl');
    if(!ctrl){
      ctrl=document.createElement('div');ctrl.className='av-problems__ctrl';
      ctrl.innerHTML='<button type="button" class="av-arrow" data-prev aria-label="Problema anterior">←</button><div class="av-dots"></div><button type="button" class="av-arrow" data-next aria-label="Próximo problema">→</button>';
      var dw=ctrl.querySelector('.av-dots');
      slides.forEach(function(_,k){var b=document.createElement('button');b.type='button';b.className='av-dot';b.setAttribute('aria-label','Ir para o problema '+(k+1));dw.appendChild(b)});
      c.appendChild(ctrl);
    }
    var dots=[].slice.call(ctrl.querySelectorAll('.av-dot')),i=0,timer,paused=false;
    function go(n){
      i=(n+slides.length)%slides.length;
      slides.forEach(function(s,k){s.classList.toggle('is-active',k===i);s.setAttribute('aria-hidden',k!==i)});
      dots.forEach(function(d){d.classList.remove('is-active','is-done')});
      void c.offsetWidth;
      dots.forEach(function(d,k){if(k<i)d.classList.add('is-done');if(k===i)d.classList.add('is-active');d.setAttribute('aria-current',k===i)});
      clearTimeout(timer);
      if(!reduce&&!paused)timer=setTimeout(function(){go(i+1)},5000);
    }
    var pv=ctrl.querySelector('[data-prev]'),nx=ctrl.querySelector('[data-next]');
    if(pv)pv.addEventListener('click',function(){go(i-1)});
    if(nx)nx.addEventListener('click',function(){go(i+1)});
    dots.forEach(function(d,k){d.addEventListener('click',function(){go(k)})});
    c.addEventListener('mouseenter',function(){paused=true;clearTimeout(timer);c.classList.add('is-paused')});
    c.addEventListener('mouseleave',function(){paused=false;c.classList.remove('is-paused');go(i)});
    var x0=null;
    c.addEventListener('touchstart',function(e){x0=e.touches[0].clientX},{passive:true});
    c.addEventListener('touchend',function(e){if(x0===null)return;var dx=e.changedTouches[0].clientX-x0;if(Math.abs(dx)>40)go(i+(dx<0?1:-1));x0=null});
    go(0);
  });

  /* Faixa de capas: duplica os itens para o loop contínuo */
  document.querySelectorAll('.av-marquee__track').forEach(function(tr){
    if(reduce||tr.dataset.avInit)return;tr.dataset.avInit='1';
    [].slice.call(tr.children).forEach(function(n){var cl=n.cloneNode(true);cl.setAttribute('aria-hidden','true');cl.classList.remove('av-reveal');[].slice.call(cl.querySelectorAll('img')).forEach(function(im){im.alt='';im.removeAttribute('srcset')});if(cl.tagName==='A')cl.setAttribute('tabindex','-1');tr.appendChild(cl)});
  });

  /* Livros sem link ainda (href="#") não fazem nada ao clicar */
  document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a.av-book');if(a&&a.getAttribute('href')==='#')e.preventDefault()});

  /* Barra fixa de compra (celular): aparece depois do hero */
  var hero=document.querySelector('.av-hero'),bar=document.querySelector('.av-sticky');
  if(hero&&bar&&'IntersectionObserver' in window){
    new IntersectionObserver(function(es){bar.classList.toggle('is-on',!es[0].isIntersecting)}).observe(hero);
  }
})();
