# Página de vendas — como montar no Elementor (baseado no Blueprint v1)

Arquivos: `aldeia-vendas.css` (visual) · `aldeia-vendas.js` (abas, contadores, barra fixa) · `../preview/vendas.html` (prévia).

## 1. Instalação
1. **Fontes**: Cinzel (700), EB Garamond (400/600/italic), Montserrat (500/600/700). Elementor → Configurações do Site → Fontes Globais (ative o carregamento local).
2. **CSS**: cole `aldeia-vendas.css` em Configurações do Site → CSS Personalizado.
3. Na página de vendas: Configurações da Página → Avançado → **Classes CSS = `av-page`** (isso isola o estilo: o resto do site não muda).
4. **JS**: widget HTML no fim da página com `<script>` + conteúdo de `aldeia-vendas.js` + `</script>` (necessário só para a barra fixa; Tabs/Counter/Accordion nativos do Elementor dispensam o resto).
5. Cores globais (tiradas da logo): azul `#0D3756`, vermelho `#CC351C` (botões e acentos), vermelho escuro `#A82B16` (textos), branco `#FFFFFF`, cinza-azulado claro `#F1F5F9` (seções alternadas), grafite `#26303B`.

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

## 2a. Novos blocos (versão com logo, imagens e carrossel)
| Bloco | Classes | Como fazer no Elementor |
|---|---|---|
| Faixa de capas (logo após os números) | `av-books` > `av-marquee` > `av-marquee__track` > vários `av-book` | Container + imagens (as capas já estão na Biblioteca de Mídia do site, `uploads/2026/07/…`). O JS duplica os itens para o loop. |
| Problemas em carrossel | `av-problems` com `data-av-carousel` (widget HTML) contendo `av-medal`, `av-problem` ×4 e os controles | Cole o HTML da prévia (seção III) em um widget HTML. O medalhão usa a variável `--av-medal` (logo atual do site). |
| Resumo com tabela de preços | `av-sum` > `av-table` | Widget HTML (tabela) ou Elementor Pro "Price Table". |
| Certificados | `av-certcard` | Imagem + texto lado a lado. |
| Mosaico da comunidade | `av-mosaic` (4 `figure`) | Fotos de evento do próprio site; usar texto alternativo descritivo. |
| Equipe | `av-team` > `av-team__item` com `av-ava` | 4 cartões (Laura, Lucas, Lavínia, Ana). Quando houver fotos, troque o `av-ava` por `<img>`. |
| Marca d'água do medalhão | `av-mark` (e `av-mark--left`) na seção | Só uma classe. |
| Fundo alternativo texturizado | `av-section--soft` | Só uma classe. |

Texturas: grão de papel sutil em todo o fundo e labirinto grego a 5% nas seções `--soft` (ambos em SVG dentro do CSS, sem imagens extras). Botões são pílula com seta.

## 2b. Toques modernos (opcionais)
- **Revelação ao rolar:** adicione `av-reveal` em qualquer bloco (cartões, colunas, tabs). Só esconde o bloco se o JS estiver ativo; respeita "reduzir movimento".
- **Cantos arredondados, vidro fosco nos painéis azuis, meandro como marca sob os títulos e cartão de números flutuante** já vêm no CSS.
- **Cabeçalho branco translúcido** (igual ao atual do site), com o botão "Garantir minha vaga".

## 3. Conferido no preview
Contraste: botão branco/terracota 4,9:1; texto/pergaminho passa AA; bronze nunca em texto pequeno. Alvos de toque ≥ 44 px. Sem rolagem horizontal em 390 px. Respeita "reduzir movimento".

## 4. Pendências (marcadas em amarelo `av-ph` na prévia — apague a classe ao preencher)
Nº de parcelas, taxa de matrícula e formas de pagamento · por quanto tempo as aulas ficam gravadas · formato e nota mínima das atividades · garantia (veja a nota jurídica no blueprint) · multa de cancelamento e link do contrato · depoimentos reais (nome, cidade, foto) · foto da Camila · gêneros/escopo do curso · logo e meandro oficiais.

## 4a. Preços e horas (turma 2027)
1 módulo: 3 aulas/mês × 1h30 = **4h30/mês**, R$ 186/mês. 2 módulos: 6 aulas/mês = **9h/mês**, R$ 262/mês. Total = mensalidade × parcelas: com **11 parcelas** (o número usado no site atual) dá R$ 2.046 e R$ 2.882. **Confirme o nº de parcelas** (o blueprint falava em 12x: seriam R$ 2.232 e R$ 3.144) e a taxa de matrícula. Os números estão em dois lugares: tabela "Seu resumo" e cartão da seção IX (e FAQ "Quanto custa?").

## 4b. Lista de espera (até as matrículas abrirem, em janeiro de 2027)
Todos os botões levam ao formulário da lista de espera (`https://tally.so/r/0QNWPy`, o mesmo do site atual) e o texto é "Entrar na lista de espera". O cartão de oferta tem o aviso `av-waitnote`. Quando as matrículas abrirem, troque o link e os textos dos botões pelo checkout e remova o aviso. O menu tem as 2 páginas do site: esta (Home, com âncoras) e Sobre.

## 5. Divergências entre o blueprint e o site atual (decidir antes de publicar)
- **Vagas:** blueprint diz ~50 por módulo; o site e o hero escolhido dizem 30. A prévia usa **30** em toda a página (aviso, números, FAQ, chamado final). Confirme.
- **Parcelas:** blueprint prevê 12x; o site hoje cobra 11x (R$ 177 / R$ 270).
- **Gravação:** o site hoje diz "gravação em até 48h"; o blueprint deixa em aberto.
- **Atividades:** o site fala em nota mínima em 75% das atividades (requisito do MEC); no blueprint isso está em aberto.
- **Equipe e módulos:** usei os nomes de professores e módulos do site atual, que o blueprint pede.
