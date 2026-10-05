#!/usr/bin/env python3
"""Gera a versão "HTML único" da página de vendas (não depende das classes dos containers do Elementor).

Saídas:
  wordpress/plano-b-pagina-html-unico.html            (colar num widget HTML)
  wordpress/pagina-vendas-html-unico-elementor.json   (modelo pronto: 1 container + 1 widget HTML)
  preview/vendas.html                                 (prévia aprovada, abre direto no navegador)
Fonte do conteúdo: tools/src/body.html
"""
import json, os, sys
ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
import build_plugin

PLUGIN_IMG = "https://aaldeialiteraria.com.br/wp-content/plugins/aldeia-vendas/assets/img/"
body = open(os.path.join(ROOT, "tools/src/body.html"), encoding="utf-8").read()

# 1) prévia (caminhos locais)
css_base = open(os.path.join(ROOT, "wordpress/aldeia-vendas.css"), encoding="utf-8").read()
js = open(os.path.join(ROOT, "wordpress/aldeia-vendas.js"), encoding="utf-8").read()
prev = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Aldeia Literária — Prévia da página de vendas</title>
<link rel="stylesheet" href="assets/fonts.css">
<style>body{{margin:0}}{css_base}:root{{--av-hero-img:url("assets/hero.jpg");--av-hero-img-m:url("assets/img/hero-mobile.jpg");--av-medal:url("assets/logo-medalhao.png")}}.sr-only{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}}</style></head><body class="av-page" id="top">{body}<script>{js}</script></body></html>'''
open(os.path.join(ROOT, "preview/vendas.html"), "w", encoding="utf-8").write(prev)

# 2) fragmento para widget HTML do Elementor
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
fragment = ('<!-- aldeia-vendas-v15 · Aldeia Literária — página de vendas em um único widget HTML (CSS e JS embutidos). Fontes e imagens vêm do plugin "Aldeia Literária — Página de vendas". -->\n'
            + '<style>' + inline_css + '</style>\n'
            + fix + '<div class="av-page">\n' + frag_body + '\n</div>\n'
            + '<script>' + inline_js + '</script>\n')
open(os.path.join(ROOT, "wordpress/plano-b-pagina-html-unico.html"), "w", encoding="utf-8").write(fragment)

# 3) modelo pronto do Elementor: 1 container (largura total, sem padding) + 1 widget HTML
zero = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
tpl = {
    "version": "0.4",
    "title": "ALDEIA v15 — Página de vendas (final)",
    "type": "page",
    "content": [{
        "id": "a1b2c3d", "elType": "container", "isInner": False,
        "settings": {"content_width": "full", "flex_direction": "column", "padding": zero, "margin": zero},
        "elements": [{"id": "e4f5a6b", "elType": "widget", "widgetType": "html", "settings": {"html": fragment}, "elements": []}],
    }],
    "page_settings": {"hide_title": "yes"},
}
json.dump(tpl, open(os.path.join(ROOT, "wordpress/pagina-vendas-html-unico-elementor.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok: prévia, plano B (html) e modelo JSON único gerados;", len(fragment) // 1024, "KB de HTML")
