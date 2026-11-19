#!/usr/bin/env python3
"""Checklist do Aulão (material de apoio) na identidade visual dos slides do Aulão Universal.
Uso: python3 tools/checklist/build_checklist.py
Saídas: materiais/checklist-aulao-universal.pdf (A4) e tools/checklist/checklist.html
Texto: o material original da Camila ("Checklist.Aulão.da.Cami"), com a numeração corrigida (1 a 9) e erros de digitação ajustados."""
import html, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
FONTS = os.path.join(ROOT, "preview", "aulao", "fonts")
LOGO = os.path.join(ROOT, "site-camila-veloso", "assets", "img", "logo-horizontal.png")
LOGO_NEG = os.path.join(ROOT, "site-camila-veloso", "assets", "img", "logo-horizontal-negativo.png")
E = html.escape

# fase, cor da fase (como no slide "9 passos para você chegar ao final da história"), passos
PHASES = [
 ("Início", "lilac", [
  (1, "Capítulo de ambientação do personagem", [
   "O objetivo deste capítulo é mostrar seu personagem no ponto A da história. É um capítulo de ambientação. Aqui, mostre a rotina do seu personagem principal e como é um dia comum na vida dele. Pode colocar alguns personagens coadjuvantes também e qual a relação deles com o personagem principal.",
   "No final deste capítulo, você já pode mostrar qual é o problema central da narrativa. Assim cria um gancho para o próximo capítulo (e deixa seu leitor curioso)."]),
  (2, "Capítulo que mostra o problema central", [
   "O objetivo deste capítulo é mostrar o conflito/problema que vai mover a narrativa, que vai forçar os personagens a saírem do ponto A. Deixe isso claro para o leitor. Aqui você também pode mostrar com mais profundidade alguns dos personagens coadjuvantes mais importantes.",
   "Explique com mais detalhes qual é o problema central da história e como o seu personagem principal lida com ele. Ele tem medo, ansiedade, quer fugir?"])]),
 ("Primeiro limiar", "lilac", [
  (3, "Capítulo que mostra o personagem se negando a resolver o problema", [
   "Como acontece na nossa vida, antes de resolver um problema a gente foge dele. Então explore isso. O objetivo deste capítulo é mostrar a primeira reação do seu personagem frente ao conflito principal, realçando quem ele é no ponto A da história.",
   "Seu personagem começa a história sendo forte ou fraco? Corajoso ou medroso? Mostre!",
   "Coloque seu personagem tentando fugir da batalha, encontro, conversa difícil com os pais (a fuga depende muito do problema)."]),
  (4, "Capítulo em que o personagem é obrigado a resolver o problema", [
   "Depois de tentar fugir, o personagem cai em si e percebe que precisa resolver o problema, ir para o encontro, brigar com o chefão, conversar com os pais (lembra que o problema depende de como é a sua história).",
   "O objetivo aqui é mostrar como o personagem tenta resolver o problema sem desenvolver novas habilidades (porque ele ainda é o personagem do ponto A, que não sabe muita coisa). É um primeiro movimento dele, e vai mostrar quem ele realmente é e se ele está disposto a crescer.",
   "Lembre-se que não precisa resolver tudo neste ponto da história."])]),
 ("Clímax", "navy", [
  (5, "Capítulo em que seu personagem consegue resolver uma parte do problema", [
   "Ele se mexeu e merece uma pequena vitória. O objetivo deste capítulo é mostrar que seu personagem está mais próximo do ponto B da história.",
   "Mostre como ele muda após essa pequena vitória. Ele tem novos amigos, novas opiniões, novos traumas?",
   "Seu personagem cresceu, amadureceu. Não é o mesmo do início da história, então deixe isso claro. Aqui você pode mostrar mudanças na aparência e na forma como ele lida com os outros personagens."]),
  (6, "Capítulo em que as coisas voltam a dar errado", [
   "Seu personagem amadureceu, mas ele ainda acha que é fácil resolver os problemas da vida. Spoiler: nunca é fácil resolver os problemas da vida.",
   "Como estamos no clímax, aqui seu personagem precisa ser testado para amadurecer. É o ponto da narrativa em que tudo acontece! As brigas, os beijos, as batalhas!",
   "O problema parcialmente resolvido traz consequências e mudanças não tão agradáveis na realidade do personagem. Isso precisa acontecer para que seu personagem se lembre que ele precisa continuar lutando para resolver totalmente o problema.",
   "O objetivo aqui é mostrar ao seu personagem que ele precisa amadurecer ainda mais, precisa de mais ajuda e de novos planos para vencer."])]),
 ("Caminho de volta", "black", [
  (7, "Capítulo em que seu personagem recebe ajuda e traça um plano", [
   "Aqui, você precisa mostrar o seu personagem se reorganizando para resolver de vez o problema. Ele pode ir fazer terapia, pedir conselhos aos amigos, refletir sobre o motivo de ter vencido, etc.",
   "Aqui seu personagem vai contar com a ajuda dos personagens que conheceu durante a história. Os sentimentos e sensações que o trouxeram até aqui vão guiá-lo, os novos amigos vão dar ferramentas novas para ajudá-lo no confronto final.",
   "O objetivo é mostrar que seu personagem está mais próximo do ponto B. Ele amadureceu, já se desafiou algumas vezes e aprendeu coisas novas. Está na hora de se arriscar mais uma vez."]),
  (8, "Capítulo em que seu personagem resolve tudo de vez", [
   "Dependendo da sua história, resolver o problema pode envolver beijar alguém pela primeira vez, assumir o controle dos poderes, viajar e vencer os medos… Mostre essa batalha final e como ela acontece nos mínimos detalhes.",
   "O objetivo aqui é mostrar que o amadurecimento do personagem é real. Ele tem novos amigos, novas estratégias, nova forma de agir, e por isso… vence.",
   "Em geral, essa é a parte que nós escritores mais gostamos de escrever, pois é o momento da ação mais interessante do livro."])]),
 ("Fim", "black", [
  (9, "Capítulo em que a vida do personagem muda", [
   "Após a jornada completa, a vida do seu personagem vai mudar. Ele vai ter uma outra aparência, outra rotina, talvez novos amigos ou poderes. Mostre como essa vida mudou.",
   "O objetivo deste capítulo é mostrar como é o ponto B da história. É um capítulo de ambientação na nova realidade."])]),
]
SHORT = {1: "Ambientação", 2: "Problema central", 3: "Recusa", 4: "Obrigado a agir", 5: "Pequena vitória", 6: "Tudo dá errado", 7: "Ajuda e plano", 8: "Confronto final", 9: "Vida nova"}
NOTE = ["Hello, escritores! Camila Veloso aqui (escritora e Produtora Editorial, vocês sabem). Esse checklist é a estrutura básica para uma narrativa de sucesso. Você pode colocar mais capítulos no seu livro se quiser, desde que pelo menos siga essa estrutura.",
        "Estou curiosa para ver as histórias que você vai criar. Boa escrita!"]

CSS = '''
@font-face{font-family:"Outfit";font-weight:600;src:url(__F__/outfit-latin-600-normal.woff2) format("woff2")}
@font-face{font-family:"Outfit";font-weight:700;src:url(__F__/outfit-latin-700-normal.woff2) format("woff2")}
@font-face{font-family:"Outfit";font-weight:800;src:url(__F__/outfit-latin-800-normal.woff2) format("woff2")}
@font-face{font-family:"Figtree";font-weight:400;src:url(__F__/figtree-latin-400-normal.woff2) format("woff2")}
@font-face{font-family:"Figtree";font-weight:500;src:url(__F__/figtree-latin-500-normal.woff2) format("woff2")}
@font-face{font-family:"Figtree";font-weight:700;src:url(__F__/figtree-latin-700-normal.woff2) format("woff2")}
:root{--cream:#f6f1ec;--navy:#083656;--ink:#111;--lilac:#e8dcfb;--violet:#6d28d9;--violet-dark:#5b21b6;--muted:#3a5568;--line:#ddd5ca;--sand:#e9e1d7}
@page{size:A4;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{font-family:"Figtree",Arial,sans-serif;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;background:var(--cream);padding:16mm 17mm 20mm;display:flex;flex-direction:column}
.page:last-child{page-break-after:auto}
.page--navy{background:var(--navy);color:#cfdce7}
h1,h2,h3{font-family:"Outfit",Arial,sans-serif;margin:0;letter-spacing:-.025em;line-height:1.05}
.kicker{font-family:"Figtree";font-weight:700;font-size:7.5pt;letter-spacing:.22em;text-transform:uppercase;color:var(--violet)}
.page--navy .kicker{color:#c9b2f2}
.head{display:flex;justify-content:space-between;align-items:center;margin-bottom:9mm}
.head .right{font-size:8pt;color:var(--muted);font-weight:500}
.foot{position:absolute;left:17mm;right:17mm;bottom:9mm;display:flex;justify-content:space-between;align-items:center;font-size:7pt;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);font-weight:700;border-top:1px solid var(--line);padding-top:3.5mm}
.page--navy .foot{color:#8fb0c8;border-color:rgba(255,255,255,.2)}
.chip{display:inline-block;align-self:flex-start;font-family:"Outfit";font-weight:700;font-size:9pt;padding:2.2mm 5mm;border-radius:3mm;line-height:1}
.chip--lilac{background:var(--lilac);color:var(--navy)}.chip--navy{background:var(--navy);color:#fff}.chip--black{background:var(--ink);color:#fff}
.phase-title{font-size:38pt;font-weight:800;color:var(--navy);margin:3mm 0 6mm}
.steps{display:flex;flex-direction:column;gap:6mm;flex:1}
.step{background:#fff;border:1px solid var(--line);border-radius:5mm;padding:7mm 8mm 6.5mm;display:grid;grid-template-columns:15mm 1fr;gap:0 6mm;align-content:start}
.step .n{width:15mm;height:15mm;border-radius:50%;display:grid;place-items:center;font-family:"Outfit";font-weight:800;font-size:19pt;color:#fff;background:var(--violet)}
.step--navy .n{background:var(--navy)}.step--black .n{background:var(--ink)}
.step h3{font-size:16pt;font-weight:700;color:var(--ink);padding-top:1mm;margin-bottom:3.5mm}
.step .body{grid-column:2}
.step p{margin:0 0 3.2mm;font-size:11pt;line-height:1.6;color:#26323b}
.mid .step p{font-size:11.9pt;line-height:1.6}.mid .step{padding:8mm 8.5mm 7mm}.mid .step h3{font-size:17pt}
.roomy .step{padding:9mm 9mm 8mm}.roomy .step h3{font-size:18pt;margin-bottom:5mm}.roomy .step p{font-size:12.6pt;line-height:1.62;margin-bottom:4.2mm}.roomy .steps{gap:8mm}.roomy .step .n{width:17mm;height:17mm;font-size:22pt}.roomy .step{grid-template-columns:17mm 1fr}
.step p:last-child{margin-bottom:0}
.hl{background:linear-gradient(transparent 55%,var(--lilac) 55%,var(--lilac) 92%,transparent 92%)}
/* capa */
.cover{justify-content:space-between}
.cover h1{font-size:60pt;font-weight:800;color:#fff;margin-top:22mm}
.cover .sub{font-family:"Outfit";font-weight:600;font-size:20pt;color:#fff;margin-top:6mm;line-height:1.25}
.cover .sub span{background:linear-gradient(transparent 50%,rgba(201,178,242,.5) 50%,rgba(201,178,242,.5) 94%,transparent 94%);padding:0 1.5mm}
.map{display:grid;grid-template-columns:repeat(5,1fr);gap:3.2mm}
.map .col{display:flex;flex-direction:column;gap:2.5mm}
.map .cell{background:var(--cream);color:var(--navy);border-radius:3mm;padding:4.5mm 3mm;font-size:9pt;line-height:1.25;font-weight:500;min-height:19mm}
.map .cell b{display:block;font-family:"Outfit";font-size:10.4pt;font-weight:700;margin-bottom:.6mm}
.map .chip{text-align:center;width:100%;font-size:10pt;padding:3mm 2mm}
.map .chip--lilac{background:var(--lilac)}
.map .chip--navy{background:#0e4a73;color:#fff}
.cover .note{font-size:10pt;color:#9fbdd3;margin-top:7mm}
.cover .bottom{display:flex;justify-content:space-between;align-items:flex-end}
.cover .bottom img{height:13mm}
.cover .tag{font-family:"Outfit";font-weight:600;font-size:10pt;color:#fff}
/* nota final */
.fim-note{margin-top:auto;background:var(--navy);border-radius:5mm;padding:9mm 10mm;color:#e3ecf3}
.fim-note .kicker{margin-bottom:3mm;display:block}
.fim-note p{margin:0 0 3.6mm;font-size:12.6pt;line-height:1.6}
.fim-note p:last-of-type{margin-bottom:0}
.fim-note .sign{margin-top:6mm;display:flex;align-items:center;justify-content:space-between}
.fim-note .sign img{height:10mm}
.fim-note .sign span{font-family:"Outfit";font-weight:600;color:#c9b2f2;font-size:10pt}
.fim-intro{font-family:"Outfit";font-weight:600;font-size:15pt;color:var(--navy);line-height:1.3;margin:6mm 0 8mm}
'''


def step_html(n, title, paras, tone):
    ps = "".join(f"<p>{E(p)}</p>" for p in paras)
    return f'<article class="step step--{tone}"><div class="n">{n}</div><h3>{E(title)}</h3><div class="body">{ps}</div></article>'


def build():
    css = CSS.replace("__F__", "file://" + FONTS)
    pages, total = [], 6
    # capa com o mapa dos 5 estágios (como no slide "9 passos")
    cols = ""
    for name, tone, steps in PHASES:
        cells = "".join(f'<div class="cell"><b>{n} · {SHORT[n]}</b></div>' for n, _, _ in steps)
        cols += f'<div class="col"><span class="chip chip--{tone}">{E(name)}</span>{cells}</div>'
    pages.append(f'''<section class="page page--navy cover"><div>
  <span class="kicker">Material de apoio · Aulão Universal</span>
  <h1>Checklist da narrativa</h1>
  <p class="sub"><span>9 passos para você chegar ao final da história</span></p></div>
  <div><div class="map">{cols}</div>
  <p class="note">Pode haver mais capítulos, desde que a estrutura seja respeitada.</p></div>
  <div class="bottom"><img src="file://{LOGO_NEG}" alt="Camila Veloso"><span class="tag">escrever um livro pode ser fácil.</span></div></section>''')
    for i, (name, tone, steps) in enumerate(PHASES[:-1] if False else PHASES, start=2):
        if name == "Fim":
            break
        nums = " e ".join(str(n) for n, _, _ in steps)
        body = "".join(step_html(n, t, ps, tone if tone != "lilac" else "lilac") for n, t, ps in steps)
        pages.append(f'''<section class="page{(' roomy' if sum(len(ps) for _, _, ps in steps) <= 5 else ' mid' if sum(len(ps) for _, _, ps in steps) == 6 else '')}"><div class="head"><span class="kicker">Checklist da narrativa</span><span class="right">Passos {nums}</span></div>
  <span class="chip chip--{tone}">Fase {i - 1} de 5</span><h2 class="phase-title">{E(name)}</h2>
  <div class="steps">{body}</div><div class="foot"><span>Aulão Universal</span><span>{i}</span></div></section>''')
    n, t, ps = PHASES[-1][2][0]
    note = "".join(f"<p>{E(p)}</p>" for p in NOTE)
    pages.append(f'''<section class="page roomy"><div class="head"><span class="kicker">Checklist da narrativa</span><span class="right">Passo 9</span></div>
  <span class="chip chip--black">Fase 5 de 5</span><h2 class="phase-title">Fim</h2>
  <div class="steps" style="flex:none">{step_html(n, t, ps, "black")}</div>
  <div class="fim-note"><span class="kicker">Observações</span>{note}<div class="sign"><img src="file://{LOGO_NEG}" alt="Camila Veloso"><span>@acamiveloso</span></div></div>
  <div class="foot"><span>Aulão Universal</span><span>{total}</span></div></section>''')
    return f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Checklist da narrativa · Aulão Universal</title><style>{css}</style></head><body>{"".join(pages)}</body></html>'


if __name__ == "__main__":
    out_html = os.path.join(HERE, "checklist.html")
    open(out_html, "w", encoding="utf-8").write(build())
    pdf = os.path.join(ROOT, "materiais", "checklist-aulao-universal.pdf")
    js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://{out_html}');await p.evaluate(()=>document.fonts.ready);
await p.pdf({{path:'{pdf}',format:'A4',printBackground:true,preferCSSPageSize:true}});await b.close();}})();"""
    r = subprocess.run(["node", "-e", js], capture_output=True, text=True)
    print(r.stdout, r.stderr[-500:])
    print("ok ->", os.path.relpath(pdf, ROOT))
