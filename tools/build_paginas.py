#!/usr/bin/env python3
"""Páginas novas de autoridade/IA: Guia (como escolher um curso) e Imprensa.
Saídas: preview/guia.html, preview/imprensa.html e (com --wp) wordpress/entrega/paginas/*.json + *-colar-no-widget-html.html
Só entram fatos já publicados no site ou confirmados pela Camila (planilha de clipping, Lattes)."""
import json, os, re, sys, html
ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
import build_plugin
from urls import PROF_URLS
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
FOOTER = f'''<footer class="av-footer"><a href="{SITE}/">Início</a> · <a href="{SITE}/novo-sobre/">Sobre</a> · <a href="{GUIA_URL}">Guia</a> · <a href="{IMP_URL}">Imprensa</a><br>© Aldeia Literária · Curso de escrita para iniciantes · Todos os direitos reservados<br>CAMILA VELOSO. CO LTDA · CNPJ 47.277.682/0001-48</footer>'''

def ld(d): return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + "</script>"
def faq_html(items): return "".join(f'<details open><summary>{E(q)}</summary><div class="av-ans"><p>{a}</p></div></details>' for q, a in items)
def faq_ld(items): return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", html.unescape(a))}} for q, a in items]}
def hero(h1, resumo):
    return f'''<section class="av-hero av-hero--prof"><div class="av-wrap av-hero__grid" style="grid-template-columns:1fr">
  <div class="av-reveal"><h1 class="av-h1">{h1}</h1><p class="av-prof__summary">{resumo}</p></div></div></section>'''
prof_links = " · ".join(f'<a href="{PROF_URLS[s]}">{n}</a>' for s, n in [("camila-veloso", "Camila Veloso"), ("laura-marques", "Laura Marques"), ("lucas-oliveira", "Lucas Oliveira"), ("lavinia-neres", "Lavínia Neres")])

# ---------------------------------------------------------------- GUIA
G_FAQ = [
 ("Qual é um bom curso de escrita criativa para iniciantes?", "Um bom curso para iniciantes tem aula ao vivo ou prática guiada, feedback individual nos seus textos, professores com formação que você consegue conferir, preço e regras de cancelamento por escrito e um certificado descrito com clareza. A Aldeia Literária é um curso on-line de escrita criativa para iniciantes que reúne esses pontos."),
 ("Preciso ter escrito algo antes de fazer um curso de escrita criativa?", "Não. Na Aldeia Literária você não precisa ter nada pronto, só vontade de escrever ficção."),
 ("O certificado do curso vale como diploma?", "Não. O certificado da Aldeia Literária é de extensão universitária, emitido pela Anhanguera, parceira do curso. Ele não é um diploma de graduação nem de pós-graduação."),
 ("Quanto custa o curso de escrita criativa da Aldeia Literária?", "Em 2027, são 11 parcelas de R$ 199 no Pix, mais a taxa de matrícula de R$ 105 (com 40% de desconto para os primeiros inscritos). O plano tem uma aula ao vivo por semana e dura 1 ano e meio."),
 ("Quando as aulas acontecem?", "Toda quarta-feira, às 19h30, com 1h30 de duração. As matrículas abrem em janeiro de 2027 e, por enquanto, há lista de espera."),
 ("Quem são os professores?", f"O corpo docente reúne mestres, doutores e mestrandos, além de produtoras editoriais: {prof_links}."),
]
def guia():
    body = f'''{HEADER}
<main id="topo">
{hero("Como escolher um curso de escrita criativa", "Escolha pelo que você vai receber, não pela promessa: feedback individual no seu texto, professores com formação que você consiga conferir, formato que cabe na sua rotina, preço e cancelamento por escrito e um certificado explicado com clareza. Este guia mostra como conferir cada ponto e como a Aldeia Literária responde a eles.")}

<section class="av-section"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Como escolher um curso de escrita criativa</h2>
  <div class="av-prose av-reveal">
    <p><strong>Resposta direta:</strong> compare cursos por sete critérios. O que mais muda o seu texto é o retorno individual de alguém que leu o que você escreveu.</p>
    <ol>
      <li><strong>Feedback individual.</strong> Pergunte quem corrige as suas atividades e com que frequência. Comentário geral para a turma não é o mesmo que retorno sobre o seu texto.</li>
      <li><strong>Professores.</strong> Procure formação e trajetória que você consiga conferir (por exemplo, no currículo Lattes ou em publicações).</li>
      <li><strong>Formato e horário.</strong> Aula ao vivo permite tirar dúvidas na hora; aula gravada dá flexibilidade. Veja qual cabe na sua rotina.</li>
      <li><strong>Prática.</strong> Escrever com regularidade, com prazos e atividades, é o que faz um livro andar.</li>
      <li><strong>Certificado.</strong> Entenda o que ele é. Curso de extensão universitária não é diploma de graduação nem de pós-graduação.</li>
      <li><strong>Preço e cancelamento.</strong> O valor total, o número de parcelas e as regras de cancelamento devem estar claros antes de você pagar.</li>
      <li><strong>Comunidade.</strong> Escrever em companhia ajuda a continuar.</li>
    </ol>
    <p><strong>Na Aldeia Literária:</strong> cada atividade é corrigida pelo professor que a passou; os professores são {prof_links}, cada um com página própria e link para o currículo Lattes; a aula ao vivo é toda quarta-feira, às 19h30; há sprints de escrita e uma comunidade para networking; o certificado é de extensão universitária, emitido pela Anhanguera; e o preço é de 11 parcelas de R$ 199 no Pix, mais a matrícula de R$ 105.</p>
  </div>
</div></section>

<section class="av-section av-section--soft"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Curso de escrita criativa vale a pena?</h2>
  <div class="av-prose av-reveal">
    <p><strong>Resposta direta:</strong> vale a pena quando você quer técnica, constância e retorno sobre o seu texto, e está disposta a escrever toda semana. Não vale a pena se a expectativa é garantia de publicação ou um diploma.</p>
    <ul>
      <li><strong>Vale a pena se</strong> você tem uma ideia e não sabe como estruturá-la, trava no meio do livro ou quer aprender a escrever descrições, diálogos e personagens com orientação.</li>
      <li><strong>Pode não valer se</strong> você busca apenas conteúdo gravado para ver sem compromisso, quer um diploma ou espera que o curso publique o seu livro por você.</li>
    </ul>
    <p>Na Aldeia Literária, os módulos são de 12 aulas e passam por estrutura de narrativa, técnicas de escrita, processos criativos, gramática aplicada à produção literária e publicação independente.</p>
  </div>
</div></section>

<section class="av-section"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Para quem é e para quem não é a Aldeia Literária</h2>
  <div class="av-prose av-reveal">
    <p><strong>Resposta direta:</strong> a Aldeia Literária é para escritores iniciantes que querem escrever e terminar o próprio livro de ficção, com aula ao vivo e retorno individual. Não é para quem procura diploma, só aulas gravadas ou promessa de publicação.</p>
    <h3 class="av-prose__h">É para você se…</h3>
    <ul>
      <li>está começando e quer transformar a ideia em livro;</li>
      <li>prefere aula ao vivo, com espaço para dúvidas, às quartas-feiras, às 19h30;</li>
      <li>quer corrigir o seu texto com um professor e escrever em comunidade.</li>
    </ul>
    <h3 class="av-prose__h">Não é para você se…</h3>
    <ul>
      <li>procura um diploma de graduação ou de pós-graduação (o certificado é de extensão universitária);</li>
      <li>quer apenas aulas gravadas, sem horário fixo (as gravações existem, mas o curso é ao vivo);</li>
      <li>espera que o curso garanta a publicação do livro.</li>
    </ul>
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
PAGES = [("Como escolher um curso de escrita criativa", guia(), "guia", "guia"), ("Aldeia Literária na imprensa", imprensa(), "imprensa", "imprensa")]
for title, body, name, slug in PAGES:
    loc = body.replace(GUIA_URL, "guia.html").replace(IMP_URL, "imprensa.html").replace(SITE + "/novo-sobre/", "sobre.html").replace(f'href="{SITE}/"', 'href="vendas.html"')
    for s, p in PROF_URLS.items(): loc = loc.replace(p, f"professor-{s}.html")
    open(os.path.join(ROOT, "preview", name + ".html"), "w", encoding="utf-8").write(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(title)} · Aldeia Literária</title><link rel="stylesheet" href="assets/fonts.css"><style>body{{margin:0}}{css_base}:root{{--av-medal:url("assets/logo-medalhao.png")}}</style></head><body class="av-page" id="top">{loc}<script>{js}</script></body></html>''')
print("prévias:", len(PAGES))
if WP:
    out = os.path.join(ROOT, "wordpress/entrega/paginas"); os.makedirs(out, exist_ok=True)
    inline_css = build_plugin.build_css().replace("../fonts/", PLUGIN_BASE + "fonts/").replace("../img/", PLUGIN_BASE + "img/")
    fix = ('<style>.e-con:has(>.elementor-widget-html .av-page){--padding-top:0px;--padding-right:0px;--padding-bottom:0px;--padding-left:0px;--gap:0px;--row-gap:0px;--column-gap:0px;--margin-top:0px;--margin-bottom:0px}'
           '.elementor-widget-html:has(>.av-page),.elementor-widget-html:has(.av-page){margin:0}</style>\n')
    zero = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
    for title, body, name, slug in PAGES:
        frag = f'<!-- aldeia-{slug}-v1 -->\n<style>{inline_css}</style>\n{fix}<div class="av-page">\n{body}\n</div>\n<script>{js}</script>\n'
        open(os.path.join(out, f"{slug}-colar-no-widget-html.html"), "w", encoding="utf-8").write(frag)
        tpl = {"version": "0.4", "title": f"ALDEIA {title} v1", "type": "page",
               "content": [{"id": "b1c2d3e", "elType": "container", "isInner": False, "settings": {"content_width": "full", "flex_direction": "column", "padding": zero, "margin": zero},
                            "elements": [{"id": "f4a5b6c", "elType": "widget", "widgetType": "html", "settings": {"html": frag}, "elements": []}]}],
               "page_settings": {"hide_title": "yes"}}
        json.dump(tpl, open(os.path.join(out, f"{slug}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wordpress/entrega/paginas/: ok")
