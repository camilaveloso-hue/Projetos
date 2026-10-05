#!/usr/bin/env python3
"""Monta o plugin do WordPress (pasta + .zip) a partir dos arquivos-fonte.

CSS final = fontes locais + reset do Elementor + CSS base (prévia) + componentes do Elementor
"""
import os, re, shutil, zipfile
ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "wordpress", "aldeia-vendas")          # pasta do plugin
ZIP = os.path.join(ROOT, "wordpress", "aldeia-vendas.zip")
rd = lambda p: open(os.path.join(ROOT, p), encoding="utf-8").read()

def fonts_css():
    out = []
    for line in rd("preview/assets/fonts.css").splitlines():
        out.append(line.replace("url(fonts/", 'url("../fonts/').replace(".woff2)", '.woff2")'))
    return "\n".join(out)

def base_css():
    s = rd("wordpress/aldeia-vendas.css")
    s = s.replace('url("https://aaldeialiteraria.com.br/wp-content/uploads/2026/09/Encerramento-scaled.png")', 'url("../img/hero.jpg")')
    s = s.replace('url("https://aaldeialiteraria.com.br/wp-content/uploads/2026/07/LOGO_DUO-1-300x300.png")', 'url("../img/logo-medalhao.png")')
    assert "../img/hero.jpg" in s and "../img/logo-medalhao.png" in s
    return s

def build_css(for_sim=False):
    css = "/* Aldeia Literária — Página de vendas (plugin) — gerado por tools/build_plugin.py */\n"
    css += "/* ===== Fontes locais ===== */\n" + fonts_css() + "\n"
    css += rd("tools/css/reset.css") + "\n" + base_css() + "\n" + rd("tools/css/components.css")
    if for_sim:
        css = css.replace("https://aaldeialiteraria.com.br/wp-content/plugins/aldeia-vendas/assets/", "assets/").replace("../fonts/", "assets/fonts/").replace("../img/hero.jpg", "assets/hero.jpg").replace("../img/logo-medalhao.png", "assets/logo-medalhao.png")
    return css

if __name__ == "__main__":
    shutil.rmtree(OUT, ignore_errors=True)
    for d in ("assets/css", "assets/js", "assets/img", "assets/fonts"):
        os.makedirs(os.path.join(OUT, d))
    open(os.path.join(OUT, "assets/css/aldeia-vendas.css"), "w", encoding="utf-8").write(build_css())
    shutil.copy(os.path.join(ROOT, "wordpress/aldeia-vendas.js"), os.path.join(OUT, "assets/js/aldeia-vendas.js"))
    A = os.path.join(ROOT, "preview/assets")
    for f in os.listdir(os.path.join(A, "fonts")):
        shutil.copy(os.path.join(A, "fonts", f), os.path.join(OUT, "assets/fonts", f))
    for f in os.listdir(os.path.join(A, "img")):
        shutil.copy(os.path.join(A, "img", f), os.path.join(OUT, "assets/img", f))
    shutil.copy(os.path.join(A, "hero.jpg"), os.path.join(OUT, "assets/img/hero.jpg"))
    shutil.copy(os.path.join(A, "logo-medalhao.png"), os.path.join(OUT, "assets/img/logo-medalhao.png"))
    shutil.copy(os.path.join(ROOT, "tools/aldeia-vendas.php"), os.path.join(OUT, "aldeia-vendas.php"))
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for base, _, files in os.walk(OUT):
            for f in files:
                p = os.path.join(base, f)
                z.write(p, os.path.join("aldeia-vendas", os.path.relpath(p, OUT)))
    print("ok ->", os.path.relpath(OUT, ROOT), "e", os.path.relpath(ZIP, ROOT))
