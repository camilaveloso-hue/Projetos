# Página de vendas — como montar no Elementor (baseado no Blueprint v1)

Arquivos: `aldeia-vendas.css` (visual) · `aldeia-vendas.js` (abas, contadores, barra fixa) · `../preview/vendas.html` (prévia).

## 1. Instalação
1. **Fontes**: Cinzel (700), EB Garamond (400/600/italic), Montserrat (500/600/700). Elementor → Configurações do Site → Fontes Globais (ative o carregamento local).
2. **CSS**: cole `aldeia-vendas.css` em Configurações do Site → CSS Personalizado.
3. Na página de vendas: Configurações da Página → Avançado → **Classes CSS = `av-page`** (isso isola o estilo: o resto do site não muda).
4. **JS**: widget HTML no fim da página com `<script>` + conteúdo de `aldeia-vendas.js` + `</script>` (necessário só para a barra fixa; Tabs/Counter/Accordion nativos do Elementor dispensam o resto).
5. Cores globais: azul-marinho `#1B2A41`, terracota `#B5533C` (só botões de compra), terracota escura `#9C4430`, bronze `#A67C37` (só decoração), pergaminho `#F4EBDD`, grafite `#2B2B2B`.

## 2. Seção → classes (Avançado → Classes CSS)
| Seção | Container / classe | Widgets |
|---|---|---|
| Barra de aviso | `av-notice` | Texto |
| Menu | `av-header` > `av-wrap`; links `av-nav`; botão `av-btn` | Nav Menu + Botão (4 âncoras: Jornada, Para quem é, Investimento, Dúvidas) |
| I Hero | `av-hero` > `av-wrap av-hero__grid` (texto à esquerda; a imagem entra por CSS, variável `--av-hero-img` = a imagem atual do site) | Selo `av-badge`, H1 `av-h1` (uma linha por `span`), subtítulo `av-sub`, botão `av-btn`, nota `av-hero__pay` |
| II Números | `av-stats` (sobe sobre o hero) > `av-stats__card` > `av-stats__grid` | 4× Counter (`av-stat`) |
| III Espelho | `av-section` > `av-mirror` | Heading + Icon List `av-quill` (ícone pena, bronze) |
| IV Jornada | `av-section av-section--navy`; `av-tabs` | Tabs (vira acordeão no celular); título da aba com numeral romano |
| V O que você leva | `av-include`; lista `av-check`; cartão `av-sum` | Icon List (check bronze) |
| VI Para quem é | `av-fit` com 2× `av-fit__card` (o 2º `av-fit__card--no`) | Icon List |
| VII Quem conduz | `av-author`; foto em `av-portrait`; equipe `av-team` | Imagem, Texto |
| VIII Depoimentos | `av-section--navy`; `av-testi` > `av-quote` | Testimonial Carousel (Pro) ou 3 cartões; Vídeo |
| IX Oferta | `av-offer` (600 px) com `av-price`, `av-box` | Heading, Botão `av-btn av-btn--block` |
| X FAQ | `av-faq` (800 px) | Accordion (+ FAQ Schema, Pro) |
| XI Chamado final | `av-final` + `av-meander av-meander--top` | Heading, Botão |
| Barra fixa (celular) | `av-sticky` | HTML (botão); aparece após o hero |
| WhatsApp flutuante | `av-wa` | HTML, link `https://wa.me/55DDDNUMERO?text=...` |
| Divisória meandro | `av-meander` | Widget HTML vazio ou fundo do container |

Botão de compra repetido em 4 pontos (hero, após "O que você leva", oferta, chamado final), sempre `av-btn`, mesmo texto e cor.

## 2b. Toques modernos (opcionais)
- **Revelação ao rolar:** adicione `av-reveal` em qualquer bloco (cartões, colunas, tabs). Só esconde o bloco se o JS estiver ativo; respeita "reduzir movimento".
- **Cantos arredondados, vidro fosco nos painéis azuis, meandro como marca sob os títulos e cartão de números flutuante** já vêm no CSS.
- **Cabeçalho branco translúcido** (igual ao atual do site), com o botão "Garantir minha vaga".

## 3. Conferido no preview
Contraste: botão branco/terracota 4,9:1; texto/pergaminho passa AA; bronze nunca em texto pequeno. Alvos de toque ≥ 44 px. Sem rolagem horizontal em 390 px. Respeita "reduzir movimento".

## 4. Pendências (marcadas em amarelo `av-ph` na prévia — apague a classe ao preencher)
Preço, parcelas, à vista, taxa de matrícula e formas de pagamento · por quanto tempo as aulas ficam gravadas · formato e nota mínima das atividades · garantia (veja a nota jurídica no blueprint) · multa de cancelamento e link do contrato · depoimentos reais (nome, cidade, foto) · foto da Camila · gêneros/escopo do curso · logo e meandro oficiais.

## 4b. Lista de espera (até as matrículas abrirem, em janeiro de 2027)
Todos os botões levam ao formulário da lista de espera (`https://tally.so/r/0QNWPy`, o mesmo do site atual) e o texto é "Entrar na lista de espera". O cartão de oferta tem o aviso `av-waitnote`. Quando as matrículas abrirem, troque o link e os textos dos botões pelo checkout e remova o aviso. O menu tem as 2 páginas do site: esta (Home, com âncoras) e Sobre.

## 5. Divergências entre o blueprint e o site atual (decidir antes de publicar)
- **Vagas:** blueprint diz ~50 por módulo; o site e o hero escolhido dizem 30. A prévia usa **30** em toda a página (aviso, números, FAQ, chamado final). Confirme.
- **Parcelas:** blueprint prevê 12x; o site hoje cobra 11x (R$ 177 / R$ 270).
- **Gravação:** o site hoje diz "gravação em até 48h"; o blueprint deixa em aberto.
- **Atividades:** o site fala em nota mínima em 75% das atividades (requisito do MEC); no blueprint isso está em aberto.
- **Equipe e módulos:** usei os nomes de professores e módulos do site atual, que o blueprint pede.
