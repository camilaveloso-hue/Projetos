#!/usr/bin/env python3
"""Gera as páginas dos professores (HTML único, mesmo sistema visual da Home e da Sobre).

Uso:
  python3 tools/build_professores.py            -> só as prévias em preview/ (professor-*.html e professores.html)
  python3 tools/build_professores.py --wp       -> também os modelos do Elementor e os arquivos "colar no widget HTML" em wordpress/professores/

Regra de ouro: só entra na página o que está em PROFS (fatos verificados). Campos opcionais
(bio, ensina, links, formacao_extra) ficam de fora se estiverem vazios; na PRÉVIA aparece uma caixa
tracejada mostrando onde eles entrarão. A caixa não existe nos arquivos do WordPress.
"""
import json, os, sys, html
ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
import build_plugin

WP = "--wp" in sys.argv
SITE = "https://aaldeialiteraria.com.br"
PLUGIN_BASE = SITE + "/wp-content/plugins/aldeia-vendas/assets/"
FORM = "https://tally.so/r/0QNWPy"
ORG = "Aldeia Literária"
CURSO = "Escrita Criativa: Desenvolvimento e Prática"
UPDATED_TXT, UPDATED_ISO = "outubro de 2026", "2026-10-29"

# ---- Fatos verificados (texto igual ao já publicado na Home/Sobre). Opcionais: preencher com dados reais. ----
PROFS = [
 dict(slug="camila-veloso", nome="Camila Veloso", f=True, foto="prof-camila.jpg",
      papel="Fundadora e mediadora das aulas", cred="Produtora Editorial (UFSM)",
      job="Fundadora e mediadora das aulas", alma=["UFSM"],
      resumo="Camila Veloso é Produtora Editorial formada pela UFSM e fundadora da Aldeia Literária, curso on-line de escrita criativa para escritores iniciantes. Criou a Aldeia em novembro de 2023 e faz a mediação das aulas ao vivo.",
      funcao="Fundadora e mediadora das aulas", formacao="Produtora Editorial (UFSM)",
      bio=[], ensina=[], links=[]),
 dict(slug="laura-marques", nome="Laura Marques", f=False, foto="prof-laura.jpg",
      papel="Professora de Escrita Criativa", cred="Produtora Editorial, mestranda em Comunicação (UFSM) e Leitora Crítica",
      job="Professora de Escrita Criativa", alma=["UFSM"],
      resumo="Laura Marques é Produtora Editorial, mestranda em Comunicação pela UFSM e Leitora Crítica. É professora do curso Escrita Criativa: Desenvolvimento e Prática, da Aldeia Literária, voltado a escritores iniciantes.",
      funcao="Professora de Escrita Criativa", formacao="Produtora Editorial; mestranda em Comunicação (UFSM); Leitora Crítica",
      bio=[], ensina=[], links=[]),
 dict(slug="lucas-oliveira", nome="Lucas Oliveira", f=False, foto="prof-lucas.jpg",
      papel="Professor de Escrita Criativa", cred="Mestre e Doutor em Literatura Portuguesa (UFRJ)",
      job="Professor de Escrita Criativa", alma=["UFRJ"],
      resumo="Lucas Oliveira é Mestre e Doutor em Literatura Portuguesa pela UFRJ. É professor do curso Escrita Criativa: Desenvolvimento e Prática, da Aldeia Literária, voltado a escritores iniciantes.",
      funcao="Professor de Escrita Criativa", formacao="Mestre e Doutor em Literatura Portuguesa (UFRJ)",
      bio=[], ensina=[], links=[]),
 dict(slug="lavinia-neres", nome="Lavínia Neres", f=False, foto="prof-lavinia.jpg",
      papel="Professora de Escrita Criativa", cred="Produtora Editorial, Bacharel em Letras e Mestra em Comunicação (UFSM)",
      job="Professora de Escrita Criativa", alma=["UFSM"],
      resumo="Lavínia Neres é Produtora Editorial, Bacharel em Letras e Mestra em Comunicação pela UFSM. É professora do curso Escrita Criativa: Desenvolvimento e Prática, da Aldeia Literária, voltado a escritores iniciantes.",
      funcao="Professora de Escrita Criativa", formacao="Produtora Editorial; Bacharel em Letras; Mestra em Comunicação (UFSM)",
      bio=[], ensina=[], links=[]),
 dict(slug="ana-ribeiro", nome="Ana Ribeiro", f=False, foto="prof-ana.jpg",
      papel="Professora de Escrita Criativa", cred="Produtora editorial e mestra em Estudos de Linguagens pelo CEFET-MG",
      job="Professora de Escrita Criativa", alma=["CEFET-MG"],
      resumo="Ana Ribeiro é Produtora Editorial e Mestra em Estudos de Linguagens pelo CEFET-MG. É professora do curso Escrita Criativa: Desenvolvimento e Prática, da Aldeia Literária, voltado a escritores iniciantes.",
      funcao="Professora de Escrita Criativa", formacao="Produtora editorial; Mestra em Estudos de Linguagens (CEFET-MG)",
      bio=[], ensina=[], links=[]),
]
E = html.escape
def url(p): return f"{SITE}/professores/{p['slug']}/"
def primeiro(p): return p["nome"].split()[0]
def art(p): return "a" if p["nome"].split()[0] in ("Camila","Laura","Lavínia","Ana") else "o"

def slot(msg):
    return "" if WP else f'<div class="pv-slot">{E(msg)}</div>'

def jsonld(d):
    return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + '</script>'

def header(active):
    return f'''<header class="av-header"><div class="av-wrap">
  <a class="av-logo" href="{SITE}/"><span>{ORG}</span></a>
  <nav class="av-nav" aria-label="Principal"><a class="av-nav__keep" href="{SITE}/">Início</a><a href="{SITE}/novo-sobre/">Sobre</a><a href="{SITE}/professores/">Professores</a></nav>
  <a class="av-btn" href="{FORM}">Entrar na lista de espera</a>
</div></header>'''

FOOTER = f'''<footer class="av-footer"><a href="{SITE}/">Início</a> · <a href="{SITE}/novo-sobre/">Sobre</a> · <a href="{SITE}/professores/">Professores</a><br>© {ORG} · Curso de escrita para iniciantes · Todos os direitos reservados</footer>'''

def person_ld(p, with_url=True):
    d = {"@type": "Person", "@id": url(p) + "#pessoa", "name": p["nome"], "jobTitle": p["job"],
         "description": p["resumo"], "image": f"{PLUGIN_BASE}img/{p['foto']}", "url": url(p),
         "worksFor": {"@type": "Organization", "name": ORG, "url": SITE + "/"},
         "alumniOf": [{"@type": "CollegeOrUniversity", "name": n} for n in p["alma"]]}
    if p["links"]: d["sameAs"] = [u for _, u in p["links"]]
    if p["ensina"]: d["knowsAbout"] = p["ensina"]
    return d

def card(p, cls=""):
    return (f'<article class="av-reveal av-tcard{cls}"><img src="assets/img/{p["foto"]}" alt="Foto de {p["nome"]}" loading="lazy" width="520" height="650">'
            f'<div class="av-tcard__txt"><h3>{p["nome"]}</h3><p>{p["cred"]}</p>'
            f'<a class="av-tmore" href="{url(p)}" aria-label="Ver o perfil de {p["nome"]}">Ver perfil</a></div></article>')

def page_prof(p):
    outros = [q for q in PROFS if q is not p]
    a = art(p)
    faq = [
      (f"Quem é {p['nome']}?", p["resumo"]),
      (f"Onde {primeiro(p)} dá aulas?", f"{p['nome']} integra o corpo docente da {ORG}, curso on-line de escrita criativa para iniciantes. As aulas são ao vivo e as gravações ficam disponíveis enquanto o aluno estiver matriculado."),
      (f"Como estudar com {primeiro(p)}?", f"As matrículas da {ORG} abrem em janeiro de 2027. Enquanto isso, é possível entrar na lista de espera para ser avisado em primeira mão."),
    ]
    fatos = [("Nome", p["nome"]), ("Formação", p["formacao"]),
             ("Curso", f"{CURSO}, na {ORG}")]
    dl = "".join(f"<dt>{k}</dt><dd>{E(v)}</dd>" for k, v in fatos)
    links = ('<p class="av-prof__links"><strong>Perfis e publicações:</strong> ' + " · ".join(f'<a href="{u}" rel="me noopener" target="_blank">{E(t)}</a>' for t, u in p["links"]) + '</p>') if p["links"] else ""
    bio = ("".join(f"<p>{E(t)}</p>" for t in p["bio"]) or slot(f"Aqui entra a trajetória {'da' if a=='a' else 'do'} {primeiro(p)} em 2 a 4 parágrafos (formação, pesquisa, experiência com livros e escritores). Só fatos que você consegue comprovar."))
    ensina = ("<ul>" + "".join(f"<li>{E(t)}</li>" for t in p["ensina"]) + "</ul>") if p["ensina"] else slot(f"Aqui entram os temas e módulos que {primeiro(p)} ensina (lista curta, uma linha cada).")
    faqh = "".join(f'<details><summary>{E(q)}</summary><div class="av-ans"><p>{E(r)}</p></div></details>' for q, r in faq)
    ld = {"@context": "https://schema.org", "@type": "ProfilePage", "dateModified": UPDATED_ISO,
          "mainEntity": person_ld(p), "url": url(p),
          "isPartOf": {"@type": "WebSite", "name": ORG, "url": SITE + "/"}}
    return f'''{header("prof")}
<main id="topo">
<section class="av-hero av-hero--prof"><div class="av-wrap av-hero__grid">
  <div class="av-reveal">
    <p class="av-breadcrumb"><a href="{SITE}/">Início</a> · <a href="{SITE}/professores/">Professores</a></p>
    <h1 class="av-h1">{p["nome"]}</h1>
    <p class="av-prof__role">{p["papel"]} · {ORG}</p>
    <p class="av-prof__summary">{E(p["resumo"])}</p>
    <div class="av-cta-row"><a class="av-btn" href="{FORM}">Entrar na lista de espera</a></div>
  </div>
  <figure class="av-prof__photo av-reveal"><img src="assets/img/{p["foto"]}" alt="Foto de {p["nome"]}, {p["papel"].lower()} na {ORG}" width="520" height="650"></figure>
</div></section>

<section class="av-section"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Em resumo</h2>
  <dl class="av-facts av-reveal">{dl}</dl>
</div></section>

<section class="av-section av-section--soft"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Trajetória</h2>
  <div class="av-prose av-reveal">{bio}{links}</div>
  <h2 class="av-h2 av-reveal" style="margin-top:56px">O que {primeiro(p)} ensina na {ORG}</h2>
  <div class="av-prose av-reveal">{ensina}</div>
  <p class="av-updated">Página atualizada em {UPDATED_TXT}</p>
</div></section>

<section class="av-section"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Perguntas frequentes</h2>
  <div class="av-faq av-reveal">{faqh}</div>
</div></section>

<section class="av-section av-section--soft"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Conheça também</h2>
  <div class="av-pcards">{"".join(card(q) for q in outros)}</div>
</div></section>
</main>
{FOOTER}
{jsonld(ld)}'''

def page_hub():
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": f"Professores da {ORG}",
          "url": SITE + "/professores/", "dateModified": UPDATED_ISO,
          "isPartOf": {"@type": "WebSite", "name": ORG, "url": SITE + "/"},
          "mainEntity": {"@type": "ItemList", "itemListElement": [
              {"@type": "ListItem", "position": i + 1, "url": url(p), "name": p["nome"]} for i, p in enumerate(PROFS)]}}
    return f'''{header("hub")}
<main id="topo">
<section class="av-hero av-hero--prof"><div class="av-wrap av-hero__grid" style="grid-template-columns:1fr">
  <div class="av-reveal">
    <p class="av-breadcrumb"><a href="{SITE}/">Início</a> · Professores</p>
    <h1 class="av-h1">Professores da {ORG}</h1>
    <p class="av-prof__summary">A {ORG} é um curso on-line de escrita criativa para escritores iniciantes, criado em 2023 por Camila Veloso. O corpo docente reúne mestres, doutores e produtoras editoriais que corrigem os seus textos e te ajudam a transformar a ideia em livro.</p>
    <div class="av-cta-row"><a class="av-btn" href="{FORM}">Entrar na lista de espera</a></div>
  </div>
</div></section>

<section class="av-section"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Quem ensina na {ORG}</h2>
  <div class="av-pcards av-pcards--5">{"".join(card(p, " av-tcard--founder" if p["f"] else "") for p in PROFS)}</div>
</div></section>

<section class="av-section av-section--soft"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Como é estudar na {ORG}</h2>
  <div class="av-prose av-reveal"><p>O curso <strong>{CURSO}</strong> tem aulas ao vivo, feedback individual do professor que passou a atividade, comunidade de escritores e palestras com profissionais do mercado editorial. Cada módulo dura 6 meses e o certificado de extensão universitária é emitido pela Anhanguera.</p>
  <p>As matrículas abrem em janeiro de 2027. <a href="{SITE}/novo-sobre/">Conheça a história da escola</a> ou <a href="{FORM}">entre na lista de espera</a>.</p></div>
  <p class="av-updated">Página atualizada em {UPDATED_TXT}</p>
</div></section>
</main>
{FOOTER}
{jsonld(ld)}'''

PV_CSS = ".pv-slot{border:2px dashed #CC351C;border-radius:16px;padding:18px 22px;color:#A82B16;background:rgba(204,53,28,.05);font:600 13px/1.5 Montserrat,sans-serif;max-width:760px}"
css_base = open(os.path.join(ROOT, "wordpress/aldeia-vendas.css"), encoding="utf-8").read()
js = open(os.path.join(ROOT, "wordpress/aldeia-vendas.js"), encoding="utf-8").read()

def local(s):  # na prévia, os links entre as páginas abrem os arquivos locais
    for p in PROFS: s = s.replace(url(p), f"professor-{p['slug']}.html")
    return s.replace(SITE + "/professores/", "professores.html").replace(SITE + "/novo-sobre/", "sobre.html").replace(f'href="{SITE}/"', 'href="vendas.html"')

def preview(title, body, name):
    doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><link rel="stylesheet" href="assets/fonts.css">
<style>body{{margin:0}}{css_base}:root{{--av-hero-img:url("assets/hero.jpg");--av-hero-img-m:url("assets/img/hero-mobile.jpg");--av-medal:url("assets/logo-medalhao.png")}}{PV_CSS}</style></head><body class="av-page" id="top">{local(body)}<script>{js}</script></body></html>'''
    open(os.path.join(ROOT, "preview", name), "w", encoding="utf-8").write(doc)

pages = [(f"{p['nome']} · professor{'a' if art(p)=='a' else ''} da {ORG}", page_prof(p), f"professor-{p['slug']}.html", p) for p in PROFS]
pages.append((f"Professores da {ORG}", page_hub(), "professores.html", None))
for t, b, n, _ in pages: preview(t, b, n)
print("prévias:", len(pages))

if WP:
    out = os.path.join(ROOT, "wordpress/professores"); os.makedirs(out, exist_ok=True)
    inline_css = build_plugin.build_css().replace("../fonts/", PLUGIN_BASE + "fonts/").replace("../img/", PLUGIN_BASE + "img/")
    fix = ('<style>.e-con:has(>.elementor-widget-html .av-page){--padding-top:0px;--padding-right:0px;--padding-bottom:0px;--padding-left:0px;--gap:0px;--row-gap:0px;--column-gap:0px;--margin-top:0px;--margin-bottom:0px}'
           '.elementor-widget-html:has(>.av-page),.elementor-widget-html:has(.av-page){margin:0}</style>\n')
    zero = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
    for t, b, n, p in pages:
        slug = p["slug"] if p else "lista"
        frag_body = b.replace('src="assets/img/', 'src="' + PLUGIN_BASE + 'img/')
        assert 'src="assets/' not in frag_body and "pv-slot" not in frag_body
        frag = (f'<!-- aldeia-professor-{slug}-v1 -->\n<style>{inline_css}</style>\n{fix}<div class="av-page">\n{frag_body}\n</div>\n<script>{js}</script>\n')
        open(os.path.join(out, f"{slug}-colar-no-widget-html.html"), "w", encoding="utf-8").write(frag)
        tpl = {"version": "0.4", "title": f"ALDEIA Professor — {p['nome'] if p else 'Lista'}", "type": "page",
               "content": [{"id": "b1c2d3e", "elType": "container", "isInner": False,
                            "settings": {"content_width": "full", "flex_direction": "column", "padding": zero, "margin": zero},
                            "elements": [{"id": "f4a5b6c", "elType": "widget", "widgetType": "html", "settings": {"html": frag}, "elements": []}]}],
               "page_settings": {"hide_title": "yes"}}
        json.dump(tpl, open(os.path.join(out, f"{slug}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wordpress/professores/: ok")
