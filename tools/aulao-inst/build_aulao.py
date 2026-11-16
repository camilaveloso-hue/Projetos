#!/usr/bin/env python3
"""AULÃO MASTER — versão institucional (Black Friday 2026).

Uso: python3 tools/aulao-inst/build_aulao.py   (SCRATCH=<pasta> também gera a prévia autocontida para o Artifact)
Saídas: preview/aulao-master-institucional.html (fotos em preview/aulao/img, fontes em preview/aulao-inst/fonts)
Conteúdo: slides do AULÃO MASTER + planilha de aprendizados de lançamentos + fatos já publicados no site da Aldeia."""
import base64, html, json, math, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
IMGDIR = os.path.join(ROOT, "preview", "aulao", "img")
FONTDIR = os.path.join(ROOT, "preview", "aulao-inst", "fonts")
E = html.escape

SITE = "https://aaldeialiteraria.com.br"
SLUG = "/aulao-master/"
URL = SITE + SLUG
CHECKOUT = "#oferta"            # TROCAR pelo link do checkout quando a plataforma estiver definida
CANC = SITE + "/politica-de-cancelamento-e-reembolso/"
WAIT = "https://tally.so/r/0QNWPy"
INSTA = "https://www.instagram.com/acamiveloso/"
INSTA_ALDEIA = "https://www.instagram.com/aldeialiteraria.oficial/"
TIKTOK = "https://www.tiktok.com/@aldeialiteraria"
GUIA = SITE + "/como-escolher-curso-de-escrita-criativa/"
IMP = SITE + "/imprensa/"
SOBRE = SITE + "/novo-sobre/"
FUNDADORA = SITE + "/sobre-a-fundadora/"
TITLE = "AULÃO MASTER: tudo o que você precisa saber para conseguir escrever um livro"
DESC = ("Aulão gravado de Camila Veloso, fundadora da Aldeia Literária: os três atos, o checklist de 9 passos, "
        "as formas de história e como escrever a premissa. R$ 97 na Black Friday, até 30/11.")

CHECK = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="11" fill="currentColor"/><path d="M7 12.5l3.2 3.2L17 8.8" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 12h15m0 0l-5-5m5 5l-5 5" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW_BTN = ARROW.replace("<svg", '<svg width="22" height="22"')

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
 ("A empresa é registrada? Como confirmo que a compra é segura?",
  "Sim. A Aldeia Literária é operada por CAMILA VELOSO. CO LTDA, CNPJ 47.277.682/0001-48, que você pode consultar na Receita Federal. Os canais oficiais são o site aaldeialiteraria.com.br e os perfis @aldeialiteraria.oficial e @acamiveloso no Instagram."),
]


def faq_html():
    return "".join(f'<details open><summary>{E(q)}</summary><div class="am-ans"><p>{a}</p></div></details>' for q, a in FAQ)


def jsonld():
    plain = lambda s: re.sub(r"<[^>]+>", "", html.unescape(s))
    data = {"@context": "https://schema.org", "@graph": [
        {"@type": "Course", "@id": URL + "#aula", "name": TITLE, "url": URL, "inLanguage": "pt-BR", "description": DESC,
         "about": ["Estrutura narrativa", "Escrita criativa", "Como escrever um livro"],
         "teaches": "Estrutura de três atos, arco do personagem, checklist de 9 passos, formas de história e premissa.",
         "educationalLevel": "Iniciante", "isAccessibleForFree": False,
         "provider": {"@type": "EducationalOrganization", "@id": SITE + "/#aldeia", "name": "Aldeia Literária", "url": SITE + "/",
                      "legalName": "CAMILA VELOSO. CO LTDA", "taxID": "47.277.682/0001-48"},
         "instructor": {"@type": "Person", "name": "Camila Veloso", "jobTitle": "Fundadora e diretora da Aldeia Literária",
                        "sameAs": [INSTA], "worksFor": {"@id": SITE + "/#aldeia"}},
         "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "online"},
         "offers": {"@type": "Offer", "price": "97.00", "priceCurrency": "BRL", "availability": "https://schema.org/InStock",
                    "url": URL, "validFrom": "2026-11-23T00:00:00-03:00", "priceValidUntil": "2026-11-30"}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in FAQ]},
    ]}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "</script>"


# ---------------------------------------------------------------- desenhos dos slides (cores da identidade institucional)
INK, RED = "#0a0a0a", "#991b1b"


def svg_forms():
    lin = (f'<svg viewBox="0 0 220 70" aria-hidden="true"><line x1="14" y1="35" x2="168" y2="35" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
           + "".join(f'<circle cx="{x}" cy="35" r="7" fill="{INK}"/>' for x in (14, 54, 94, 134))
           + f'<circle cx="168" cy="35" r="13" fill="{RED}"/><path d="M190 22v26l22-13z" fill="{RED}"/></svg>')
    sin = (f'<svg viewBox="0 0 220 70" aria-hidden="true"><path d="M14 56C40 56 46 14 74 14S104 58 134 58 176 30 196 24" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
           f'<circle cx="14" cy="56" r="7" fill="{INK}"/><circle cx="200" cy="22" r="12" fill="{RED}"/></svg>')
    sp = ""
    for i in range(12):
        a = i * math.tau / 12 + .25
        r1, r2 = 20, 28 + (i % 3) * 5
        x1, y1, x2, y2 = 110 + r1 * math.cos(a) * 1.6, 35 + r1 * math.sin(a), 110 + r2 * math.cos(a) * 2.3, 35 + r2 * math.sin(a) * 1.15
        sp += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/><circle cx="{x2:.1f}" cy="{y2:.1f}" r="4.5" fill="{INK}"/>'
    exp = f'<svg viewBox="0 0 220 70" aria-hidden="true">{sp}<circle cx="110" cy="35" r="13" fill="{RED}"/></svg>'
    return lin, sin, exp


def svg_arc():
    z = ('<rect x="0" y="0" width="150" height="190" rx="12" fill="#fef8c3"/><rect x="154" y="0" width="292" height="190" rx="12" fill="#f0efec"/>'
         '<rect x="450" y="0" width="150" height="190" rx="12" fill="#dcfce7"/>')
    path = f'<path d="M24 112C70 114 100 104 150 92C215 76 255 55 285 88C305 112 312 156 330 160C365 166 400 108 450 98C500 88 535 46 576 40" fill="none" stroke="{INK}" stroke-width="4.5" stroke-linecap="round"/>'
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="9" fill="{RED}"/>' for x, y in ((24, 112), (150, 92), (330, 160), (450, 98), (576, 40)))
    return f'<svg viewBox="0 0 600 190" role="img" aria-label="Curva do arco do personagem nos três atos">{z}{path}{dots}</svg>'


def blocks():
    lin, sin, exp = svg_forms()
    steps = [("Início", [("Ambientação", "Rotina do personagem no ponto A."), ("Problema central", "O conflito que move a história.")]),
             ("Primeiro limiar", [("Recusa", "Ele foge do problema."), ("Obrigado a agir", "Tenta resolver sem novas habilidades.")]),
             ("Clímax", [("Pequena vitória", "Ele muda e se aproxima do ponto B."), ("Tudo dá errado", "O personagem é testado e amadurece.")]),
             ("Caminho de volta", [("Ajuda e plano", "Aliados dão novas ferramentas."), ("Confronto final", "O amadurecimento prova ser real.")]),
             ("Fim", [("Vida nova", "Mostra como é o ponto B.")])]
    n, steps_html = 0, ""
    for head, items in steps:
        cells = ""
        for t, d in items:
            n += 1
            cells += f'<p><b><span>{n}</span> · {E(t)}</b>{E(d)}</p>'
        steps_html += f'<div><h4>{E(head)}</h4>{cells}</div>'

    def head(num, title, sub):
        return f'<div class="am-block__head"><span class="am-block__n" aria-hidden="true">{num}</span><span class="am-block__sub">{sub}</span><h3>{title}</h3></div>'

    b1 = f'''<article class="am-block">{head(1, "Os três atos e o arco", "O esqueleto e a mudança do personagem")}
  <p>Toda história tem um esqueleto. Você vai ver como ele se divide em três atos e como o personagem muda do começo ao fim, da fraqueza e da necessidade até o novo equilíbrio.</p>
  <div><div class="am-acts"><div class="a1">Ato I<small>Apresentação · 25%</small></div><div class="a2">Ato II<small>Confronto · 50%</small></div><div class="a3">Ato III<small>Resolução · 25%</small></div></div>
  <ul class="am-qs"><li><b>Ato I</b><span>Quem é o herói e o que está em jogo?</span></li><li><b>Ato II</b><span>O que acontece quando ele tenta conseguir o que quer?</span></li><li><b>Ato III</b><span>Como termina e o que mudou?</span></li></ul>
  <div class="am-arc">{svg_arc()}<ol><li>Fraqueza e necessidade</li><li>Primeiro limiar</li><li>Provação suprema</li><li>Autorrevelação</li><li>Novo equilíbrio</li></ol></div></div></article>'''
    b2 = f'''<article class="am-block">{head(2, "O checklist da história", "9 passos até o final")}
  <p>Um caminho de nove passos para você chegar ao final da sua história sem travar no meio. Pode haver mais capítulos, desde que a estrutura seja respeitada.</p>
  <div class="am-steps">{steps_html}</div></article>'''
    b3 = f'''<article class="am-block">{head(3, "Por que você lê livros", "A função de uma história")}
  <p>Contamos histórias para entender como a vida funciona e como agir nela. O herói é a porta de entrada do leitor: ele se identifica, atravessa a jornada junto e volta transformado.</p>
  <div><div class="am-flow"><div class="f1">Desejo<small>o que a pessoa quer conseguir</small></div>{ARROW}<div class="f2">Obstáculo<small>o que se coloca no caminho</small></div>{ARROW}<div class="f3">Transformação<small>quem ela é no final</small></div></div>
  <p class="am-flowcap">Alguém quer algo, enfrenta obstáculos e muda.</p></div></article>'''
    b4 = f'''<article class="am-block">{head(4, "As formas de história", "Linear, sinuosa e explosiva")}
  <p>O esqueleto é parecido, mas a forma muda de história para história. Desejo, obstáculo e transformação aparecem em todas; o ritmo é que varia.</p>
  <div class="am-forms">
    <div class="am-form">{lin}<h4>Linear</h4><p>Um único protagonista, do começo ao fim, perseguindo um desejo com muita intensidade.</p><em>Cinderela · Star Wars · Die Hard</em></div>
    <div class="am-form">{sin}<h4>Sinuosa</h4><p>Caminho cheio de voltas, desejo menos intenso e muitos encontros pelo caminho.</p><em>Odisseia · Dom Quixote · Tom Jones</em></div>
    <div class="am-form">{exp}<h4>Explosiva</h4><p>Vários caminhos ao mesmo tempo, contados em cortes alternados entre as linhas da história.</p><em>Pulp Fiction · Crash · Nashville</em></div>
  </div></article>'''
    b5 = f'''<article class="am-block">{head(5, "Premissa, princípio e arco", "Da ideia à página")}
  <p>O princípio dá a direção, a premissa conta o que acontece e o arco mostra quem muda. Você vai aprender a resumir sua história em uma frase e a enxergar o arco em duas fotografias: antes e depois.</p>
  <div><div class="am-trio"><article class="t1"><h4>Princípio narrativo</h4><p>A ideia central que sustenta a história inteira e dá sentido a cada cena.</p></article>
  <article class="t2"><h4>Premissa</h4><p>A história resumida em uma frase: quem é o personagem, o que quer, o que o impede e qual a consequência.</p></article>
  <article class="t3"><h4>Arco</h4><p>A mudança do personagem do início ao fim, de uma falha para uma transformação.</p></article></div>
  <div class="am-scrooge"><div><b>Antes · Ato I</b>Scrooge só pensa em dinheiro e se isola.</div><div><b>Depois · Ato III</b>Scrooge se torna generoso e celebra o Natal com os outros.</div></div>
  <p class="am-scrooge-cap">Exemplo: Um conto de Natal, de Charles Dickens.</p></div></article>'''
    b6 = f'''<article class="am-block">{head(6, "Próximos passos", "O que vem depois do básico")}
  <p>O básico é só o primeiro degrau. Para fechar, você vê o mapa completo da escalada: do que aprendeu no aulão até a publicação independente do seu livro.</p>
  <div class="am-ladder"><div class="l0">O básico<small>você está aqui</small></div><div class="l1">Módulo I<small>Fundamentos da narrativa</small></div><div class="l2">Módulo II<small>Técnicas avançadas</small></div><div class="l3">Módulo III<small>Processos criativos</small></div><div class="l4">Módulo IV<small>Gramática e produção literária</small></div><div class="l5">Módulo V<small>Publicação independente</small></div></div></article>'''
    return "\n".join([b1, b2, b3, b4, b5, b6])


def page():
    outcomes = ["Dividir sua história nos três atos e saber o que cada um precisa responder.",
                "Usar o checklist de 9 passos para chegar ao final sem travar no meio.",
                "Escolher a forma da sua história: linear, sinuosa ou explosiva.",
                "Resumir o livro em uma premissa de uma frase e desenhar o arco do personagem."]
    profs = [("camila", "Camila Veloso", "Fundadora e mediadora das aulas. Produtora editorial (UFSM)."),
             ("laura", "Laura Marques", "Produtora editorial e leitora crítica (UFSM)."),
             ("lucas", "Lucas Oliveira", "Mestre e doutor em Literatura Portuguesa (UFRJ)."),
             ("lavinia", "Lavínia Neres", "Produtora editorial, bacharel em Letras e mestra em Comunicação (UFSM)."),
             ("ana", "Ana Ribeiro", "Produtora editorial e mestra em Estudos de Linguagens (CEFET-MG).")]
    profs_html = "".join(f'<div class="am-prof"><img src="{{IMG:prof-{k}.jpg}}" alt="Foto de {n}" width="300" height="375" loading="lazy"><h3>{n}</h3><p>{d}</p></div>' for k, n, d in profs)
    modules = [("Módulo I", "Fundamentos da narrativa", "Estruturação da narrativa, desenvolvimento de personagem e mercado editorial brasileiro."),
               ("Módulo II", "Técnicas avançadas", "Descrições, diálogos e técnicas específicas de escrita criativa e produção de livros no Brasil."),
               ("Módulo III", "Processos criativos", "Como lidar com bloqueios criativos e lapidar ideias."),
               ("Módulo IV", "Gramática e produção literária", "Normas gramaticais aplicadas à produção literária, ritmo e voz do texto."),
               ("Módulo V", "Publicação independente", "Oportunidades, fornecedores e estratégias de autopublicação e mercado editorial.")]
    modules_html = "".join(f"<li><div><small>{a}</small><b>{b}</b></div><span>{c}</span></li>" for a, b, c in modules)
    ig = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/></svg>'
    return f'''
<div class="am-alert" role="status"><div class="am-wrap">
  <span class="am-alert__txt am-open"><strong>Black Friday:</strong> o AULÃO MASTER sai do ar em</span>
  <span class="am-count am-open" data-count="sale" aria-hidden="true"><span>7<small>d</small></span><span>00<small>h</small></span><span>00<small>min</small></span><span>00<small>s</small></span></span>
  <span class="am-alert__txt am-closed">Vendas encerradas. O AULÃO MASTER saiu do ar.</span>
</div></div>

<header class="am-top"><div class="am-wrap">
  <a class="am-brand" href="{SITE}/" aria-label="Aldeia Literária, página inicial">Aldeia Literária<i>.</i></a>
  <nav class="am-nav" aria-label="Principal"><a href="{SITE}/">Início</a><a href="{SOBRE}">Sobre</a><a href="{GUIA}">Guia</a><a href="{IMP}">Imprensa</a></nav>
  <a class="am-btn am-btn--sm am-open" href="{CHECKOUT}">Quero o aulão</a>
</div></header>

<main id="topo">
<section class="am-hero" aria-labelledby="h1"><div class="am-wrap">
  <span class="am-pill">Página oficial · Aula gravada · Black Friday 2026</span>
  <h1 id="h1">AULÃO MASTER<span class="am-sr">: </span><span class="am-serif">tudo o que você precisa saber para conseguir escrever um livro.</span></h1>
  <p class="am-lead">Uma aula gravada em seis blocos que mostra a estrutura por trás de toda boa história e <span class="am-mark">leva você da ideia solta ao final do livro</span>. Para quem quer escrever e não sabe por onde começar.</p>
  <div class="am-author"><img src="{{IMG:camila-sorrindo.jpg}}" alt="Camila Veloso" width="100" height="100">
    <div><strong>Camila Veloso</strong><span>Fundadora da Aldeia Literária · Produtora editorial (UFSM) · <a href="{INSTA}" rel="noopener">@acamiveloso</a></span></div></div>

  <div class="am-buy" id="comprar">
    <div class="am-open" style="display:grid;gap:18px">
      <div class="am-buy__price"><small>Preço da Black Friday</small><strong>R$ 97</strong><span>até 30/11, às 23h59 · depois disso a aula sai do ar</span></div>
      <div class="am-buy__bonus" data-bonus><b>Bônus do 1º dia:</b> quem comprar na segunda, 23/11, ganha 50% de desconto na matrícula da Aldeia Literária 2027.</div>
      <a id="am-hero-cta" class="am-btn am-btn--xl" href="{CHECKOUT}">Quero o AULÃO MASTER {ARROW_BTN}</a>
      <p class="am-buy__micro">Acesso depois da confirmação do pagamento. 7 dias para desistir e receber o reembolso. <a href="{CANC}">Ver política</a>.</p>
    </div>
    <div class="am-closed"><p class="am-lead" style="font-size:1.1rem">As vendas do AULÃO MASTER foram encerradas. As matrículas da Aldeia Literária abrem em janeiro de 2027.</p><p style="margin-top:14px"><a class="am-btn am-btn--ink am-btn--sm" href="{WAIT}">Entrar na lista de espera</a></p></div>
  </div>
</div></section>

<section class="am-sec am-sec--tight" id="o-que-e" aria-labelledby="t-oque"><div class="am-wrap">
  <p class="am-kicker">Resposta direta</p>
  <h2 class="am-h2" id="t-oque">O que é o AULÃO MASTER?</h2>
  <div class="am-prose" style="margin-top:24px">
    <p class="am-lead"><strong>O AULÃO MASTER é uma aula gravada sobre o básico da narrativa, para quem quer escrever um livro.</strong> Ela reúne em um só lugar o que você precisa saber para estruturar uma história: os três atos, o arco do personagem, um checklist de 9 passos até o final, as formas de história e a premissa.</p>
    <p>Quem dá a aula é Camila Veloso, fundadora da Aldeia Literária, escola e comunidade de escrita criativa. Todo o conteúdo parte de uma ideia simples: alguém quer algo, enfrenta obstáculos e muda.</p>
  </div>
  <figure class="am-figure" style="margin-top:34px"><img src="{{IMG:camila-livros-sorriso.jpg}}" alt="Camila Veloso de óculos laranja sorrindo com livros nas mãos" width="898" height="1600" loading="lazy"><figcaption>Camila Veloso, fundadora da Aldeia Literária e professora do AULÃO MASTER.</figcaption></figure>
  <p class="am-kicker" style="margin-top:44px">Ao final da aula, você sabe</p>
  <ul class="am-outcomes" style="margin-top:0">{"".join(f"<li>{CHECK}<span>{o}</span></li>" for o in outcomes)}</ul>
</div></section>

<section class="am-sec am-sec--ink am-quoteband" aria-label="A ideia central da aula"><div class="am-wrap">
  <p>“Alguém quer algo, enfrenta obstáculos e muda.”</p>
  <cite>A síntese do AULÃO MASTER</cite>
</div></section>

<section class="am-sec am-sec--warm" id="conteudo" aria-labelledby="t-conteudo"><div class="am-wrap am-wrap--wide">
  <div style="max-width:var(--read)"><p class="am-kicker">Neste aulão</p><h2 class="am-h2" id="t-conteudo">O que você vai aprender, <span class="am-serif">em seis blocos.</span></h2>
  <p class="am-lead" style="margin-top:18px">Tudo o que você precisa saber para escrever um livro, na ordem em que a aula acontece.</p></div>
  <div class="am-blocks">{blocks()}</div>
</div></section>

<section class="am-sec" id="depoimentos" aria-labelledby="t-dep"><div class="am-wrap am-wrap--wide">
  <div style="max-width:var(--read)"><p class="am-kicker">Quem já escreve com a Aldeia</p><h2 class="am-h2" id="t-dep">O que dizem as pessoas <span class="am-serif">da Aldeia.</span></h2>
  <p class="am-lead" style="margin-top:18px">Depoimentos de alunos e alunas, os mesmos que estão publicados na Home da Aldeia Literária.</p></div>
  <div class="am-quotes">
    <figure class="am-quote am-quote--lead"><blockquote><span class="am-pill">Depoimento</span><p>Camila, queria agradecer por essas aulas. Minha mente evoluiu muito com essas descobertas, mas o mais importante é que eu consegui me encontrar na escrita, ter paciência comigo mesmo e me cobrar menos. Obrigado por ser tão lendária, a escrita tem um lugar no meu coração e agora irá desbravar o mundo comigo!</p></blockquote><figcaption><strong>Jader Emmanuel</strong></figcaption></figure>
    <figure class="am-quote"><blockquote><span class="am-pill">Depoimento</span><p>uma das coisas mais daora da aldeia (pra mim) é vc perceber q vc n ta sozinha e tem MT gnt kakak como vc</p></blockquote><figcaption><strong>Carlos Thomaz Evangelista</strong></figcaption></figure>
    <figure class="am-quote"><blockquote><span class="am-pill">Depoimento</span><p>A Cami é a melhor prof que a gente poderia ter no mundo todo, perfeita</p></blockquote><figcaption><strong>Taty Fe Rocha</strong></figcaption></figure>
    <figure class="am-quote"><blockquote><span class="am-pill">Depoimento</span><p>Falou tudo Taty, Camila tem um lugarzinho especial no coração de todos nós</p></blockquote><figcaption><strong>Martina Vian</strong>autora de Desejei às Estrelas</figcaption></figure>
    <figure class="am-quote"><blockquote><span class="am-pill">Depoimento</span><p>A Cami é um anjo! O propósito dela é lindo e isso faz dela incrível!</p></blockquote><figcaption><strong>Ingrid Maitê</strong></figcaption></figure>
  </div>
</div></section>

<section class="am-sec am-sec--warm" id="quem-sou-eu" aria-labelledby="t-eu"><div class="am-wrap">
  <p class="am-kicker">Quem dá a aula</p>
  <h2 class="am-h2" id="t-eu">Deixa eu me apresentar. <span class="am-serif">Sou a Camila.</span></h2>
  <figure class="am-figure" style="margin-top:30px"><img src="{{IMG:camila-oculos-livros.jpg}}" alt="Camila Veloso de óculos laranja segurando uma pilha de livros" width="898" height="1600" loading="lazy" style="object-position:50% 38%"></figure>
  <div class="am-bio"><div class="am-prose">
    <p>Sou fundadora e diretora da <strong>Aldeia Literária</strong>, escola e comunidade de escrita criativa criada em 2023. Hoje ajudo escritores iniciantes a desenvolver e publicar seus livros, e mais de 400 pessoas já estudaram por aqui.</p>
    <p>O AULÃO MASTER é o que eu mostraria a qualquer pessoa que me dissesse "quero escrever um livro, mas não sei por onde começar".</p></div>
    <ul class="am-bio__facts">
      <li>{CHECK}<span>Comunicação Social, Produção Editorial (UFSM)</span></li>
      <li>{CHECK}<span>Mais de seis anos em marketing e conteúdo, em B2B e B2C</span></li>
      <li>{CHECK}<span>Ajudo escritores iniciantes a desenvolver e publicar seus livros</span></li>
    </ul>
    <p class="am-bio__sign">Camila Veloso</p><p class="am-bio__role">Fundadora da Aldeia Literária · <a href="{INSTA}" rel="noopener">@acamiveloso</a> · <a href="{FUNDADORA}">Sobre a fundadora</a></p>
  </div>
</div></section>

<section class="am-sec" id="seguranca" aria-labelledby="t-seg"><div class="am-wrap am-wrap--wide"><div class="am-verify">
  <h2 id="t-seg">Compre com segurança. <span class="am-serif">Dá para conferir cada informação.</span></h2>
  <div class="am-verify__grid">
    <div><b>7 dias</b><strong>Reembolso do valor pago</strong><p>Você tem 7 dias corridos depois da compra para desistir. O retorno vem em até 5 dias úteis. <a href="{CANC}">Ler a política completa</a>.</p></div>
    <div><b>CNPJ</b><strong>Empresa registrada</strong><p>CAMILA VELOSO. CO LTDA, CNPJ 47.277.682/0001-48. Você pode consultar na Receita Federal.</p></div>
    <div><b>Oficial</b><strong>Canais da Aldeia</strong><p>Site <a href="{SITE}/">aaldeialiteraria.com.br</a>, Instagram <a href="{INSTA_ALDEIA}" rel="noopener">@aldeialiteraria.oficial</a> e <a href="{INSTA}" rel="noopener">@acamiveloso</a>. Veja também a página <a href="{IMP}">Imprensa</a>.</p></div>
  </div>
  <p class="am-verify__close">Quem confere antes de comprar decide melhor.</p>
</div></div></section>

<section class="am-sec am-sec--warm" id="oferta" aria-labelledby="t-oferta"><div class="am-wrap">
  <p class="am-kicker">Black Friday</p>
  <h2 class="am-h2" id="t-oferta">Sua vaga no AULÃO MASTER. <span class="am-serif">Uma oferta, um preço, um prazo.</span></h2>
  <div class="am-offer">
    <div class="am-offer__body">
      <ul class="am-list">
        <li>{CHECK}<span>A aula gravada AULÃO MASTER, em seis blocos</span></li>
        <li>{CHECK}<span>Os três atos, o checklist de 9 passos, as formas de história e a premissa</span></li>
        <li>{CHECK}<span>Acesso liberado depois da confirmação do pagamento</span></li>
        <li>{CHECK}<span>7 dias para desistir e receber o reembolso</span></li>
      </ul>
      <div class="am-offer__price"><strong>R$ 97</strong><span>preço da Black Friday, só até 30/11, às 23h59</span></div>
      <div class="am-open"><a class="am-btn am-btn--xl" href="{CHECKOUT}">Quero o AULÃO MASTER {ARROW_BTN}</a></div>
      <div class="am-closed"><a class="am-btn am-btn--ink am-btn--xl" href="{WAIT}">Vendas encerradas. Entrar na lista de espera</a></div>
    </div>
    <div class="am-offer__bonus" data-bonus><b>Bônus só no 1º dia: 50% de desconto na matrícula da Aldeia Literária 2027</b>
      <span>Vale para quem comprar até segunda, 23/11, às 23h59. As matrículas abrem em janeiro de 2027.</span>
      <span class="am-count" data-count="bonus" aria-hidden="true"></span></div>
    <div class="am-offer__foot">
      <strong>A aula sai do ar em</strong>
      <div class="am-open"><span class="am-count am-count--big" data-count="sale" aria-hidden="true"></span></div>
      <p class="am-note am-open">A venda encerra em 30/11, às 23h59 (horário de Brasília). Depois disso o AULÃO MASTER sai do ar e não será reaberto. Regras na <a href="{CANC}">política de cancelamento e reembolso</a>.</p>
      <p class="am-note am-closed">A venda foi encerrada.</p>
    </div>
  </div>
</div></section>

<section class="am-sec" id="aldeia" aria-labelledby="t-aldeia"><div class="am-wrap am-wrap--wide">
  <div style="max-width:var(--read)"><p class="am-kicker">Onde a escalada continua</p>
  <h2 class="am-h2" id="t-aldeia">Aldeia Literária: <span class="am-serif">do zero à publicação, em comunidade.</span></h2>
  <p class="am-lead" style="margin-top:18px">Curso online de escrita criativa para escritores iniciantes, em extensão universitária de 120 horas. Aulas ao vivo e gravadas, atividades e feedback individual. Matrículas abrem em janeiro de 2027, com vagas limitadas.</p></div>
  <div class="am-structure">
    <article><h3>Aulas ao vivo</h3><p>Quartas-feiras, às 19h30. 12 aulas por módulo, todas gravadas.</p></article>
    <article><h3>Feedback</h3><p>4 atividades por mês, com retorno individual sobre o seu texto.</p></article>
    <article><h3>Comunidade</h3><p>Grupo e espaço oficial com atividades extras e troca entre escritores.</p></article>
    <article><h3>Sprints</h3><p>Desafios de escrita em grupo para avançar no seu livro.</p></article>
  </div>
  <ol class="am-modules">{modules_html}</ol>
  <p class="am-kicker" style="margin-top:50px">Quem caminha com você</p><h3 class="am-h2" style="font-size:clamp(1.7rem,3.6vw,2.3rem)">Professores da Aldeia</h3>
  <div class="am-profs">{profs_html}</div>
  <div class="am-cert"><img src="{{IMG:certificados.jpg}}" alt="Certificado de extensão universitária da Aldeia Literária" width="150" height="224" loading="lazy"><div><h3>Certificado emitido pela Anhanguera</h3><p>A Aldeia Literária é um curso de extensão universitária com carga horária de 120h, reconhecida pelo MEC, em parceria com a Anhanguera. Ao concluir o curso, você recebe o seu certificado, emitido pela Anhanguera. Não é um curso de graduação ou de pós-graduação.</p></div></div>
</div></section>

<section class="am-sec am-sec--warm" id="duvidas" aria-labelledby="t-faq"><div class="am-wrap">
  <p class="am-kicker">Perguntas frequentes</p>
  <h2 class="am-h2" id="t-faq">Tire suas dúvidas <span class="am-serif">sobre o AULÃO MASTER.</span></h2>
  <div class="am-faq">{faq_html()}</div>
</div></section>

<section class="am-sec" id="fechamento" aria-labelledby="t-fim"><div class="am-wrap">
  <h2 class="am-h2" id="t-fim">Uma última coisa.</h2>
  <div class="am-letter" style="margin-top:28px">
    <p>Olha,</p>
    <p>Eu quero que você decida com calma, mas com data. O AULÃO MASTER fica no ar até 30/11, às 23h59. Depois disso, ele sai do ar e eu não volto a vender.</p>
    <p>Se você tem uma ideia de livro e não sabe por onde começar, essa aula foi feita para você. Se ainda não é o momento, tudo bem: as matrículas da Aldeia abrem em janeiro de 2027.</p>
    <p>Todo livro começa do mesmo jeito: alguém quer algo, enfrenta obstáculos e muda. Comece pelo seu.</p>
    <p class="am-serif">Um abraço,<br>Camila.</p>
  </div>
  <div class="am-cta">
    <div class="am-open" style="display:grid;gap:16px;justify-items:center;width:100%">
      <h3>Comece o seu livro pelo AULÃO MASTER</h3>
      <span class="am-count am-count--big" data-count="sale" aria-hidden="true"></span>
      <a class="am-btn" href="{CHECKOUT}">Quero o AULÃO MASTER por R$ 97 {ARROW_BTN}</a>
      <p class="am-note">Aula gravada · acesso depois da confirmação do pagamento · 7 dias para desistir</p>
    </div>
    <div class="am-closed"><h3>As vendas foram encerradas</h3><p class="am-note" style="margin-top:8px">As matrículas da Aldeia abrem em janeiro de 2027.</p></div>
  </div>
</div></section>
</main>

<footer class="am-footer"><div class="am-wrap">
  <div class="am-footer__grid">
    <div><a class="am-brand" href="{SITE}/">Aldeia Literária<i>.</i></a><p><strong>Escola e comunidade de escrita criativa</strong> para escritores iniciantes. Página oficial do AULÃO MASTER, aula gravada de Camila Veloso.</p></div>
    <div><h3>Camila Veloso</h3><ul><li><a href="{INSTA}" rel="noopener">Instagram @acamiveloso</a></li><li><a href="{FUNDADORA}">Sobre a fundadora</a></li></ul></div>
    <div><h3>Aldeia Literária</h3><ul><li><a href="{SITE}/">Início</a></li><li><a href="{SOBRE}">Sobre</a></li><li><a href="{GUIA}">Guia</a></li><li><a href="{IMP}">Imprensa</a></li><li><a href="{CANC}">Cancelamento e reembolso</a></li><li><a href="{INSTA_ALDEIA}" rel="noopener">{ig} Instagram oficial</a></li><li><a href="{TIKTOK}" rel="noopener">TikTok oficial</a></li></ul></div>
  </div>
  <p class="am-footer__legal">Razão social: CAMILA VELOSO. CO LTDA · CNPJ: 47.277.682/0001-48<br>© 2026 Aldeia Literária. Todos os direitos reservados.</p>
</div></footer>

<div class="am-sticky am-open" id="am-sticky"><div><b>R$ 97</b><small>sai do ar em 30/11</small></div><a class="am-btn am-btn--sm" href="{CHECKOUT}">Quero o aulão</a></div>
{jsonld()}
'''


FONTS = [("Bricolage Grotesque", "bricolage-grotesque", 700, "normal"), ("Bricolage Grotesque", "bricolage-grotesque", 800, "normal"),
         ("Instrument Serif", "instrument-serif", 400, "normal"), ("Instrument Serif", "instrument-serif", 400, "italic"),
         ("Manrope", "manrope", 400, "normal"), ("Manrope", "manrope", 500, "normal"), ("Manrope", "manrope", 700, "normal"), ("Manrope", "manrope", 800, "normal")]


def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()


def font_css(inline):
    out = ""
    for fam, slug, w, st in FONTS:
        f = f"{slug}-latin-{w}-{st}.woff2"
        src = b64(os.path.join(FONTDIR, f), "font/woff2") if inline else f"aulao-inst/fonts/{f}"
        out += f'@font-face{{font-family:"{fam}";font-weight:{w};font-style:{st};font-display:swap;src:url({src}) format("woff2")}}\n'
    return out


def assemble(inline):
    def img(m):
        f = m.group(1)
        return b64(os.path.join(IMGDIR, f), "image/png" if f.endswith(".png") else "image/jpeg") if inline else f"aulao/img/{f}"
    body = re.sub(r"\{IMG:([^}]+)\}", img, page())
    css = open(os.path.join(HERE, "aulao.css"), encoding="utf-8").read()
    js = open(os.path.join(HERE, "aulao.js"), encoding="utf-8").read()
    return f"<style>\n{font_css(inline)}{css}</style>\n{body}\n<script>\n{js}</script>\n"


def main():
    head = f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{E(TITLE)} | Aldeia Literária</title>
<meta name="description" content="{E(DESC)}">
<link rel="canonical" href="{URL}">
<meta property="og:type" content="website"><meta property="og:title" content="{E(TITLE)}"><meta property="og:description" content="{E(DESC)}"><meta property="og:url" content="{URL}"><meta property="og:locale" content="pt_BR">
</head><body>
'''
    open(os.path.join(ROOT, "preview", "aulao-master-institucional.html"), "w", encoding="utf-8").write(head + assemble(False) + "</body></html>\n")
    scratch = os.environ.get("SCRATCH")
    if scratch:
        art = '<title>AULÃO MASTER</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n' + assemble(True)
        open(os.path.join(scratch, "aulao-master-inst-artifact.html"), "w", encoding="utf-8").write(art)
        print("artifact", len(art) // 1024, "KB")
    print("ok")


if __name__ == "__main__":
    main()
