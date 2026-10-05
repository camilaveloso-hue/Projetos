#!/usr/bin/env python3
"""Gera a página SOBRE (HTML único, mesmo sistema visual da página de vendas).

Saídas:
  preview/sobre.html                                   (prévia no navegador)
  wordpress/aldeia-sobre-v1.json                       (modelo do Elementor: 1 container + 1 widget HTML)
  wordpress/aldeia-sobre-v1-colar-no-widget-html.html  (para colar num widget HTML)
Fonte: tools/src/sobre.html  |  CSS/JS: os mesmos da página de vendas
"""
import json, os, sys
ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
import build_plugin

VERSION = "v4"
PLUGIN_BASE = "https://aaldeialiteraria.com.br/wp-content/plugins/aldeia-vendas/assets/"
body = open(os.path.join(ROOT, "tools/src/sobre.html"), encoding="utf-8").read()
css_base = open(os.path.join(ROOT, "wordpress/aldeia-vendas.css"), encoding="utf-8").read()
js = open(os.path.join(ROOT, "wordpress/aldeia-vendas.js"), encoding="utf-8").read()

prev = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Aldeia Literária — Prévia da página Sobre</title>
<link rel="stylesheet" href="assets/fonts.css">
<style>body{{margin:0}}{css_base}:root{{--av-hero-img:url("assets/hero.jpg");--av-hero-img-m:url("assets/img/hero-mobile.jpg");--av-medal:url("assets/logo-medalhao.png");--av-sobre-banner:url("assets/img/sobre-banner.jpg")}}.sr-only{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}}</style></head><body class="av-page" id="top">{body}<script>{js}</script></body></html>'''
open(os.path.join(ROOT, "preview/sobre.html"), "w", encoding="utf-8").write(prev)

frag_body = body.replace('src="assets/img/', 'src="' + PLUGIN_BASE + 'img/')
assert 'src="assets/' not in frag_body
fix = ('<style>.e-con:has(>.elementor-widget-html .av-page){--padding-top:0px;--padding-right:0px;--padding-bottom:0px;--padding-left:0px;'
       '--gap:0px;--row-gap:0px;--column-gap:0px;--margin-top:0px;--margin-bottom:0px}'
       '.elementor-widget-html:has(>.av-page),.elementor-widget-html:has(.av-page){margin:0}</style>\n')
inline_css = build_plugin.build_css().replace("../fonts/", PLUGIN_BASE + "fonts/").replace("../img/", PLUGIN_BASE + "img/")
fragment = ('<!-- aldeia-sobre-v4 · Aldeia Literária — página SOBRE em um único widget HTML (CSS e JS embutidos). Fontes e imagens vêm do plugin "Aldeia Literária — Página de vendas". -->\n'
            + '<style>' + inline_css + '</style>\n' + fix + '<div class="av-page">\n' + frag_body + '\n</div>\n'
            + '<script>' + js + '</script>\n')
open(os.path.join(ROOT, f"wordpress/aldeia-sobre-{VERSION}-colar-no-widget-html.html"), "w", encoding="utf-8").write(fragment)

zero = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
tpl = {"version": "0.4", "title": f"ALDEIA Sobre {VERSION} — Página Sobre", "type": "page",
       "content": [{"id": "b1c2d3e", "elType": "container", "isInner": False,
                    "settings": {"content_width": "full", "flex_direction": "column", "padding": zero, "margin": zero},
                    "elements": [{"id": "f4a5b6c", "elType": "widget", "widgetType": "html", "settings": {"html": fragment}, "elements": []}]}],
       "page_settings": {"hide_title": "yes"}}
json.dump(tpl, open(os.path.join(ROOT, f"wordpress/aldeia-sobre-{VERSION}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok: sobre — prévia, modelo e arquivo para colar;", len(fragment) // 1024, "KB")
