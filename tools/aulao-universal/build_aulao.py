#!/usr/bin/env python3
"""AULÃO UNIVERSAL — versão curta para celular (Black Friday 2026).
Uso: python3 tools/aulao-universal/build_aulao.py   (SCRATCH=<pasta> também gera a prévia autocontida para o Artifact)
Saída: preview/aulao-universal.html (fotos em preview/aulao/img, fontes em preview/aulao-v3/fonts)
Regras: R$ 70 até 30/11 às 23h59 (Brasília). A versão de Black Friday NÃO traz o preço de R$ 100 no código; a versão para depois de 30/11 (POS=True) sai de build_wp.py --pos-promocao. A aula é produto perpétuo."""
import base64, html, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
IMGDIR = os.path.join(ROOT, "preview", "aulao", "img")
FONTDIR = os.path.join(ROOT, "preview", "aulao-v3", "fonts")
E = html.escape

SITE = "https://aaldeialiteraria.com.br"
URL = SITE + "/aulao-universal/"
CHECKOUT = "https://pay.kiwify.com.br/TyiiZBm"      # link de compra (Kiwify)
CANC = SITE + "/politica-de-cancelamento-e-reembolso/"
INSTA = "https://www.instagram.com/acamiveloso/"
CAMILA_URL = SITE + "/sobre-a-fundadora/"
ALDEIA_URL = SITE + "/"
WAIT = "https://tally.so/r/0QNWPy"                   # lista de espera da matrícula
BLOG = [(SITE + "/como-criar-uma-rotina-de-escrita-e-se-organizar-para-escrever/", "Como criar uma rotina de escrita e se organizar para escrever"),
        (SITE + "/curso-de-escrita-criativa-vale-a-pena-como-escolher-o-melhor-para-iniciantes/", "Curso de escrita criativa: vale a pena? Como escolher o melhor para iniciantes"),
        (SITE + "/como-escolher-curso-de-escrita-criativa/", "Guia: como escolher um curso de escrita criativa")]

# POS = True gera a versão para depois de 30/11 (R$ 100, sem promoção). A versão de Black Friday NÃO traz o preço de R$ 100 no código.
POS = False
PRICE_PROMO, PRICE_FULL = "70", "100"
PUBLISHED, PUBLISHED_ISO = "19/11/2026", "2026-11-19"   # data de publicação registrada pelo WordPress (Yoast)
UPDATED, UPDATED_ISO = "23/11/2026", "2026-11-23"

TITLE = "AULÃO UNIVERSAL: aula de escrita criativa para iniciantes | Aldeia Literária"
DESC = ("Aula gravada de escrita criativa para iniciantes: aprenda como escrever um livro com três atos, "
        "premissa e checklist de 9 passos. Com Camila Veloso.")

CHECK = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="11" fill="currentColor"/><path d="M7 12.5l3.2 3.2L17 8.8" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
STAR = '<svg viewBox="0 0 44 44" fill="none" aria-hidden="true"><circle cx="22" cy="22" r="22" style="fill:var(--ic-bg)"/><path d="M13 22.8l6 6L31 16" style="stroke:var(--ic-fg)" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 12h15m0 0l-5-5m5 5l-5 5" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def price_now():
    return PRICE_FULL if POS else PRICE_PROMO


def faq_items():
    """Perguntas frequentes. A de preço muda conforme a versão (Black Friday ou depois de 30/11)."""
    if POS:
        preco = ("Quanto custa o AULÃO UNIVERSAL?",
                 f"O AULÃO UNIVERSAL custa R$ {PRICE_FULL}, com acesso por 1 ano.", False)
    else:
        preco = ("Quanto custa o AULÃO UNIVERSAL e até quando vale o preço de Black Friday?",
                 f"Na Black Friday, o AULÃO UNIVERSAL custa R$ {PRICE_PROMO}, com acesso por 1 ano. O preço promocional vale até 30/11, às 23h59 (horário de Brasília). Depois dessa data, o valor da aula muda.", True)
    return [
        ("Para quem é o AULÃO UNIVERSAL?",
         "Para quem está começando e quer escrever o primeiro livro, mas não sabe por onde começar. Você não precisa ter nada pronto.", False),
        ("O AULÃO UNIVERSAL serve para quem nunca escreveu?",
         "Sim. A aula foi feita para iniciantes e parte do começo: você não precisa ter escrito nada antes.", False),
        ("Preciso ter um texto pronto?",
         "Não. Basta ter vontade de escrever. Se você já tem uma ideia de história, melhor, mas não precisa de capítulos nem de rascunho.", False),
        ("Qual é a duração e o formato da aula?",
         "É uma aula gravada de 55 minutos, que você assiste pelo celular ou pelo computador. Junto vêm o checklist de 9 passos, o material de apoio e uma atividade.", False),
        preco,
        ("Por quanto tempo posso assistir?",
         "O acesso dura 1 ano a partir da compra. Você assiste quando quiser e quantas vezes precisar.", False),
        ("O AULÃO UNIVERSAL ensina a publicar um livro?",
         "A aula é sobre como estruturar e começar o seu livro. O último bloco mostra os próximos passos, incluindo a publicação, mas o ensino detalhado de publicação independente está no curso completo da Aldeia Literária.", False),
        ("Qual é a diferença entre o AULÃO UNIVERSAL e o curso completo da Aldeia?",
         "O AULÃO UNIVERSAL é uma aula única e gravada sobre o básico da narrativa. O curso completo da Aldeia Literária tem cinco módulos, aulas ao vivo às quartas-feiras, atividades e feedback individual. As matrículas abrem em janeiro de 2027.", False),
        ("Posso pedir reembolso?",
         "Sim. Você tem 7 dias corridos depois da compra para desistir e pedir o reembolso. Veja a <a href=\"" + CANC + "\">política de cancelamento e reembolso</a>.", False),
        ("Quem dá a aula? A compra é segura?",
         "Camila Veloso, fundadora da Aldeia Literária e produtora editorial (UFSM). A venda é feita por CAMILA VELOSO. CO LTDA, CNPJ 47.277.682/0001-48, que você pode consultar na Receita Federal.", False),
    ]


def faq_html():
    return "".join(f'<details{" data-promo" if promo else ""}><summary>{E(q)}</summary><div class="am-ans"><p>{a}</p></div></details>' for q, a, promo in faq_items())


def jsonld():
    """Course, Person e FAQPage. A organização (Aldeia Literária), o site e a página já vêm do Yoast: aqui só se referencia o @id dele."""
    plain = lambda t: re.sub(r"<[^>]+>", "", html.unescape(t))
    org = {"@id": SITE + "/#organization"}
    person = {"@type": "Person", "@id": URL + "#camila-veloso", "name": "Camila Veloso", "url": CAMILA_URL,
              "jobTitle": "Fundadora e diretora da Aldeia Literária", "sameAs": [INSTA], "worksFor": org,
              "alumniOf": {"@type": "CollegeOrUniversity", "name": "Universidade Federal de Santa Maria"}}
    offer = {"@type": "Offer", "category": "Paid", "price": price_now() + ".00", "priceCurrency": "BRL",
             "availability": "https://schema.org/InStock", "url": URL, "seller": org}
    if not POS:
        offer["priceValidUntil"] = "2026-11-30"
    course = {"@type": "Course", "@id": URL + "#aula", "name": "AULÃO UNIVERSAL", "alternateName": "AULÃO UNIVERSAL: tudo o que você precisa saber para conseguir escrever um livro",
              "url": URL, "inLanguage": "pt-BR",
              "description": "Aula gravada de escrita criativa para iniciantes, de 55 minutos, que ensina estrutura de três atos, premissa e um checklist de 9 passos para escrever um livro. Acesso por 1 ano, com checklist, material de apoio e atividade.",
              "about": ["Escrita criativa", "Estrutura narrativa", "Como escrever um livro"],
              "teaches": "Estrutura de três atos e arco do personagem, checklist de 9 passos, formas de história, premissa e princípio narrativo, próximos passos para publicar.",
              "educationalLevel": "Iniciante", "isAccessibleForFree": False, "timeRequired": "PT55M",
              "provider": org, "instructor": {"@id": person["@id"]},
              "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "online", "courseWorkload": "PT55M", "instructor": {"@id": person["@id"]}},
              "offers": offer}
    faq = {"@type": "FAQPage", "@id": URL + "#faq", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a, _ in faq_items()]}
    data = {"@context": "https://schema.org", "@graph": [course, person, faq]}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "</script>"


ALTS = {
    1: "Selfie de Camila Veloso com três participantes diante de um estande de livros, em evento literário",
    2: "Camila Veloso e uma participante de óculos posam sorrindo, cada uma com uma ecobag bege com o selo da Aldeia Literária",
    3: "Selfie de Camila Veloso com duas participantes, uma delas de cabelo com mechas azuis, em um corredor movimentado de evento literário",
    5: "Camila Veloso abraça uma participante de camiseta preta e crachá, com uma ecobag bege no ombro",
    6: "Camila Veloso ao lado de uma participante de óculos e blusa estampada que segura uma ecobag da Aldeia Literária",
    8: "Selfie de Camila Veloso com quatro jovens participantes sorrindo em um estande colorido",
    10: "Camila Veloso com uma participante de vestido roxo que segura uma sacola de brinde, em um pavilhão de evento",
    12: "Camila Veloso posa ao lado de um participante de óculos e camiseta cinza, em frente a uma parede de madeira",
    14: "Selfie de Camila Veloso com uma participante ruiva de óculos, ambas de crachá, em evento literário",
    18: "Camila Veloso com um grupo de jovens participantes, alguns agachados, em um estande iluminado em azul",
    21: "Camila Veloso com quatro participantes em pé, duas delas com ecobags bege, em frente a uma estante de evento",
    22: "Selfie de Camila Veloso com um participante de cabelo cacheado fazendo sinal de positivo, em um pavilhão cheio de gente",
}


def page():
    promo = not POS
    benefits = [
        ("", "Aula gravada", "Liberada assim que o pagamento for confirmado"),
        ("is-hot", "Com metodologia única", "Para quem quer começar a escrever, mas não sabe como"),
        ("is-hot", "Fundadora da Aldeia Literária", "Camila Veloso, Produtora Editorial (UFSM)"),
        ("", "Disponível por um ano", "Assista quando quiser e quantas vezes precisar"),
        ("is-hot", "Para quem está começando", "Escritores iniciantes que desejam começar a escrever"),
    ]
    ben_html = "".join(f'<li class="{c}">{STAR}<b><span class="am-m">{E(t)}</span></b><span>{E(d)}</span></li>' for c, t, d in benefits)
    if promo:
        ben_html += f'<li class="is-hot" data-promo>{STAR}<b><span class="am-m">Promoção</span></b><span>R$ {PRICE_PROMO} só até 30/11.</span></li>'
    else:
        ben_html += f'<li class="is-hot">{STAR}<b><span class="am-m">Valor</span></b><span>R$ {PRICE_FULL}, com acesso por 1 ano.</span></li>'

    parts = [("Os três atos e o arco", "Os três atos dividem uma história em apresentação, confronto e resolução. O arco é a mudança do personagem ao longo deles. Você aprende a enxergar essa estrutura e a aplicá-la ao seu livro."),
             ("O checklist de 9 passos", "Um roteiro de nove etapas que leva a história do início ao fim. Ele acompanha o material de apoio e a atividade e ajuda a saber em que ponto você está e o que escrever em seguida."),
             ("A função da narrativa", "A leitura é a base da escrita. Entender por que as histórias funcionam para quem lê ajuda você a escrever pensando no leitor."),
             ("Estruturas narrativas", "Outras formas de estruturar uma narrativa. Você descobre qual delas combina com a sua ideia."),
             ("Premissa, princípio e arco", "A premissa é a sua história resumida em uma frase. O princípio é a ideia central que a sustenta. Você aprende a transformar uma ideia solta nisso."),
             ("Próximos passos", "Como seguir depois da aula para terminar o livro e chegar à publicação, e onde a Aldeia Literária entra nesse caminho.")]
    parts_html = "".join(f"<li><div><h3>{E(t)}</h3><p>{E(d)}</p></div></li>" for t, d in parts)

    ids = [1, 2, 3, 5, 6, 8, 10, 12, 14, 18, 21, 22]
    slides = "".join(f'<li class="am-slide"><img src="{{IMG:comunidade-{n:02d}.jpg}}" alt="{E(ALTS[n])}" width="420" height="560" loading="lazy"></li>' for n in ids)

    if promo:
        alert = ('<div class="am-alert__info"><span class="am-alert__txt" data-promo>A promoção acaba em:</span>'
                 '<span class="am-count" data-count="sale" data-promo><noscript>30/11, às 23h59</noscript></span></div>')
        pill = '<span class="am-pill">Aula gravada de escrita criativa</span>'
        price_block = (f'<span class="am-pill" data-promo>Preço de Black Friday</span>'
                       f'<div class="am-price" data-promo><strong>R$ {PRICE_PROMO}</strong><span>só até 30/11, às 23h59</span></div>')
        bonus = '<div class="am-bonus" data-promo><b>Bônus:</b> quem comprar até 30/11, às 23h59, ganha <b>R$ 70 de desconto na matrícula da Aldeia Literária</b>.</div>'
        final_info = (f'<p class="am-lead" data-promo>A promoção acaba em:</p><span class="am-count am-count--big" data-count="sale" data-promo><noscript>30/11, às 23h59</noscript></span>'
                      f'<p class="am-price-line" data-promo>R$ {PRICE_PROMO}</p>')
    else:
        alert = '<div class="am-alert__info"><span class="am-alert__txt">Aula gravada de escrita criativa · acesso por 1 ano</span></div>'
        pill = '<span class="am-pill">Aula gravada de escrita criativa</span>'
        price_block = f'<div class="am-price"><strong>R$ {PRICE_FULL}</strong><span>acesso por 1 ano</span></div>'
        bonus = ""
        final_info = f'<p class="am-price-line">R$ {PRICE_FULL}</p>'

    blog_links = "".join(f'<li><a href="{u}">{E(t)}</a></li>' for u, t in BLOG)
    dates = f'Publicado em <time datetime="{PUBLISHED_ISO}">{PUBLISHED}</time> · Atualizado em <time datetime="{UPDATED_ISO}">{UPDATED}</time>'
    return f'''
<div class="am-alert" role="status"><div class="am-wrap">
  {alert}
  <a class="am-btn am-btn--yellow am-btn--bar" href="{CHECKOUT}">QUERO O AULÃO</a>
</div></div>

<main id="topo">
<section class="am-hero am-mtn am-mtn--light" aria-labelledby="h1"><div class="am-wrap">
  {pill}
  <h1 id="h1">AULÃO UNIVERSAL<span class="am-sr">: </span><span class="am-tag"><span class="am-hl">escrever um livro pode ser fácil.</span></span></h1>
  <p class="am-lead am-def">Um guia para quem deseja escrever, mas não sabe por onde começar. Aula de 55 minutos com metodologia única para escritores iniciantes. Tudo o que você precisa saber para escrever bons livros.</p>
  <ul class="am-facts" aria-label="Resumo da aula"><li>Aula gravada</li><li>55 minutos</li><li>Acesso por 1 ano</li><li>Checklist + atividade</li></ul>
  <div class="am-author"><img src="{{IMG:camila-sorriso.jpg}}" alt="Camila Veloso, professora do AULÃO UNIVERSAL" width="92" height="92"><div><strong>Camila Veloso</strong><span>Fundadora da Aldeia Literária</span></div></div>
  <p class="am-dates">{dates}</p>
  <div class="am-hero__cta"><a id="am-hero-cta" class="am-btn" href="{CHECKOUT}">Quero o AULÃO UNIVERSAL {ARROW}</a></div>
</div></section>

<section class="am-sec am-what" id="leva" aria-labelledby="t-oque"><div class="am-wrap am-center">
  <h2 class="am-h2" id="t-oque">O que é o AULÃO UNIVERSAL?</h2>
  <p class="am-lead"><strong>Aula gravada com metodologia única para iniciantes, explicando tudo o que você precisa saber para conseguir escrever um livro.</strong></p>
  <ul class="am-benefits" aria-label="O que você leva">{ben_html}</ul>
</div></section>

<section class="am-sec am-dark am-mtn am-mtn--dark" id="conteudo" aria-labelledby="t-partes"><div class="am-wrap">
  <h2 class="am-h2" id="t-partes">O que você aprende nas <span style="color:var(--yellow)">6 partes da aula</span></h2>
  <ol class="am-parts">{parts_html}</ol>
</div></section>

<section class="am-sec" id="para-quem" aria-labelledby="t-quem"><div class="am-wrap">
  <h2 class="am-h2" id="t-quem">Para quem é o AULÃO UNIVERSAL</h2>
  <ul class="am-checks">
    <li>{CHECK}<span>Quem quer escrever o primeiro livro e não sabe por onde começar.</span></li>
    <li>{CHECK}<span>Quem tem uma ideia de história, mas ainda não sabe como estruturá-la.</span></li>
    <li>{CHECK}<span>Quem nunca escreveu: você não precisa ter nada pronto.</span></li>
  </ul>
  <h2 class="am-h2" id="t-naoe" style="margin-top:44px">Para quem não é</h2>
  <ul class="am-checks am-checks--no">
    <li>{CHECK}<span>Quem já domina estrutura narrativa e busca técnicas avançadas de escrita.</span></li>
    <li>{CHECK}<span>Quem quer acompanhamento contínuo e retorno individual sobre os próprios textos.</span></li>
  </ul>
  <p class="am-lead" style="margin-top:20px">Nesses casos, faz mais sentido o <a href="{ALDEIA_URL}"><strong>curso completo da Aldeia Literária</strong></a>: curso online de escrita criativa para iniciantes, com cinco módulos, aulas ao vivo às quartas-feiras, atividades e feedback individual. As matrículas abrem em janeiro de 2027, com vagas limitadas. <a href="{WAIT}">Entre na lista de espera</a>.</p>
</div></section>

<section class="am-sec am-warm" id="oferta" aria-labelledby="t-oferta"><div class="am-wrap am-center">
  <h2 class="am-h2" id="t-oferta">O que você leva agora</h2>
  <div class="am-offer">
    <ul class="am-list">
      <li>{CHECK}<span>Aula gravada de 55 minutos</span></li>
      <li>{CHECK}<span>Metodologia única para iniciantes</span></li>
      <li>{CHECK}<span>Conhecimento exclusivo em escrita criativa</span></li>
      <li>{CHECK}<span>Material de apoio</span></li>
      <li>{CHECK}<span>Acesso por 1 ano</span></li>
    </ul>
    <details class="am-reveal">
      <summary class="am-btn am-btn--ghost am-btn--sm">Ver o preço <span aria-hidden="true">↓</span></summary>
      <div class="am-reveal__body">
        {price_block}
        <a class="am-btn" href="{CHECKOUT}">Quero o AULÃO UNIVERSAL {ARROW}</a>
        {bonus}
        <p class="am-note">7 dias para desistir e pedir o reembolso. <a href="{CANC}">Ver política</a>.</p>
      </div>
    </details>
  </div>
</div></section>

<section class="am-sec" id="quem-sou-eu" aria-labelledby="t-eu"><div class="am-wrap">
  <div class="am-bio">
    <div class="am-bio__photo"><img src="{{IMG:camila-livros-cabeca.jpg}}" alt="Camila Veloso, de óculos, equilibrando uma pilha de livros na cabeça diante de uma estante" width="898" height="1600" loading="lazy"></div>
    <div><h2 id="t-eu">Quem é a professora: Camila Veloso</h2>
    <p class="am-lead">Camila Veloso é fundadora e diretora da <a href="{ALDEIA_URL}">Aldeia Literária</a>, escola e comunidade de escrita criativa. É formada em Comunicação Social, Produção Editorial pela UFSM, tem mais de seis anos de experiência em marketing e conteúdo e ajuda escritores iniciantes a desenvolver e publicar seus livros.</p>
    <ul class="am-chips"><li>Produção Editorial · UFSM</li><li>6+ anos em marketing e conteúdo</li></ul>
    <p class="am-note" style="margin-top:14px"><a href="{CAMILA_URL}">Conheça a Camila Veloso</a> · <a href="{INSTA}" rel="noopener">@acamiveloso</a></p></div>
  </div>
</div></section>

<section class="am-sec am-dark am-center am-mtn am-mtn--dark" id="pessoas" aria-labelledby="t-pessoas" style="padding-bottom:clamp(36px,7vw,60px)"><div class="am-wrap">
  <h2 class="am-h2" id="t-pessoas">Eu sou real. <span style="color:var(--yellow)">E eles também.</span></h2>
</div>
<div class="am-carousel" data-carousel>
  <ul class="am-track" aria-label="Fotos de Camila Veloso com alunos e leitores da Aldeia Literária" tabindex="0">{slides}</ul>
  <div class="am-carousel__nav"><button type="button" class="am-arrow" data-dir="-1" aria-label="Foto anterior">&#8592;</button><button type="button" class="am-arrow" data-dir="1" aria-label="Próxima foto">&#8594;</button></div>
</div></section>

<section class="am-sec" id="duvidas" aria-labelledby="t-faq"><div class="am-wrap">
  <h2 class="am-h2 am-center" id="t-faq">Perguntas frequentes</h2>
  <div class="am-faq">{faq_html()}</div>
</div></section>

<section class="am-sec am-warm" id="leia-tambem" aria-labelledby="t-links"><div class="am-wrap">
  <h2 class="am-h2 am-center" id="t-links" style="font-size:clamp(1.6rem,6vw,2.1rem)">Continue aprendendo a escrever</h2>
  <ul class="am-links">
    {blog_links}
    <li><a href="{CAMILA_URL}">Camila Veloso, fundadora da Aldeia Literária</a></li>
    <li><a href="{ALDEIA_URL}">Aldeia Literária: curso de escrita criativa para iniciantes</a></li>
    <li><a href="{WAIT}">Lista de espera da matrícula 2027</a></li>
  </ul>
</div></section>

<section class="am-sec am-dark am-final am-mtn am-mtn--dark" id="comprar" aria-label="Comprar o AULÃO UNIVERSAL"><div class="am-wrap">
  <p class="am-h2">Escrever um livro <span style="color:var(--yellow)">pode ser fácil.</span></p>
  {final_info}
  <a class="am-btn am-btn--yellow" href="{CHECKOUT}">Quero o AULÃO UNIVERSAL {ARROW}</a>
</div></section>
</main>

<footer class="am-footer"><div class="am-wrap">
  <b>Aldeia Literária</b>
  <p>CAMILA VELOSO. CO LTDA · CNPJ 47.277.682/0001-48</p>
  <p><a href="{CANC}">Cancelamento e reembolso</a> · <a href="{INSTA}" rel="noopener">@acamiveloso</a></p>
  <p>© 2026 Aldeia Literária. Todos os direitos reservados.</p>
</div></footer>

{jsonld()}
'''


FONTS = [("Playfair Display", "playfair-display", 700, "normal"), ("Playfair Display", "playfair-display", 900, "normal"), ("Playfair Display", "playfair-display", 900, "italic"),
         ("DM Sans", "dm-sans", 400, "normal"), ("DM Sans", "dm-sans", 500, "normal"), ("DM Sans", "dm-sans", 700, "normal")]


# ---------------------------------------------------------------- relevo de montanhas (SVG em linha, usado como fundo)
def _ridge(seed, base, amp, step):
    """Silhueta de cordilheira: poucos picos largos, encostas retas, vales marcados e um ombro em cada encosta."""
    import random
    r = random.Random(seed)
    pts, x = [(-20, base)], -20 + step * 0.3
    while x < 1240:
        h = amp * (0.45 + 0.55 * r.random())
        pts.append((x, base - h))                                   # pico
        pts.append((x + step * 0.28, base - h * (0.5 + 0.1 * r.random())))   # ombro
        x += step * 0.55
        pts.append((x, base - amp * 0.12 * r.random()))             # vale
        x += step * 0.45
    d = f"M{pts[0][0]:.0f} {pts[0][1]:.0f}" + "".join(f" L{px:.0f} {py:.0f}" for px, py in pts[1:])
    return d, pts


def mountains(fills, stroke, sw=1.4):
    """Três camadas de montanhas; as de trás são mais altas e mais claras."""
    out = ""
    for k, (seed, base, amp, step) in enumerate([(11, 190, 120, 330), (29, 214, 92, 260), (53, 240, 66, 210)]):
        d, _ = _ridge(seed, base, amp, step)
        out += f'<path d="{d} L1240 260 L-20 260 Z" fill="{fills[k]}"/>'
        out += f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round" opacity="{0.9 - k*0.2:.1f}"/>'
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 260" preserveAspectRatio="none">{out}</svg>'
    import urllib.parse
    return 'url("data:image/svg+xml,' + urllib.parse.quote(svg, safe="/:=,'()") + '")'


MTN_LIGHT = mountains(["#e9f2fa", "#dbeaf6", "#cde0f1"], "#6f9cc4")
MTN_DARK = mountains(["rgba(255,255,255,.04)", "rgba(255,255,255,.06)", "rgba(255,255,255,.09)"], "#9fc4e6")



def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()


def font_css(inline):
    out = ""
    for fam, slug, w, st in FONTS:
        f = f"{slug}-latin-{w}-{st}.woff2"
        src = b64(os.path.join(FONTDIR, f), "font/woff2") if inline else f"aulao-v3/fonts/{f}"
        out += f'@font-face{{font-family:"{fam}";font-weight:{w};font-style:{st};font-display:swap;src:url({src}) format("woff2")}}\n'
    return out


def assemble(inline):
    def img(m):
        f = m.group(1)
        return b64(os.path.join(IMGDIR, f), "image/png" if f.endswith(".png") else "image/jpeg") if inline else f"aulao/img/{f}"
    body = re.sub(r"\{IMG:([^}]+)\}", img, page())
    css = open(os.path.join(HERE, "aulao.css"), encoding="utf-8").read().replace("{MTN_LIGHT}", MTN_LIGHT).replace("{MTN_DARK}", MTN_DARK)
    js = open(os.path.join(HERE, "aulao.js"), encoding="utf-8").read()
    return f"<style>\n{font_css(inline)}{css}</style>\n{body}\n<script>\n{js}</script>\n"


def main():
    head = f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{E(TITLE)}</title>
<meta name="description" content="{E(DESC)}">
<link rel="canonical" href="{URL}">
<meta property="og:type" content="website"><meta property="og:title" content="{E(TITLE)}"><meta property="og:description" content="{E(DESC)}"><meta property="og:url" content="{URL}"><meta property="og:locale" content="pt_BR">
</head><body>
'''
    open(os.path.join(ROOT, "preview", "aulao-universal.html"), "w", encoding="utf-8").write(head + assemble(False) + "</body></html>\n")
    scratch = os.environ.get("SCRATCH")
    if scratch:
        art = '<title>AULÃO UNIVERSAL</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n' + assemble(True)
        open(os.path.join(scratch, "aulao-universal-artifact.html"), "w", encoding="utf-8").write(art)
        print("artifact", len(art) // 1024, "KB")
    print("ok")


if __name__ == "__main__":
    main()
