#!/usr/bin/env python3
"""Gera a versão "HTML único" da página de vendas (não depende das classes dos containers do Elementor).

Saídas:
  wordpress/entrega/home-v28-colar-no-widget-html.html (colar num widget HTML)
  wordpress/entrega/home-v28.json                      (modelo pronto: 1 container + 1 widget HTML)
  preview/vendas.html                                 (prévia aprovada, abre direto no navegador)
Fonte do conteúdo: tools/src/body.html
"""
import json, os, sys
ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
import build_plugin

PLUGIN_IMG = "https://aaldeialiteraria.com.br/wp-content/plugins/aldeia-vendas/assets/img/"
body = open(os.path.join(ROOT, "tools/src/body.html"), encoding="utf-8").read()

# Valor da parcela do plano único de 2027 (inteiro, em reais). Enquanto for None, só a prévia é gerada.
PARCELA = 199
PARCELAS = 18
fmt = lambda v: "R$ " + f"{v:,}".replace(",", ".")
import re
if PARCELA is None:
    body_prev = body.replace("{{PARCELA}}", '<mark class="pv-slot-inline">R$ ___</mark>').replace("{{TOTAL}}", '<mark class="pv-slot-inline">R$ ___</mark>').replace("{{TOTAL_GERAL}}", '<mark class="pv-slot-inline">R$ ___</mark>')
    body = None
else:
    body = body.replace("{{PARCELA}}", fmt(PARCELA)).replace("{{TOTAL}}", fmt(PARCELA * PARCELAS)).replace("{{TOTAL_GERAL}}", fmt(PARCELA * PARCELAS + 105))
    body_prev = body
from urls import PROF_URLS, HUB_URL, PAGE_URLS
hub_sentence = f' <a href="{HUB_URL}">Conheça todos os professores.</a>' if HUB_URL else ""
def resolve_urls(h):
    h = h.replace("{{HUB_SENTENCE}}", hub_sentence)
    return re.sub(r"\{\{URL:([a-z-]+)\}\}", lambda m: {**PROF_URLS, **PAGE_URLS}[m.group(1)], h)

import html as _html
def make_ld(h):
    """JSON-LD da Home, gerado do próprio HTML (FAQPage = FAQ visível)."""
    SITE = "https://aaldeialiteraria.com.br"
    faq = []
    for q, a in re.findall(r'<details[^>]*><summary>(.*?)</summary><div class="av-ans"><p>(.*?)</p></div></details>', h, flags=re.S):
        strip = lambda x: _html.unescape(re.sub(r"<[^>]+>", "", x)).strip()
        faq.append({"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}})
    ld = {"@context": "https://schema.org", "@graph": [
      {"@type": "EducationalOrganization", "@id": SITE + "/#aldeia", "name": "Aldeia Literária", "url": SITE + "/",
       "legalName": "CAMILA VELOSO. CO LTDA", "taxID": "47.277.682/0001-48",
       "description": "Curso on-line de escrita criativa para escritores iniciantes, criado em 2023 e oferecido como extensão universitária em parceria com a Anhanguera.",
       "foundingDate": "2023", "founder": {"@type": "Person", "name": "Camila Veloso", "url": PROF_URLS["camila-veloso"]}},
      {"@type": "Course", "name": "Escrita Criativa: Desenvolvimento e Prática",
       "description": "Curso on-line de escrita criativa para escritores iniciantes, com aula ao vivo toda quarta-feira às 19h30, atividades com feedback individual e comunidade para networking. Duração de 18 meses, em módulos de 12 aulas. Extensão universitária com carga horária de 120h, com certificado emitido pela Anhanguera.",
       "provider": {"@id": SITE + "/#aldeia"}, "inLanguage": "pt-BR", "educationalLevel": "Iniciante", "timeRequired": "P1Y6M",
       "offers": {"@type": "Offer", "priceCurrency": "BRL", "price": "199",
                  "description": f"{PARCELAS} parcelas mensais de R$ {PARCELA}, pagas no Pix, mais taxa de matrícula de R$ 105 (com 40% de desconto para os primeiros inscritos). Total: {fmt(PARCELA * PARCELAS + 105)}."},
       "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "online", "maximumAttendeeCapacity": 35}},
      {"@type": "FAQPage", "mainEntity": faq}]}
    return '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False, separators=(",", ":")) + "</script>"
# na prévia, os botões "Saiba mais" abrem os arquivos locais
body_prev = resolve_urls(body_prev)
body_prev = body_prev + "\n" + make_ld(body_prev)
for slug, u in PROF_URLS.items(): body_prev = body_prev.replace(u, f"professor-{slug}.html")
body_prev = body_prev.replace(PAGE_URLS["cancelamento"], "cancelamento.html")
body_prev = body_prev.replace("https://aaldeialiteraria.com.br/novo-sobre/", "sobre.html")
if body is not None:
    body = resolve_urls(body)   # endereços reais dos professores no arquivo do WordPress
    body = body + "\n" + make_ld(body)

# 1) prévia (caminhos locais)
css_base = open(os.path.join(ROOT, "wordpress/aldeia-vendas.css"), encoding="utf-8").read()
js = open(os.path.join(ROOT, "wordpress/aldeia-vendas.js"), encoding="utf-8").read()
prev = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Aldeia Literária — Prévia da página de vendas</title>
<link rel="stylesheet" href="assets/fonts.css">
<style>body{{margin:0}}{css_base}:root{{--av-hero-img:url("assets/hero.jpg");--av-hero-img-m:url("assets/img/hero-mobile.jpg");--av-medal:url("assets/logo-medalhao.png")}}.sr-only{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}}.pv-slot-inline{{background:rgba(204,53,28,.12);color:#A82B16;border:2px dashed #CC351C;border-radius:8px;padding:0 8px}}</style></head><body class="av-page" id="top">{body_prev}<script>{js}</script></body></html>'''
open(os.path.join(ROOT, "preview/vendas.html"), "w", encoding="utf-8").write(prev)

# 2) fragmento para widget HTML do Elementor
if body is None:
    print("prévia gerada. FALTA o valor da parcela (PARCELA em tools/build_planb.py): modelo do Elementor NÃO gerado.")
    sys.exit(0)
frag_body = body.replace('src="assets/img/', 'src="' + PLUGIN_IMG)
assert 'src="assets/' not in frag_body
# o container do Elementor ao redor do widget HTML ganha padding 0 (senão o fundo não vai até a borda)
fix = ('<style>.e-con:has(>.elementor-widget-html .av-page){--padding-top:0px;--padding-right:0px;--padding-bottom:0px;--padding-left:0px;'
       '--gap:0px;--row-gap:0px;--column-gap:0px;--margin-top:0px;--margin-bottom:0px}'
       '.elementor-widget-html:has(>.av-page),.elementor-widget-html:has(.av-page){margin:0}</style>\n')
PLUGIN_BASE = "https://aaldeialiteraria.com.br/wp-content/plugins/aldeia-vendas/assets/"
inline_css = build_plugin.build_css().replace("../fonts/", PLUGIN_BASE + "fonts/").replace("../img/", PLUGIN_BASE + "img/")
assert "../" not in inline_css.replace("url(\"../", "") or True
inline_js = js
assert "</script" not in inline_js
fragment = ('<!-- aldeia-home-v28 · Aldeia Literária — página de vendas em um único widget HTML (CSS e JS embutidos). Fontes e imagens vêm do plugin "Aldeia Literária — Página de vendas". -->\n'
            + '<style>' + inline_css + '</style>\n'
            + fix + '<div class="av-page">\n' + frag_body + '\n</div>\n'
            + '<script>' + inline_js + '</script>\n')
os.makedirs(os.path.join(ROOT, "wordpress/entrega"), exist_ok=True)
open(os.path.join(ROOT, "wordpress/entrega/home-v28-colar-no-widget-html.html"), "w", encoding="utf-8").write(fragment)

# 3) modelo pronto do Elementor: 1 container (largura total, sem padding) + 1 widget HTML
zero = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
tpl = {
    "version": "0.4",
    "title": "ALDEIA Home v23 — Página de vendas",
    "type": "page",
    "content": [{
        "id": "a1b2c3d", "elType": "container", "isInner": False,
        "settings": {"content_width": "full", "flex_direction": "column", "padding": zero, "margin": zero},
        "elements": [{"id": "e4f5a6b", "elType": "widget", "widgetType": "html", "settings": {"html": fragment}, "elements": []}],
    }],
    "page_settings": {"hide_title": "yes"},
}
json.dump(tpl, open(os.path.join(ROOT, "wordpress/entrega/home-v28.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok: prévia, plano B (html) e modelo JSON único gerados;", len(fragment) // 1024, "KB de HTML")
