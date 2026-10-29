#!/usr/bin/env python3
"""Gera as páginas dos professores (HTML único, mesmo sistema visual da Home e da Sobre).

Uso:
  python3 tools/build_professores.py            -> só as prévias em preview/ (professor-*.html e professores.html)
  python3 tools/build_professores.py --wp       -> também os modelos do Elementor e os arquivos "colar no widget HTML" em wordpress/professores/

Regra de ouro: só entra na página o que está em PROFS (fatos verificados). Campos opcionais
(bio, ensina, links, formacao_extra) ficam de fora se estiverem vazios; na PRÉVIA aparece uma caixa
tracejada mostrando onde eles entrarão. A caixa não existe nos arquivos do WordPress.
"""
import json, os, sys, html
ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
import build_plugin

WP = "--wp" in sys.argv
SITE = "https://aaldeialiteraria.com.br"
PLUGIN_BASE = SITE + "/wp-content/plugins/aldeia-vendas/assets/"
FORM = "https://tally.so/r/0QNWPy"
ORG = "Aldeia Literária"
CURSO = "Escrita Criativa: Desenvolvimento e Prática"
UPDATED_TXT, UPDATED_ISO = "outubro de 2026", "2026-10-29"

# ---- Fatos verificados: Currículos Lattes enviados pelos próprios professores (PDF de 29/10/2026) + texto já publicado no site. ----
# Dados de contato (telefone, endereço) do Lattes NÃO são publicados.
LATTES = "http://lattes.cnpq.br/"
PROFS = [
 dict(slug="camila-veloso", nome="Camila Veloso", nome_completo="Camila Veloso", f=True, foto="prof-camila.jpg",
      papel="Fundadora da Aldeia Literária", cred="Produtora Editorial (UFSM)",
      job="Fundadora e CEO da Aldeia Literária", alma=["Universidade Federal de Santa Maria"],
      alt=["Camila Alves Veloso dos Santos", "VELOSO, C. A. S."],
      resumo="Camila Veloso é Produtora Editorial formada pela UFSM e fundadora da Aldeia Literária, curso de escrita criativa para escritores iniciantes. Atualmente cuida da administração do curso e mediação das aulas.",
      funcao_curso="Administração e mediação das aulas. Se você tiver dúvidas sobre o mercado editorial ou quiser conversar por whatsapp sobre algum exercício da Aldeia Literária, ou mesmo um feedback sobre o seu livro, você falará com ela.",
      atua="Camila Veloso é a fundadora da Aldeia Literária, cuida da administração do curso e faz a mediação das aulas",
      funcao="Fundadora e mediadora das aulas", formacao="Graduada em Comunicação Social – Produção Editorial (UFSM, 2020)",
      bio=["Camila Veloso foi bolsista de iniciação científica da FAPERGS em 2019, no grupo de estudos Consumo e Culturas Digitais. Fez mobilidade acadêmica na Universidad Autónoma de Tlaxcala, no México, onde estudou criatividade e tutoria educativa, matérias que a ajudaram a fundar a Aldeia Literária mais tarde. Também cursou disciplinas na pós-graduação da USP (2021 e 2026) e da UFSCar (2023), sobre séries televisivas, microeconomia e estudos de recepção.",
           "Antes da Aldeia, atuou como analista de conteúdo e de marketing (2021–2023), e o conhecimento adquirido no mundo corporativo foi essencial para a carreira no empreendedorismo.",
           "Em 2023, fundou a Aldeia Literária, baseada no Cohort Learning Method. Aqui, os alunos avançam juntos, em comunidade, e são guiados por mestres e doutores em literatura e produção editorial."],
      ensina=["Escrita criativa", "Produção editorial", "Criação de conteúdo e mídias digitais", "Narrativas audiovisuais"],
      destaques=["Prêmio Camaleão Dourado, da Coordenação do Curso de Produção Editorial da UFSM (2018)",
                 "Prêmio de melhor produção audiovisual para mídias digitais, no Intercom Sul (2020)"],
      links=[("Currículo Lattes", LATTES + "4829305175751173")], lattes="4829305175751173",
      imprensa=[("Aldeia Literária passa a ser um curso de extensão universitária", "PublishNews", "28 de agosto de 2024", "https://www.publishnews.com.br/materias/2024/08/28/aldeia-literaria-passa-a-ser-um-curso-de-extensao-universitaria/")]),
 dict(slug="laura-marques", nome="Laura Marques", nome_completo="Laura Marques", f=False, foto="prof-laura.jpg",
      papel="Professora de escrita criativa e leitora crítica", cred="Produtora Editorial, mestranda em comunicação (UFSM) & Leitora Crítica",
      job="Professora de escrita criativa e leitora crítica", alma=["Universidade Federal de Santa Maria", "Universidade do Vale do Rio dos Sinos"],
      alt=["Laura Simon Marques", "MARQUES, L. S."],
      resumo="Laura Marques é graduada em Comunicação Social – Produção Editorial pela UFSM, especialista em Relações Internacionais e Diplomacia pela UNISINOS e mestranda em Produção Editorial (UFSM). Trabalha como leitora crítica e dá aulas na Aldeia Literária.",
      funcao_curso="Aulas sobre estrutura da narrativa e de exercícios, ajudando os escritores a destravarem a escrita e fugirem de bloqueios criativos. Também faz palestras sobre leitura beta, leitura crítica e tendências do mercado editorial brasileiro.",
      funcao="Professora de escrita criativa e produção editorial", formacao="Graduada em Comunicação Social – Produção Editorial (UFSM, 2019); especialista em Relações Internacionais e Diplomacia (UNISINOS, 2021); Mestranda em Produção Editorial (UFSM, 2026)",
      formacao_faq="Graduada em Comunicação Social – Produção Editorial (UFSM, 2019); especialista em Relações Internacionais e Diplomacia (UNISINOS, 2021) e mestranda em Produção Editorial (UFSM, 2026)",
      bio=["Laura Marques é graduada em Comunicação Social – Produção Editorial pela Universidade Federal de Santa Maria (UFSM, 2019) e especialista em Relações Internacionais e Diplomacia pela UNISINOS (2021).",
           "Na UFSM, foi bolsista de iniciação científica em 2018, no projeto “Construção do feminino: do livro às redes sociais digitais”, que estudou como livros de referência sobre feminismo circulam e são usados nas redes sociais. Seu trabalho de conclusão de curso analisou o fenômeno editorial de “50 Tons de Cinza” e depois virou capítulo do livro Estudos Editoriais: série caleidoscópio (pE.com, 2023)."],
      ensina=["Escrita criativa", "Produção editorial", "Leitura crítica", "Estudos editoriais: best-sellers e mercado do livro"],
      destaques=["“50 Tons de um best-seller: o impacto de 50 Tons de Cinza no mercado editorial”, capítulo em Estudos Editoriais: série caleidoscópio (pE.com, 2023)",
                 "“As mulheres da capa: leitura das mudanças editoriais da GQ Magazine Brasil”, artigo na revista Animus (2022)",
                 "“Vai malandra: Anitta e as discussões no Twitter acerca da representatividade da mulher brasileira”, artigo na revista Cambiassu (2020)"],
      links=[("Currículo Lattes", LATTES + "2026357811720354")], lattes="2026357811720354", imprensa=[]),
 dict(slug="lucas-oliveira", nome="Lucas Oliveira", nome_completo="Lucas Laurentino de Oliveira", f=False, foto="prof-lucas.jpg",
      papel="Mestre e Doutor em Literatura Portuguesa (UFRJ)", cred="Mestre e Doutor em Literatura Portuguesa (UFRJ)",
      job="Professor de Escrita Criativa", alma=["Universidade Federal do Rio de Janeiro"],
      alt=["Lucas Laurentino de Oliveira", "OLIVEIRA, L. L.", "LAURENTINO, Lucas"],
      resumo="Lucas Oliveira é Doutor em Letras (Letras Vernáculas) pela UFRJ, na área de Literatura Portuguesa, com pesquisa sobre o poeta Jorge de Sena.",
      funcao_curso="Aulas de repertório teórico em literatura brasileira, diálogos, tom de voz e narração. Também traz exemplos de mangás e animes, mostrando técnica literária com viés contemporâneo.",
      funcao="Professor de Escrita Criativa", formacao="Doutor em Letras – Letras Vernáculas (UFRJ, 2025); mestre em Letras (UFRJ, 2020); graduado em Letras – Português e Literaturas de Língua Portuguesa (UFRJ, 2018)",
      bio=["Lucas Laurentino de Oliveira, conhecido como Lucas Oliveira, é Doutor em Letras (Letras Vernáculas) pela Universidade Federal do Rio de Janeiro, na área de Literatura Portuguesa. Defendeu em 2025 a tese “Pedagogia das testemunhas: leitura de Jorge de Sena enquanto professor”, com bolsa do CNPq. No mestrado (UFRJ, 2020), escreveu “Lampejos nos tempos sombrios: Hannah Arendt e Jorge de Sena”. Cursou a graduação em Letras – Português e Literaturas de Língua Portuguesa na mesma universidade (2018).",
           "Pesquisa poesia portuguesa do século XX, com foco em Jorge de Sena e na relação entre poesia e ensaio, e cultura pop, em especial o horror audiovisual. Administra o site Ler Jorge de Sena, dedicado a divulgar a obra e os estudos sobre o autor.",
           "Na UFRJ, foi professor convidado da pós-graduação em Letras Vernáculas (disciplina “Literatura e Cultura”, 2025) e professor auxiliar de Poesia Portuguesa III na graduação (2022–2023). Também é coautor do material de Língua Portuguesa do pré-vestibular da Fundação Cecierj e publicou o livro “Deixai vir a mim as criancinhas: a infância no espelho do horror” (Desalinho, 2022)."],
      ensina=["Literatura Portuguesa", "Poesia do século XX", "Jorge de Sena", "Cultura pop e estética do horror"],
      destaques=["Tese de doutorado “Pedagogia das testemunhas: leitura de Jorge de Sena enquanto professor” (UFRJ, 2025)",
                 "Livro “Deixai vir a mim as criancinhas: a infância no espelho do horror” (Desalinho, 2022)",
                 "“A tetralogia camoniana de Jorge de Sena”, artigo na Revista Convergência Lusíada (2025)",
                 "“A ‘esperança desesperada’ de Jorge de Sena ou os paradoxos da revolução”, capítulo em 25 de abril, 50 anos depois (Parábola, 2025)"],
      links=[("Currículo Lattes", LATTES + "7845502157662932"), ("ORCID", "https://orcid.org/0000-0002-5475-2000")], lattes="7845502157662932", imprensa=[]),
 dict(slug="lavinia-neres", nome="Lavínia Neres", nome_completo="Lavínia Neres Feronato", f=False, foto="prof-lavinia.jpg",
      papel="Produtora Editorial, Bacharel em Letras e Mestra em Comunicação (UFSM)", cred="Produtora Editorial, Bacharel em Letras e Mestra em Comunicação (UFSM)",
      job="Professora de Escrita Criativa", alma=["Universidade Federal de Santa Maria"],
      alt=["Lavínia Neres Feronato", "FERONATO, L. N."],
      resumo="Lavínia Neres é mestra em Comunicação pela UFSM, com pesquisa sobre leitura de livros digitais, e graduada em Produção Editorial e Letras (UFSM).",
      funcao_curso="Aulas de gramática focadas em construção de ritmo e construção de emoção. Ajuda os alunos a perceberem as possibilidades da língua portuguesa e o que ela oferece aos escritores como ferramenta.",
      funcao="Professora de Escrita Criativa", formacao="Mestra em Comunicação (UFSM, 2024); graduada em Comunicação Social – Produção Editorial (UFSM, 2019); graduada em Letras – Língua Portuguesa (UFSM)",
      bio=["Lavínia Neres Feronato, conhecida como Lavínia Neres, é mestra em Comunicação pela Universidade Federal de Santa Maria (UFSM, 2024), na linha Mídias e Identidades Contemporâneas. Sua dissertação, “Leituras em um clique: consumo e práticas de leitura de livros digitais”, foi orientada por Sandra Dalcul Depexe e contou com bolsa da CAPES. É graduada em Comunicação Social – Produção Editorial (2019) e em Letras – Língua Portuguesa, também pela UFSM.",
           "Pesquisa consumo cultural, leitura digital e mercado editorial, com estudos sobre o BookTok e sobre as tendências do campo editorial. Desde 2024, coordena a pesquisa “A portas fechadas: a gravidez na literatura”.",
           "Atua com revisão e edição de texto: integrou a Grámmatos Júnior, empresa júnior de revisão textual da UFSM (2021–2023), e fez os cursos Formação de Editor de Textos (2019) e Revisão Editorial (2026). Em 2022, apresentou a palestra “Publicando meu livro na Amazon: diário de uma escritora independente”."],
      ensina=["Leitura e consumo de livros", "Mercado editorial", "Revisão e edição de textos", "Literatura brasileira, gênero e narrativa"],
      destaques=["Dissertação “Leituras em um clique: consumo e práticas de leitura de livros digitais” (UFSM, 2024)",
                 "“Leitura de livro digital: consumo e acesso pela pirataria”, artigo na revista Eco-Pós (2024)",
                 "“Leitura e capitais editoriais: um estudo de caso da história em quadrinhos Arlindo”, artigo na Revista Latinoamericana de Ciencias de la Comunicación (2025)",
                 "“Festival de literatura pop: estratégias para o consumo de literatura jovem YA da Editora Seguinte”, capítulo em Estudos Editoriais: série caleidoscópio (pE.com, 2023)"],
      links=[("Currículo Lattes", LATTES + "8933104647688517")], lattes="8933104647688517", imprensa=[]),

 dict(slug="ana-ribeiro", nome="Ana Ribeiro", nome_completo="Ana Ribeiro", f=False, foto="prof-ana.jpg",
      papel="Professora de Escrita Criativa · Aldeia Literária", cred="Produtora editorial e mestra em Estudos de Linguagens pelo CEFET-MG",
      job="Professora de Escrita Criativa", alma=["Centro Federal de Educação Tecnológica de Minas Gerais"],
      resumo="Ana Ribeiro é Produtora Editorial e Mestra em Estudos de Linguagens pelo CEFET-MG. É professora do curso Escrita Criativa: Desenvolvimento e Prática, da Aldeia Literária, voltado a escritores iniciantes.",
      funcao="Professora de Escrita Criativa", formacao="Produtora editorial; mestra em Estudos de Linguagens (CEFET-MG)",
      bio=[], ensina=[], destaques=[], links=[], imprensa=[]),
]
E = html.escape
def url(p): return f"{SITE}/professores/{p['slug']}/"
def primeiro(p): return p["nome"].split()[0]
def art(p): return "a" if p["nome"].split()[0] in ("Camila","Laura","Lavínia","Ana") else "o"

def slot(msg):
    return "" if WP else f'<div class="pv-slot">{E(msg)}</div>'

def jsonld(d):
    return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + '</script>'

def header(active):
    return f'''<header class="av-header"><div class="av-wrap">
  <a class="av-logo" href="{SITE}/"><span>{ORG}</span></a>
  <nav class="av-nav" aria-label="Principal"><a class="av-nav__keep" href="{SITE}/">Início</a><a href="{SITE}/novo-sobre/">Sobre</a><a href="{SITE}/professores/">Professores</a></nav>
  <a class="av-btn" href="{FORM}">Entrar na lista de espera</a>
</div></header>'''

FOOTER = f'''<footer class="av-footer"><a href="{SITE}/">Início</a> · <a href="{SITE}/novo-sobre/">Sobre</a> · <a href="{SITE}/professores/">Professores</a><br>© {ORG} · Curso de escrita para iniciantes · Todos os direitos reservados</footer>'''

def person_ld(p, with_url=True):
    d = {"@type": "Person", "@id": url(p) + "#pessoa", "name": p["nome"], "jobTitle": p["job"],
         "description": p["resumo"], "image": f"{PLUGIN_BASE}img/{p['foto']}", "url": url(p),
         "worksFor": {"@type": "Organization", "name": ORG, "url": SITE + "/"},
         "alumniOf": [{"@type": "CollegeOrUniversity", "name": n} for n in p["alma"]]}
    if p.get("lattes"): d["identifier"] = {"@type": "PropertyValue", "propertyID": "Currículo Lattes", "value": p["lattes"]}
    if p["links"]: d["sameAs"] = [u for _, u in p["links"]]
    if p["ensina"]: d["knowsAbout"] = p["ensina"]
    return d

def card(p, cls=""):
    return (f'<article class="av-reveal av-tcard{cls}"><img src="assets/img/{p["foto"]}" alt="Foto de {p["nome"]}" loading="lazy" width="520" height="650">'
            f'<div class="av-tcard__txt"><h3>{p["nome"]}</h3><p>{p["cred"]}</p>'
            f'<a class="av-tmore" href="{url(p)}" aria-label="Ver o perfil de {p["nome"]}">Ver perfil</a></div></article>')

def page_prof(p):
    outros = [q for q in PROFS if q is not p]
    a = art(p)
    n, pn = p["nome"], primeiro(p)
    atua = p.get("atua") or f"{n} atua como {p['funcao'][0].lower() + p['funcao'][1:]} na {ORG}"
    ff = p.get("formacao_faq", p["formacao"])
    faq = [
      (f"Quem pode me ajudar a transformar a minha ideia em livro, sendo escritor iniciante?",
       f"A {ORG} é um curso on-line de escrita criativa feito para escritores iniciantes. {atua}. Lá, o professor que passa a atividade corrige o texto do aluno e ajuda a melhorá-lo."),
      (f"Qual é a formação de {n}?", f"{ff}."),
      ("Existe curso de escrita criativa para iniciantes com professores mestres e doutores?",
       f"Sim. O corpo docente da {ORG} inclui mestres e doutores, além de produtoras editoriais. Entre os integrantes está {n}: {ff[0].lower() + ff[1:]}."),
      (f"Em quais temas {n} é especialista?", f"Áreas de atuação de {n}: " + "; ".join(p["ensina"]) + "." ) if p["ensina"] else None,
      (f"Como funciona o curso {CURSO}?",
       f"São aulas ao vivo on-line, com três aulas por mês em cada módulo, e as gravações ficam disponíveis enquanto o aluno estiver matriculado. Cada módulo dura 6 meses. Há comunidade de escritores no WhatsApp, sprints de escrita e palestras com editores, revisores, agentes literários e escritores."),
      ("O curso dá certificado?", "Sim. Os alunos que finalizam o curso recebem um certificado de extensão universitária, emitido pela Anhanguera, parceira da Aldeia Literária."),
      ("Quando abre a próxima turma?",
       "As matrículas abrem em janeiro de 2027. Até lá, é possível entrar na lista de espera para ser avisado em primeira mão."),
    ]
    faq = [q for q in faq if q]
    fatos = [("Nome", p["nome"]), ("Formação", p["formacao"])]
    dl = "".join(f"<dt>{k}</dt><dd>{E(v)}</dd>" for k, v in fatos)
    fc = p.get("funcao_curso")
    if fc: dl += f"<dt>Função no curso</dt><dd>{E(fc)}</dd>"
    elif not WP: dl += f'<dt>Função no curso</dt><dd><div class="pv-slot">Aqui entra o que {primeiro(p)} faz no curso (aulas, temas, atendimento aos alunos).</div></dd>'
    dest = ('<h3 class="av-prose__h">Destaques</h3><ul>' + "".join(f"<li>{E(t)}</li>" for t in p["destaques"]) + '</ul>') if p.get("destaques") else ""
    imp = p.get("imprensa", [])
    imprensa = ('<h3 class="av-prose__h">Na imprensa</h3><ul>' + "".join(f'<li><a href="{u}" rel="noopener" target="_blank">{E(t)}</a> — {E(f)}, {E(d)}</li>' for t, f, d, u in imp) + '</ul>') if imp else ""
    links = ('<p class="av-prof__links"><strong>Perfis e publicações:</strong> ' + " · ".join(f'<a href="{u}" rel="me noopener" target="_blank">{E(t)}</a>' for t, u in p["links"]) + '</p>') if p["links"] else ""
    bio = ("".join(f"<p>{E(t)}</p>" for t in p["bio"]) or slot(f"Aqui entra a trajetória {'da' if a=='a' else 'do'} {primeiro(p)} em 2 a 4 parágrafos (formação, pesquisa, experiência com livros e escritores). Só fatos que você consegue comprovar."))
    ensina = ("<ul>" + "".join(f"<li>{E(t)}</li>" for t in p["ensina"]) + "</ul>") if p["ensina"] else slot(f"Aqui entram os temas e módulos que {primeiro(p)} ensina (lista curta, uma linha cada).")
    faqh = "".join(f'<details open><summary>{E(q)}</summary><div class="av-ans"><p>{E(r)}</p></div></details>' for q, r in faq)
    ld = {"@context": "https://schema.org", "@type": "ProfilePage", "dateModified": UPDATED_ISO,
          "mainEntity": person_ld(p), "url": url(p),
          "isPartOf": {"@type": "WebSite", "name": ORG, "url": SITE + "/"}}
    return f'''{header("prof")}
<main id="topo">
<section class="av-hero av-hero--prof"><div class="av-wrap av-hero__grid">
  <div class="av-reveal">
    <p class="av-breadcrumb"><a href="{SITE}/">Início</a> · <a href="{SITE}/professores/">Professores</a></p>
    <h1 class="av-h1">{p["nome"]}</h1>
    <p class="av-prof__role">{p["papel"]}</p>
    <p class="av-prof__summary">{E(p["resumo"])}</p>
  </div>
  <figure class="av-prof__photo av-reveal"><img src="assets/img/{p["foto"]}" alt="Foto de {p["nome"]}, {p["job"][0].lower() + p["job"][1:]}" width="520" height="650"></figure>
</div></section>

<section class="av-section"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Em resumo</h2>
  <dl class="av-facts av-reveal">{dl}</dl>
</div></section>

<section class="av-section av-section--soft"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Trajetória</h2>
  <div class="av-prose av-reveal">{bio}{dest}{links}{imprensa}</div>
  <h2 class="av-h2 av-reveal" style="margin-top:56px">Áreas de atuação</h2>
  <div class="av-prose av-reveal">{ensina}</div>
  <p class="av-updated">Página atualizada em {UPDATED_TXT}</p>
</div></section>

<section class="av-section"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Perguntas frequentes</h2>
  <div class="av-faq av-reveal">{faqh}</div>
</div></section>

<section class="av-section av-section--soft"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Conheça também</h2>
  <div class="av-pcards">{"".join(card(q) for q in outros)}</div>
</div></section>
</main>
{FOOTER}
{jsonld(ld)}'''

def page_hub():
    hf = [
      (f"Quem são os professores da {ORG}?", "O corpo docente reúne " + ", ".join(f"{q['nome']} ({q['cred']})" for q in PROFS) + "."),
      ("Existe curso de escrita criativa para iniciantes com professores mestres e doutores?", f"Sim. A {ORG} é um curso on-line de escrita criativa para escritores iniciantes, com professores mestres e doutores, aulas ao vivo e feedback individual nas atividades."),
      ("Quando abre a próxima turma?", "As matrículas abrem em janeiro de 2027. Até lá, é possível entrar na lista de espera."),
    ]
    hubfaq = "".join(f'<details open><summary>{E(q)}</summary><div class="av-ans"><p>{E(r)}</p></div></details>' for q, r in hf)
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": f"Professores da {ORG}",
          "url": SITE + "/professores/", "dateModified": UPDATED_ISO,
          "isPartOf": {"@type": "WebSite", "name": ORG, "url": SITE + "/"},
          "mainEntity": {"@type": "ItemList", "itemListElement": [
              {"@type": "ListItem", "position": i + 1, "url": url(p), "name": p["nome"]} for i, p in enumerate(PROFS)]}}
    return f'''{header("hub")}
<main id="topo">
<section class="av-hero av-hero--prof"><div class="av-wrap av-hero__grid" style="grid-template-columns:1fr">
  <div class="av-reveal">
    <p class="av-breadcrumb"><a href="{SITE}/">Início</a> · Professores</p>
    <h1 class="av-h1">Professores da {ORG}</h1>
    <p class="av-prof__summary">A {ORG} é um curso on-line de escrita criativa para escritores iniciantes, criado em 2023 por Camila Veloso. O corpo docente reúne mestres, doutores e produtoras editoriais que corrigem os seus textos e te ajudam a transformar a ideia em livro.</p>
    <div class="av-cta-row"><a class="av-btn" href="{FORM}">Entrar na lista de espera</a></div>
  </div>
</div></section>

<section class="av-section"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Quem ensina na {ORG}</h2>
  <div class="av-pcards av-pcards--5">{"".join(card(p, " av-tcard--founder" if p["f"] else "") for p in PROFS)}</div>
</div></section>

<section class="av-section av-section--soft"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Como é estudar na {ORG}</h2>
  <div class="av-prose av-reveal"><p>O curso <strong>{CURSO}</strong> tem aulas ao vivo, feedback individual do professor que passou a atividade, comunidade de escritores e palestras com profissionais do mercado editorial. Cada módulo dura 6 meses e o certificado de extensão universitária é emitido pela Anhanguera.</p>
  <p>As matrículas abrem em janeiro de 2027. <a href="{SITE}/novo-sobre/">Conheça a história da escola</a> ou <a href="{FORM}">entre na lista de espera</a>.</p></div>
  <p class="av-updated">Página atualizada em {UPDATED_TXT}</p>
</div></section>

<section class="av-section"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Perguntas frequentes</h2>
  <div class="av-faq av-reveal">{hubfaq}</div>
</div></section>
</main>
{FOOTER}
{jsonld(ld)}'''

PV_CSS = ".pv-slot{border:2px dashed #CC351C;border-radius:16px;padding:18px 22px;color:#A82B16;background:rgba(204,53,28,.05);font:600 13px/1.5 Montserrat,sans-serif;max-width:760px}"
css_base = open(os.path.join(ROOT, "wordpress/aldeia-vendas.css"), encoding="utf-8").read()
js = open(os.path.join(ROOT, "wordpress/aldeia-vendas.js"), encoding="utf-8").read()

def local(s):  # na prévia, os links entre as páginas abrem os arquivos locais
    for p in PROFS: s = s.replace(url(p), f"professor-{p['slug']}.html")
    return s.replace(SITE + "/professores/", "professores.html").replace(SITE + "/novo-sobre/", "sobre.html").replace(f'href="{SITE}/"', 'href="vendas.html"')

def preview(title, body, name):
    doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><link rel="stylesheet" href="assets/fonts.css">
<style>body{{margin:0}}{css_base}:root{{--av-hero-img:url("assets/hero.jpg");--av-hero-img-m:url("assets/img/hero-mobile.jpg");--av-medal:url("assets/logo-medalhao.png")}}{PV_CSS}</style></head><body class="av-page" id="top">{local(body)}<script>{js}</script></body></html>'''
    open(os.path.join(ROOT, "preview", name), "w", encoding="utf-8").write(doc)

pages = [(f"{p['nome']} · professor{'a' if art(p)=='a' else ''} da {ORG}", page_prof(p), f"professor-{p['slug']}.html", p) for p in PROFS]
pages.append((f"Professores da {ORG}", page_hub(), "professores.html", None))
for t, b, n, _ in pages: preview(t, b, n)
print("prévias:", len(pages))

if WP:
    out = os.path.join(ROOT, "wordpress/professores"); os.makedirs(out, exist_ok=True)
    inline_css = build_plugin.build_css().replace("../fonts/", PLUGIN_BASE + "fonts/").replace("../img/", PLUGIN_BASE + "img/")
    fix = ('<style>.e-con:has(>.elementor-widget-html .av-page){--padding-top:0px;--padding-right:0px;--padding-bottom:0px;--padding-left:0px;--gap:0px;--row-gap:0px;--column-gap:0px;--margin-top:0px;--margin-bottom:0px}'
           '.elementor-widget-html:has(>.av-page),.elementor-widget-html:has(.av-page){margin:0}</style>\n')
    zero = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
    for t, b, n, p in pages:
        slug = p["slug"] if p else "lista"
        frag_body = b.replace('src="assets/img/', 'src="' + PLUGIN_BASE + 'img/')
        assert 'src="assets/' not in frag_body and "pv-slot" not in frag_body
        frag = (f'<!-- aldeia-professor-{slug}-v1 -->\n<style>{inline_css}</style>\n{fix}<div class="av-page">\n{frag_body}\n</div>\n<script>{js}</script>\n')
        open(os.path.join(out, f"{slug}-colar-no-widget-html.html"), "w", encoding="utf-8").write(frag)
        tpl = {"version": "0.4", "title": f"ALDEIA Professor — {p['nome'] if p else 'Lista'}", "type": "page",
               "content": [{"id": "b1c2d3e", "elType": "container", "isInner": False,
                            "settings": {"content_width": "full", "flex_direction": "column", "padding": zero, "margin": zero},
                            "elements": [{"id": "f4a5b6c", "elType": "widget", "widgetType": "html", "settings": {"html": frag}, "elements": []}]}],
               "page_settings": {"hide_title": "yes"}}
        json.dump(tpl, open(os.path.join(out, f"{slug}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wordpress/professores/: ok")
