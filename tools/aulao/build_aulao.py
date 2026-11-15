#!/usr/bin/env python3
"""Gera a página de vendas do AULÃO MASTER (Black Friday 2026).

Saídas (uso: python3 tools/aulao/build_aulao.py):
  preview/aulao-master.html                       -> prévia local (arquivos em preview/aulao/)
  <scratchpad>/aulao-master-artifact.html         -> prévia autocontida (imagens e fontes embutidas)
O conteúdo vem dos slides "AULÃO MASTER" e da planilha de aprendizados de lançamentos."""
import base64, html, json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
ASSETS = os.path.join(ROOT, "preview", "aulao")
E = html.escape

SITE = "https://aaldeialiteraria.com.br"
SLUG = "/aulao-master/"
URL = SITE + SLUG
CHECKOUT = "#oferta"           # TROCAR pelo link do checkout quando a plataforma estiver definida
CANC = SITE + "/politica-de-cancelamento-e-reembolso/"
WAIT = "https://tally.so/r/0QNWPy"
INSTA = "https://www.instagram.com/acamiveloso/"
INSTA_ALDEIA = "https://www.instagram.com/aldeialiteraria.oficial/"
TIKTOK = "https://www.tiktok.com/@aldeialiteraria"
GUIA = SITE + "/como-escolher-curso-de-escrita-criativa/"
IMP = SITE + "/imprensa/"
SOBRE = SITE + "/novo-sobre/"
TITLE = "AULÃO MASTER: tudo o que você precisa saber para conseguir escrever um livro"
DESC = ("Aulão gravado de Camila Veloso, fundadora da Aldeia Literária: os três atos, o checklist de 9 passos, "
        "as formas de história e como escrever a premissa. R$ 97 na Black Friday, até 30/11.")

CHECK = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="11" fill="currentColor"/><path d="M7 12.5l3.2 3.2L17 8.8" stroke="#fff8f2" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 12h15m0 0l-5-5m5 5l-5 5" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

FAQ = [
 ("O que é o AULÃO MASTER?",
  "O AULÃO MASTER é uma aula gravada de Camila Veloso, fundadora da Aldeia Literária, que reúne o básico da narrativa para quem quer escrever um livro: os três atos e o arco do personagem, o checklist de 9 passos até o final, a função de uma história, as formas de história (linear, sinuosa e explosiva) e como escrever a premissa."),
 ("Para quem é o AULÃO MASTER?",
  "Para quem está começando e quer escrever o primeiro livro, mas não sabe por onde começar. Você não precisa ter nada pronto, só vontade de contar uma história. Quem já domina estrutura narrativa vai rever a base, e a Aldeia Literária oferece módulos mais avançados."),
 ("Quanto custa e até quando posso comprar?",
  "O AULÃO MASTER custa R$ 97 na Black Friday. A venda vai de 23/11 até 30/11, às 23h59 (horário de Brasília). Depois disso, a aula sai do ar e não será vendida novamente."),
 ("Como eu assisto à aula?",
  "A aula é gravada. Depois da confirmação do pagamento, você recebe o acesso e assiste no seu ritmo, quantas vezes quiser dentro do período de acesso informado na compra."),
 ("Qual é o bônus de quem compra no primeiro dia?",
  "Quem comprar na segunda-feira, 23/11, ganha 50% de desconto na matrícula da Aldeia Literária 2027. As matrículas abrem em janeiro de 2027, com vagas limitadas. A partir de 24/11 o bônus deixa de valer."),
 ("Posso pedir reembolso?",
  "Sim. Você tem 7 dias corridos após a compra para desistir e pedir o reembolso do valor pago. As regras completas estão na <a href=\"" + CANC + "\">política de cancelamento e reembolso</a>."),
 ("Qual é a diferença entre o AULÃO MASTER e a Aldeia Literária?",
  "O AULÃO MASTER é uma aula única, gravada, sobre o básico da narrativa. A Aldeia Literária é a escola e comunidade de escrita criativa: cinco módulos de 12 aulas, aulas ao vivo às quartas-feiras, às 19h30, todas gravadas, com atividades e feedback individual."),
 ("Quem dá a aula?",
  "Camila Veloso, fundadora e diretora da Aldeia Literária. Ela é formada em Comunicação Social, Produção Editorial (UFSM), tem mais de seis anos de experiência em marketing e conteúdo e ajuda escritores iniciantes a desenvolver e publicar seus livros."),
]


def faq_html():
    return "".join(f'<details open><summary>{E(q)}</summary><div class="am-ans"><p>{a}</p></div></details>' for q, a in FAQ)


def jsonld():
    plain = lambda s: re.sub(r"<[^>]+>", "", html.unescape(s))
    data = {"@context": "https://schema.org", "@graph": [
        {"@type": "Course", "@id": URL + "#aula", "name": TITLE, "url": URL, "inLanguage": "pt-BR",
         "description": DESC,
         "about": ["Estrutura narrativa", "Escrita criativa", "Como escrever um livro"],
         "teaches": "Estrutura de três atos, arco do personagem, checklist de 9 passos, formas de história e premissa.",
         "educationalLevel": "Iniciante", "isAccessibleForFree": False,
         "provider": {"@type": "EducationalOrganization", "@id": SITE + "/#aldeia", "name": "Aldeia Literária", "url": SITE + "/"},
         "instructor": {"@type": "Person", "name": "Camila Veloso", "jobTitle": "Fundadora e diretora da Aldeia Literária",
                        "sameAs": [INSTA], "worksFor": {"@id": SITE + "/#aldeia"}},
         "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "online", "courseWorkload": "PT1H"},
         "offers": {"@type": "Offer", "price": "97.00", "priceCurrency": "BRL", "availability": "https://schema.org/InStock",
                    "url": URL, "validFrom": "2026-11-23T00:00:00-03:00", "priceValidUntil": "2026-11-30"}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in FAQ]},
    ]}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "</script>"


# ---------------------------------------------------------------- SVGs dos slides
def svg_forms():
    lin = ('<svg viewBox="0 0 220 70" aria-hidden="true"><line x1="14" y1="35" x2="168" y2="35" stroke="#083656" stroke-width="5" stroke-linecap="round"/>'
           + "".join(f'<circle cx="{x}" cy="35" r="8" fill="#083656"/>' for x in (14, 54, 94, 134))
           + '<circle cx="168" cy="35" r="14" fill="#cc341b"/><path d="M190 22v26l22-13z" fill="#cc341b"/></svg>')
    sin = ('<svg viewBox="0 0 220 70" aria-hidden="true"><path d="M14 56C40 56 46 14 74 14S104 58 134 58 176 30 196 24" fill="none" stroke="#083656" stroke-width="5" stroke-linecap="round"/>'
           '<circle cx="14" cy="56" r="8" fill="#083656"/><circle cx="200" cy="22" r="13" fill="#cc341b"/></svg>')
    sp = ""
    for i in range(12):
        a = i * math.tau / 12 + .25
        r1, r2 = 20, 28 + (i % 3) * 5
        x1, y1, x2, y2 = 110 + r1 * math.cos(a) * 1.6, 35 + r1 * math.sin(a), 110 + r2 * math.cos(a) * 2.3, 35 + r2 * math.sin(a) * 1.15
        sp += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#083656" stroke-width="4" stroke-linecap="round"/><circle cx="{x2:.1f}" cy="{y2:.1f}" r="5" fill="#083656"/>'
    exp = f'<svg viewBox="0 0 220 70" aria-hidden="true">{sp}<circle cx="110" cy="35" r="13" fill="#cc341b"/></svg>'
    return lin, sin, exp


def svg_arc():
    z = ('<rect x="0" y="0" width="150" height="190" rx="14" fill="#efd2ca"/><rect x="154" y="0" width="292" height="190" rx="14" fill="#dfdede"/>'
         '<rect x="450" y="0" width="150" height="190" rx="14" fill="#d1cdc9"/>')
    path = '<path d="M24 112C70 114 100 104 150 92C215 76 255 55 285 88C305 112 312 156 330 160C365 166 400 108 450 98C500 88 535 46 576 40" fill="none" stroke="#083656" stroke-width="5" stroke-linecap="round"/>'
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="9" fill="#cc341b"/>' for x, y in ((24, 112), (150, 92), (330, 160), (450, 98), (576, 40)))
    return f'<svg viewBox="0 0 600 190" role="img" aria-label="Curva do arco do personagem nos três atos">{z}{path}{dots}</svg>'


def blocks():
    lin, sin, exp = svg_forms()
    steps = [("Início", [("Ambientação", "Rotina do personagem no ponto A."), ("Problema central", "O conflito que move a história.")]),
             ("Primeiro limiar", [("Recusa", "Ele foge do problema."), ("Obrigado a agir", "Tenta resolver sem novas habilidades.")]),
             ("Clímax", [("Pequena vitória", "Ele muda e se aproxima do ponto B."), ("Tudo dá errado", "O personagem é testado e amadurece.")]),
             ("Caminho de volta", [("Ajuda e plano", "Aliados dão novas ferramentas."), ("Confronto final", "O amadurecimento prova ser real.")]),
             ("Fim", [("Vida nova", "Mostra como é o ponto B.")])]
    n = 0
    steps_html = ""
    for head, items in steps:
        cells = ""
        for t, d in items:
            n += 1
            cells += f'<p><b>{n} · {E(t)}</b>{E(d)}</p>'
        steps_html += f'<div><h4>{E(head)}</h4>{cells}</div>'

    b1 = f'''<article class="am-block">
  <div><span class="am-block__n" aria-hidden="true">1</span><h3>Os três atos e o arco</h3><p class="am-block__sub">O esqueleto e a mudança do personagem</p>
  <p>Toda história tem um esqueleto. Você vai ver como ele se divide em três atos e como o personagem muda do começo ao fim, da fraqueza e da necessidade até o novo equilíbrio.</p></div>
  <div>
    <div class="am-acts"><div class="a1">Ato I<small>Apresentação · 25%</small></div><div class="a2">Ato II<small>Confronto · 50%</small></div><div class="a3">Ato III<small>Resolução · 25%</small></div></div>
    <ul class="am-qs"><li><b>Ato I</b><span>Quem é o herói e o que está em jogo?</span></li><li><b>Ato II</b><span>O que acontece quando ele tenta conseguir o que quer?</span></li><li><b>Ato III</b><span>Como termina e o que mudou?</span></li></ul>
    <div class="am-arc" style="margin-top:14px">{svg_arc()}<ol><li>Fraqueza e necessidade</li><li>Primeiro limiar</li><li>Provação suprema</li><li>Autorrevelação</li><li>Novo equilíbrio</li></ol></div>
  </div></article>'''
    b2 = f'''<article class="am-block am-block--navy am-block--wide">
  <div><span class="am-block__n" aria-hidden="true">2</span><h3>O checklist da história</h3><p class="am-block__sub">9 passos até o final</p>
  <p>Um caminho de nove passos para você chegar ao final da sua história sem travar no meio. Pode haver mais capítulos, desde que a estrutura seja respeitada.</p></div>
  <div class="am-steps">{steps_html}</div></article>'''
    b3 = f'''<article class="am-block">
  <div><span class="am-block__n" aria-hidden="true">3</span><h3>Por que você lê livros</h3><p class="am-block__sub">A função de uma história</p>
  <p>Contamos histórias para entender como a vida funciona e como agir nela. O herói é a porta de entrada do leitor: ele se identifica, atravessa a jornada junto e volta transformado.</p></div>
  <div><div class="am-flow"><div class="f1">Desejo<small>o que a pessoa quer conseguir</small></div>{ARROW}<div class="f2">Obstáculo<small>o que se coloca no caminho</small></div>{ARROW}<div class="f3">Transformação<small>quem ela é no final</small></div></div>
  <p class="am-flowcap">Alguém quer algo, enfrenta obstáculos e muda.</p></div></article>'''
    b4 = f'''<article class="am-block am-block--navy am-block--wide">
  <div><span class="am-block__n" aria-hidden="true">4</span><h3>As formas de história</h3><p class="am-block__sub">Linear, sinuosa e explosiva</p>
  <p>O esqueleto é parecido, mas a forma muda de história para história. Desejo, obstáculo e transformação aparecem em todas; o ritmo é que varia.</p></div>
  <div class="am-forms">
    <div class="am-form">{lin}<h4>Linear</h4><p>Um único protagonista, do começo ao fim, perseguindo um desejo com muita intensidade.</p><em>Cinderela · Star Wars · Die Hard</em></div>
    <div class="am-form">{sin}<h4>Sinuosa</h4><p>Caminho cheio de voltas, desejo menos intenso e muitos encontros pelo caminho.</p><em>Odisseia · Dom Quixote · Tom Jones</em></div>
    <div class="am-form">{exp}<h4>Explosiva</h4><p>Vários caminhos ao mesmo tempo, contados em cortes alternados entre as linhas da história.</p><em>Pulp Fiction · Crash · Nashville</em></div>
  </div></article>'''
    b5 = f'''<article class="am-block">
  <div><span class="am-block__n" aria-hidden="true">5</span><h3>Premissa, princípio e arco</h3><p class="am-block__sub">Da ideia à página</p>
  <p>O princípio dá a direção, a premissa conta o que acontece e o arco mostra quem muda. Você vai aprender a resumir sua história em uma frase e a enxergar o arco em duas fotografias: antes e depois.</p></div>
  <div>
    <div class="am-trio"><article class="t1"><h4>Princípio narrativo</h4><p>A ideia central que sustenta a história inteira e dá sentido a cada cena.</p></article>
    <article class="t2"><h4>Premissa</h4><p>A história resumida em uma frase: quem é o personagem, o que quer, o que o impede e qual a consequência.</p></article>
    <article class="t3"><h4>Arco</h4><p>A mudança do personagem do início ao fim, de uma falha para uma transformação.</p></article></div>
    <div class="am-scrooge"><div class="s1"><b>Antes · Ato I</b>Scrooge só pensa em dinheiro e se isola.</div><div class="s2"><b>Depois · Ato III</b>Scrooge se torna generoso e celebra o Natal com os outros.</div></div>
    <p class="am-scrooge-cap">Exemplo: Um conto de Natal, de Charles Dickens.</p>
  </div></article>'''
    b6 = f'''<article class="am-block am-block--wide">
  <div><span class="am-block__n" aria-hidden="true">6</span><h3>Próximos passos</h3><p class="am-block__sub">O que vem depois do básico</p>
  <p>O básico é só o primeiro degrau. Para fechar, você vê o mapa completo da escalada: do que aprendeu no aulão até a publicação independente do seu livro.</p></div>
  <div class="am-ladder"><div class="l0">O básico<small>você está aqui</small></div><div class="l1">Módulo I<small>Fundamentos da narrativa</small></div><div class="l2">Módulo II<small>Técnicas avançadas</small></div><div class="l3">Módulo III<small>Processos criativos</small></div><div class="l4">Módulo IV<small>Gramática e produção literária</small></div><div class="l5">Módulo V<small>Publicação independente</small></div></div></article>'''
    return "\n".join([b1, b2, b3, b4, b5, b6])


def page():
    cta_top = f'<a class="am-btn am-btn--sm am-open" href="{CHECKOUT}">Quero o aulão</a>'
    outcomes = [
        "Dividir sua história nos três atos e saber o que cada um precisa responder.",
        "Usar o checklist de 9 passos para chegar ao final sem travar no meio.",
        "Escolher a forma da sua história: linear, sinuosa ou explosiva.",
        "Resumir o livro em uma premissa de uma frase e desenhar o arco do personagem.",
    ]

    books = [("querida-tia-liz", "Querida Tia Liz"), ("dois-lados-da-coroa", "Os Dois Lados da Coroa"), ("violeta", "Violeta"),
             ("dinamene-e-gavita", "Dinamene & Gavita"), ("ultimo-natal-com-ela", "O Último Natal com Ela"),
             ("melhores-anos", "Os Melhores Anos de Nossas Vidas"), ("resgate-de-muriel", "O Resgate de Muriel"),
             ("inconfidencia-da-magia", "A Inconfidência da Magia"), ("sombras-que-me-vestem", "As Sombras que me Vestem"),
             ("formula-encontro-perfeito", "A Fórmula do Encontro Perfeito"), ("perdida-em-teu-olhar", "Perdida em teu olhar"),
             ("desejei-as-estrelas", "Desejei às Estrelas"), ("estrelas-do-cosme-velho", "Estrelas do Cosme Velho"),
             ("quando-as-sombras-falam", "Quando as Sombras Falam")]
    books_html = "".join(f'<li><img src="{{IMG:livro-{f}.jpg}}" alt="Capa do livro {E(t)}, escrito por aluno da Aldeia" width="200" height="300" loading="lazy"></li>' for f, t in books)
    gallery_html = "".join(f'<li><img src="{{IMG:comunidade-{n:02d}.jpg}}" alt="Escritores da comunidade da Aldeia Literária em encontro presencial" width="300" height="400" loading="lazy"></li>' for n in (1, 2, 4, 5, 7, 10, 12, 18))
    profs = [("camila", "Camila Veloso", "Fundadora e mediadora das aulas. Produtora editorial (UFSM)."),
             ("laura", "Laura Marques", "Produtora editorial e leitora crítica (UFSM)."),
             ("lucas", "Lucas Oliveira", "Mestre e doutor em Literatura Portuguesa (UFRJ)."),
             ("lavinia", "Lavínia Neres", "Produtora editorial, bacharel em Letras e mestra em Comunicação (UFSM)."),
             ("ana", "Ana Ribeiro", "Produtora editorial e mestra em Estudos de Linguagens (CEFET-MG).")]
    profs_html = "".join(f'<div class="am-prof"><img src="{{IMG:prof-{k}.jpg}}" alt="Foto de {n}" width="300" height="375" loading="lazy"><h3>{n}</h3><p>{d}</p></div>' for k, n, d in profs)
    press = ["PublishNews", "Digestivo Cultural", "Leia Já", "Hoje PR", "Reino Literário", "O Candeeiro", "Jornal Folk", "Gazeta da Semana"]
    press_html = "".join(f"<li>{E(x)}</li>" for x in press)
    ig = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1" fill="currentColor" stroke="none"/></svg>'
    tt = '<svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor" aria-hidden="true"><path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg>'
    return f'''
<div class="am-alert" role="status"><div class="am-wrap">
  <span class="am-alert__txt am-open"><strong>Black Friday:</strong> o AULÃO MASTER sai do ar em</span>
  <span class="am-count am-open" data-count="sale" aria-hidden="true"><span>7<small>d</small></span><span>00<small>h</small></span><span>00<small>min</small></span><span>00<small>s</small></span></span>
  <span class="am-alert__txt am-closed">Vendas encerradas. O AULÃO MASTER saiu do ar.</span>
</div></div>

<header class="am-top"><div class="am-wrap">
  <a class="am-brand" href="{SITE}/" aria-label="Aldeia Literária, página inicial"><img src="{{IMG:medalhao.png}}" alt="" width="46" height="46"><span>Aldeia Literária</span></a>
  <nav class="am-nav" aria-label="Principal"><a href="{SITE}/">Início</a><a href="{SOBRE}">Sobre</a><a href="{GUIA}">Guia</a><a href="{IMP}">Imprensa</a></nav>
  {cta_top}
</div></header>

<main id="topo">
<section class="am-hero" aria-labelledby="h1"><div class="am-wrap am-hero__grid">
  <div>
    <p class="am-eyebrow">Aula gravada · Black Friday 2026</p>
    <h1 id="h1"><span class="am-h1__big">AULÃO MASTER</span><span class="am-sr">: </span><span class="am-h1__sub">tudo o que você precisa saber para conseguir escrever um livro</span></h1>
    <p class="am-lede">Uma aula em seis blocos que mostra a estrutura por trás de toda boa história e leva você da ideia solta ao final do livro. Para quem quer escrever e não sabe por onde começar.</p>
    <div class="am-hero__buy">
      <div class="am-open" style="display:grid;gap:14px">
        <div class="am-price"><strong>R$ 97</strong><span>preço da Black Friday, só até 30/11</span></div>
        <div class="am-bonus-pill" data-bonus><b>1º dia:</b><span>quem comprar na segunda, 23/11, ganha 50% de desconto na matrícula da Aldeia Literária 2027.</span></div>
        <a id="am-hero-cta" class="am-btn am-btn--xl" href="{CHECKOUT}">Quero o AULÃO MASTER {ARROW.replace('<svg','<svg width="22" height="22"')}</a>
        <p class="am-micro">Acesso depois da confirmação do pagamento. 7 dias para desistir e receber o reembolso.</p>
      </div>
      <div class="am-closed"><p class="am-micro" style="font-size:1.05rem;color:var(--paper)">As vendas do AULÃO MASTER foram encerradas. As matrículas da Aldeia Literária abrem em janeiro de 2027.</p><p style="margin-top:12px"><a class="am-btn am-btn--light am-btn--sm" href="{WAIT}">Entrar na lista de espera</a></p></div>
    </div>
  </div>
  <div class="am-photo am-hero__photo">
    <img src="{{IMG:hero}}" alt="Camila Veloso, fundadora da Aldeia Literária, sorrindo diante de uma estante de livros" width="898" height="1600" fetchpriority="high">
    <div class="am-tag">Camila Veloso<small>Fundadora da Aldeia Literária</small></div>
  </div>
</div></section>

<section class="am-stats" aria-label="A Aldeia Literária em números"><div class="am-wrap"><div class="am-stats__card"><ul>
  <li><b>+400</b><span>escritores estudaram aqui</span></li>
  <li><b>2023</b><span>ano de fundação da Aldeia Literária</span></li>
  <li><b>120h</b><span>de extensão universitária, com certificado Anhanguera</span></li>
  <li><b>6h</b><span>de aula ao vivo por mês + atividades práticas semanais</span></li>
</ul></div></div></section>

<section class="am-band" id="o-que-e" aria-labelledby="t-oque"><div class="am-wrap am-answer">
  <div>
    <p class="am-eyebrow">Resposta direta</p>
    <h2 class="am-h2" id="t-oque">O que é o AULÃO MASTER?</h2>
    <p style="margin-top:20px"><strong>O AULÃO MASTER é uma aula gravada sobre o básico da narrativa, para quem quer escrever um livro.</strong> Ela reúne em um só lugar o que você precisa saber para estruturar uma história: os três atos, o arco do personagem, um checklist de 9 passos até o final, as formas de história e a premissa.</p>
    <p>Quem dá a aula é Camila Veloso, fundadora da Aldeia Literária, escola e comunidade de escrita criativa. Todo o conteúdo parte de uma ideia simples: alguém quer algo, enfrenta obstáculos e muda.</p>
  </div>
  <div>
    <p class="am-eyebrow">Ao final da aula, você sabe</p>
    <ul class="am-outcomes">{"".join(f"<li>{CHECK}<span>{o}</span></li>" for o in outcomes)}</ul>
  </div>
</div></section>

<section class="am-band am-band--sand" id="conteudo" aria-labelledby="t-conteudo"><div class="am-wrap">
  <div class="am-center"><p class="am-eyebrow">Neste aulão</p><h2 class="am-h2" id="t-conteudo">O que você vai aprender, em seis blocos</h2>
  <p class="am-lede" style="margin-top:14px">Tudo o que você precisa saber para escrever um livro, na ordem em que a aula acontece.</p></div>
  <div class="am-blocks">{blocks()}</div>
</div></section>

<section class="am-band am-band--navy" id="quem-sou-eu" aria-labelledby="t-eu"><div class="am-wrap am-about">
  <div class="am-photo"><img src="{{IMG:about}}" alt="Camila Veloso de óculos laranja segurando uma pilha de livros" width="898" height="1600" loading="lazy"></div>
  <div>
    <p class="am-eyebrow">Quem sou eu</p>
    <h2 id="t-eu">Camila Veloso</h2>
    <p class="am-lede">Fundadora e diretora da Aldeia Literária, escola e comunidade de escrita criativa.</p>
    <ul class="am-facts-list">
      <li>Comunicação Social, Produção Editorial (UFSM)</li>
      <li>Mais de seis anos em marketing e conteúdo, em B2B e B2C</li>
      <li>Ajudo escritores iniciantes a desenvolver e publicar seus livros</li>
      <li><a href="{INSTA}" rel="noopener">@acamiveloso</a></li>
    </ul>
  </div>
</div></section>


<section class="am-band" id="livros" aria-labelledby="t-livros"><div class="am-wrap">
  <div class="am-center"><p class="am-eyebrow">Comunidade de autores</p><h2 class="am-h2" id="t-livros">Livros escritos aqui</h2>
  <p class="am-lede" style="margin-top:14px">Alguns dos livros de escritores que passaram pela Aldeia Literária.</p></div>
  <ul class="am-books">{books_html}</ul>
</div></section>

<section class="am-band am-band--navy" id="depoimentos" aria-labelledby="t-dep"><div class="am-wrap">
  <div class="am-center"><p class="am-eyebrow">Quem já escreve com a Aldeia</p><h2 class="am-h2" id="t-dep">O que dizem as pessoas da Aldeia</h2></div>
  <div class="am-quotes">
    <figure class="am-quote am-quote--lead"><blockquote><p>Camila, queria agradecer por essas aulas. Minha mente evoluiu muito com essas descobertas, mas o mais importante é que eu consegui me encontrar na escrita, ter paciência comigo mesmo e me cobrar menos. Obrigado por ser tão lendária, a escrita tem um lugar no meu coração e agora irá desbravar o mundo comigo!</p></blockquote><figcaption><strong>Jader Emmanuel</strong></figcaption></figure>
    <figure class="am-quote"><blockquote><p>uma das coisas mais daora da aldeia (pra mim) é vc perceber q vc n ta sozinha e tem MT gnt kakak como vc</p></blockquote><figcaption><strong>Carlos Thomaz Evangelista</strong></figcaption></figure>
    <figure class="am-quote"><blockquote><p>A Cami é a melhor prof que a gente poderia ter no mundo todo, perfeita</p></blockquote><figcaption><strong>Taty Fe Rocha</strong></figcaption></figure>
    <figure class="am-quote"><blockquote><p>Falou tudo Taty, Camila tem um lugarzinho especial no coração de todos nós</p></blockquote><figcaption><strong>Martina Vian</strong><span>autora de Desejei às Estrelas</span></figcaption></figure>
    <figure class="am-quote"><blockquote><p>A Cami é um anjo! O propósito dela é lindo e isso faz dela incrível!</p></blockquote><figcaption><strong>Ingrid Maitê</strong></figcaption></figure>
  </div>
</div></section>

<section class="am-band" id="oferta" aria-labelledby="t-oferta"><div class="am-wrap">
  <div class="am-center"><p class="am-eyebrow">Black Friday</p><h2 class="am-h2" id="t-oferta">Sua vaga no AULÃO MASTER</h2>
  <p class="am-lede" style="margin-top:14px">Uma oferta, um preço e um prazo. Depois de 30/11, às 23h59, a aula sai do ar.</p></div>
  <div class="am-offer">
    <div class="am-card am-card--price">
      <h3>O que você leva</h3>
      <ul class="am-list">
        <li>{CHECK}<span>A aula gravada AULÃO MASTER, em seis blocos</span></li>
        <li>{CHECK}<span>Os três atos, o checklist de 9 passos, as formas de história e a premissa</span></li>
        <li>{CHECK}<span>Acesso liberado depois da confirmação do pagamento</span></li>
        <li>{CHECK}<span>7 dias para desistir e receber o reembolso</span></li>
      </ul>
      <div class="am-price"><strong>R$ 97</strong><span>pagamento da Black Friday</span></div>
      <div class="am-open"><a class="am-btn am-btn--xl" href="{CHECKOUT}">Quero o AULÃO MASTER {ARROW.replace('<svg','<svg width="22" height="22"')}</a></div>
      <div class="am-closed"><a class="am-btn am-btn--light" href="{WAIT}">Vendas encerradas. Entrar na lista de espera</a></div>
      <p class="am-note">Veja as regras na <a href="{CANC}">política de cancelamento e reembolso</a>.</p>
    </div>
    <div class="am-deadline">
      <div class="am-bonus" data-bonus><b>Bônus só no 1º dia: 50% de desconto na matrícula da Aldeia Literária 2027</b>
        <span>Vale para quem comprar até segunda, 23/11, às 23h59. As matrículas abrem em janeiro de 2027.</span>
        <span class="am-count" data-count="bonus" aria-hidden="true"></span></div>
      <div class="am-card" style="width:100%"><h3 style="font-size:1.35rem">A aula sai do ar em</h3>
        <div class="am-open"><span class="am-count am-count--big" data-count="sale" style="margin-top:14px" aria-hidden="true"></span>
        <p class="am-note" style="margin-top:12px">Venda encerra em 30/11, às 23h59 (horário de Brasília). Não vamos reabrir.</p></div>
        <p class="am-closed">A venda foi encerrada.</p></div>
    </div>
  </div>
</div></section>

<section class="am-band am-band--sand" id="aldeia" aria-labelledby="t-aldeia"><div class="am-wrap">
  <div class="am-center"><p class="am-eyebrow">Onde a escalada continua</p><h2 class="am-h2" id="t-aldeia">Aldeia Literária: do zero à publicação, em comunidade</h2>
  <p class="am-lede" style="margin-top:14px">Curso online de escrita criativa para escritores iniciantes, com extensão universitária de 120 horas e certificado emitido pela Anhanguera. Aulas ao vivo e gravadas, atividades e feedback individual.</p></div>
  <ul class="am-gallery" aria-label="A comunidade da Aldeia em encontros presenciais">{gallery_html}</ul>
  <div class="am-structure">
    <article><h3>Aulas ao vivo</h3><p>Quartas-feiras, às 19h30. 12 aulas por módulo, todas gravadas.</p></article>
    <article><h3>Feedback</h3><p>4 atividades por mês, com retorno individual sobre o seu texto.</p></article>
    <article><h3>Comunidade</h3><p>Grupo e espaço oficial com atividades extras e troca entre escritores.</p></article>
    <article><h3>Sprints</h3><p>Desafios de escrita em grupo para avançar no seu livro.</p></article>
  </div>
  <ol class="am-modules">
    <li><div><small>Módulo I</small><b>Fundamentos da narrativa</b></div><span>Estruturação da narrativa, desenvolvimento de personagem e mercado editorial brasileiro.</span></li>
    <li><div><small>Módulo II</small><b>Técnicas avançadas</b></div><span>Descrições, diálogos e técnicas específicas de escrita criativa e produção de livros no Brasil.</span></li>
    <li><div><small>Módulo III</small><b>Processos criativos</b></div><span>Como lidar com bloqueios criativos e lapidar ideias.</span></li>
    <li><div><small>Módulo IV</small><b>Gramática e produção literária</b></div><span>Normas gramaticais aplicadas à produção literária, ritmo e voz do texto.</span></li>
    <li><div><small>Módulo V</small><b>Publicação independente</b></div><span>Oportunidades, fornecedores e estratégias de autopublicação e mercado editorial.</span></li>
  </ol>
  <div class="am-center" style="margin-top:44px"><p class="am-eyebrow">Quem caminha com você</p><h3 class="am-h2" style="font-size:clamp(1.6rem,3vw,2.2rem)">Professores da Aldeia</h3></div>
  <div class="am-profs">{profs_html}</div>
  <div class="am-cert"><img src="{{IMG:certificados.jpg}}" alt="Certificado de extensão universitária da Aldeia Literária" width="190" height="285" loading="lazy"><div><h3>Certificado emitido pela Anhanguera</h3><p>A Aldeia Literária é um curso de extensão universitária com carga horária de 120h, reconhecida pelo MEC, em parceria com a Anhanguera. Ao concluir o curso, você recebe o seu certificado, emitido pela Anhanguera. Não é um curso de graduação ou de pós-graduação.</p></div></div>
  <p class="am-center" style="margin-top:28px;font-family:var(--f-title);font-weight:700;color:var(--navy);font-size:1.15rem">Matrículas abrem em janeiro de 2027. Vagas limitadas.</p>
</div></section>

<section class="am-band am-band--paper" id="midia" aria-labelledby="t-midia"><div class="am-wrap am-center">
  <p class="am-eyebrow">Imprensa</p><h2 class="am-h2" id="t-midia">Aldeia Literária na mídia</h2>
  <ul class="am-press">{press_html}</ul>
  <p style="margin-top:26px"><a class="am-btn am-btn--navy am-btn--sm" href="{IMP}">Ver todas as matérias</a></p>
</div></section>

<section class="am-band" id="duvidas" aria-labelledby="t-faq"><div class="am-wrap">
  <div class="am-center"><p class="am-eyebrow">Perguntas frequentes</p><h2 class="am-h2" id="t-faq">Tire suas dúvidas sobre o AULÃO MASTER</h2></div>
  <div class="am-faq">{faq_html()}</div>
</div></section>

<section class="am-band am-band--red am-mark" id="comprar" aria-labelledby="t-final"><div class="am-wrap am-final">
  <div>
    <p class="am-eyebrow">Última chamada</p>
    <h2 id="t-final">Escreva o seu livro. O primeiro passo custa R$ 97.</h2>
    <p>O AULÃO MASTER sai do ar em 30/11, às 23h59. Quem comprar na segunda, 23/11, ainda leva 50% de desconto na matrícula da Aldeia Literária 2027.</p>
    <div class="am-open"><span class="am-count am-count--big" data-count="sale" aria-hidden="true"></span><a class="am-btn am-btn--light am-btn--xl" href="{CHECKOUT}">Quero o AULÃO MASTER por R$ 97</a></div>
    <p class="am-closed">As vendas foram encerradas. As matrículas da Aldeia abrem em janeiro de 2027.</p>
  </div>
  <div class="am-photo"><img src="{{IMG:final}}" alt="Camila Veloso de óculos laranja sorrindo com livros nas mãos" width="898" height="1600" loading="lazy"></div>
</div></section>
</main>

<footer class="am-footer"><div class="am-wrap">
  <div class="am-footer__social" aria-label="Redes sociais da Aldeia Literária">
    <a class="am-footer__ico" href="{INSTA_ALDEIA}" target="_blank" rel="noopener noreferrer me" aria-label="Instagram da Aldeia Literária">{ig}</a>
    <a class="am-footer__ico" href="{TIKTOK}" target="_blank" rel="noopener noreferrer me" aria-label="TikTok da Aldeia Literária">{tt}</a>
  </div>
  <p><a class="am-footer__media" href="{IMP}">Aldeia Literária na mídia</a></p>
  <p><a href="{SITE}/">Início</a> · <a href="{SOBRE}">Sobre</a> · <a href="{GUIA}">Guia</a> · <a href="{IMP}">Imprensa</a> · <a href="{CANC}">Cancelamento e reembolso</a></p>
  <p>© Aldeia Literária · Curso de escrita para iniciantes · Todos os direitos reservados</p>
  <p>CAMILA VELOSO. CO LTDA · CNPJ 47.277.682/0001-48</p>
</div></footer>

<div class="am-sticky am-open" id="am-sticky"><div><b>R$ 97</b><small>sai do ar em 30/11</small></div><a class="am-btn am-btn--sm" href="{CHECKOUT}">Quero o aulão</a></div>
{jsonld()}
'''


FONTS = [("Outfit", 600), ("Outfit", 700), ("Outfit", 800), ("Figtree", 400), ("Figtree", 500), ("Figtree", 600), ("Figtree", 700)]
IMGS = {"hero": "camila-sorrindo.jpg", "about": "camila-oculos-livros.jpg", "final": "camila-livros-sorriso.jpg", "logo": "logo-camila-veloso-branco.png"}


def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()


def font_css(inline):
    out = ""
    for fam, w in FONTS:
        f = f"{fam.lower()}-latin-{w}-normal.woff2"
        src = b64(os.path.join(ASSETS, "fonts", f), "font/woff2") if inline else f"aulao/fonts/{f}"
        out += f'@font-face{{font-family:"{fam}";font-weight:{w};font-style:normal;font-display:swap;src:url({src}) format("woff2")}}\n'
    return out


def assemble(inline):
    body = page()
    def img(m):
        k = m.group(1)
        f = IMGS.get(k, k)
        mime = "image/png" if f.endswith(".png") else "image/jpeg"
        return b64(os.path.join(ASSETS, "img", f), mime) if inline else f"aulao/img/{f}"
    body = re.sub(r"\{IMG:([^}]+)\}", img, body)
    css = open(os.path.join(HERE, "aulao.css"), encoding="utf-8").read()
    css = re.sub(r"\{IMGURL:([^}]+)\}", lambda m: b64(os.path.join(ASSETS, "img", m.group(1)), "image/png") if inline else f"aulao/img/{m.group(1)}", css)
    js = open(os.path.join(HERE, "aulao.js"), encoding="utf-8").read()
    return f"<style>\n{font_css(inline)}{css}</style>\n{body}\n<script>\n{js}</script>\n"


def main():
    frag = assemble(False)
    head = f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{E(TITLE)} | Aldeia Literária</title>
<meta name="description" content="{E(DESC)}">
<link rel="canonical" href="{URL}">
<meta property="og:type" content="website"><meta property="og:title" content="{E(TITLE)}"><meta property="og:description" content="{E(DESC)}"><meta property="og:url" content="{URL}"><meta property="og:locale" content="pt_BR">
</head><body>
'''
    open(os.path.join(ROOT, "preview", "aulao-master.html"), "w", encoding="utf-8").write(head + frag + "</body></html>\n")
    scratch = os.environ.get("SCRATCH")
    if scratch:
        art = ('<title>AULÃO MASTER</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n' + assemble(True))
        open(os.path.join(scratch, "aulao-master-artifact.html"), "w", encoding="utf-8").write(art)
        print("artifact", len(art) // 1024, "KB")
    print("ok", len(frag) // 1024, "KB")


if __name__ == "__main__":
    main()
