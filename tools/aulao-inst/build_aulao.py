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
GUIA = SITE + "/como-escolher-curso-de-escrita-criativa/"
IMP = SITE + "/imprensa/"
SOBRE = SITE + "/novo-sobre/"
FUNDADORA = SITE + "/sobre-a-fundadora/"
TITLE = "AULÃO MASTER: tudo o que você precisa saber para conseguir escrever um livro"
DESC = ("Aula gravada de Camila Veloso para quem quer escrever um livro e não sabe por onde começar: "
        "estrutura da história, checklist de 9 passos, formas de história e premissa. R$ 97 na Black Friday, até 30/11.")

CHECK = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="11" fill="currentColor"/><path d="M7 12.5l3.2 3.2L17 8.8" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 12h15m0 0l-5-5m5 5l-5 5" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW_BTN = ARROW.replace("<svg", '<svg width="22" height="22"')

FAQ = [
 ("O que é o AULÃO MASTER?",
  "O AULÃO MASTER é uma aula gravada de Camila Veloso para quem quer escrever um livro. Ela reúne o básico da narrativa em seis partes: os três atos e o arco do personagem, o checklist de 9 passos até o final, a função de uma história, as formas de história, a premissa e os próximos passos."),
 ("Para quem é o AULÃO MASTER?",
  "Para quem está começando e quer escrever o primeiro livro, mas não sabe por onde começar. Você não precisa ter nada pronto, só vontade de contar uma história."),
 ("Quanto custa e até quando posso comprar?",
  "O AULÃO MASTER custa R$ 97 na Black Friday. A venda vai de 23/11 até 30/11, às 23h59 (horário de Brasília). Depois disso, a aula sai do ar e não será vendida novamente."),
 ("Como eu assisto à aula?",
  "A aula é gravada. Depois da confirmação do pagamento, você recebe o acesso e assiste no seu ritmo, quantas vezes quiser dentro do período de acesso informado na compra."),
 ("Qual é o bônus de quem compra no primeiro dia?",
  "Quem comprar na segunda-feira, 23/11, ganha 50% de desconto na matrícula da Aldeia Literária 2027. As matrículas abrem em janeiro de 2027, com vagas limitadas. A partir de 24/11 o bônus deixa de valer."),
 ("Posso pedir reembolso?",
  "Sim. Você tem 7 dias corridos após a compra para desistir e pedir o reembolso do valor pago. As regras completas estão na <a href=\"" + CANC + "\">política de cancelamento e reembolso</a>."),
 ("Quem dá a aula?",
  "Camila Veloso. Ela é formada em Comunicação Social, Produção Editorial (UFSM), tem mais de seis anos de experiência em marketing e conteúdo e ajuda escritores iniciantes a desenvolver e publicar seus livros."),
 ("A empresa é registrada? Como confirmo que a compra é segura?",
  "Sim. A venda é feita por CAMILA VELOSO. CO LTDA, CNPJ 47.277.682/0001-48, que você pode consultar na Receita Federal. O site oficial é aaldeialiteraria.com.br e o perfil oficial da professora é @acamiveloso, no Instagram."),
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


def topics():
    """Só título, subtítulo e a promessa de cada parte da aula. O conteúdo em si fica dentro da aula."""
    items = [("Os três atos e o arco", "O esqueleto e a mudança do personagem",
              "Entenda como uma história se sustenta de pé e como fazer o seu personagem mudar de verdade do começo ao fim."),
             ("O checklist da história", "9 passos até o final",
              "Um passo a passo para você saber em que ponto da história está e o que escrever em seguida, sem travar no meio."),
             ("Por que você lê livros", "A função de uma história",
              "Antes de escrever para o leitor, entenda por que as histórias funcionam para ele."),
             ("As formas de história", "Linear, sinuosa e explosiva",
              "Descubra qual forma combina com a sua ideia, com exemplos de livros e filmes que você conhece."),
             ("Premissa, princípio e arco", "Da ideia à página",
              "Transforme uma ideia solta em uma frase clara que guia o livro inteiro."),
             ("Próximos passos", "O que vem depois do básico",
              "Termine a aula sabendo por onde seguir para escrever e publicar o seu livro.")]
    return "".join(f'<li><span class="am-topics__n" aria-hidden="true">{i}</span><small>{E(sub)}</small><h3>{E(t)}</h3><p>{E(d)}</p></li>'
                   for i, (t, sub, d) in enumerate(items, 1))


def page():
    outcomes = ["Saber por onde começar o seu livro e o que fazer em cada etapa, do começo ao fim.",
                "Ter um mapa claro da sua história para chegar ao final sem travar no meio.",
                "Escolher a forma que combina com a sua ideia e saber como contá-la.",
                "Resumir o livro em uma frase e transformar a ideia solta em um projeto de livro.",
                "Sair da aula com o caminho definido para escrever e publicar o seu livro."]
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
  <div class="am-author" id="am-hero-cta"><img src="{{IMG:camila-sorriso.jpg}}" alt="Camila Veloso" width="100" height="100">
    <div><strong>Camila Veloso</strong><span>Professora do AULÃO MASTER · Produtora editorial (UFSM) · <a href="{INSTA}" rel="noopener">@acamiveloso</a></span></div></div>

</div></section>

<section class="am-sec am-sec--tight" id="o-que-e" aria-labelledby="t-oque"><div class="am-wrap">
  <p class="am-kicker">Resposta direta</p>
  <h2 class="am-h2" id="t-oque">O que é o AULÃO MASTER?</h2>
  <div class="am-prose" style="margin-top:24px">
    <p class="am-lead"><strong>O AULÃO MASTER é uma aula gravada sobre o básico da narrativa, para quem quer escrever um livro.</strong> Em seis partes, ela reúne o que você precisa saber para sair da ideia solta e chegar ao final da sua história.</p>
    <p>A aula é dada por Camila Veloso, produtora editorial (UFSM) que ajuda escritores iniciantes a desenvolver e publicar seus livros.</p>
  </div>
  <div class="am-tablewrap"><table class="am-table">
    <caption>O AULÃO MASTER em resumo</caption>
    <tbody>
      <tr><th scope="row">O que é</th><td>Uma aula gravada sobre o básico da narrativa, para quem quer escrever um livro.</td></tr>
      <tr><th scope="row">Para quem é</th><td>Quem está começando e não sabe por onde começar. Você não precisa ter nada pronto.</td></tr>
      <tr><th scope="row">Quem dá a aula</th><td>Camila Veloso, produtora editorial (UFSM).</td></tr>
      <tr><th scope="row">Como funciona</th><td>Aula gravada, em seis partes. O acesso é liberado depois da confirmação do pagamento.</td></tr>
      <tr><th scope="row">O que você leva</th><td>Estrutura da história, checklist de 9 passos, formas de história e premissa do seu livro.</td></tr>
      <tr><th scope="row">Quando comprar</th><td>De 23/11 a 30/11, às 23h59. Depois disso, a aula sai do ar.</td></tr>
      <tr><th scope="row">Segurança</th><td>7 dias para desistir e pedir o reembolso do valor pago.</td></tr>
    </tbody></table></div>
  <p class="am-kicker" style="margin-top:48px">Ao final da aula</p>
  <h3 class="am-h2" style="font-size:clamp(1.8rem,4.2vw,2.5rem)">Você vai saber como escrever o seu livro, <span class="am-serif">do começo ao fim.</span></h3>
  <p class="am-lead" style="margin-top:16px">A ideia que hoje está solta na sua cabeça passa a ter caminho. Depois do AULÃO MASTER, você vai conseguir:</p>
  <ul class="am-outcomes" style="margin-top:22px">{"".join(f"<li>{CHECK}<span>{o}</span></li>" for o in outcomes)}</ul>
</div></section>

<section class="am-sec am-sec--warm" id="conteudo" aria-labelledby="t-conteudo"><div class="am-wrap">
  <p class="am-kicker">Neste aulão</p><h2 class="am-h2" id="t-conteudo">O que você vai aprender, <span class="am-serif">em seis partes.</span></h2>
  <p class="am-lead" style="margin-top:18px">Uma aula só, do começo ao fim, na ordem em que você vai precisar de cada coisa.</p>
  <ol class="am-topics">{topics()}</ol>
</div></section>

<section class="am-sec" id="oferta" aria-labelledby="t-oferta"><div class="am-wrap">
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
      <span>Vale para quem comprar até segunda, 23/11, às 23h59.</span>
      <span class="am-count" data-count="bonus" aria-hidden="true"></span></div>
    <div class="am-offer__foot">
      <strong>A aula sai do ar em</strong>
      <div class="am-open"><span class="am-count am-count--big" data-count="sale" aria-hidden="true"></span></div>
      <p class="am-note am-open">A venda encerra em 30/11, às 23h59 (horário de Brasília). Depois disso o AULÃO MASTER sai do ar e não será reaberto. Regras na <a href="{CANC}">política de cancelamento e reembolso</a>.</p>
      <p class="am-note am-closed">A venda foi encerrada.</p>
    </div>
  </div>
</div></section>

<section class="am-sec" id="quem-sou-eu" aria-labelledby="t-eu"><div class="am-wrap">
  <p class="am-kicker">Quem dá a aula</p>
  <h2 class="am-h2" id="t-eu">Deixa eu me apresentar. <span class="am-serif">Sou a Camila.</span></h2>
  <figure class="am-figure" style="margin-top:30px"><img src="{{IMG:camila-professora.jpg}}" alt="Camila Veloso, professora do AULÃO MASTER, diante de uma estante de livros" width="898" height="1600" loading="lazy" style="object-position:50% 30%"></figure>
  <div class="am-bio"><div class="am-prose">
    <p>Sou <strong>produtora editorial</strong>, formada em Comunicação Social, Produção Editorial pela UFSM. Tenho mais de seis anos de experiência em marketing e conteúdo, em B2B e B2C, e ajudo escritores iniciantes a desenvolver e publicar seus livros.</p>
    <p>O AULÃO MASTER é o que eu mostraria a qualquer pessoa que me dissesse "quero escrever um livro, mas não sei por onde começar".</p></div>
    <ul class="am-bio__facts">
      <li>{CHECK}<span>Comunicação Social, Produção Editorial (UFSM)</span></li>
      <li>{CHECK}<span>Mais de seis anos em marketing e conteúdo, em B2B e B2C</span></li>
      <li>{CHECK}<span>Ajudo escritores iniciantes a desenvolver e publicar seus livros</span></li>
    </ul>
    <p class="am-bio__sign">Camila Veloso</p><p class="am-bio__role">Professora do AULÃO MASTER · <a href="{INSTA}" rel="noopener">@acamiveloso</a></p>
  </div>
</div></section>

<section class="am-sec am-sec--warm" id="seguranca" aria-labelledby="t-seg"><div class="am-wrap am-wrap--wide"><div class="am-verify">
  <h2 id="t-seg">Compre com segurança. <span class="am-serif">Dá para conferir cada informação.</span></h2>
  <div class="am-verify__grid">
    <div><b>7 dias</b><strong>Reembolso do valor pago</strong><p>Você tem 7 dias corridos depois da compra para desistir. O retorno vem em até 5 dias úteis. <a href="{CANC}">Ler a política completa</a>.</p></div>
    <div><b>CNPJ</b><strong>Empresa registrada</strong><p>CAMILA VELOSO. CO LTDA, CNPJ 47.277.682/0001-48. Você pode consultar na Receita Federal.</p></div>
    <div><b>Oficial</b><strong>Canais oficiais</strong><p>Site <a href="{SITE}/">aaldeialiteraria.com.br</a> e Instagram da professora, <a href="{INSTA}" rel="noopener">@acamiveloso</a>.</p></div>
  </div>
  <p class="am-verify__close">Quem confere antes de comprar decide melhor.</p>
</div></div></section>

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
    <p>Se você tem uma ideia de livro e não sabe por onde começar, essa aula foi feita para você. Se ainda não é o momento, tudo bem. Mas saiba que quem começa com um mapa na mão chega mais longe.</p>
    <p class="am-serif">Um abraço,<br>Camila.</p>
  </div>
  <div class="am-cta">
    <div class="am-open" style="display:grid;gap:16px;justify-items:center;width:100%">
      <h3>Comece o seu livro pelo AULÃO MASTER</h3>
      <span class="am-count am-count--big" data-count="sale" aria-hidden="true"></span>
      <a class="am-btn" href="{CHECKOUT}">Quero o AULÃO MASTER por R$ 97 {ARROW_BTN}</a>
      <p class="am-note">Aula gravada · acesso depois da confirmação do pagamento · 7 dias para desistir</p>
    </div>
    <div class="am-closed"><h3>As vendas foram encerradas</h3><p class="am-note" style="margin-top:8px">O AULÃO MASTER saiu do ar.</p></div>
  </div>
</div></section>
</main>

<footer class="am-footer"><div class="am-wrap">
  <div class="am-footer__grid">
    <div><a class="am-brand" href="{SITE}/">Aldeia Literária<i>.</i></a><p><strong>Página oficial do AULÃO MASTER</strong>, aula gravada de Camila Veloso para quem quer escrever um livro.</p></div>
    <div><h3>Camila Veloso</h3><ul><li><a href="{INSTA}" rel="noopener">Instagram @acamiveloso</a></li><li><a href="{FUNDADORA}">Sobre a fundadora</a></li></ul></div>
    <div><h3>Site</h3><ul><li><a href="{SITE}/">Início</a></li><li><a href="{SOBRE}">Sobre</a></li><li><a href="{GUIA}">Guia</a></li><li><a href="{IMP}">Imprensa</a></li><li><a href="{CANC}">Cancelamento e reembolso</a></li></ul></div>
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
