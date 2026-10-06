#!/usr/bin/env python3
"""Gera o site estático (HTML) de Camila Veloso.

Uso:  python3 tools/build.py            (roda na pasta site-camila-veloso/)
Para trocar o domínio, redes sociais ou links de compra, edite só o bloco SITE.
"""
import json, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- CONFIG
SITE = {
    "dominio": "https://www.camilaveloso.com.br",  # TROCAR pelo domínio real
    "nome": "Camila Veloso",
    "email": "",  # opcional: contato@seudominio.com.br
    "instagram": "",  # opcional: URL completa do perfil
    "podcast": "",  # opcional: URL do podcast Patricinha Literária
    "aldeia": "https://aaldeialiteraria.com.br/",
    # Contagem de visitas e cliques (GoatCounter, grátis e sem cookies). Crie a conta em goatcounter.com,
    # escolha um código (ex.: camilaveloso) e escreva aqui. Vazio = sem medição.
    "goatcounter": "",
}
LINK_EDITORA = "https://www.editorafissura.com.br/produtos/pre-venda-o-diario-de-amelia-1amj0/"
PRECO = "59,49"       # preço da pré-venda: tem que bater com o da loja da Editora Fissura
PRECO_DE = "69,99"
HOJE = datetime.date.today().isoformat()

FONTS = ("https://fonts.googleapis.com/css2?family=Shrikhand&family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,800"
         "&family=DM+Sans:ital,wght@0,400;0,500;0,700;1,400&display=swap")

NAV = [("/", "Home"), ("/aldeia/", "Aldeia"), ("/links/", "Links")]

# ---------------------------------------------------------------- PEÇAS COMUNS
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def preencher(html):
    return (html.replace("{{PRECO_INT}}", PRECO.split(",")[0]).replace("{{PRECO_DE}}", PRECO_DE)
            .replace("{{PRECO}}", PRECO).replace("{{ALDEIA}}", SITE["aldeia"]).replace("{{LINK}}", LINK_EDITORA))

def fragmento(nome):
    return preencher((ROOT / "tools" / "paginas" / f"{nome}.html").read_text(encoding="utf-8"))

def header(atual):
    itens = "".join(
        f'<a href="{h}"{" class=on aria-current=page" if atual == h else ""}>{t}</a>' for h, t in NAV)
    return f"""<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<div class="aviso">🎉 Pré-venda: livro <b>autografado</b> + brindes por <b>R$ {PRECO}</b> · lançamento em 23 de outubro</div>
<header class="topo"><div class="w topo__in">
  <a class="marca" href="/" aria-label="Camila Veloso, página inicial">camila veloso</a>
  <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav class="nav" id="nav" aria-label="Principal">{itens}
    <a class="btn" href="{LINK_EDITORA}" target="_blank" rel="noopener">Quero o meu</a></nav>
</div></header>"""

def footer():
    sociais = ""
    for chave, rotulo in (("instagram", "Instagram"), ("podcast", "Podcast Patricinha Literária"), ("aldeia", "Aldeia Literária")):
        if SITE[chave]:
            sociais += f'<a href="{SITE[chave]}" target="_blank" rel="noopener me">{rotulo}</a>'
    if SITE["email"]:
        sociais += f'<a href="mailto:{SITE["email"]}">{SITE["email"]}</a>'
    return f"""<footer class="rod"><div class="w rod__g">
  <div><div class="marca">camila veloso</div><small>Escritora · Aldeia Literária · Patricinha Literária</small>
  <small>© {datetime.date.today().year} Camila Veloso. Todos os direitos reservados.</small></div>
  <nav class="nav" aria-label="Rodapé"><a href="/aldeia/">Aldeia</a><a href="/links/">Links</a><a href="/jogo/">Jogo da Amélia</a>{sociais}</nav>
</div></footer>
<div class="fix"><span>O Diário de Amélia · pré-venda <b>R$ {PRECO}</b></span><a class="btn btn--am" href="{LINK_EDITORA}" target="_blank" rel="noopener">Quero o meu</a></div>
<script src="/assets/js/site.js" defer></script>"""

def medicao():
    c = SITE["goatcounter"]
    if not c:
        return ""
    return f'<script data-goatcounter="https://{c}.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'

def pessoa_ld():
    return {"@type": "Person", "@id": SITE["dominio"] + "/#camila", "name": "Camila Veloso",
            "url": SITE["dominio"] + "/", "jobTitle": "Escritora",
            "description": "Escritora, produtora editorial e fundadora da Aldeia Literária. Autora de O Diário de Amélia.",
            "alumniOf": "Universidade Federal de Santa Maria (UFSM)",
            "sameAs": [v for k, v in SITE.items() if k in ("instagram", "podcast", "aldeia") and v]}

def pagina(caminho, titulo, desc, corpo, ld=None, og_img="/assets/img/og-diario-de-amelia.jpg", tipo="website", atual=None, noindex=False, classe=""):
    url = SITE["dominio"] + caminho
    grafo = [{"@type": "WebSite", "@id": SITE["dominio"] + "/#site", "url": SITE["dominio"] + "/",
              "name": "Camila Veloso, escritora", "inLanguage": "pt-BR",
              "publisher": {"@id": SITE["dominio"] + "/#camila"}}, pessoa_ld()]
    if ld:
        grafo += ld if isinstance(ld, list) else [ld]
    jsonld = json.dumps({"@context": "https://schema.org", "@graph": grafo}, ensure_ascii=False)
    robots = '<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    html = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(titulo)}</title>
<meta name="description" content="{esc(desc)}">
{robots}
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#FFD83D">
<meta property="og:locale" content="pt_BR">
<meta property="og:type" content="{tipo}">
<meta property="og:site_name" content="Camila Veloso">
<meta property="og:title" content="{esc(titulo)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE['dominio']}{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/assets/img/favicon.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="/assets/css/style.css">
<script type="application/ld+json">{jsonld}</script>
{medicao()}
</head>
<body{f' class="{classe}"' if classe else ""}>
{header(atual or caminho)}
<main id="conteudo">
{corpo}
</main>
{footer()}
</body>
</html>
"""
    destino = ROOT / caminho.strip("/") / "index.html" if caminho != "/" else ROOT / "index.html"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(html, encoding="utf-8")
    return caminho

def migalhas_ld(itens):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE["dominio"] + c}
        for i, (c, n) in enumerate(itens)]}

paginas = []
FAQ = [
    ("O livro vem autografado?", "Sim. Quem compra na pré-venda recebe o livro autografado pela Camila. Ela só vai autografar nesta etapa e não haverá sessão de lançamento."),
    ("Quais são os brindes?", "Marcador de página duplo, marcador duplo temático, brinde sortido e o Manual de sobrevivência do jovem adulto, exclusivo de quem compra na pré-venda."),
    ("Quando sai O Diário de Amélia?", "A edição impressa, pela Editora Fissura, sai em 23 de outubro de 2026. A pré-venda já está aberta."),
    ("Onde eu compro?", "O livro físico autografado está em pré-venda na loja da Editora Fissura."),
    ("É pra quem?", "Para jovens e adultos que gostam de romance de amadurecimento, autodescoberta, amizade e primeiro amor, com humor e emoção."),
    ("Quantas páginas tem?", "250 páginas, brochura de 14 × 21 cm, miolo em papel Pólen 80 g/m² e capa em Cartão Supremo 300 g/m²."),
    ("Quem escreveu?", "Camila Veloso, escritora, produtora editorial, fundadora da Aldeia Literária e apresentadora do podcast Patricinha Literária."),
]
FAQ_HTML = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in FAQ)

def com_faq(html):
    return html.replace("<!--FAQ-->", FAQ_HTML)

# ---------------------------------------------------------------- HOME (livro, FAQ e dados do livro para o Google ficam aqui)
book_ld = [
    {"@type": "Book", "@id": SITE["dominio"] + "/o-diario-de-amelia/#livro", "name": "O Diário de Amélia",
     "author": {"@id": SITE["dominio"] + "/#camila"}, "inLanguage": "pt-BR", "genre": ["Romance jovem-adulto", "Romance de amadurecimento"],
     "image": SITE["dominio"] + "/assets/img/og-diario-de-amelia.jpg",
     "description": "Romance sobre Amélia, de dezoito anos, que precisa se libertar das expectativas dos pais e de um ambiente familiar opressor para criar a vida que sempre quis.",
     "publisher": {"@type": "Organization", "name": "Editora Fissura", "url": "https://www.editorafissura.com.br/"},
     "datePublished": "2026-10-23",
     "workExample": [{"@type": "Book", "bookFormat": "https://schema.org/Paperback", "numberOfPages": 250, "inLanguage": "pt-BR",
        "datePublished": "2026-10-23",
        "offers": {"@type": "Offer", "url": LINK_EDITORA, "priceCurrency": "BRL", "price": PRECO.replace(",", "."),
                   "availability": "https://schema.org/PreOrder", "itemCondition": "https://schema.org/NewCondition"}}],
     "review": [{"@type": "Review", "author": {"@type": "Person", "name": "Karine Leôncio"}, "reviewBody": "Um livro para rir, mas com o peito apertado do começo ao fim."},
                {"@type": "Review", "author": {"@type": "Person", "name": "Amanda Gambogi"}, "reviewBody": "História sobre autodescoberta e amizades, um abraço carinhoso."}]},
    {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
    migalhas_ld([("/", "Início"), ("/o-diario-de-amelia/", "O Diário de Amélia")]),
]
home_ld = [{"@type": "WebPage", "@id": SITE["dominio"] + "/#pagina", "url": SITE["dominio"] + "/", "name": "Camila Veloso, escritora",
         "isPartOf": {"@id": SITE["dominio"] + "/#site"}, "about": {"@id": SITE["dominio"] + "/#camila"}}] + book_ld[:2]
paginas.append(pagina("/", "O Diário de Amélia, romance de Camila Veloso sobre liberdade | Pré-venda autografada",
    f"O Diário de Amélia, de Camila Veloso: romance jovem-adulto sobre liberdade, família opressora e primeiras vezes. 250 páginas, Editora Fissura. Pré-venda por R$ {PRECO}, autografada e com brindes.",
    com_faq(fragmento("home")), ld=home_ld, tipo="book"))

# ---------------------------------------------------------------- ALDEIA
paginas.append(pagina("/aldeia/", "Aldeia Literária: curso de escrita criado por Camila Veloso",
    "Conheça a Aldeia Literária, comunidade e curso de escrita para iniciantes fundado por Camila Veloso: aulas ao vivo, feedback individual e mercado editorial por dentro.",
    fragmento("aldeia"),
    ld=[migalhas_ld([("/", "Início"), ("/aldeia/", "Aldeia")]),
        {"@type": "Organization", "name": "Aldeia Literária", "url": SITE["aldeia"], "foundingDate": "2023-11", "founder": {"@id": SITE["dominio"] + "/#camila"}}]))

# ---------------------------------------------------------------- LINKS (bio das redes)
paginas.append(pagina("/links/", "Links da Camila Veloso", "Pré-venda de O Diário de Amélia, jogo, newsletter, YouTube e Aldeia Literária.",
    fragmento("links"), classe="pag-links", noindex=True))

# ---------------------------------------------------------------- JOGO
paginas.append(pagina("/jogo/", "Jogue com a Amélia: pegue as ideias e fuja das regras | Camila Veloso",
    "Um jogo rápido inspirado em O Diário de Amélia, de Camila Veloso: pegue as ideias, desvie das regras e ajude Amélia a ganhar liberdade.",
    fragmento("jogo"), ld=[migalhas_ld([("/", "Início"), ("/jogo/", "Jogo")])], atual="/links/", classe="pag-jogo"))

# ---------------------------------------------------------------- 404
nf = """<section class="sec"><div class="w" style="text-align:center;max-width:36rem">
<h1 class="fat">Essa página fugiu de casa.</h1><p class="lede" style="margin-block:1rem 1.5rem">Mas a gente ajuda você a voltar.</p>
<a class="btn btn--g" href="/">Ir para o início</a></div></section>"""
pagina("/404", "Página não encontrada | Camila Veloso", "Página não encontrada.", nf, noindex=True)
(ROOT / "404.html").write_text((ROOT / "404" / "index.html").read_text(encoding="utf-8"), encoding="utf-8")
import shutil; shutil.rmtree(ROOT / "404")

# ---------------------------------------------------------------- sitemap + robots
publicas = [p for p in paginas if p != "/links/"]
urls = "".join(f"<url><loc>{SITE['dominio']}{p}</loc><lastmod>{HOJE}</lastmod></url>" for p in publicas)
(ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n', encoding="utf-8")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE['dominio']}/sitemap.xml\n", encoding="utf-8")
print("OK:", len(paginas), "páginas")
