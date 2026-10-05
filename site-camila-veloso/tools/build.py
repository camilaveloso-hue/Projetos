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
    "aldeia": "",  # opcional: URL da Aldeia Literária
}
LINK_EDITORA = "https://www.editorafissura.com.br/produtos/pre-venda-o-diario-de-amelia-1amj0/"
LINK_AMAZON = "https://www.amazon.com.br/Di%C3%A1rio-Am%C3%A9lia-Camila-Veloso-ebook/dp/B0CQZ4PRKB"
HOJE = datetime.date.today().isoformat()

FONTS = ("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800"
         "&family=Instrument+Sans:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap")

NAV = [("/o-diario-de-amelia/", "O Diário de Amélia"), ("/livros/", "Livros"),
       ("/manifesto/", "Manifesto"), ("/leituras/", "Leituras"), ("/sobre/", "Sobre")]

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
<p>Foi exatamente essa a ideia de <strong>O Diário de Amélia</strong>: um romance jovem-adulto sobre uma garota de dezoito anos que precisa se libertar das expectativas dos pais para criar a vida que sempre quis. Um manual básico, e bem-humorado, para jovens que querem mudar de vida mas não sabem como.</p>
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

def link_ext(url, txt, cls="btn"):
    return f'<a class="{cls}" href="{url}" target="_blank" rel="noopener">{txt}</a>'

def header(atual):
    cur = ' aria-current="page"'
    itens = "".join(
        f'<a href="{h}"{cur if atual == h else ""}>{t}</a>' for h, t in NAV)
    return f"""<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="topo"><div class="wrap topo__in">
  <a class="topo__logo" href="/" aria-label="Camila Veloso — página inicial"><img src="/assets/img/logo-horizontal.png" alt="Camila Veloso" width="132" height="44"></a>
  <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav class="nav" id="nav" aria-label="Principal">{itens}
    <a class="btn btn--sol" href="{LINK_EDITORA}" target="_blank" rel="noopener">Garantir o meu</a></nav>
</div></header>"""

def footer():
    sociais = ""
    for chave, rotulo in (("instagram", "Instagram"), ("podcast", "Podcast Patricinha Literária"), ("aldeia", "Aldeia Literária")):
        if SITE[chave]:
            sociais += f'<li><a href="{SITE[chave]}" target="_blank" rel="noopener me">{rotulo}</a></li>'
    if SITE["email"]:
        sociais += f'<li><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></li>'
    sociais = sociais or "<li>Em breve, mais por aqui.</li>"
    return f"""<footer class="rodape"><div class="wrap">
 <div class="rodape__grid">
  <div><img class="logo" src="/assets/img/logo-negativo.png" alt="Camila Veloso" width="116" height="92">
   <p class="serif-i" style="font-size:1.3rem;max-width:26ch">Criar é inerente ao ser humano. A arte é o caminho de volta pra si.</p></div>
  <div><h4>Explorar</h4><ul>
   <li><a href="/o-diario-de-amelia/">O Diário de Amélia</a></li><li><a href="/livros/">Todos os livros</a></li>
   <li><a href="/manifesto/">Manifesto</a></li><li><a href="/leituras/">Leituras</a></li><li><a href="/sobre/">Sobre Camila</a></li></ul></div>
  <div><h4>Comprar &amp; seguir</h4><ul>
   <li><a href="{LINK_EDITORA}" target="_blank" rel="noopener">Pré-venda na Editora Fissura</a></li>
   <li><a href="{LINK_AMAZON}" target="_blank" rel="noopener">E-book na Amazon</a></li>{sociais}</ul></div>
 </div>
 <small>© {datetime.date.today().year} Camila Veloso. Todos os direitos reservados.</small>
</div></footer>
<script>
(function(){{var b=document.querySelector('.menu-btn'),n=document.getElementById('nav');
b.addEventListener('click',function(){{var o=n.classList.toggle('is-open');b.setAttribute('aria-expanded',o)}});}})();
</script>"""

def pessoa_ld():
    d = {"@type": "Person", "@id": SITE["dominio"] + "/#camila", "name": "Camila Veloso",
         "url": SITE["dominio"] + "/sobre/",
         "jobTitle": "Escritora",
         "description": "Escritora, fundadora da Aldeia Literária e apresentadora do podcast Patricinha Literária. Autora de O Diário de Amélia.",
         "alumniOf": "Universidade Federal de Santa Maria (UFSM)",
         "sameAs": [v for k, v in SITE.items() if k in ("instagram", "podcast", "aldeia") and v]}
    return d

def pagina(caminho, titulo, desc, corpo, ld=None, og_img="/assets/img/og-diario-de-amelia.jpg", tipo="website", atual=None, noindex=False):
    url = SITE["dominio"] + caminho
    grafo = [{"@type": "WebSite", "@id": SITE["dominio"] + "/#site", "url": SITE["dominio"] + "/",
              "name": "Camila Veloso — Escritora", "inLanguage": "pt-BR",
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
<meta name="theme-color" content="#CC341B">
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
</head>
<body>
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

BTN_COMPRA = (f'<div class="btns">{link_ext(LINK_EDITORA, "Pré-venda na Editora Fissura →", "btn btn--sol")}'
              f'{link_ext(LINK_AMAZON, "E-book na Amazon", "btn btn--vazado")}</div>')

CAPA = ('<img class="capa" src="/assets/img/capa-diario-de-amelia.webp" width="541" height="432" '
        'alt="Capa do livro O Diário de Amélia, de Camila Veloso: capa vermelha com ilustração de uma jovem de mãos nos bolsos">')

paginas = []

# ---------------------------------------------------------------- HOME
marq = ["liberdade", "criatividade", "arte que empodera", "coragem", "primeiras vezes", "escrever a própria história", "ser quem você é"]
marq_html = "".join(f"<span>{t}</span><i>✺</i>" for t in marq) * 2

def ico(svg):
    return f'<svg class="card__ico" viewBox="0 0 54 54" aria-hidden="true">{svg}</svg>'

ICO1 = ico('<circle cx="27" cy="27" r="26" fill="#CC341B"/><path d="M27 12v30M12 27h30M17 17l20 20M37 17 17 37" stroke="#FFF6EA" stroke-width="4" stroke-linecap="round"/>')
ICO2 = ico('<circle cx="27" cy="27" r="26" fill="#622064"/><path d="M14 38c4-14 10-20 26-22-2 16-8 22-22 24z" fill="#FFD83D"/><path d="M14 40 30 24" stroke="#622064" stroke-width="3" stroke-linecap="round"/>')
ICO3 = ico('<path d="M30 3C14 6 8 20 12 30c3 7 10 10 15 12-4 4-9 6-13 6 0 0 6 6 18 3 14-4 22-16 20-30C50 12 42 2 30 3z" fill="#008CFF"/>')

home = f"""
<section class="hero"><div class="wrap hero__grid">
  <div>
    <span class="selo">Pré-venda · lançamento em 23 de outubro de 2026</span>
    <h1>Um livro sobre <span class="l2">sair</span> <span class="l3">da casa pequena demais</span> para os seus sonhos.</h1>
    <p class="lede">Romance jovem-adulto de <strong>Camila Veloso</strong> sobre liberdade, família, primeiras vezes e a coragem de criar a vida que a gente sempre quis.</p>
    {BTN_COMPRA}
  </div>
  <div class="hero__capa">
    <img class="estrela" src="/assets/img/insignia-estrela.png" alt="" width="600" height="600">
    {CAPA}
  </div>
</div></section>

<div class="marquee" aria-hidden="true"><div class="marquee__in">{marq_html}</div></div>

<section class="sec"><div class="wrap duas">
  <div class="sinopse">
    <span class="eyebrow">A história</span>
    <h2>O Diário de Amélia</h2>
    <p class="abre">Aos dezoito anos, Amélia se sente sem graça, sem personalidade e tão confusa quanto as anotações nos seus cadernos do cursinho.</p>
    <p>Seus pais frequentam uma seita — mas, se você perguntar, ela vai dizer que é mentira — e, para eles, a filha deve aprender a servir, se casar com um membro da comunidade e manter-se longe de pensamentos impuros.</p>
    <p>O problema é que Amélia tem uma cabeça cheia de opiniões, pensamentos impuros e beijos imaginados com um certo colega. Em uma montanha-russa de primeiras vezes, lapsos de coragem e muitas queixas, ela vai descobrir que precisa confiar mais no seu coração para se libertar das expectativas dos pais.</p>
    <p><a href="/o-diario-de-amelia/">Ler a sinopse completa e conhecer o livro →</a></p>
  </div>
  <aside class="fichaq" aria-label="Para quem é este livro">
    <h3>Este livro é para você se…</h3>
    <ul class="paraquem">
      <li>Cresceu em um lar pequeno demais para os seus sonhos.</li>
      <li>Já se sentiu culpada por ter opinião própria.</li>
      <li>Procura um romance de amadurecimento com humor e coração apertado.</li>
      <li>Quer ler sobre liberdade, independência e recomeço.</li>
      <li>Ama histórias de autodescoberta e amizade.</li>
    </ul>
  </aside>
</div></section>

<section class="sec sec--marinho"><div class="wrap">
  <div class="sec__head"><span class="eyebrow">No que eu acredito</span>
   <p class="frase">Criatividade não é <em>habilidade</em>. É o que a gente é.</p></div>
  <div class="cards">
    <article class="card"><span class="card__n">01</span>{ICO1}<h3>Criatividade é característica</h3><p>Ninguém nasce sem ela. Criar é inerente ao ser humano — o que muda é o quanto nos deixaram usá-la.</p></article>
    <article class="card"><span class="card__n">02</span>{ICO2}<h3>A arte empodera</h3><p>Quem escreve, pinta, canta ou inventa deixa de ser plateia da própria vida e vira autora.</p></article>
    <article class="card"><span class="card__n">03</span>{ICO3}<h3>Liberdade é o ponto</h3><p>Para criar, é preciso poder errar, discordar e tentar o que ninguém aprovou. Amélia que o diga.</p></article>
  </div>
  <p style="margin-top:2rem"><a href="/manifesto/">Ler o manifesto completo →</a></p>
</div></section>

<section class="sec sec--papel"><div class="wrap">
  <div class="sec__head"><span class="eyebrow">Quem já leu</span><h2>Para rir e apertar o peito.</h2></div>
  <div class="citas">
    <figure class="cita" style="margin:0"><blockquote>“Um livro para rir, mas com o peito apertado do começo ao fim.”</blockquote><figcaption><cite>Karine Leôncio · Kabook TV</cite></figcaption></figure>
    <figure class="cita" style="margin:0"><blockquote>“História sobre autodescoberta e amizades, um abraço carinhoso.”</blockquote><figcaption><cite>Amanda Gambogi · autora</cite></figcaption></figure>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec__head"><span class="eyebrow">Meu trabalho</span><h2>Livros de Camila Veloso</h2>
   <p>Romance, crônicas e poesia: tudo nasce do mesmo lugar — a vontade de dar voz a quem foi ensinada a ficar quieta.</p></div>
  {{LIVROS_GRID}}
  <p style="margin-top:2rem"><a class="btn btn--vazado" href="/livros/">Ver todos os livros</a></p>
</div></section>

<section class="sec sec--roxo"><div class="wrap duas" style="align-items:center">
  <div class="foto-slot" role="img" aria-label="Espaço reservado para a foto de Camila Veloso"><img class="estrela" src="/assets/img/insignia-estrela.png" alt="" loading="lazy" width="600" height="600"></div>
  <div>
    <span class="eyebrow">A autora</span>
    <h2>Escritora, professora de escrita e fundadora da Aldeia Literária.</h2>
    <p>Camila cresceu em uma casa reservada e escolheu ser artista. Formada em Comunicação Social — Produção Editorial pela UFSM, já ensinou escrita a mais de 430 autores e comanda o podcast <em>Patricinha Literária</em>.</p>
    <div class="nums">
      <div class="num"><b>430+</b><span>autores ensinados</span></div>
      <div class="num"><b>5 mi</b><span>de alcance anual com conteúdo</span></div>
      <div class="num"><b>4</b><span>livros publicados</span></div>
    </div>
    <a class="btn btn--claro" href="/sobre/">Conhecer a Camila</a>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec__head"><span class="eyebrow">Leituras</span><h2>Conversas sobre liberdade, arte e crescer.</h2></div>
  {{LEITURAS}}
</div></section>

<section class="sec sec--sol"><div class="wrap" style="text-align:center;max-width:44rem">
  <h2>Chegou a hora de ler (e de escrever) a sua própria história.</h2>
  <p class="lede" style="color:#fff">Pré-venda aberta. O Diário de Amélia chega em 23 de outubro de 2026.</p>
  <div class="btns" style="justify-content:center">{link_ext(LINK_EDITORA, "Garantir o meu exemplar →", "btn btn--claro")}</div>
</div></section>
"""

LIVROS = [
    ("O Diário de Amélia", "Romance jovem-adulto · 2026", "Estreia no romance. Uma jovem de 18 anos e a coragem de criar a própria vida.", "c0", "/o-diario-de-amelia/", True),
    ("Encontrei um Pote com Tempo Dentro", "2022", "", "c2", None, False),
    ("Cartas ao Sol", "2021", "", "c3", None, False),
    ("Traumas de uma Grande Gostosa", "2021", "", "c4", None, False),
]

def livros_grid():
    out = ['<div class="livros">']
    for t, ano, d, cls, href, destaque in LIVROS:
        capa = (f'<img src="/assets/img/capa-diario-de-amelia.webp" alt="Capa de {esc(t)}" width="541" height="432" loading="lazy" style="object-fit:contain;padding:.6rem">'
                if destaque else f'<b>{esc(t)}</b><small>Camila Veloso</small>')
        tag = '<span class="tag">Pré-venda</span><br>' if destaque else ""
        inner = (f'<div class="livro__capa {cls}">{capa}</div><div>{tag}<h3>{esc(t)}</h3>'
                 f'<p>{esc(ano)}{(" — " + esc(d)) if d else ""}</p></div>')
        out.append(f'<a class="livro" href="{href}">{inner}</a>' if href else f'<div class="livro">{inner}</div>')
    out.append("</div>")
    return "".join(out)

def leituras_grid(excluir=None):
    out = ['<div class="leituras">']
    for a in ARTIGOS:
        if a["slug"] == excluir:
            continue
        out.append(f'<a class="leitura" href="/leituras/{a["slug"]}/"><h3>{esc(a["h1"])}</h3><p>{esc(a["resumo"])}</p><span class="mais">Ler →</span></a>')
    out.append("</div>")
    return "".join(out)

home = home.replace("{LIVROS_GRID}", livros_grid()).replace("{LEITURAS}", leituras_grid())
paginas.append(pagina("/", "Camila Veloso — Escritora | O Diário de Amélia, romance sobre liberdade",
    "Site oficial de Camila Veloso, autora de O Diário de Amélia: romance jovem-adulto sobre liberdade, autodescoberta e coragem. Pré-venda aberta. Conheça também o meu manifesto sobre criatividade e arte.",
    home, ld=[{"@type": "WebPage", "@id": SITE["dominio"] + "/#pagina", "url": SITE["dominio"] + "/", "name": "Camila Veloso — Escritora", "isPartOf": {"@id": SITE["dominio"] + "/#site"}, "about": {"@id": SITE["dominio"] + "/#camila"}}]))

# ---------------------------------------------------------------- O DIÁRIO DE AMÉLIA
FAQ = [
    ("Quando sai O Diário de Amélia?", "O lançamento da edição impressa pela Editora Fissura está previsto para 23 de outubro de 2026, com pré-venda aberta."),
    ("Onde comprar O Diário de Amélia?", "A pré-venda do livro físico está na loja da Editora Fissura. O e-book está disponível na Amazon Brasil."),
    ("Sobre o que é O Diário de Amélia?", "É um romance jovem-adulto sobre Amélia, uma garota de dezoito anos que cresce em uma família ligada a uma seita e precisa descobrir como se libertar das expectativas dos pais para criar a vida que quer."),
    ("Para quem é indicado?", "Para jovens e adultos que gostam de romances de amadurecimento (coming-of-age), histórias de autodescoberta, liberdade, independência, amizade e primeiros amores, com humor e emoção."),
    ("Quantas páginas tem e qual o formato?", "A edição impressa tem 250 páginas, formato brochura de 14 × 21 cm, miolo em papel Pólen 80 g/m² e capa em Cartão Supremo 300 g/m²."),
    ("Quem é a autora?", "Camila Veloso é escritora, formada em Comunicação Social — Produção Editorial pela UFSM, fundadora da Aldeia Literária e apresentadora do podcast Patricinha Literária."),
]
faq_html = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in FAQ)
book_ld = [
    {"@type": "Book", "@id": SITE["dominio"] + "/o-diario-de-amelia/#livro", "name": "O Diário de Amélia",
     "author": {"@id": SITE["dominio"] + "/#camila"}, "inLanguage": "pt-BR", "genre": ["Romance jovem-adulto", "Romance de amadurecimento"],
     "image": SITE["dominio"] + "/assets/img/og-diario-de-amelia.jpg",
     "description": "Romance sobre Amélia, de dezoito anos, que precisa se libertar das expectativas dos pais e de um ambiente familiar opressor para criar a vida que sempre quis.",
     "publisher": {"@type": "Organization", "name": "Editora Fissura", "url": "https://www.editorafissura.com.br/"},
     "datePublished": "2026-10-23",
     "workExample": [{"@type": "Book", "bookFormat": "https://schema.org/Paperback", "numberOfPages": 250, "inLanguage": "pt-BR",
        "datePublished": "2026-10-23",
        "offers": {"@type": "Offer", "url": LINK_EDITORA, "priceCurrency": "BRL", "price": "59.49", "availability": "https://schema.org/PreOrder", "itemCondition": "https://schema.org/NewCondition"}},
        {"@type": "Book", "bookFormat": "https://schema.org/EBook", "inLanguage": "pt-BR", "url": LINK_AMAZON}],
     "review": [{"@type": "Review", "author": {"@type": "Person", "name": "Karine Leôncio"}, "reviewBody": "Um livro para rir, mas com o peito apertado do começo ao fim."},
                {"@type": "Review", "author": {"@type": "Person", "name": "Amanda Gambogi"}, "reviewBody": "História sobre autodescoberta e amizades, um abraço carinhoso."}]},
    {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
    migalhas_ld([("/", "Início"), ("/o-diario-de-amelia/", "O Diário de Amélia")]),
]
book = f"""
<section class="pagina-topo"><img class="estrela-bg" src="/assets/img/insignia-estrela.png" alt="" width="460" height="460">
 <div class="wrap hero__grid" style="align-items:center">
  <div><nav class="migalha" aria-label="Você está em"><a href="/">Início</a> / O Diário de Amélia</nav>
   <span class="selo">Pré-venda · 23 de outubro de 2026</span>
   <h1>O Diário de Amélia</h1>
   <p class="lede">Um romance sobre quem cresceu em lar pequeno demais para os seus sonhos. <span class="serif-i">Um manual básico para jovens que querem mudar de vida, mas não sabem como.</span></p>
   {BTN_COMPRA}</div>
  <div class="hero__capa" style="min-height:360px">{CAPA}</div>
 </div></section>

<section class="sec"><div class="wrap duas">
 <div class="sinopse"><span class="eyebrow">Sinopse</span><h2>Uma montanha-russa de primeiras vezes</h2>
  <p class="abre">O Diário de Amélia é uma história para todos que cresceram em lares pequenos demais para os seus sonhos.</p>
  <p>Aos dezoito anos, Amélia se sente sem graça, sem personalidade e tão confusa quanto as anotações nos seus cadernos do cursinho. Seus pais frequentam uma seita — mas, se você perguntar, ela vai dizer que é mentira — e, para eles, a filha deve aprender a servir, se casar com um membro da comunidade e manter-se longe de pensamentos impuros.</p>
  <p>O problema é que Amélia tem uma cabeça cheia de opiniões, pensamentos impuros e beijos imaginados com um certo colega. Só que, aparentemente, a única forma de viver as aventuras que imagina é se tornando independente de seu ambiente familiar caótico e opressor.</p>
  <p>Em uma montanha-russa de primeiras vezes, lapsos de coragem e muitas queixas, Amélia vai descobrir que precisa confiar mais no seu coração se quiser se libertar das expectativas dos pais e criar a vida que ela sempre quis. E, de quebra, dar uns beijos no garoto que ela gosta.</p></div>
 <div>
  <aside class="fichaq"><h3>Ficha do livro</h3><dl class="ficha">
   <dt>Autora</dt><dd>Camila Veloso</dd><dt>Editora</dt><dd>Editora Fissura</dd>
   <dt>Gênero</dt><dd>Romance jovem-adulto (young adult)</dd><dt>Páginas</dt><dd>250</dd>
   <dt>Formato</dt><dd>Brochura, 14 × 21 cm</dd><dt>Lançamento</dt><dd>23 de outubro de 2026</dd>
   <dt>Pré-venda</dt><dd>R$ 59,49 <s style="opacity:.6">R$ 69,99</s></dd></dl>{BTN_COMPRA}</aside>
 </div>
</div></section>

<section class="sec sec--marinho"><div class="wrap duas">
 <div><span class="eyebrow">Temas</span><h2>Do que este livro fala</h2></div>
 <ul class="paraquem" style="color:var(--creme)">
  <li>Autodescoberta e independência</li><li>Família opressora e liberdade</li>
  <li>Amadurecimento e primeiras vezes</li><li>Amizade, humor e coragem</li><li>Criar a própria vida, escrevendo a própria história</li></ul>
</div></section>

<section class="sec sec--papel"><div class="wrap"><div class="citas">
 <figure class="cita" style="margin:0"><blockquote>“Um livro para rir, mas com o peito apertado do começo ao fim.”</blockquote><figcaption><cite>Karine Leôncio · Kabook TV</cite></figcaption></figure>
 <figure class="cita" style="margin:0"><blockquote>“História sobre autodescoberta e amizades, um abraço carinhoso.”</blockquote><figcaption><cite>Amanda Gambogi · autora</cite></figcaption></figure></div></div></section>

<section class="sec"><div class="wrap" style="max-width:48rem"><span class="eyebrow">Dúvidas</span><h2>Perguntas frequentes</h2>{faq_html}</div></section>

<section class="sec sec--sol"><div class="wrap" style="text-align:center;max-width:44rem">
 <h2>Amélia está esperando por você.</h2>{'' }
 <div class="btns" style="justify-content:center">{link_ext(LINK_EDITORA, "Garantir na pré-venda →", "btn btn--claro")}{link_ext(LINK_AMAZON, "Ler o e-book na Amazon", "btn btn--claro")}</div></div></section>
"""
paginas.append(pagina("/o-diario-de-amelia/", "O Diário de Amélia — romance de Camila Veloso | Pré-venda",
    "O Diário de Amélia, de Camila Veloso: romance jovem-adulto sobre liberdade, família opressora e primeiras vezes. 250 páginas, Editora Fissura. Pré-venda por R$ 59,49.",
    book, ld=book_ld, tipo="book"))

# ---------------------------------------------------------------- LIVROS
livros_pg = f"""
<section class="pagina-topo"><img class="estrela-bg" src="/assets/img/insignia-estrela.png" alt="" width="460" height="460"><div class="wrap">
 <nav class="migalha" aria-label="Você está em"><a href="/">Início</a> / Livros</nav>
 <span class="eyebrow">Obra</span><h1>Livros de Camila Veloso</h1>
 <p class="lede" style="max-width:40rem">Romance, crônicas e poesia sobre liberdade, corpo, tempo e coragem.</p></div></section>
<section class="sec"><div class="wrap">{livros_grid()}
 <p style="margin-top:2.5rem;color:var(--suave)">Em breve: sinopses, capas e links de compra de cada título.</p></div></section>
<section class="sec sec--marinho"><div class="wrap duas" style="align-items:center"><div><h2>Lançamento: O Diário de Amélia</h2><p>O primeiro romance de Camila Veloso chega em 23 de outubro de 2026.</p>{BTN_COMPRA}</div><div class="hero__capa" style="min-height:300px">{CAPA}</div></div></section>
"""
paginas.append(pagina("/livros/", "Livros de Camila Veloso — romance, crônicas e poesia",
    "Todos os livros de Camila Veloso: O Diário de Amélia, Encontrei um Pote com Tempo Dentro, Cartas ao Sol e Traumas de uma Grande Gostosa.",
    livros_pg, ld=[migalhas_ld([("/", "Início"), ("/livros/", "Livros")]),
                   {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": {"@type": "Book", "name": t, "author": {"@id": SITE["dominio"] + "/#camila"}}} for i, (t, *_r) in enumerate(LIVROS)]}]))

# ---------------------------------------------------------------- MANIFESTO
manifesto = f"""
<section class="pagina-topo"><img class="estrela-bg" src="/assets/img/insignia-estrela.png" alt="" width="460" height="460"><div class="wrap">
 <nav class="migalha" aria-label="Você está em"><a href="/">Início</a> / Manifesto</nav>
 <span class="eyebrow">Manifesto</span><h1>No que eu acredito</h1></div></section>
<section class="sec"><div class="wrap artigo">
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
    manifesto, ld=[migalhas_ld([("/", "Início"), ("/manifesto/", "Manifesto")])]))

# ---------------------------------------------------------------- SOBRE
sobre = f"""
<section class="pagina-topo"><img class="estrela-bg" src="/assets/img/insignia-estrela.png" alt="" width="460" height="460"><div class="wrap">
 <nav class="migalha" aria-label="Você está em"><a href="/">Início</a> / Sobre</nav>
 <span class="eyebrow">Sobre</span><h1>Oi, eu sou a Camila.</h1></div></section>
<section class="sec"><div class="wrap duas" style="align-items:center">
 <div class="foto-slot" role="img" aria-label="Espaço reservado para a foto de Camila Veloso"><img class="estrela" src="/assets/img/insignia-estrela.png" alt="" width="600" height="600"></div>
 <div class="sinopse"><p class="abre">Cresci em uma casa reservada e escolhi ser artista.</p>
  <p>Sou escritora, formada em Comunicação Social — Produção Editorial pela UFSM e fundadora da <strong>Aldeia Literária</strong>, onde já ensinei escrita a mais de 430 autores. Meu conteúdo alcança cerca de 5 milhões de pessoas por ano e eu apresento o podcast <em>Patricinha Literária</em>.</p>
  <p>Publiquei <em>Traumas de uma Grande Gostosa</em> (2021), <em>Cartas ao Sol</em> (2021) e <em>Encontrei um Pote com Tempo Dentro</em> (2022). <strong>O Diário de Amélia</strong> é o meu primeiro romance.</p>
  <p>Acredito em empoderamento através da arte, em liberdade e que criatividade é uma característica humana, não um talento raro.</p>
  <div class="btns"><a class="btn" href="/manifesto/">Ler o manifesto</a><a class="btn btn--vazado" href="/o-diario-de-amelia/">Conhecer o livro</a></div></div>
</div></section>
"""
paginas.append(pagina("/sobre/", "Sobre Camila Veloso — escritora, professora e fundadora da Aldeia Literária",
    "Camila Veloso é escritora, fundadora da Aldeia Literária, apresentadora do podcast Patricinha Literária e autora de O Diário de Amélia.",
    sobre, ld=[migalhas_ld([("/", "Início"), ("/sobre/", "Sobre")]), {"@type": "AboutPage", "url": SITE["dominio"] + "/sobre/", "about": {"@id": SITE["dominio"] + "/#camila"}}]))

# ---------------------------------------------------------------- LEITURAS
hub = f"""
<section class="pagina-topo"><img class="estrela-bg" src="/assets/img/insignia-estrela.png" alt="" width="460" height="460"><div class="wrap">
 <nav class="migalha" aria-label="Você está em"><a href="/">Início</a> / Leituras</nav>
 <span class="eyebrow">Leituras</span><h1>Conversas sobre liberdade, arte e crescer</h1></div></section>
<section class="sec"><div class="wrap">{leituras_grid()}</div></section>
"""
paginas.append(pagina("/leituras/", "Leituras: livros sobre liberdade, amadurecimento e criatividade",
    "Guias e reflexões sobre livros de liberdade e independência, romances de amadurecimento young adult e a ideia de que criatividade é inerente ao ser humano.",
    hub, ld=[migalhas_ld([("/", "Início"), ("/leituras/", "Leituras")])]))

for a in ARTIGOS:
    c = f"/leituras/{a['slug']}/"
    corpo = f"""
<section class="sec"><div class="wrap artigo">
 <nav class="migalha" aria-label="Você está em"><a href="/">Início</a> / <a href="/leituras/">Leituras</a></nav>
 <span class="eyebrow">Leituras</span><h1>{esc(a['h1'])}</h1>
 {a['corpo']}
 <aside class="cta-livro"><img src="/assets/img/capa-diario-de-amelia.webp" alt="Capa de O Diário de Amélia" width="541" height="432" loading="lazy">
  <div><h3>O Diário de Amélia</h3><p>Romance de Camila Veloso sobre liberdade, família e a coragem de criar a própria vida. Pré-venda aberta.</p>
  <a class="btn btn--claro" href="/o-diario-de-amelia/">Conhecer o livro →</a></div></aside>
 <h2>Continue lendo</h2>{leituras_grid(a['slug'])}
</div></section>"""
    ld = [{"@type": "Article", "headline": a["h1"], "description": a["desc"], "inLanguage": "pt-BR",
           "author": {"@id": SITE["dominio"] + "/#camila"}, "publisher": {"@id": SITE["dominio"] + "/#camila"},
           "datePublished": HOJE, "dateModified": HOJE, "mainEntityOfPage": SITE["dominio"] + c,
           "image": SITE["dominio"] + "/assets/img/og-diario-de-amelia.jpg"},
          migalhas_ld([("/", "Início"), ("/leituras/", "Leituras"), (c, a["h1"])])]
    paginas.append(pagina(c, a["titulo"] + " | Camila Veloso", a["desc"], corpo, ld=ld, tipo="article", atual="/leituras/"))

# ---------------------------------------------------------------- 404
nf = """<section class="sec"><div class="wrap" style="text-align:center;max-width:36rem">
<img src="/assets/img/insignia-virgula.png" alt="" width="120" height="150" style="margin:0 auto 1rem">
<h1>Essa página fugiu de casa.</h1><p class="lede">Mas a gente pode te ajudar a voltar.</p>
<div class="btns" style="justify-content:center"><a class="btn" href="/">Ir para o início</a></div></div></section>"""
pagina("/404.html".replace(".html", ""), "Página não encontrada | Camila Veloso", "Página não encontrada.", nf, noindex=True)
(ROOT / "404.html").write_text((ROOT / "404" / "index.html").read_text(encoding="utf-8"), encoding="utf-8")
import shutil; shutil.rmtree(ROOT / "404")

# ---------------------------------------------------------------- sitemap + robots
urls = "".join(f"<url><loc>{SITE['dominio']}{p}</loc><lastmod>{HOJE}</lastmod></url>" for p in paginas)
(ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n', encoding="utf-8")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE['dominio']}/sitemap.xml\n", encoding="utf-8")
print("OK:", len(paginas), "páginas")
