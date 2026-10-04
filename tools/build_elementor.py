#!/usr/bin/env python3
"""Gera o modelo de página do Elementor (JSON) da página de vendas da Aldeia Literária.

Uso:  python3 tools/build_elementor.py
Saída: wordpress/pagina-vendas-elementor.json

A página usa containers e widgets NATIVOS do Elementor (Título, Editor de Texto, Botão, Imagem,
Contador, Abas, Acordeão, HTML). Todo o visual vem das classes "av-*" (CSS do plugin).
"""
import hashlib
import json
import os

SITE = "https://aaldeialiteraria.com.br"
IMG = SITE + "/wp-content/plugins/aldeia-vendas/assets/img/"
WAIT = "https://tally.so/r/0QNWPy"          # formulário da lista de espera (o mesmo do site atual)
WHATS = "https://chat.whatsapp.com/ChsnBR1LbBW6pkZRI17hnw"
SOBRE = SITE + "/sobre/"

_n = [0]


def _id():
    _n[0] += 1
    return hashlib.md5(("av%d" % _n[0]).encode()).hexdigest()[:7]


def _link(url, external=False):
    return {"url": url, "is_external": "on" if external else "", "nofollow": "", "custom_attributes": ""}


def C(cls, children=None, row=False, tag=None, mobile_column=False):
    """Container (flexbox) em largura total."""
    # Atenção: em CONTAINERS o campo de classes se chama "css_classes" (nos widgets é "_css_classes").
    settings = {"content_width": "full", "flex_direction": "row" if row else "column", "css_classes": cls}
    if mobile_column:
        settings["flex_direction_mobile"] = "column"
    if tag:
        settings["html_tag"] = tag
    return {"id": _id(), "elType": "container", "settings": settings, "elements": children or [], "isInner": False}


def W(kind, settings, cls=""):
    s = dict(settings)
    if cls:
        s["_css_classes"] = cls
    return {"id": _id(), "elType": "widget", "widgetType": kind, "settings": s, "elements": []}


def H(text, tag="h2", cls="", url=None):
    s = {"title": text, "header_size": tag}
    if url:
        s["link"] = _link(url)
    return W("heading", s, cls)


def T(html, cls=""):
    return W("text-editor", {"editor": html}, cls)


def B(text, url, cls="av-btn"):
    return W("button", {"text": text, "link": _link(url, url.startswith("http") and SITE not in url), "size": "sm"}, cls)


def I(file_or_url, alt, cls=""):
    url = file_or_url if file_or_url.startswith("http") else IMG + file_or_url
    return W("image", {"image": {"url": url, "id": "", "alt": alt, "source": "library"}, "image_size": "full"}, cls)


def HTML(code, cls=""):
    return W("html", {"html": code}, cls)


def COUNTER(to, title, prefix="", suffix="", cls="av-stat"):
    return W("counter", {"starting_number": 0, "ending_number": to, "prefix": prefix, "suffix": suffix,
                         "duration": 1800, "title": title, "thousand_separator": ""}, cls)


def TABS(items, cls):
    return W("tabs", {"type": "vertical", "tabs": [{"_id": _id(), "tab_title": t, "tab_content": c} for t, c in items]}, cls)


def ACC(items, cls):
    return W("accordion", {"tabs": [{"_id": _id(), "tab_title": t, "tab_content": c} for t, c in items],
                           "title_html_tag": "h3", "faq_schema": "yes"}, cls)


PH = '<span class="av-ph">%s</span>'


def ph(t):
    return PH % t


def meander():
    """Faixa de meandro grego no topo da seção (widget HTML: não aparece como container vazio no editor)."""
    return HTML('<div class="av-meander av-meander--top"></div>', "av-meander-w")


def section(cls, children, wrap_cls="av-wrap", top_meander=False):
    kids = ([meander()] if top_meander else []) + [C(wrap_cls, children)]
    return C(cls, kids)


def _mark_inner(elements):
    """Containers aninhados precisam de isInner=True (o Elementor usa isso para e-child/e-parent)."""
    for e in elements:
        if e["elType"] == "container":
            e["isInner"] = True
        _mark_inner(e["elements"])


# ----------------------------------------------------------------------------------------------
# Conteúdo
# ----------------------------------------------------------------------------------------------
def build():
    _n[0] = 0
    S = []  # filhos do container principal (av-page)

    # Aviso + cabeçalho
    S.append(C("av-notice", [T("<p>Matrículas abrem em janeiro de 2027 · Lista de espera aberta · <strong>30 vagas</strong> por módulo</p>")]))
    S.append(C("av-header", [C("av-wrap av-row", [
        H("Aldeia Literária", "div", "av-logo", url=SITE + "/"),
        T('<p><a href="#jornada">Jornada</a><a href="#para-quem">Para quem é</a><a href="#duvidas">Dúvidas</a><a href="%s">Sobre</a></p>' % SOBRE, "av-nav"),
        B("Lista de espera", WAIT, "av-btn av-btn--sm"),
    ], row=True)]))

    # I · Hero
    S.append(C("av-hero", [C("av-wrap av-hero__grid", [C("av-hero__txt av-reveal", [
        H("Extensão universitária • Certificado MEC", "p", "av-badge"),
        H("Escrita Criativa:<br>Desenvolvimento e Prática", "h1", "av-h1"),
        T("<p>Formação online da Aldeia Literária para quem está começando. Aulas ao vivo, comunidade, feedback de mestres e doutores.</p>", "av-sub"),
        C("av-cta-row", [B("Entrar na lista da próxima turma", WAIT)], row=True),
        T("<p>Próxima turma: janeiro de 2027 · 30 vagas por módulo · aulas às 19h30 com gravação</p>", "av-hero__pay"),
    ])])]))

    # II · Números (contadores nativos)
    S.append(C("av-stats", [C("av-wrap", [C("av-stats__card av-reveal", [C("av-stats__grid", [
        C("av-stat-box", [COUNTER(500, "escritores já passaram pela Aldeia", prefix="+")]),
        C("av-stat-box", [COUNTER(4, "de aula ao vivo por mês<br>1 módulo · 3 aulas de 1h30", suffix="h30")]),
        C("av-stat-box", [COUNTER(9, "de aula ao vivo por mês<br>2 módulos · 6 aulas de 1h30", suffix="h")]),
        C("av-stat-box", [COUNTER(30, "vagas por módulo")]),
    ])])])]))

    # Livros escritos aqui (faixa de capas)
    books = [("querida-tia-liz", "Querida Tia Liz"), ("dois-lados-da-coroa", "Os Dois Lados da Coroa"), ("violeta", "Violeta"),
             ("dinamene-e-gavita", "Dinamene & Gavita"), ("ultimo-natal-com-ela", "O Último Natal com Ela"),
             ("melhores-anos", "Os Melhores Anos de Nossas Vidas"), ("resgate-de-muriel", "O Resgate de Muriel"),
             ("inconfidencia-da-magia", "A Inconfidência da Magia"), ("sombras-que-me-vestem", "As Sombras que me Vestem"),
             ("formula-encontro-perfeito", "A Fórmula do Encontro Perfeito"), ("perdida-em-teu-olhar", "Perdida em teu olhar"),
             ("desejei-as-estrelas", "Desejei às Estrelas"), ("estrelas-do-cosme-velho", "Estrelas do Cosme Velho"),
             ("quando-as-sombras-falam", "Quando as Sombras Falam")]
    S.append(C("av-books", [
        C("av-books__head av-center av-reveal", [H("Prova viva do método", "p", "av-label"), H("Livros escritos aqui", "h2", "av-h2")]),
        C("av-marquee", [C("av-marquee__track", [I("livro-%s.jpg" % f, "Capa do livro %s, escrito por aluno da Aldeia" % t, "av-book") for f, t in books], row=True)]),
    ]))

    # III · Problema (carrossel)
    problems = ["Você sabe como a história começa, mas não sabe como ela termina.",
                "Já começou vários rascunhos e nenhum chegou ao fim.",
                "Escreve sozinha ou sozinho e não sabe se o texto está bom.",
                "Sonha em publicar, mas não sabe por onde começar."]
    S.append(section("av-section", [
        C("av-reveal", [
            H("III · O problema", "p", "av-label"),
            H("Você tem a ideia. Falta a técnica.", "h2", "av-h2"),
            T("<p>Você abre o documento, escreve três parágrafos e a história volta pra gaveta. Acontece com muita gente que começa, e não é falta de talento. Todo livro é uma travessia longa, e toda travessia pede mapa, companhia e ritmo.</p>"),
            T("<p><strong>Se você se viu em alguma dessas linhas, o curso foi desenhado para esse ponto da jornada.</strong></p>", "av-mirror-close"),
        ]),
        C("av-reveal av-problems", [C("av-problems__stage", [C("av-problem", [T("<p>%s</p>" % p)]) for p in problems])]),
    ], wrap_cls="av-wrap av-mirror"))

    # IV · Jornada (Abas nativas)
    def mod(title, desc, learn, meta):
        return ("<h3>%s</h3><p>%s</p><h4>O que você aprende</h4><p>%s</p><h5>%s</h5>" % (title, desc, learn, meta))
    tabs = [
        ("Fundamentos da Narrativa", mod("Módulo I · Fundamentos da Narrativa", "Conceitos fundamentais de estruturação de narrativa e mercado editorial brasileiro.", "Você aprende a organizar a sua ideia e entender como desenvolver o seu personagem.", "Terça · 19h30 · com gravação")),
        ("Técnicas Avançadas", mod("Módulo II · Técnicas Avançadas", "Aulas teóricas e práticas com técnicas específicas de escrita criativa e produção de livros no Brasil.", "Você aprende a escrever boas descrições e diálogos, dentro de uma narrativa envolvente.", "Quarta · 19h30")),
        ("Processos criativos", mod("Módulo III · Processos criativos e Escrita Criativa", "Entenda como trabalhar com a criatividade, fugindo dos bloqueios criativos e outros problemas na escrita.", "Você aprende a lapidar suas ideias e entende os segredos do mercado editorial brasileiro.", "Segunda · 19h30")),
        ("Gramática e produção literária", mod("Módulo IV · Gramática e produção literária", "Estudo das normas gramaticais e sua aplicação na produção literária.", "A língua portuguesa é seu instrumento de trabalho. Aqui você relembra as regras essenciais para criar ritmo e criar uma voz única para o seu texto.", "Quinta · 19h30")),
        ("Publicação Independente", mod("Módulo V · Publicação Independente", "Conheça as melhores oportunidades, fornecedores e estratégias para escritores em início de carreira.", "Publicar o livro é uma das partes mais importantes e difíceis. Aqui você terá aulas de autopublicação e mercado editorial.", "Quarta · 19h30 · mesmo horário do Módulo II, em sala diferente")),
    ]
    S.append(section("av-section av-section--navy av-mark", [
        H("IV · O caminho", "p", "av-label"),
        H("Do chamado ao ponto final, um módulo por vez.", "h2", "av-h2"),
        T("<p>Cada módulo tem 3 aulas ao vivo por mês. Em cada etapa você aprende uma habilidade e sai com algo escrito.</p>", "av-lead"),
        TABS(tabs, "av-tabs av-reveal"),
    ], top_meander=True))

    # V · O que você leva + resumo com tabela
    table = ('<table class="av-table"><thead><tr><th scope="col"></th><th scope="col">1 módulo</th><th scope="col">2 módulos</th></tr></thead><tbody>'
             '<tr><th scope="row">Aulas ao vivo por mês</th><td>3</td><td>6</td></tr>'
             '<tr><th scope="row">Horas de aula por mês</th><td>4h30</td><td>9h</td></tr>'
             '<tr class="av-table__price"><th scope="row">Mensalidade</th><td>R$ 186</td><td>R$ 262</td></tr>'
             '<tr><th scope="row">Parcelas</th><td>11x</td><td>11x</td></tr>'
             '<tr><th scope="row">Investimento total</th><td>R$ 2.046</td><td>R$ 2.882</td></tr>'
             '</tbody></table>')
    S.append(section("av-section", [
        C("av-reveal", [
            H("V · O que está incluído", "p", "av-label"),
            H("Tudo o que você recebe ao entrar na Aldeia", "h2", "av-h2"),
            T("<ul><li><strong>Aulas ao vivo:</strong> 3 por mês em cada módulo, às 19h30, com 1h30 de duração.</li>"
              "<li><strong>Atividades com feedback individual:</strong> em cada atividade, você recebe um retorno personalizado sobre o seu texto.</li>"
              "<li><strong>Entrada no ecossistema da Aldeia Literária:</strong> comunidade e demais espaços dos alunos %s.</li>"
              "<li><strong>Bônus:</strong> palestras com psicólogas e profissionais do mercado editorial.</li></ul>" % ph("detalhar"), "av-check"),
            C("av-certcard", [
                I("certificados.jpg", "Aluna da Aldeia segurando um certificado"),
                C("av-certcard__txt", [H("Dois certificados na sua formação", "h4"),
                                       T("<p>Um ao final de cada módulo, com as competências e a carga horária, e, ao concluir a jornada completa, o certificado de extensão universitária emitido pela Anhanguera.</p>")]),
            ], row=True, mobile_column=True),
            C("av-btn-row", [B("Entrar na lista de espera", WAIT)]),
        ]),
        C("av-reveal av-sum", [
            H("Seu resumo · turma de 2027", "h3", "av-sum__ttl"),
            HTML(table, "av-table-w"),
            T("<p>Mais taxa de matrícula de R$ %s. Dois módulos saem R$ 110 por mês mais baratos do que dois planos de 1 módulo (2 × R$ 186 = R$ 372).</p>" % ph("M"), "av-small"),
            T("<p>%s</p>" % ph("confirmar nº de parcelas: o site atual usa 11x"), "av-small"),
            B("Entrar na lista de espera", WAIT, "av-btn av-btn--block"),
        ]),
    ], wrap_cls="av-wrap av-include"))

    # VI · Para quem é
    S.append(section("av-section av-section--soft", [
        H("VI · Para quem é", "p", "av-label"),
        H("Serve para o seu momento?", "h2", "av-h2"),
        C("av-fit", [
            C("av-reveal av-fit__card", [H("Esta jornada é para você se…", "h3"), T(
                "<ul><li>Quer escrever ficção (romance, fantasia, conto e afins) %s.</li><li>Está começando, ou já começou e travou no meio.</li>"
                "<li>Pode acompanhar aulas ao vivo às 19h30, três vezes por mês.</li><li>Topa praticar entre as aulas e receber feedback individual nas atividades.</li></ul>" % ph("ajustar gêneros"))]),
            C("av-reveal av-fit__card av-fit__card--no", [H("Talvez ainda não seja o momento se…", "h3"), T(
                "<ul><li>Procura uma fórmula pronta de best-seller. Aqui o caminho é feito de prática.</li>"
                "<li>Não consegue reservar tempo para as aulas e atividades agora. Sem problema: a próxima turma estará aqui.</li>"
                "<li>Quer escrever %s.</li></ul>" % ph("não ficção / roteiro / outro: confirmar escopo"))]),
        ]),
    ], top_meander=True))

    # VII · Quem conduz
    team = [("LM", "Laura Marques", "Produtora Editorial, mestranda em comunicação (UFSM) &amp; Leitora Crítica"),
            ("LO", "Lucas Oliveira", "Mestre e Doutor em Literatura Portuguesa (UFRJ)"),
            ("LN", "Lavínia Neres", "Produtora Editorial, Bacharel em Letras e Mestra em Comunicação (UFSM)"),
            ("AR", "Ana Ribeiro", "Produtora editorial e mestra em Estudos de Linguagens pelo CEFET-MG")]
    S.append(section("av-section", [
        C("av-author", [
            C("av-reveal av-portrait", [I("foto-camila-placeholder.png", "Foto da Camila Veloso (trocar pela foto real)")]),
            C("av-author__txt", [
                H("VII · Quem conduz", "p", "av-label"),
                H("Camila Veloso, fundadora da Aldeia Literária", "h2", "av-h2"),
                T("<p>Formada em Comunicação Social com habilitação em Produção Editorial pela UFSM, Camila criou a Aldeia nas redes sociais para ajudar escritores iniciantes a desenvolver e publicar seus livros. Hoje a Aldeia é uma escola e uma comunidade de quem escreve junto. %s</p>" % ph("conferir e ajustar à sua voz")),
            ]),
        ], row=True),
        C("av-team", [C("av-reveal av-team__item", [H(i, "div", "av-ava"), H(n, "h4"), T("<p>%s</p>" % d)]) for i, n, d in team]),
    ]))

    # VIII · Depoimentos + comunidade
    photos = [("comunidade-1.jpg", "Alunos da Aldeia Literária em evento, com ecobags da Aldeia"),
              ("comunidade-2.jpg", "Alunos da Aldeia Literária sorrindo em evento"),
              ("comunidade-3.jpg", "Alunas da Aldeia Literária juntas em evento"),
              ("comunidade-4.jpg", "Alunas da Aldeia Literária posando em evento")]
    quotes = ["frase com resultado específico: terminei meu primeiro rascunho…",
              "frase com resultado específico: tive coragem de enviar para editoras…",
              "frase ou print real de mensagem de aluno"]
    S.append(section("av-section av-section--navy av-mark av-mark--left", [
        H("VIII · Quem já atravessou", "p", "av-label"),
        H("Veja o que acontece quando o rascunho ganha caminho", "h2", "av-h2"),
        C("av-mosaic av-reveal", [I(f, a, "av-photo") for f, a in photos], row=True),
        T("<p>A comunidade Aldeia, ao vivo</p>", "av-mosaic-cap"),
        C("av-testi", [C("av-reveal av-quote", [
            T("<p>“%s”</p>" % ph(q)),
            C("av-quote__by", [C("av-face"), T("<p>%s</p>" % ph("Nome, cidade/UF"))], row=True)]) for q in quotes], row=True),
        HTML('<div class="av-video">▶ Vídeo curto de depoimento (troque este bloco por um widget Vídeo)</div>'),
    ], top_meander=True))

    # IX · Oferta
    S.append(section("av-section", [
        H("IX · Seu investimento", "p", "av-label"),
        H("Turma de janeiro de 2027", "h2", "av-h2"),
        C("av-reveal av-offer", [
            T("<p>Matrículas abrem em janeiro de 2027.<br>Por enquanto, temos apenas a lista de espera.</p>", "av-waitnote"),
            H("Mensalidade", "p", "av-class"),
            H("<small>a partir de</small> R$ 186<small>/mês</small>", "div", "av-price"),
            T("<p>1 módulo · 3 aulas por mês (4h30 de aula ao vivo)<br>ou <strong>R$ 262/mês</strong> com 2 módulos · 6 aulas por mês (9h)</p>"),
            T("<p>Investimento total: R$ 2.046 (1 módulo) ou R$ 2.882 (2 módulos), em 11 parcelas %s. Mais taxa de matrícula de R$ %s, que cobre a formulação do seu contrato e a sua entrada no ecossistema da Aldeia Literária.</p>" % (ph("confirmar nº de parcelas"), ph("M")), "av-small"),
            B("Entrar na lista de espera", WAIT, "av-btn av-btn--block"),
            T("<p>Pagamento: %s</p>" % ph("Pix e cartão em até X vezes"), "av-small"),
            C("av-box", [H("Transparência", "h4"), T("<p>Você lê o contrato completo antes de decidir %s. Ele prevê multa em caso de cancelamento antes do fim do curso: %s.</p>" % (ph("link"), ph("regra/valor")))]),
            C("av-box", [H("Garantia", "h4"), T("<p>%s</p>" % ph("texto da garantia conforme a decisão tomada (veja a nota do blueprint)"))]),
        ]),
    ], wrap_cls="av-wrap av-center", top_meander=True))

    # X · FAQ (Acordeão nativo)
    faq = [("Quando começa a turma?", "<p>Em janeiro de 2027.</p>"),
           ("Já posso me matricular?", "<p>Ainda não. As matrículas abrem em janeiro de 2027. Por enquanto, temos apenas a lista de espera.</p>"),
           ("Como são as aulas?", "<p>Ao vivo, 3 por mês em cada módulo, às 19h30, com 1h30 de duração. As aulas ficam gravadas. %s</p>" % ph("Por quanto tempo ficam disponíveis?")),
           ("Preciso ter algo escrito antes?", "<p>O curso é para quem está começando. Você não precisa ter nada pronto, só vontade de escrever ficção.</p>"),
           ("Quantas vagas existem?", "<p>30 por módulo.</p>"),
           ("Os módulos 2 e 5 têm o mesmo horário?", "<p>Sim, em salas diferentes. A jornada é organizada para você nunca precisar cursar os dois ao mesmo tempo.</p>"),
           ("Quanto custa?", "<p>Em 2027: R$ 186 por mês no plano de 1 módulo (3 aulas por mês) ou R$ 262 por mês no plano de 2 módulos (6 aulas por mês), mais a taxa de matrícula. %s</p>" % ph("confirmar nº de parcelas")),
           ("O que é a taxa de matrícula?", "<p>Ela cobre a formulação do seu contrato e a sua entrada no ecossistema da Aldeia Literária.</p>"),
           ("Posso cancelar?", "<p>Você pode pedir o cancelamento. O contrato prevê multa quando isso acontece antes do fim do curso. %s</p>" % ph("detalhar a regra")),
           ("Como as atividades são avaliadas?", "<p>Nas atividades, cada aluno recebe um feedback individual. %s</p>" % ph("explicar formato e nota mínima")),
           ("Como posso pagar?", "<p>%s</p>" % ph("Pix, cartão, parcelas")),
           ("Existe garantia?", "<p>%s</p>" % ph("texto conforme a decisão tomada"))]
    S.append(section("av-section av-section--soft", [
        H("X · Dúvidas", "p", "av-label"),
        H("Perguntas frequentes", "h2", "av-h2"),
        C("av-reveal av-faq", [ACC(faq, "av-accordion")]),
        C("av-btn-row av-btn-row--center", [B("Entrar na lista de espera", WAIT)]),
    ], wrap_cls="av-wrap av-center", top_meander=True))

    # XI · Chamado final
    S.append(C("av-final av-mark av-mark--left", [meander(), C("av-wrap", [
        H("XI · O chamado", "p", "av-label"),
        H("O chamado já chegou. Falta atravessar a porta.", "h2", "av-h2"),
        T("<p>A turma de janeiro de 2027 tem vagas limitadas: 30 por módulo. As matrículas abrem em janeiro; por enquanto, temos apenas a lista de espera. Se este é o seu momento de escrever o livro, a Aldeia te espera.</p>"),
        C("av-btn-row av-btn-row--center", [B("Entrar na lista de espera", WAIT)]),
        T('<p>Ficou com dúvida? <a href="%s">Fale com a gente no WhatsApp</a></p>' % WHATS, "av-small"),
    ])]))

    # Rodapé
    S.append(C("av-footer", [T('<p><a href="%s/">Home</a> · <a href="%s">Sobre</a></p><p>© Aldeia Literária · Curso de escrita para iniciantes · Todos os direitos reservados</p>' % (SITE, SOBRE))]))

    # Barra fixa (celular) + WhatsApp flutuante
    S.append(C("av-sticky", [B("Lista de espera", WAIT, "av-btn av-btn--block")]))
    S.append(HTML('<a class="av-wa" href="%s" aria-label="Falar no WhatsApp"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 13.9c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.6-3.9-4.7-4.1-.1-.2-1.1-1.5-1.1-2.8s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.1.1.3 0 .5l-.3.5-.4.5c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.1 1 2.1 1.3 2.4 1.4.3.1.5.1.6-.1l.9-1.1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.8-.1 1.4z"/></svg></a>' % WHATS, "av-wa-w"))

    page = C("av-page", S)
    _mark_inner(page["elements"])
    return {
        "version": "0.4",
        "title": "Aldeia Literária — Página de vendas (turma 2027) v2",
        "type": "page",
        "content": [page],
        "page_settings": {"hide_title": "yes"},
    }


if __name__ == "__main__":
    data = build()
    out = os.path.join(os.path.dirname(__file__), "..", "wordpress", "pagina-vendas-elementor.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    # confere ids únicos
    ids = []

    def walk(els):
        for e in els:
            ids.append(e["id"])
            walk(e["elements"])
    walk(data["content"])
    assert len(ids) == len(set(ids)), "ids duplicados"
    print("ok:", len(ids), "elementos ->", os.path.normpath(out))
