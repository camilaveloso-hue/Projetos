#!/usr/bin/env python3
"""Gera o modelo do Elementor da página do AULÃO UNIVERSAL e atualiza o plugin.

Uso:  python3 tools/aulao-universal/build_wp.py [--checkout https://link] [--pos-promocao]
Saídas:
  wordpress/entrega/aulao-universal-v1.json                       modelo para importar no Elementor
  wordpress/entrega/aulao-universal-v1-colar-no-widget-html.html  plano B: colar num widget HTML
  wordpress/entrega/aldeia-vendas.zip                             plugin 1.4.0 (fotos e fontes do aulão em assets/aulao/)
A página é um único widget HTML (CSS e JS embutidos), como as outras páginas do site."""
import json, os, re, shutil, subprocess, sys, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
import build_aulao as B

VERSION = "v2"
POS = "--pos-promocao" in sys.argv     # versão para depois de 30/11: R$ 100, sem promoção, bônus nem contagem
B.POS = POS
SUF = "-pos-promocao" if POS else ""
PLUGIN_BASE = B.SITE + "/wp-content/plugins/aldeia-vendas/assets/aulao/"

if "--checkout" in sys.argv:
    B.CHECKOUT = sys.argv[sys.argv.index("--checkout") + 1]

# 1) corpo da página, com fotos apontando para o plugin
body = B.page()
imgs = sorted(set(re.findall(r"\{IMG:([^}]+)\}", body)))
body = re.sub(r"\{IMG:([^}]+)\}", lambda m: PLUGIN_BASE + "img/" + m.group(1), body)
assert "{IMG:" not in body

# 2) CSS com fontes do plugin e relevo de montanhas
css = open(os.path.join(HERE, "aulao.css"), encoding="utf-8").read().replace("{MTN_LIGHT}", B.MTN_LIGHT).replace("{MTN_DARK}", B.MTN_DARK)
fonts = ""
used_fonts = []
for fam, slug, w, st in B.FONTS:
    f = f"{slug}-latin-{w}-{st}.woff2"
    used_fonts.append(f)
    fonts += f'@font-face{{font-family:"{fam}";font-weight:{w};font-style:{st};font-display:swap;src:url({PLUGIN_BASE}fonts/{f}) format("woff2")}}\n'
js = open(os.path.join(HERE, "aulao.js"), encoding="utf-8").read()

# o Elementor põe espaçamento em volta do widget: zera só nesta página
fix = ('.e-con:has(>.elementor-widget-html .am-root){--padding-top:0px;--padding-right:0px;--padding-bottom:0px;--padding-left:0px;--gap:0px;--row-gap:0px;--column-gap:0px;--margin-top:0px;--margin-bottom:0px}'
       '.am-root{background:#fdfaec;color:#09090a}'
       '.elementor-widget-html:has(.am-root){margin:0}.elementor-widget-html:has(.am-root)>.elementor-widget-container{margin:0;padding:0}')
fragment = (f'<!-- aulao-universal-{VERSION} · AULÃO UNIVERSAL em um único widget HTML (CSS e JS embutidos). Fotos e fontes vêm do plugin "Aldeia Literária — Página de vendas" 1.4.0. -->\n'
            f'<style>\n{fonts}{css}\n{fix}</style>\n<div class="am-root">\n{body}\n</div>\n<script>\n{js}</script>\n')

# 3) arquivos de saída
ent = os.path.join(ROOT, "wordpress", "entrega")
os.makedirs(ent, exist_ok=True)
open(os.path.join(ent, f"aulao-universal-{VERSION}{SUF}-colar-no-widget-html.html"), "w", encoding="utf-8").write(fragment)
zero = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
tpl = {"version": "0.4", "title": f"ALDEIA Aulão Universal {VERSION}{' (pós-promoção, R$ 100)' if POS else ' (Black Friday)'}", "type": "page",
       "content": [{"id": "a1b2c3d", "elType": "container", "isInner": False,
                    "settings": {"content_width": "full", "flex_direction": "column", "padding": zero, "margin": zero},
                    "elements": [{"id": "e4f5a6b", "elType": "widget", "widgetType": "html", "settings": {"html": fragment}, "elements": []}]}],
       "page_settings": {"hide_title": "yes"}}
json.dump(tpl, open(os.path.join(ent, f"aulao-universal-{VERSION}{SUF}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# 4) fotos e fontes no plugin
assets = os.path.join(ROOT, "wordpress", "aulao-assets")
shutil.rmtree(assets, ignore_errors=True)
os.makedirs(os.path.join(assets, "img")); os.makedirs(os.path.join(assets, "fonts"))
for f in imgs:
    shutil.copy(os.path.join(B.IMGDIR, f), os.path.join(assets, "img", f))
for f in used_fonts:
    shutil.copy(os.path.join(B.FONTDIR, f), os.path.join(assets, "fonts", f))
subprocess.run([sys.executable, os.path.join(ROOT, "tools", "build_plugin.py")], check=True)
print("ok:", len(fragment) // 1024, "KB; fotos:", len(imgs), "; checkout:", B.CHECKOUT, "; versão:", "pós-promoção" if POS else "Black Friday")
