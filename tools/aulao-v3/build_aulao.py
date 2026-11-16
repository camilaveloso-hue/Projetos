#!/usr/bin/env python3
"""AULÃO MASTER — versão curta para celular (Black Friday 2026).
Uso: python3 tools/aulao-v3/build_aulao.py   (SCRATCH=<pasta> também gera a prévia autocontida para o Artifact)
Saída: preview/aulao-master-v3.html (fotos em preview/aulao/img, fontes em preview/aulao-v3/fonts)
Regras de negócio: R$ 67 até 30/11 às 23h59 (horário de Brasília); depois, R$ 100. A aula é produto perpétuo: não sai do ar."""
import base64, html, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
IMGDIR = os.path.join(ROOT, "preview", "aulao", "img")
FONTDIR = os.path.join(ROOT, "preview", "aulao-v3", "fonts")
E = html.escape

SITE = "https://aaldeialiteraria.com.br"
URL = SITE + "/aulao-master/"
CHECKOUT = "#oferta"            # TROCAR pelo link do checkout quando a plataforma estiver definida
CANC = SITE + "/politica-de-cancelamento-e-reembolso/"
INSTA = "https://www.instagram.com/acamiveloso/"
PRICE, PRICE_FULL = "67", "100"
TITLE = "AULÃO MASTER: tudo o que você precisa saber para conseguir escrever um livro"
DESC = ("Aula gravada de Camila Veloso, fundadora da Aldeia Literária, para quem quer escrever um livro. "
        "Disponível por 1 ano. R$ 67 na Black Friday, até 30/11.")

CHECK = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="11" fill="currentColor"/><path d="M7 12.5l3.2 3.2L17 8.8" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
STAR = '<svg viewBox="0 0 44 44" fill="none" aria-hidden="true"><circle cx="22" cy="22" r="22" fill="#ffd60a"/><path d="M13 22.8l6 6L31 16" stroke="#09090a" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 12h15m0 0l-5-5m5 5l-5 5" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

FAQ = [
 ("Para quem é o AULÃO MASTER?",
  "Para quem está começando e quer escrever o primeiro livro, mas não sabe por onde começar. Você não precisa ter nada pronto."),
 ("Por quanto tempo posso assistir?",
  "O acesso dura 1 ano a partir da compra. Você assiste quando quiser e quantas vezes precisar, inclusive pelo celular."),
 ("Até quando vale o preço de R$ 67?",
  "O preço promocional de Black Friday vale até 30/11, às 23h59 (horário de Brasília). Depois disso, o AULÃO MASTER continua disponível, por R$ 100."),
 ("Posso pedir reembolso?",
  "Sim. Você tem 7 dias corridos depois da compra para desistir e pedir o reembolso. Veja a <a href=\"" + CANC + "\">política de cancelamento e reembolso</a>."),
 ("Quem dá a aula? A compra é segura?",
  "Camila Veloso, fundadora da Aldeia Literária e produtora editorial (UFSM). A venda é feita por CAMILA VELOSO. CO LTDA, CNPJ 47.277.682/0001-48, que você pode consultar na Receita Federal."),
]


def faq_html():
    return "".join(f'<details><summary>{E(q)}</summary><div class="am-ans"><p>{a}</p></div></details>' for q, a in FAQ)


def jsonld():
    plain = lambda s: re.sub(r"<[^>]+>", "", html.unescape(s))
    data = {"@context": "https://schema.org", "@graph": [
        {"@type": "Course", "@id": URL + "#aula", "name": TITLE, "url": URL, "inLanguage": "pt-BR", "description": DESC,
         "about": ["Escrita criativa", "Estrutura narrativa", "Como escrever um livro"],
         "teaches": "Estrutura de três atos, checklist de 9 passos, formas de história e premissa.",
         "educationalLevel": "Iniciante", "isAccessibleForFree": False,
         "provider": {"@type": "EducationalOrganization", "name": "Aldeia Literária", "url": SITE + "/",
                      "legalName": "CAMILA VELOSO. CO LTDA", "taxID": "47.277.682/0001-48"},
         "instructor": {"@type": "Person", "name": "Camila Veloso", "jobTitle": "Fundadora da Aldeia Literária", "sameAs": [INSTA]},
         "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "online"},
         "offers": {"@type": "Offer", "price": PRICE + ".00", "priceCurrency": "BRL", "availability": "https://schema.org/InStock",
                    "url": URL, "priceValidUntil": "2026-11-30"}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in FAQ]},
    ]}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "</script>"


def page():
    benefits = [
        ("is-hot", "Aula com a fundadora da Aldeia", "Camila Veloso ensina o passo a passo, direto ao ponto."),
        ("", "Disponível por 1 ano", "Assista quando quiser e quantas vezes precisar."),
        ("", "Checklist de 9 passos", "Para começar a escrever o seu livro assim que a aula terminar."),
        ("", "Para quem está começando", "Você não precisa ter nada pronto, só a vontade de escrever."),
        ("", "Acesso imediato, no celular", "Liberado assim que o pagamento for confirmado."),
        ("is-hot", "Preço promocional", "R$ 67 só até 30/11. Depois, R$ 100."),
    ]
    ben_html = "".join(f'<li class="{c}">{STAR}<b>{E(t)}</b><span>{E(d)}</span></li>' for c, t, d in benefits)
    parts = ["Os três atos e o arco", "O checklist de 9 passos", "Por que você lê livros", "As formas de história", "Premissa, princípio e arco", "Próximos passos"]
    parts_html = "".join(f"<li><span>{E(p)}</span></li>" for p in parts)
    ids = [1, 2, 3, 5, 6, 8, 10, 12, 14, 18, 21, 22]
    slides = "".join(f'<li class="am-slide"><img src="{{IMG:comunidade-{n:02d}.jpg}}" alt="Camila Veloso com alunos e leitores em encontro presencial" width="420" height="560" loading="lazy"></li>' for n in ids)
    return f'''
<div class="am-alert" role="status"><div class="am-wrap">
  <span class="am-alert__txt am-promo">A promoção acaba em:</span>
  <span class="am-count am-promo" data-count="sale" aria-hidden="true"><span>7<small>d</small></span><span>00<small>h</small></span><span>00<small>min</small></span><span>00<small>s</small></span></span>
  <span class="am-alert__txt am-regular">A promoção de Black Friday terminou. Valor atual: <b>R$ {PRICE_FULL}</b></span>
</div></div>

<main id="topo">
<section class="am-hero" aria-labelledby="h1"><div class="am-wrap">
  <span class="am-pill">Aula gravada<span class="am-promo">· Black Friday</span></span>
  <h1 id="h1">AULÃO MASTER<span class="am-sr">: tudo o que você precisa saber para conseguir escrever um livro</span></h1>
  <p class="am-tag"><span class="am-hl">escrever um livro pode ser fácil.</span></p>
  <p class="am-lead">Tudo o que você precisa saber para conseguir escrever um livro, em uma aula com a fundadora da Aldeia Literária.</p>
  <div class="am-author"><img src="{{IMG:camila-sorriso.jpg}}" alt="Camila Veloso" width="92" height="92"><div><strong>Camila Veloso</strong><span>Fundadora da Aldeia Literária</span></div></div>
  <div class="am-hero__cta"><a id="am-hero-cta" class="am-btn am-btn--ghost" href="#leva">Ver o que você leva {ARROW}</a></div>
</div></section>

<section class="am-sec am-what" id="leva" aria-labelledby="t-oque"><div class="am-wrap">
  <h2 class="am-h2" id="t-oque">O que é o AULÃO MASTER?</h2>
  <p class="am-lead"><strong>É uma aula gravada em que Camila Veloso, fundadora da Aldeia Literária, ensina, com metodologia única para iniciantes, tudo o que você precisa saber para conseguir escrever um livro.</strong></p>
  <ul class="am-benefits" aria-label="O que você leva">{ben_html}</ul>
</div></section>

<section class="am-sec am-dark" id="conteudo" aria-labelledby="t-partes"><div class="am-wrap">
  <h2 class="am-h2" id="t-partes">Na aula, <span style="color:var(--yellow)">6 partes.</span></h2>
  <ol class="am-parts">{parts_html}</ol>
</div></section>

<section class="am-sec" id="oferta" aria-labelledby="t-oferta"><div class="am-wrap am-center">
  <h2 class="am-h2" id="t-oferta">Garanta o seu AULÃO MASTER</h2>
  <div class="am-offer">
    <span class="am-pill am-promo">Preço de Black Friday</span>
    <div class="am-price">
      <s class="am-promo">de R$ {PRICE_FULL}</s>
      <strong><span class="am-promo">R$ {PRICE}</span><span class="am-regular">R$ {PRICE_FULL}</span></strong>
      <span class="am-promo">só até 30/11, às 23h59</span>
    </div>
    <ul class="am-list"><li>{CHECK}<span>Aula gravada</span></li><li>{CHECK}<span>Checklist com 9 passos</span></li><li>{CHECK}<span>Acesso imediato por 1 ano</span></li></ul>
    <a class="am-btn" href="{CHECKOUT}">Quero o AULÃO MASTER {ARROW}</a>
    <div class="am-bonus am-promo" data-bonus><b>Bônus do 1º dia:</b> comprando até 23/11, você ganha 50% de desconto na matrícula da Aldeia Literária 2027.
      <span class="am-count" data-count="bonus" aria-hidden="true"></span></div>
    <p class="am-note">7 dias para desistir e pedir o reembolso. <a href="{CANC}">Ver política</a>.</p>
  </div>
</div></section>

<section class="am-sec" style="padding-top:0" id="quem-sou-eu" aria-labelledby="t-eu"><div class="am-wrap">
  <div class="am-bio">
    <div class="am-bio__photo"><img src="{{IMG:camila-livros-cabeca.jpg}}" alt="Camila Veloso, de óculos, equilibrando uma pilha de livros na cabeça" width="898" height="1600" loading="lazy"></div>
    <div><h2 id="t-eu">Oi, eu sou a Camila.</h2>
    <p class="am-lead">Fundadora da Aldeia Literária e produtora editorial. Ajudo escritores iniciantes a desenvolver e publicar seus livros.</p>
    <ul class="am-chips"><li>+400 escritores na Aldeia</li><li>Produção Editorial · UFSM</li><li>6+ anos em conteúdo</li></ul></div>
  </div>
</div></section>

<section class="am-sec am-dark am-center" id="pessoas" aria-labelledby="t-pessoas" style="padding-bottom:clamp(36px,7vw,60px)"><div class="am-wrap">
  <h2 class="am-h2" id="t-pessoas">Eu sou real. <span style="color:var(--yellow)">E eles também.</span></h2>
</div>
<div class="am-carousel" data-carousel>
  <ul class="am-track" aria-label="Fotos de Camila Veloso com alunos da Aldeia Literária" tabindex="0">{slides}</ul>
  <div class="am-carousel__nav"><button type="button" class="am-arrow" data-dir="-1" aria-label="Foto anterior">&#8592;</button><button type="button" class="am-arrow" data-dir="1" aria-label="Próxima foto">&#8594;</button></div>
</div></section>

<section class="am-sec" id="duvidas" aria-labelledby="t-faq"><div class="am-wrap">
  <h2 class="am-h2 am-center" id="t-faq">Dúvidas rápidas</h2>
  <div class="am-faq">{faq_html()}</div>
</div></section>

<section class="am-sec am-dark am-final" id="comprar" aria-labelledby="t-final"><div class="am-wrap">
  <h2 id="t-final">Escrever um livro <span style="color:var(--yellow)">pode ser fácil.</span></h2>
  <p class="am-lead am-promo">A promoção acaba em:</p>
  <span class="am-count am-count--big am-promo" data-count="sale" aria-hidden="true"></span>
  <p class="am-price-line"><span class="am-promo"><s>R$ {PRICE_FULL}</s> R$ {PRICE}</span><span class="am-regular">R$ {PRICE_FULL}</span></p>
  <a class="am-btn am-btn--yellow" href="{CHECKOUT}">Quero o AULÃO MASTER {ARROW}</a>
</div></section>
</main>

<footer class="am-footer"><div class="am-wrap">
  <b>Aldeia Literária</b>
  <p>CAMILA VELOSO. CO LTDA · CNPJ 47.277.682/0001-48</p>
  <p><a href="{CANC}">Cancelamento e reembolso</a> · <a href="{INSTA}" rel="noopener">@acamiveloso</a></p>
  <p>© 2026 Aldeia Literária. Todos os direitos reservados.</p>
</div></footer>

<div class="am-sticky" id="am-sticky"><div><b><s class="am-promo">R$ {PRICE_FULL}</s><span class="am-promo">R$ {PRICE}</span><span class="am-regular">R$ {PRICE_FULL}</span></b><small class="am-promo">promoção até 30/11</small></div><a class="am-btn am-btn--sm" href="{CHECKOUT}">Quero o aulão</a></div>
{jsonld()}
'''


FONTS = [("Playfair Display", "playfair-display", 700, "normal"), ("Playfair Display", "playfair-display", 900, "normal"), ("Playfair Display", "playfair-display", 900, "italic"),
         ("DM Sans", "dm-sans", 400, "normal"), ("DM Sans", "dm-sans", 500, "normal"), ("DM Sans", "dm-sans", 700, "normal")]


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
    open(os.path.join(ROOT, "preview", "aulao-master-v3.html"), "w", encoding="utf-8").write(head + assemble(False) + "</body></html>\n")
    scratch = os.environ.get("SCRATCH")
    if scratch:
        art = '<title>AULÃO MASTER</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n' + assemble(True)
        open(os.path.join(scratch, "aulao-master-v3-artifact.html"), "w", encoding="utf-8").write(art)
        print("artifact", len(art) // 1024, "KB")
    print("ok")


if __name__ == "__main__":
    main()
