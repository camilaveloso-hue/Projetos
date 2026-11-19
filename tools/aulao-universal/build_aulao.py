#!/usr/bin/env python3
"""AULÃO UNIVERSAL — versão curta para celular (Black Friday 2026).
Uso: python3 tools/aulao-universal/build_aulao.py   (SCRATCH=<pasta> também gera a prévia autocontida para o Artifact)
Saída: preview/aulao-universal.html (fotos em preview/aulao/img, fontes em preview/aulao-v3/fonts)
Regras de negócio: R$ 70 até 30/11 às 23h59 (horário de Brasília); depois, R$ 100. A aula é produto perpétuo: não sai do ar."""
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
PRICE, PRICE_FULL = "70", "100"
TITLE = "AULÃO UNIVERSAL: tudo o que você precisa saber para conseguir escrever um livro"
DESC = ("Aula gravada de Camila Veloso, fundadora da Aldeia Literária, para quem quer escrever um livro. "
        "Disponível por 1 ano. R$ 70 na Black Friday, até 30/11.")

CHECK = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="11" fill="currentColor"/><path d="M7 12.5l3.2 3.2L17 8.8" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
STAR = '<svg viewBox="0 0 44 44" fill="none" aria-hidden="true"><circle cx="22" cy="22" r="22" style="fill:var(--ic-bg)"/><path d="M13 22.8l6 6L31 16" style="stroke:var(--ic-fg)" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 12h15m0 0l-5-5m5 5l-5 5" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

FAQ = [
 ("Para quem é o AULÃO UNIVERSAL?",
  "Para quem está começando e quer escrever o primeiro livro, mas não sabe por onde começar. Você não precisa ter nada pronto."),
 ("Por quanto tempo posso assistir?",
  "O acesso dura 1 ano a partir da compra. Você assiste quando quiser e quantas vezes precisar, inclusive pelo celular."),
 ("Até quando vale o preço de R$ 70?",
  "O preço promocional de Black Friday vale até 30/11, às 23h59 (horário de Brasília). Depois disso, o AULÃO UNIVERSAL continua disponível, por R$ 100."),
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
        ("", "Aula gravada", "Liberada assim que o pagamento for confirmado"),
        ("is-hot", "Com metodologia única", "Para quem quer começar a escrever, mas não sabe como"),
        ("is-hot", "Fundadora da Aldeia Literária", "Camila Veloso, Produtora Editorial (UFSM)"),
        ("", "Disponível por um ano", "Assista quando quiser e quantas vezes precisar"),
        ("is-hot", "Para quem está começando", "Escritores iniciantes que desejam começar a escrever"),
    ]
    ben_html = "".join(f'<li class="{c}">{STAR}<b><span class="am-m">{E(t)}</span></b><span>{E(d)}</span></li>' for c, t, d in benefits)
    # último cartão muda sozinho depois de 30/11 (a promoção acaba, a aula continua à venda)
    ben_html += (f'<li class="is-hot">{STAR}<b><span class="am-m am-promo">Promoção</span><span class="am-m am-regular">Valor</span></b>'
                 f'<span><span class="am-promo">R$ {PRICE} só até 30/11.</span><span class="am-regular">R$ {PRICE_FULL}.</span></span></li>')
    parts = [("Os três atos e o arco", "Entenda como uma história se sustenta e como fazer o seu personagem mudar do começo ao fim."),
             ("O checklist de 9 passos", "Um passo a passo para saber onde você está na história e o que escrever em seguida."),
             ("Por que você lê livros", "Antes de escrever para o leitor, entenda por que as histórias funcionam para ele."),
             ("As formas de história", "Descubra qual forma combina com a sua ideia, com exemplos que você conhece."),
             ("Premissa, princípio e arco", "Transforme uma ideia solta em uma frase clara que guia o livro inteiro."),
             ("Próximos passos", "Termine a aula sabendo por onde seguir para escrever e publicar o seu livro.")]
    parts_html = "".join(f"<li><span>{E(t)}<small>{E(d)}</small></span></li>" for t, d in parts)
    ids = [1, 2, 3, 5, 6, 8, 10, 12, 14, 18, 21, 22]
    slides = "".join(f'<li class="am-slide"><img src="{{IMG:comunidade-{n:02d}.jpg}}" alt="Camila Veloso com alunos e leitores em encontro presencial" width="420" height="560" loading="lazy"></li>' for n in ids)
    return f'''
<div class="am-alert" role="status"><div class="am-wrap">
  <div class="am-alert__info">
    <span class="am-alert__txt am-promo">A promoção acaba em:</span>
    <span class="am-count am-promo" data-count="sale" aria-hidden="true"><span>7<small>d</small></span><span>00<small>h</small></span><span>00<small>min</small></span><span>00<small>s</small></span></span>
    <span class="am-alert__txt am-regular">A promoção terminou. Valor atual: <b>R$ {PRICE_FULL}</b></span>
  </div>
  <a class="am-btn am-btn--yellow am-btn--bar" href="{CHECKOUT}">QUERO O AULÃO</a>
</div></div>

<main id="topo">
<section class="am-hero am-mtn am-mtn--light" aria-labelledby="h1"><div class="am-wrap">
  <span class="am-pill"><span>Aula gravada<span class="am-promo"> · Black Friday</span></span></span>
  <h1 id="h1">AULÃO UNIVERSAL<span class="am-sr">: tudo o que você precisa saber para conseguir escrever um livro</span></h1>
  <p class="am-tag"><span class="am-hl">escrever um livro pode ser fácil.</span></p>
  <p class="am-lead">Tudo o que você precisa saber para conseguir escrever um livro, em uma aula com a fundadora da Aldeia Literária.</p>
  <div class="am-author"><img src="{{IMG:camila-sorriso.jpg}}" alt="Camila Veloso" width="92" height="92"><div><strong>Camila Veloso</strong><span>Fundadora da Aldeia Literária</span></div></div>
  <div class="am-hero__cta"><a id="am-hero-cta" class="am-btn" href="{CHECKOUT}">Quero o AULÃO UNIVERSAL {ARROW}</a></div>
</div></section>

<section class="am-sec am-what" id="leva" aria-labelledby="t-oque"><div class="am-wrap am-center">
  <h2 class="am-h2" id="t-oque">O que é o AULÃO UNIVERSAL?</h2>
  <p class="am-lead"><strong>Aula gravada com metodologia única para iniciantes, explicando tudo o que você precisa saber para conseguir escrever um livro.</strong></p>
  <ul class="am-benefits" aria-label="O que você leva">{ben_html}</ul>
</div></section>

<section class="am-sec am-dark am-mtn am-mtn--dark" id="conteudo" aria-labelledby="t-partes"><div class="am-wrap">
  <h2 class="am-h2" id="t-partes">Na aula, <span style="color:var(--yellow)">6 partes.</span></h2>
  <ol class="am-parts">{parts_html}</ol>
</div></section>

<section class="am-sec" id="oferta" aria-labelledby="t-oferta"><div class="am-wrap am-center">
  <h2 class="am-h2" id="t-oferta">Garanta o seu AULÃO UNIVERSAL</h2>
  <div class="am-offer">
    <ul class="am-list">
      <li>{CHECK}<span>Aula gravada, liberada assim que o pagamento for confirmado</span></li>
      <li>{CHECK}<span>Metodologia única para quem está começando</span></li>
      <li>{CHECK}<span>Aula com a fundadora da Aldeia Literária</span></li>
      <li>{CHECK}<span>Checklist de 9 passos + material de apoio e atividade</span></li>
      <li>{CHECK}<span>Disponível por 1 ano, para assistir quantas vezes quiser</span></li>
      <li>{CHECK}<span>Acesso pelo celular ou computador, no seu ritmo</span></li>
    </ul>
    <details class="am-reveal">
      <summary class="am-btn am-btn--ghost am-btn--sm">Ver o preço <span aria-hidden="true">↓</span></summary>
      <div class="am-reveal__body">
        <span class="am-pill am-promo">Preço de Black Friday</span>
        <div class="am-price">
          <s class="am-promo">de R$ {PRICE_FULL}</s>
          <strong><span class="am-promo">R$ {PRICE}</span><span class="am-regular">R$ {PRICE_FULL}</span></strong>
          <span class="am-promo">só até 30/11, às 23h59</span>
        </div>
        <a class="am-btn" href="{CHECKOUT}">Quero o AULÃO UNIVERSAL {ARROW}</a>
        <div class="am-bonus am-promo" data-bonus><b>Bônus do 1º dia:</b> comprando até 23/11, você ganha 50% de desconto na matrícula da Aldeia Literária 2027.
          <span class="am-count" data-count="bonus" aria-hidden="true"></span></div>
        <p class="am-note">7 dias para desistir e pedir o reembolso. <a href="{CANC}">Ver política</a>.</p>
      </div>
    </details>
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

<section class="am-sec am-dark am-center am-mtn am-mtn--dark" id="pessoas" aria-labelledby="t-pessoas" style="padding-bottom:clamp(36px,7vw,60px)"><div class="am-wrap">
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

<section class="am-sec am-dark am-final am-mtn am-mtn--dark" id="comprar" aria-labelledby="t-final"><div class="am-wrap">
  <h2 id="t-final">Escrever um livro <span style="color:var(--yellow)">pode ser fácil.</span></h2>
  <p class="am-lead am-promo">A promoção acaba em:</p>
  <span class="am-count am-count--big am-promo" data-count="sale" aria-hidden="true"></span>
  <p class="am-price-line"><span class="am-promo"><s>R$ {PRICE_FULL}</s> R$ {PRICE}</span><span class="am-regular">R$ {PRICE_FULL}</span></p>
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


MTN_LIGHT = mountains(["#efe6fc", "#e5d8fa", "#dccbf6"], "#9b7be0")
MTN_DARK = mountains(["rgba(255,255,255,.04)", "rgba(255,255,255,.06)", "rgba(255,255,255,.09)"], "#c9b2f2")



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
<title>{E(TITLE)} | Aldeia Literária</title>
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
