#!/usr/bin/env python3
"""Páginas novas de autoridade/IA: Guia (como escolher um curso) e Imprensa.
Saídas: preview/guia.html, preview/imprensa.html e (com --wp) wordpress/entrega/paginas/*.json + *-colar-no-widget-html.html
Só entram fatos já publicados no site ou confirmados pela Camila (planilha de clipping, Lattes)."""
import json, os, re, sys, html
ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
import build_plugin
from urls import PROF_URLS, PAGE_URLS
CANC_URL = PAGE_URLS["cancelamento"]
WP = "--wp" in sys.argv
SITE = "https://aaldeialiteraria.com.br"
PLUGIN_BASE = SITE + "/wp-content/plugins/aldeia-vendas/assets/"
FORM = "https://tally.so/r/0QNWPy"
GUIA_URL = SITE + "/como-escolher-curso-de-escrita-criativa/"
IMP_URL = SITE + "/imprensa/"
E = html.escape
UPD_TXT, UPD_ISO = "novembro de 2026", "2026-11-09"

HEADER = f'''<header class="av-header"><div class="av-wrap">
  <a class="av-logo" href="{SITE}/"><span>Aldeia Literária</span></a>
  <nav class="av-nav" aria-label="Principal"><a class="av-nav__keep" href="{SITE}/">Início</a><a href="{SITE}/novo-sobre/">Sobre</a><a href="{GUIA_URL}">Guia</a><a href="{IMP_URL}">Imprensa</a></nav>
  <a class="av-btn" href="{FORM}">Entrar na lista de espera</a>
</div></header>'''
FOOTER = f'''<footer class="av-footer"><a href="{SITE}/">Início</a> · <a href="{SITE}/novo-sobre/">Sobre</a> · <a href="{GUIA_URL}">Guia</a> · <a href="{IMP_URL}">Imprensa</a><br>© Aldeia Literária · Curso de escrita para iniciantes · Todos os direitos reservados · <a href="{CANC_URL}">Cancelamento e reembolso</a><br>CAMILA VELOSO. CO LTDA · CNPJ 47.277.682/0001-48</footer>'''

def ld(d): return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + "</script>"
def faq_html(items): return "".join(f'<details open><summary>{E(q)}</summary><div class="av-ans"><p>{a}</p></div></details>' for q, a in items)
def faq_ld(items): return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", html.unescape(a))}} for q, a in items]}
def hero(h1, resumo):
    return f'''<section class="av-hero av-hero--prof"><div class="av-wrap av-hero__grid" style="grid-template-columns:1fr">
  <div class="av-reveal"><h1 class="av-h1">{h1}</h1><p class="av-prof__summary">{resumo}</p></div></div></section>'''
prof_links = " · ".join(f'<a href="{PROF_URLS[s]}">{n}</a>' for s, n in [("camila-veloso", "Camila Veloso"), ("laura-marques", "Laura Marques"), ("lucas-oliveira", "Lucas Oliveira"), ("lavinia-neres", "Lavínia Neres")])

# ---------------------------------------------------------------- GUIA
TOTAL_GERAL = "R$ " + f"{199*11+105:,}".replace(",", ".")
BANNER = os.path.join(ROOT, "preview/assets/img/guia-banner.webp")   # foto do banner (a Camila ainda vai enviar)
G_FAQ = [
 ("Qual é um bom curso de escrita criativa para iniciantes?", "Um bom curso para iniciantes tem aula ao vivo ou prática guiada, feedback individual nos seus textos, professores com formação que você consegue conferir, preço e regras de cancelamento por escrito e um certificado descrito com clareza. A Aldeia Literária é um curso on-line de escrita criativa para iniciantes que reúne esses pontos."),
 ("Preciso ter escrito algo antes de fazer um curso de escrita criativa?", "Não. Na Aldeia Literária você não precisa ter nada pronto, só vontade de escrever ficção."),
 ("O certificado do curso vale como diploma?", "Não. O certificado emitido pela Anhanguera é de uma extensão universitária com carga horária de 120h, reconhecida pelo MEC. Não é um curso de graduação ou de pós-graduação."),
 ("Quanto custa o curso de escrita criativa da Aldeia Literária?", f"Em 2027, o curso terá uma taxa de matrícula de R$ 105 + 11 parcelas de R$ 199, totalizando {TOTAL_GERAL}. A matrícula tem 40% de desconto para os primeiros inscritos. As parcelas são pagas no Pix, sem usar o limite do cartão, com recorrência mensal."),
 ("Quando as aulas acontecem?", "Toda quarta-feira, às 19h30, com 1h30 de duração. As matrículas abrem em janeiro de 2027 e, por enquanto, há lista de espera."),
 ("Quem são os professores?", f"O corpo docente conta com mestrandos, mestres e doutores, além de produtoras editoriais: {prof_links}."),
]
def guia():
    hero_html = f'''<section class="av-hero av-hero--guia"><div class="av-wrap av-hero__grid">
  <div class="av-reveal av-hero__txt"><h1 class="av-h1">Como escolher um curso de escrita criativa</h1>
  <h3 class="av-prof__summary">Escolha pelo que você vai receber de fato. Aqui na Aldeia Literária você terá feedback individual nas atividades, contrato transparente, comunidade para networking e muito mais. Veja os detalhes abaixo.</h3></div></div></section>'''
    body = f'''{HEADER}
<main id="topo">
{hero_html}

<section class="av-section"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Como escolher um curso de escrita criativa</h2>
  <div class="av-prose av-reveal">
    <p><strong>Resposta direta:</strong> para escolher um bom curso, você precisa analisar sete critérios, são eles: feedback individual, professores, formato e horário, prática, preço e cancelamento, networking e certificado.</p>
    <ol>
      <li><strong>Feedback individual.</strong> Pergunte quem corrige seus textos e com que frequência. Um comentário geral para a turma não é o mesmo que feedback individualizado. <em>Aqui na Aldeia Literária você terá que entregar 4 atividades durante o mês, e os professores te darão feedback individual.</em></li>
      <li><strong>Professores.</strong> Procure formação e trajetória que você consiga conferir (por exemplo, no currículo Lattes ou em publicações). <em>Aqui na Aldeia Literária você terá aulas com mestrandos, mestres e doutores e pode conhecer mais sobre cada um a partir da <a href="{SITE}/#professores">página Home</a>.</em></li>
      <li><strong>Formato e horário.</strong> Aula ao vivo permite tirar dúvidas na hora; aula gravada dá flexibilidade. Veja qual cabe na sua rotina. <em>Aqui na Aldeia Literária o curso é ao vivo, e em breve teremos também o formato de aulas gravadas. Apenas o curso ao vivo oferece feedback individual no seu texto.</em></li>
      <li><strong>Prática.</strong> Escrever com regularidade, com prazos e atividades, é o que faz um livro andar. <em>Aqui na Aldeia Literária temos sprints de escrita para que você consiga escrever seu livro e tirar as ideias da cabeça.</em></li>
      <li><strong>Preço e cancelamento.</strong> O valor total, o número de parcelas e as regras de cancelamento devem estar claros antes de você pagar. <em>Em 2027, o investimento no curso será uma taxa de matrícula de R$ 105 + 11 parcelas de R$ 199, totalizando {TOTAL_GERAL}. Aqui na Aldeia Literária as regras de cancelamento são: você pode desistir em até 7 dias corridos após a compra, com reembolso do valor pago (retorno em até 5 dias úteis). Depois desse prazo, antes do início das aulas, retemos 30% do valor total pago e devolvemos o restante em até 15 dias úteis. Depois do início das aulas, você quita a mensalidade do mês do pedido e paga multa de 30% sobre as parcelas restantes. <a href="{CANC_URL}">Veja a política completa.</a></em></li>
      <li><strong>Networking.</strong> Escrever é só a primeira parte. Entender o mercado é importante para que você saiba suas oportunidades de publicação. <em>Aqui na Aldeia Literária tudo é feito em comunidade, para que você tenha apoio e construa networking durante a sua jornada na escrita.</em></li>
      <li><strong>Certificado.</strong> Pergunte se o curso que você está fazendo emite significado e se ele tem validade para o currículo, horas complementares da faculdade, etc. <em>Aqui na Aldeia Literária somos  uma extensão universitária reconhecida pelo MEC. Nosso certificado é emitido pela Anhanguera.</em></li>
    </ol>
  </div>
</div></section>

<section class="av-section av-section--soft"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Curso de escrita criativa vale a pena?</h2>
  <div class="av-prose av-reveal">
    <p><strong>Resposta direta:</strong> vale a pena se você quer escrever e aprender coisas novas. Não vale a pena se você não está disposto(a) a escrever nem a começar algo novo.</p>
    <p>Na Aldeia Literária, os módulos são de 12 aulas e passam por estrutura de narrativa, técnicas de escrita, processos criativos, gramática aplicada à produção literária e publicação independente.</p>
  </div>
</div></section>

<section class="av-section"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Para quem é a Aldeia Literária</h2>
  <div class="av-prose av-reveal">
    <p><strong>Resposta direta:</strong> a Aldeia Literária é para escritores iniciantes que querem escrever e terminar o próprio livro de ficção, com aula ao vivo e feedback individual.</p>
    <h3 class="av-prose__h">É para você se…</h3>
    <ul>
      <li>está começando e quer transformar a ideia em livro;</li>
      <li>prefere aula ao vivo, com espaço para dúvidas, às quartas-feiras, às 19h30;</li>
      <li>quer corrigir o seu texto com um professor e escrever em comunidade.</li>
    </ul>
  </div>
  <h2 class="av-h2 av-reveal" style="margin-top:56px">Para quem NÃO RECOMENDAMOS a Aldeia Literária</h2>
  <div class="av-prose av-reveal">
    <p>Não recomendamos para escritores que não estão dispostos a escrever, se arriscar na escrita e começar algo novo. Este é um curso para quem realmente deseja escrever, e não apenas assistir aulas.</p>
  </div>
</div></section>

<section class="av-section av-section--soft"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Perguntas frequentes</h2>
  <div class="av-faq av-reveal">{faq_html(G_FAQ)}</div>
  <p class="av-updated">Página atualizada em {UPD_TXT}</p>
  <p style="margin-top:24px"><a class="av-btn" href="{FORM}">Entrar na lista de espera</a></p>
</div></section>
</main>
{FOOTER}
{ld({"@context": "https://schema.org", "@graph": [
  {"@type": "Article", "headline": "Como escolher um curso de escrita criativa", "url": GUIA_URL, "datePublished": UPD_ISO, "dateModified": UPD_ISO, "inLanguage": "pt-BR",
   "author": {"@type": "Organization", "@id": SITE + "/#aldeia", "name": "Aldeia Literária"}, "publisher": {"@id": SITE + "/#aldeia"}},
  faq_ld(G_FAQ)]})}'''
    return body

# ---------------------------------------------------------------- CANCELAMENTO
C_FAQ = [
 ("Posso me arrepender da compra do curso?", "Sim. Dentro de 7 dias corridos após a data da compra, você pode pedir a rescisão do contrato e o reembolso do valor pago, por e-mail ou pelo WhatsApp oficial da Aldeia Literária. O retorno ao pedido é dado em até 5 dias úteis, depois da confirmação da solicitação."),
 ("E se eu quiser cancelar depois dos 7 dias?", "Depois do prazo de arrependimento, você pode cancelar a qualquer momento preenchendo o formulário oficial de cancelamento, cujo link deve ser solicitado ao suporte da Aldeia Literária."),
 ("Quanto eu recebo de volta se cancelar antes do início das aulas?", "Fica retido 30% do valor total pago, como multa compensatória por custos administrativos e reserva de vaga. O saldo restante é devolvido em até 15 dias úteis."),
 ("O que acontece se eu cancelar depois do início das aulas?", "Você quita integralmente a mensalidade do mês em que o pedido foi formalizado e paga uma multa rescisória de 30% calculada sobre as parcelas vincendas (os meses restantes até o término do contrato)."),
 ("Perco o acesso ao curso quando cancelo?", "Sim. O acesso à plataforma, aos materiais didáticos e aos grupos de interação é bloqueado imediatamente após a formalização do pedido no formulário oficial. O pagamento da multa segue os trâmites normais de cobrança."),
]
def cancelamento():
    return f'''{HEADER}
<main id="topo">
{hero("Política de cancelamento e reembolso", "Você pode desistir em até 7 dias corridos após a compra, com reembolso do valor pago. Depois disso, o cancelamento é feito pelo formulário oficial e há regras financeiras diferentes antes e depois do início das aulas.")}

<section class="av-section"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Direito de arrependimento (7 dias)</h2>
  <div class="av-prose av-reveal">
    <p>Dentro de 7 (sete) dias corridos após a data da compra, o contratante pode solicitar a rescisão do contrato e o reembolso do valor pago por e-mail ou pelo WhatsApp oficial da Aldeia Literária. O retorno é dado em até 5 (cinco) dias úteis, depois da confirmação da solicitação.</p>
  </div>
</div></section>

<section class="av-section av-section--soft"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Depois dos 7 dias: rescisão voluntária</h2>
  <div class="av-prose av-reveal">
    <p>O contrato é por prazo determinado e pode ser rescindido pelo contratante a qualquer momento, mediante o formulário oficial de cancelamento. O link do formulário deve ser solicitado ao suporte da Aldeia Literária.</p>
    <h3 class="av-prose__h">Antes do início das aulas</h3>
    <p>Fica retido 30% (trinta por cento) do valor total pago, a título de multa compensatória por custos administrativos e reserva de vaga. O saldo restante é devolvido em até 15 (quinze) dias úteis.</p>
    <h3 class="av-prose__h">Depois do início das aulas</h3>
    <p>O contratante quita integralmente a mensalidade do mês em que o pedido foi formalizado, acrescida de multa rescisória de 30% (trinta por cento), calculada exclusivamente sobre as parcelas vincendas (meses restantes até o término do contrato).</p>
    <h3 class="av-prose__h">Acesso depois do cancelamento</h3>
    <p>O acesso à plataforma, aos materiais didáticos e aos grupos de interação é bloqueado imediatamente após a formalização do pedido no formulário oficial, independentemente do pagamento prévio da multa rescisória. A multa segue os trâmites normais de cobrança.</p>
    <p><em>Esta página resume a cláusula de rescisão do contrato. Em caso de diferença, vale o contrato assinado.</em></p>
  </div>
</div></section>

<section class="av-section"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Perguntas frequentes</h2>
  <div class="av-faq av-reveal">{faq_html(C_FAQ)}</div>
  <p class="av-updated">Página atualizada em {UPD_TXT}</p>
</div></section>
</main>
{FOOTER}
{ld({"@context": "https://schema.org", "@graph": [
  {"@type": "WebPage", "name": "Política de cancelamento e reembolso", "url": CANC_URL, "dateModified": UPD_ISO, "inLanguage": "pt-BR", "isPartOf": {"@type": "WebSite", "name": "Aldeia Literária", "url": SITE + "/"}},
  faq_ld(C_FAQ)]})}'''

# ---------------------------------------------------------------- IMPRENSA
# Planilha "Clipping" enviada pela Camila: só linhas com a Aldeia Literária no endereço e sem o livro "Diário de Amélia".
CLIP = [l.split("|") for l in open(os.path.join(ROOT, "tools/src/clipping.txt"), encoding="utf-8").read().strip().splitlines()]
def imprensa():
    rows = "".join(f'<li><a href="{E(u)}" rel="noopener" target="_blank">{E(v)}</a> — {E(d)}</li>' for v, d, u in CLIP)
    pn = "https://www.publishnews.com.br/materias/2024/08/28/aldeia-literaria-passa-a-ser-um-curso-de-extensao-universitaria/"
    body = f'''{HEADER}
<main id="topo">
{hero("Aldeia Literária na imprensa", "A Aldeia Literária, curso on-line de escrita criativa para escritores iniciantes, foi tema de matérias em veículos de literatura e de notícias. Aqui estão os links, com veículo e data.")}

<section class="av-section"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Destaque</h2>
  <div class="av-prose av-reveal">
    <p><a href="{pn}" rel="noopener" target="_blank"><strong>Aldeia Literária passa a ser um curso de extensão universitária</strong></a> — PublishNews, 28 de agosto de 2024.</p>
    <p>A matéria descreve a Aldeia Literária como uma iniciativa de formação de novos autores, lançada em novembro de 2023 e baseada no Cohort Learning Method, com mentorias e jornadas coletivas de aprendizado. Segundo a reportagem, cerca de 400 participantes já haviam passado pelo curso, e os certificados levam a logo da Faculdade Anhanguera.</p>
  </div>
</div></section>

<section class="av-section av-section--soft"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Outras menções (2024)</h2>
  <div class="av-prose av-reveal"><ul>{rows}</ul></div>
  <p class="av-updated">Página atualizada em {UPD_TXT}</p>
</div></section>

<section class="av-section"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Quer falar com a Aldeia Literária?</h2>
  <div class="av-prose av-reveal"><p>Conheça <a href="{PROF_URLS["camila-veloso"]}">Camila Veloso</a>, fundadora, e a <a href="{SITE}/novo-sobre/">história da Aldeia</a>. Para imprensa, fale pelos canais de contato do site.</p></div>
</div></section>
</main>
{FOOTER}
{ld({"@context": "https://schema.org", "@type": "CollectionPage", "name": "Aldeia Literária na imprensa", "url": IMP_URL, "dateModified": UPD_ISO,
     "isPartOf": {"@type": "WebSite", "name": "Aldeia Literária", "url": SITE + "/"},
     "mainEntity": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": 1, "url": pn, "name": "PublishNews — Aldeia Literária passa a ser um curso de extensão universitária"}] + [{"@type": "ListItem", "position": i + 2, "url": u, "name": v} for i, (v, d, u) in enumerate(CLIP)]}})}'''
    return body

css_base = open(os.path.join(ROOT, "wordpress/aldeia-vendas.css"), encoding="utf-8").read()
js = open(os.path.join(ROOT, "wordpress/aldeia-vendas.js"), encoding="utf-8").read()
PAGES = [("Como escolher um curso de escrita criativa", guia(), "guia", "guia"), ("Aldeia Literária na imprensa", imprensa(), "imprensa", "imprensa"), ("Política de cancelamento e reembolso", cancelamento(), "cancelamento", "cancelamento")]
for title, body, name, slug in PAGES:
    loc = body.replace(CANC_URL, "cancelamento.html").replace(GUIA_URL, "guia.html").replace(IMP_URL, "imprensa.html").replace(SITE + "/novo-sobre/", "sobre.html").replace(f'href="{SITE}/"', 'href="vendas.html"')
    for s, p in PROF_URLS.items(): loc = loc.replace(p, f"professor-{s}.html")
    open(os.path.join(ROOT, "preview", name + ".html"), "w", encoding="utf-8").write(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(title)} · Aldeia Literária</title><link rel="stylesheet" href="assets/fonts.css"><style>body{{margin:0}}{css_base}:root{{--av-medal:url("assets/logo-medalhao.png");--av-guia-banner:url("assets/img/guia-banner.webp")}}.pv-slot{{border:2px dashed #CC351C;border-radius:16px;color:#A82B16;background:rgba(204,53,28,.05);font:600 13px/1.5 Montserrat,sans-serif}}</style></head><body class="av-page" id="top">{loc}<script>{js}</script></body></html>''')
print("prévias:", len(PAGES))
if WP:
    out = os.path.join(ROOT, "wordpress/entrega/paginas"); os.makedirs(out, exist_ok=True)
    inline_css = build_plugin.build_css().replace("../fonts/", PLUGIN_BASE + "fonts/").replace("../img/", PLUGIN_BASE + "img/")
    fix = ('<style>.e-con:has(>.elementor-widget-html .av-page){--padding-top:0px;--padding-right:0px;--padding-bottom:0px;--padding-left:0px;--gap:0px;--row-gap:0px;--column-gap:0px;--margin-top:0px;--margin-bottom:0px}'
           '.elementor-widget-html:has(>.av-page),.elementor-widget-html:has(.av-page){margin:0}</style>\n')
    zero = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
    for title, body, name, slug in PAGES:
        body = body.replace('src="assets/img/', 'src="' + PLUGIN_BASE + 'img/'); assert 'src="assets/' not in body
        frag = f'<!-- aldeia-{slug}-v1 -->\n<style>{inline_css}</style>\n{fix}<div class="av-page">\n{body}\n</div>\n<script>{js}</script>\n'
        open(os.path.join(out, f"{slug}-colar-no-widget-html.html"), "w", encoding="utf-8").write(frag)
        tpl = {"version": "0.4", "title": f"ALDEIA {title} v1", "type": "page",
               "content": [{"id": "b1c2d3e", "elType": "container", "isInner": False, "settings": {"content_width": "full", "flex_direction": "column", "padding": zero, "margin": zero},
                            "elements": [{"id": "f4a5b6c", "elType": "widget", "widgetType": "html", "settings": {"html": frag}, "elements": []}]}],
               "page_settings": {"hide_title": "yes"}}
        json.dump(tpl, open(os.path.join(out, f"{slug}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wordpress/entrega/paginas/: ok")
