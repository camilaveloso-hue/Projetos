#!/usr/bin/env python3
"""Simula, no navegador, como o Elementor 4.x (CSS real do site + tema Hello) renderiza o JSON gerado.
Só para conferência visual: gera preview/_elementor-sim.html."""
import html, json, os, re, sys
ROOT = os.path.join(os.path.dirname(__file__), "..")
ELC = "/tmp/claude-0/elc"   # CSS do Elementor baixado do site

data = json.load(open(os.path.join(ROOT, "wordpress", "pagina-vendas-elementor.json"), encoding="utf-8"))
first_tab = {}

def esc(s): return html.escape(s, quote=True)

def render(el, parent_is_page=True, depth=0):
    t = el["elType"]; s = el["settings"]; cls = s.get("css_classes", "") if el["elType"] == "container" else s.get("_css_classes", ""); i = el["id"]
    if t == "container":
        style = ""
        if s.get("flex_direction") == "row": style = ' style="--flex-direction:row"'
        if s.get("flex_direction_mobile") == "column": cls += " sim-mobile-col"
        kind = "e-parent" if depth == 0 else "e-child"
        inner = "".join(render(c, False, depth + 1) for c in el["elements"])
        return f'<div class="elementor-element elementor-element-{i} e-con-full e-flex e-con {kind} {cls}" data-id="{i}" data-element_type="container"{style}>{inner}</div>'
    w = el["widgetType"]; base = f'elementor-element elementor-element-{i} elementor-widget elementor-widget-{w} {"elementor-tabs-view-vertical" if w=="tabs" else ""} {cls}'
    if w == "heading":
        tag = s.get("header_size", "h2"); title = s["title"]
        if s.get("link"): title = f'<a href="{esc(s["link"]["url"])}">{title}</a>'
        return f'<div class="{base}" data-id="{i}" data-element_type="widget" data-widget_type="heading.default"><{tag} class="elementor-heading-title elementor-size-default">{title}</{tag}></div>'
    if w == "text-editor":
        return f'<div class="{base}" data-id="{i}" data-element_type="widget" data-widget_type="text-editor.default">{s["editor"]}</div>'
    if w == "button":
        return (f'<div class="{base}" data-id="{i}" data-element_type="widget" data-widget_type="button.default"><a class="elementor-button elementor-button-link elementor-size-sm" href="{esc(s["link"]["url"])}">'
                f'<span class="elementor-button-content-wrapper"><span class="elementor-button-text">{s["text"]}</span></span></a></div>')
    if w == "image":
        im = s["image"]; u = im["url"]
        if u.startswith("http") and "/plugins/aldeia-vendas/assets/img/" in u:
            u = "assets/img/" + u.rsplit("/", 1)[1]
        return f'<div class="{base}" data-id="{i}" data-element_type="widget" data-widget_type="image.default"><img loading="lazy" src="{esc(u)}" alt="{esc(im.get("alt",""))}" class="attachment-full size-full"></div>'
    if w == "counter":
        return (f'<div class="{base}" data-id="{i}" data-element_type="widget" data-widget_type="counter.default"><div class="elementor-counter"><div class="elementor-counter-number-wrapper">'
                f'<span class="elementor-counter-number-prefix">{s["prefix"]}</span><span class="elementor-counter-number" data-duration="1800" data-to-value="{s["ending_number"]}" data-from-value="0">{s["ending_number"]}</span>'
                f'<span class="elementor-counter-number-suffix">{s["suffix"]}</span></div><div class="elementor-counter-title">{s["title"]}</div></div></div>')
    if w == "tabs":
        tabs = s["tabs"]; titles = ""; contents = ""
        for n, tb in enumerate(tabs, 1):
            act = " elementor-active" if n == 1 else ""
            titles += f'<div id="elementor-tab-title-{n}" class="elementor-tab-title elementor-tab-desktop-title{act}" data-tab="{n}" role="tab"><a href="">{tb["tab_title"]}</a></div>'
            contents += (f'<div class="elementor-tab-title elementor-tab-mobile-title{act}" data-tab="{n}" role="tab">{tb["tab_title"]}</div>'
                         f'<div id="elementor-tab-content-{n}" class="elementor-tab-content elementor-clearfix{act}" data-tab="{n}" role="tabpanel"{"" if n==1 else " hidden"} style="display:{"block" if n==1 else "none"}">{tb["tab_content"]}</div>')
        return (f'<div class="{base}" data-id="{i}" data-element_type="widget" data-widget_type="tabs.default"><div class="elementor-tabs"><div class="elementor-tabs-wrapper" role="tablist">{titles}</div>'
                f'<div class="elementor-tabs-content-wrapper" role="tablist">{contents}</div></div></div>')
    if w == "accordion":
        items = ""
        for n, tb in enumerate(s["tabs"], 1):
            op = n == 1
            items += (f'<div class="elementor-accordion-item"><h3 id="elementor-tab-title-{n}" class="elementor-tab-title{" elementor-active" if op else ""}" data-tab="{n}" role="button" aria-expanded="{str(op).lower()}">'
                      f'<span class="elementor-accordion-icon elementor-accordion-icon-right" aria-hidden="true"><span class="elementor-accordion-icon-closed"><svg class="e-font-icon-svg e-fas-plus" viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg"><path d="M416 208H272V64c0-17.67-14.33-32-32-32h-32c-17.67 0-32 14.33-32 32v144H32c-17.67 0-32 14.33-32 32v32c0 17.67 14.33 32 32 32h144v144c0 17.67 14.33 32 32 32h32c17.67 0 32-14.33 32-32V304h144c17.67 0 32-14.33 32-32v-32c0-17.67-14.33-32-32-32z"></path></svg></span>'
                      f'<span class="elementor-accordion-icon-opened"><svg class="e-font-icon-svg e-fas-minus" viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg"><path d="M416 208H32c-17.67 0-32 14.33-32 32v32c0 17.67 14.33 32 32 32h384c17.67 0 32-14.33 32-32v-32c0-17.67-14.33-32-32-32z"></path></svg></span></span>'
                      f'<a class="elementor-accordion-title" tabindex="0">{tb["tab_title"]}</a></h3>'
                      f'<div id="elementor-tab-content-{n}" class="elementor-tab-content elementor-clearfix{" elementor-active" if op else ""}" data-tab="{n}" role="region" style="display:{"block" if op else "none"}">{tb["tab_content"]}</div></div>')
        return f'<div class="{base}" data-id="{i}" data-element_type="widget" data-widget_type="accordion.default"><div class="elementor-accordion">{items}</div></div>'
    if w == "html":
        return f'<div class="{base}" data-id="{i}" data-element_type="widget" data-widget_type="html.default">{s["html"]}</div>'
    raise SystemExit("widget não suportado no simulador: " + w)

def rd(p): return open(os.path.join(ELC, p), encoding="utf-8").read()
elementor_css = rd("frontend.min.css")
widgets_css = "\n".join(rd(f) for f in ["widget-heading.min.css", "widget-text-editor.min.css", "widget-image.min.css", "widget-counter.min.css", "widget-tabs.min.css", "widget-accordion.min.css"])
hello = """body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;font-size:1rem;font-weight:400;line-height:1.5;color:#333;background-color:#fff;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4,h5,h6{margin-block-start:.5rem;margin-block-end:1rem;font-family:inherit;font-weight:500;line-height:1.2;color:inherit}
h1{font-size:2.5rem}h2{font-size:2rem}h3{font-size:1.75rem}h4{font-size:1.5rem}h5{font-size:1.25rem}h6{font-size:1rem}
p{margin-block-start:0;margin-block-end:.9rem}a{background-color:transparent;text-decoration:none;color:#c36}a:active,a:hover{color:#336}
img{border-style:none;height:auto;max-width:100%}ul,ol{margin-block:0 1rem}
button,[type=button]{font-family:inherit;border-radius:3px;display:inline-block;font-weight:400;color:#c36;text-align:center;border:1px solid #c36;padding:.5rem 1rem;font-size:1rem}
table{width:100%;margin-block-end:15px;font-size:.9em;background-color:transparent;border-collapse:collapse}table td,table th{padding:15px;line-height:1.5;vertical-align:top;border:1px solid hsla(0,0%,50%,.5019607843)}
table thead th{background-color:hsla(0,0%,50%,.0705882353)}table tbody>tr:nth-child(odd)>td,table tbody>tr:nth-child(odd)>th{background-color:hsla(0,0%,50%,.0705882353)}
"""
sys.path.insert(0, os.path.dirname(__file__))
import build_plugin
mine = build_plugin.build_css(for_sim=True)
body = "".join(render(c) for c in data["content"])
page = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Simulação Elementor</title>
<link rel="stylesheet" href="assets/fonts.css"><style>{hello}</style><style>{elementor_css}</style><style>{rd("kit.css")}</style>
<style>{mine}@media(max-width:767px){{.sim-mobile-col{{--flex-direction:column!important}}}}</style><style>{widgets_css}</style></head>
<body class="elementor-kit-6 page-template-default"><div data-elementor-type="wp-page" data-elementor-id="40" class="elementor elementor-40">{body}</div>
<script src="../wordpress/aldeia-vendas.js"></script></body></html>'''
open(os.path.join(ROOT, "preview", "_elementor-sim.html"), "w", encoding="utf-8").write(page)
print("ok -> preview/_elementor-sim.html")
