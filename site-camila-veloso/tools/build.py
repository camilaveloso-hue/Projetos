#!/usr/bin/env python3
"""Gera o site estático (HTML) de Camila Veloso.

Uso:  python3 tools/build.py            (roda na pasta site-camila-veloso/)
Para trocar o domínio, redes sociais ou links de compra, edite só o bloco SITE.
"""
import json, pathlib, datetime, hashlib

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
    "goatcounter": "camilaveloso",
}
LINK_EDITORA = "https://www.editorafissura.com.br/produtos/pre-venda-o-diario-de-amelia-1amj0/"
PRECO = "59,90"       # preço da pré-venda: tem que bater com o da loja da Editora Fissura
PRECO_DE = "69,99"
HOJE = datetime.date.today().isoformat()

def _versao(caminho):
    # muda quando o arquivo muda: evita que o navegador use CSS/JS antigo guardado em cache
    return hashlib.md5((ROOT / caminho).read_bytes()).hexdigest()[:8]


FONTS = ("https://fonts.googleapis.com/css2?family=Shrikhand&family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,800"
         "&family=DM+Sans:ital,wght@0,400;0,500;0,700;1,400&display=swap")

NAV = [("/", "Home"), ("/o-diario-de-amelia/", "O Diário de Amélia"), ("/livros/", "Livros"),
       ("/sobre/", "Sobre"), ("/aldeia/", "Aldeia"), ("/links/", "Links")]

# ---------------------------------------------------------------- ARTIGOS (SEO)
ARTIGOS = [
    {
        "slug": "livros-sobre-liberdade-e-independencia",
        "titulo": "Livros sobre liberdade e independência: o que ler para ganhar coragem",
        "h1": "Livros sobre liberdade e independência para quem precisa de coragem",
        "desc": "Como escolher livros sobre liberdade, independência e recomeço — e por que histórias de quem rompe com o que esperavam dela podem mudar a sua.",
        "resumo": "Por que histórias de gente que rompe com o que esperavam dela funcionam como ensaio geral para a nossa própria coragem.",
        "corpo": """
<p class="lede">Existe um tipo de leitura que não serve para fugir da vida. Serve para ensaiar a sua. É o livro que você termina e fica olhando pro teto pensando: “eu também posso”.</p>
<h2>O que faz um livro sobre liberdade funcionar</h2>
<p>Livros sobre liberdade e independência raramente são sobre grandes revoluções. Quase sempre são sobre o primeiro “não” dito em voz alta, a primeira mudança de endereço, a primeira escolha que ninguém aprovou. A literatura é boa nisso porque deixa a gente viver a decisão antes de ter que tomá-la.</p>
<ul>
  <li><strong>Protagonistas imperfeitas:</strong> quem tem medo, erra, volta atrás e tenta de novo. Heroína sem dúvida não ensina nada.</li>
  <li><strong>Conflito real:</strong> família, dinheiro, crença, expectativa. A liberdade custa alguma coisa, e o livro bom mostra o preço.</li>
  <li><strong>Humor:</strong> rir da própria encrenca é uma forma de coragem.</li>
</ul>
<h2>Para quem cresceu em casa pequena demais para os sonhos</h2>
<p>Se você cresceu num ambiente que cabia pouco do que você queria ser, vale procurar histórias de amadurecimento (o chamado <em>coming-of-age</em>) em que a protagonista descobre que independência é um músculo — e que se treina aos poucos, entre lapsos de coragem e muitas queixas.</p>
<p>Foi exatamente essa a ideia de <strong>O Diário de Amélia</strong>: um romance jovem-adulto sobre uma garota de dezoito anos que precisa se libertar das expectativas dos pais para criar a vida que sempre quis. Um livro bem-humorado para jovens que querem mudar de vida, mas não sabem como.</p>
<blockquote>Liberdade não é um dia em que tudo muda. É uma sequência de pequenas escolhas feitas com o coração um pouco mais firme.</blockquote>
<h2>Como escolher a sua próxima leitura</h2>
<p>Pergunte-se qual liberdade você está procurando: de uma família, de uma crença, de um emprego, de uma versão antiga de você? Depois busque livros em que a protagonista enfrente algo parecido. A identificação é o que transforma a leitura em movimento.</p>
""",
    },
    {
        "slug": "livros-sobre-familia-opressora-e-religiao",
        "titulo": "Romances sobre família opressora e religião controladora",
        "h1": "Romances sobre família opressora e religião controladora",
        "desc": "Leituras para quem cresceu sob regras rígidas, culpa e controle: por que a ficção ajuda a nomear o que viveu e a imaginar a saída.",
        "resumo": "Ficção que ajuda a nomear o que a gente viveu sob regras rígidas, culpa e controle — e a imaginar a saída.",
        "corpo": """
<p class="lede">Crescer sob regras que ninguém explica, onde pensar diferente é “impureza”, deixa marcas que a gente demora a nomear. A ficção ajuda: dá nome, dá cena, dá companhia.</p>
<h2>Por que ler sobre isso</h2>
<p>Quem cresceu em ambiente controlador — religioso ou não — costuma carregar uma culpa difusa: por querer, por opinar, por desejar. Ver uma personagem passar pelo mesmo dilema, e rir e chorar junto com ela, ajuda a separar o que é seu do que foi imposto.</p>
<h2>O que observar numa boa história sobre o tema</h2>
<ul>
  <li><strong>Sem caricatura:</strong> os pais também são gente, e o conflito é mais verdadeiro quando existe afeto no meio.</li>
  <li><strong>A voz da protagonista:</strong> opiniões, dúvidas, humor. É a voz dela que a liberta primeiro.</li>
  <li><strong>Saída possível:</strong> o livro precisa acreditar que dá para recomeçar.</li>
</ul>
<h2>Um romance jovem-adulto para começar</h2>
<p>Em <strong>O Diário de Amélia</strong>, a protagonista tem dezoito anos, uma cabeça cheia de opiniões, “pensamentos impuros” e beijos imaginados — e pais que frequentam uma seita (mesmo que ela jure que é mentira). Para a família, a filha deve aprender a servir, casar com alguém da comunidade e se manter longe de ideias próprias.</p>
<p>É uma história sobre autodescoberta, amizade e primeiras vezes, contada com humor. Como disse uma leitora crítica, é um livro “para rir, mas com o peito apertado do começo ao fim”.</p>
<blockquote>Você não precisa de permissão para ter uma cabeça cheia de opiniões.</blockquote>
""",
    },
    {
        "slug": "romances-de-amadurecimento-young-adult",
        "titulo": "Romances de amadurecimento (young adult): o que são e como escolher",
        "h1": "Romances de amadurecimento young adult: guia para escolher o seu",
        "desc": "O que é um romance de amadurecimento (coming-of-age), por que ele conversa com leitores jovens e adultos e o que procurar antes de começar.",
        "resumo": "O que é um romance de amadurecimento, por que ele conversa com jovens e adultos e o que procurar antes de começar.",
        "corpo": """
<p class="lede">Romance de amadurecimento é aquela história em que alguém entra de um jeito e sai de outro. Ninguém é igual depois da primeira vez que se escolhe sozinho.</p>
<h2>O que é um romance de amadurecimento</h2>
<p>Também chamado <em>coming-of-age</em> ou, em alemão, <em>Bildungsroman</em>, é o gênero que acompanha o crescimento de uma pessoa — normalmente na passagem da adolescência para a vida adulta — e as descobertas, perdas e escolhas que moldam quem ela se torna.</p>
<h2>Young adult não é só para jovens</h2>
<p>A etiqueta <em>young adult</em> (jovem-adulto) descreve protagonistas jovens, mas o tema é universal: identidade, pertencimento, amor, independência. Muita gente com trinta, quarenta, cinquenta anos lê esses livros porque o sentimento de “quem sou eu fora do que esperam de mim?” não tem prazo de validade.</p>
<h2>Três coisas para procurar</h2>
<ul>
  <li><strong>Voz marcante:</strong> narradoras que parecem conversar com você, como um diário.</li>
  <li><strong>Humor e emoção juntos:</strong> a vida real mistura os dois.</li>
  <li><strong>Primeiras vezes:</strong> beijo, mudança, desobediência, escolha. É nelas que o personagem cresce.</li>
</ul>
<h2>Do diário à vida</h2>
<p><strong>O Diário de Amélia</strong>, estreia de Camila Veloso no romance, é um exemplo contemporâneo e brasileiro do gênero: uma montanha-russa de primeiras vezes, lapsos de coragem e muitas queixas, narrada por uma garota de dezoito anos que quer ser independente de um ambiente familiar caótico e opressor — e, de quebra, dar uns beijos no garoto de quem gosta.</p>
""",
    },
    {
        "slug": "criatividade-nao-e-habilidade",
        "titulo": "Criatividade não é habilidade: é uma característica humana",
        "h1": "Criatividade não é habilidade. É uma característica humana.",
        "desc": "Por que a criatividade é inerente a todo ser humano, como a arte empodera e o que isso tem a ver com escrever, ler e criar a própria vida.",
        "resumo": "Por que a criatividade é inerente a todo ser humano, como a arte empodera e o que isso tem a ver com criar a própria vida.",
        "corpo": """
<p class="lede">“Eu não sou criativa” é uma das frases mais inventadas da história. Criar é o que a nossa espécie faz desde que existe.</p>
<h2>Criatividade é característica, não talento</h2>
<p>Pense em uma criança brincando: ela inventa mundos sem pedir licença. Ninguém precisou ensinar. Com o tempo, a gente aprende a achar que criar é coisa de “gente especial” — e silencia uma parte inteira de quem somos. A criatividade não é uma habilidade rara que alguns têm e outros não. É inerente ao ser humano. O que varia é o quanto a gente foi autorizado a usá-la.</p>
<h2>Arte como empoderamento</h2>
<p>Quando alguém escreve a própria história, desenha, canta, monta, inventa, essa pessoa deixa de ser só espectadora da vida. Ela passa a autora. Por isso acredito em <strong>empoderamento através da arte</strong>: criar devolve a gente a nós mesmas.</p>
<blockquote>Quem cria a própria história descobre que também pode criar a própria vida.</blockquote>
<h2>E a liberdade?</h2>
<p>Liberdade e criatividade andam juntas. Para criar, é preciso poder errar, discordar, tentar o que ninguém aprovou. É essa a energia que move <strong>O Diário de Amélia</strong>: uma garota que descobre, escrevendo, quem ela é — e o que quer fazer com a vida.</p>
<h2>Por onde começar</h2>
<ul>
  <li>Escreva sem a intenção de mostrar a ninguém, nem que sejam cinco linhas.</li>
  <li>Troque “eu não sei fazer” por “eu ainda não tentei do meu jeito”.</li>
  <li>Cerque-se de gente que celebra o seu processo, não só o resultado.</li>
</ul>
""",
    },
]

# ---------------------------------------------------------------- PEÇAS COMUNS
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def preencher(html):
    return (html.replace("{{PRECO_INT}}", PRECO.split(",")[0]).replace("{{PRECO_DE}}", PRECO_DE)
            .replace("{{PRECO}}", PRECO))

def fragmento(nome):
    return preencher((ROOT / "tools" / "paginas" / f"{nome}.html").read_text(encoding="utf-8"))

def header(atual, links=False):
    aviso = (f'<div class="aviso aviso--camila">Pré-venda com brindes exclusivos + livro autografado por <b>R$ {PRECO}</b>. Últimos dias.</div>' if links else
             f'<div class="aviso">🎉 Pré-venda: livro <b>autografado</b> + brindes por <b>R$ {PRECO}</b> · últimos dias</div>')
    itens = "".join(
        f'<a href="{h}"{" class=on aria-current=page" if atual == h else ""}>{t}</a>' for h, t in NAV[1:])
    return f"""<a class="skip" href="#conteudo">Pular para o conteúdo</a>
{aviso}
<header class="topo"><div class="w topo__in">
  <a class="marca" href="/" aria-label="Página inicial"{" aria-current=page" if atual == "/" else ""}>Home</a>
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
  <nav class="nav" aria-label="Rodapé"><a href="/o-diario-de-amelia/">O Diário de Amélia</a><a href="/livros/">Livros</a><a href="/sobre/">Sobre</a><a href="/manifesto/">Manifesto</a><a href="/leituras/">Leituras</a><a href="/links/">Links</a>{sociais}</nav>
</div></footer>
<div class="fix"><span>O Diário de Amélia · pré-venda <b>R$ {PRECO}</b></span><a class="btn btn--am" href="{LINK_EDITORA}" target="_blank" rel="noopener">Quero o meu</a></div>
<script src="/assets/js/site.js?v={_versao("assets/js/site.js")}" defer></script>"""

def medicao():
    c = SITE["goatcounter"]
    if not c:
        return ""
    return f'<script data-goatcounter="https://{c}.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'

def pessoa_ld():
    return {"@type": "Person", "@id": SITE["dominio"] + "/#camila", "name": "Camila Veloso",
            "url": SITE["dominio"] + "/sobre/", "jobTitle": "Escritora",
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
<link rel="stylesheet" href="/assets/css/style.css?v={_versao("assets/css/style.css")}">
<script type="application/ld+json">{jsonld}</script>
{medicao()}
</head>
<body{f' class="{classe}"' if classe else ""}>
{header(atual or caminho, "pag-links" in classe and "pag-aldeia" not in classe)}
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

def leituras_grid(excluir=None):
    out = ['<div class="leituras">']
    for a in ARTIGOS:
        if a["slug"] == excluir:
            continue
        out.append(f'<a class="leitura" href="/leituras/{a["slug"]}/"><h3>{esc(a["h1"])}</h3><p>{esc(a["resumo"])}</p><span class="mais">Ler →</span></a>')
    out.append("</div>")
    return "".join(out)

paginas = []
FAQ = [
    ("O livro vem autografado?", "Sim. Quem compra na pré-venda recebe o livro autografado pela Camila. Ela só vai autografar nesta etapa e não haverá sessão de lançamento."),
    ("Quais são os brindes?", "Marcador de página duplo, cartela de adesivos e o Manual de sobrevivência do jovem adulto, um card exclusivo com conteúdo extra, só para quem compra na pré-venda."),
    ("Quando sai O Diário de Amélia?", "A edição impressa, pela Editora Fissura, sai em 23 de outubro de 2026. A pré-venda já está aberta."),
    ("Onde eu compro?", "O livro físico autografado está em pré-venda na loja da Editora Fissura."),
    ("É pra quem?", "Para jovens e adultos que gostam de romance de amadurecimento, autodescoberta, amizade e primeiro amor, com humor e emoção."),
    ("Quantas páginas tem?", "250 páginas, brochura de 14 × 21 cm, miolo em papel Pólen 80 g/m² e capa em Cartão Supremo 300 g/m²."),
    ("Quem escreveu?", "Camila Veloso, escritora, produtora editorial, fundadora da Aldeia Literária e apresentadora do podcast Patricinha Literária."),
]
FAQ_HTML = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in FAQ)

def com_faq(html):
    return html.replace("<!--FAQ-->", FAQ_HTML)

# ---------------------------------------------------------------- HOME
paginas.append(pagina("/", "Camila Veloso, escritora | O Diário de Amélia, romance sobre liberdade",
    "Site oficial de Camila Veloso, autora de O Diário de Amélia: romance jovem-adulto sobre liberdade, autodescoberta e coragem. Pré-venda autografada com brindes.",
    com_faq(fragmento("home")),
    ld=[{"@type": "WebPage", "@id": SITE["dominio"] + "/#pagina", "url": SITE["dominio"] + "/", "name": "Camila Veloso, escritora",
         "isPartOf": {"@id": SITE["dominio"] + "/#site"}, "about": {"@id": SITE["dominio"] + "/#camila"}}]))

# ---------------------------------------------------------------- O DIÁRIO DE AMÉLIA
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
paginas.append(pagina("/o-diario-de-amelia/", "O Diário de Amélia, romance de Camila Veloso | Pré-venda autografada",
    f"O Diário de Amélia, de Camila Veloso: romance jovem-adulto sobre liberdade, família opressora e primeiras vezes. 250 páginas, Editora Fissura. Pré-venda por R$ {PRECO}, autografada e com brindes.",
    com_faq(fragmento("diario")), ld=book_ld, tipo="book"))

# ---------------------------------------------------------------- LIVROS
paginas.append(pagina("/livros/", "Livros de Camila Veloso: romance, crônicas e poesia",
    "Todos os livros de Camila Veloso: O Diário de Amélia, Encontrei um Pote com Tempo Dentro, Cartas ao Sol e Traumas de uma Grande Gostosa.",
    fragmento("livros"),
    ld=[migalhas_ld([("/", "Início"), ("/livros/", "Livros")]),
        {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": {"@type": "Book", "name": t, "author": {"@id": SITE["dominio"] + "/#camila"}}}
         for i, t in enumerate(["O Diário de Amélia", "Traumas de uma Grande Gostosa", "Encontrei um Pote com Tempo Dentro", "Cartas ao Sol"])]}]))

# ---------------------------------------------------------------- SOBRE
paginas.append(pagina("/sobre/", "Sobre Camila Veloso: escritora, produtora editorial e fundadora da Aldeia Literária",
    "Camila Veloso é escritora, produtora editorial, fundadora da Aldeia Literária, apresentadora do podcast Patricinha Literária e autora de O Diário de Amélia.",
    fragmento("sobre"),
    ld=[migalhas_ld([("/", "Início"), ("/sobre/", "Sobre")]), {"@type": "AboutPage", "url": SITE["dominio"] + "/sobre/", "about": {"@id": SITE["dominio"] + "/#camila"}}]))

# ---------------------------------------------------------------- LINKS (bio das redes)
paginas.append(pagina("/links/", "Links da Camila Veloso e da Aldeia Literária", "Pré-venda de O Diário de Amélia, newsletter, YouTube, Aldeia Literária e TikTok.",
    fragmento("links"), classe="pag-links", noindex=True))

# ---------------------------------------------------------------- ALDEIA LITERÁRIA (links do TikTok)
paginas.append(pagina("/aldeia/", "Aldeia Literária: site oficial e TikTok", "Links da Aldeia Literária, curso de extensão da Camila Veloso: site oficial e TikTok.",
    fragmento("aldeia"), classe="pag-links pag-aldeia", og_img="/assets/img/aldeia-literaria-logo.png"))

# ---------------------------------------------------------------- MANIFESTO
manifesto = """
<section class="pt"><div class="w"><span class="eyebrow">Manifesto</span><h1 class="fat">No que eu acredito</h1></div></section>
<section class="sec"><div class="w artigo">
 <p class="lede">Escrevo porque acredito que ninguém precisa pedir licença para criar.</p>
 <h2>1. Criatividade é característica, não habilidade.</h2>
 <p>Ela é inerente ao ser humano. Não existe gente “sem criatividade”: existe gente a quem disseram, cedo demais, que criar era para outros.</p>
 <h2>2. A arte empodera.</h2>
 <p>Quando você escreve, desenha, canta ou inventa, deixa de ser plateia e vira autora da própria vida. A arte devolve a voz.</p>
 <h2>3. Liberdade vem antes de tudo.</h2>
 <p>Liberdade de pensar diferente, errar, discordar, tentar. Cada Amélia que existe por aí merece uma casa grande o suficiente para os próprios sonhos.</p>
 <h2>4. Primeiras vezes são sagradas.</h2>
 <p>O primeiro “não”, o primeiro beijo, a primeira mudança, o primeiro texto. É nelas que a gente descobre quem é.</p>
 <h2>5. Ninguém cria sozinha.</h2>
 <p>Comunidade, escuta e incentivo fazem a coragem durar. Por isso ensino, converso e escrevo: para que mais gente se enxergue como criadora.</p>
 <blockquote>Quem cria a própria história descobre que também pode criar a própria vida.</blockquote>
 <p><a href="/leituras/criatividade-nao-e-habilidade/">Leia: Criatividade não é habilidade, é uma característica humana →</a></p>
</div></section>
"""
paginas.append(pagina("/manifesto/", "Manifesto: criatividade, arte e liberdade | Camila Veloso",
    "No que Camila Veloso acredita: criatividade é característica e não habilidade, a arte empodera e a liberdade vem antes de tudo.",
    manifesto, ld=[migalhas_ld([("/", "Início"), ("/manifesto/", "Manifesto")])], atual="/sobre/"))

# ---------------------------------------------------------------- LEITURAS
hub = f"""
<section class="pt"><div class="w"><span class="eyebrow">Leituras</span><h1 class="fat">Conversas sobre liberdade, arte e crescer</h1></div></section>
<section class="sec"><div class="w artigo" style="max-width:none">{leituras_grid()}</div></section>
"""
paginas.append(pagina("/leituras/", "Leituras: livros sobre liberdade, amadurecimento e criatividade",
    "Guias e reflexões sobre livros de liberdade e independência, romances de amadurecimento young adult e a ideia de que criatividade é inerente ao ser humano.",
    hub, ld=[migalhas_ld([("/", "Início"), ("/leituras/", "Leituras")])], atual="/sobre/"))

for a in ARTIGOS:
    c = f"/leituras/{a['slug']}/"
    corpo = f"""
<section class="sec"><div class="w artigo">
 <nav class="migalha" aria-label="Você está em"><a href="/">Início</a> / <a href="/leituras/">Leituras</a></nav>
 <span class="eyebrow">Leituras</span><h1>{esc(a['h1'])}</h1>
 {a['corpo']}
 <aside class="cta-livro"><img src="/assets/img/capa-diario-de-amelia-capa.jpg" alt="Capa de O Diário de Amélia" width="480" height="720" loading="lazy">
  <div><h3>O Diário de Amélia</h3><p>Romance de Camila Veloso sobre liberdade, família e a coragem de criar a própria vida. Pré-venda autografada, com brindes.</p>
  <a class="btn btn--am" href="/o-diario-de-amelia/">Conhecer o livro →</a></div></aside>
 <h2>Continue lendo</h2>{leituras_grid(a['slug'])}
</div></section>"""
    ld = [{"@type": "Article", "headline": a["h1"], "description": a["desc"], "inLanguage": "pt-BR",
           "author": {"@id": SITE["dominio"] + "/#camila"}, "publisher": {"@id": SITE["dominio"] + "/#camila"},
           "datePublished": HOJE, "dateModified": HOJE, "mainEntityOfPage": SITE["dominio"] + c,
           "image": SITE["dominio"] + "/assets/img/og-diario-de-amelia.jpg"},
          migalhas_ld([("/", "Início"), ("/leituras/", "Leituras"), (c, a["h1"])])]
    paginas.append(pagina(c, a["titulo"] + " | Camila Veloso", a["desc"], corpo, ld=ld, tipo="article", atual="/sobre/"))

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
