# Aulão Universal: identidade visual e estrutura (para reaproveitar em outros projetos)

Página de vendas curta, pensada para celular. Gerada por `build_aulao.py` (conteúdo), `aulao.css` (visual) e `aulao.js` (contagem, carrossel).
Prévia local: `preview/aulao-universal.html`. Para regenerar: `python3 tools/aulao-universal/build_aulao.py`.

## Cores (tokens em `:root` de `aulao.css`)
| Token | Valor | Uso |
|---|---|---|
| `--paper` | `#ffffff` | cartões, fundo de capa |
| `--cream` | `#f6f1ec` | fundo da página |
| `--navy` | `#083656` | seções escuras, selos, bordas do cartão de oferta |
| `--navy-deep` | `#062a44` | faixa fixa do topo, rodapé |
| `--ink` | `#111111` | texto e títulos |
| `--lilac` | `#e8dcfb` | grifa-texto, cartões em destaque, fichas |
| `--violet` | `#6d28d9` | botão principal, ícones, acento |
| `--violet-light` | `#c9b2f2` | pontos, números, detalhes sobre azul |
| `--muted` | `#3a5568` | texto secundário |

Os tons vêm dos slides do Aulão Universal. O vermelho `#cc341b` do Aulão Master foi trocado por lilás e roxo.

## Tipografia
- Títulos: **Outfit** 700 e 800, espaçamento `-0.03em` a `-0.04em`.
- Texto: **Figtree** 400, 500 e 700.
- Frase-chave: Outfit 600, com marcador lilás atrás do texto (`.am-hl`).
- Arquivos das fontes em `preview/aulao/fonts/` (woff2).

## Componentes
- **Faixa fixa do topo** (`.am-alert`): "A promoção acaba em:" + cronômetro + botão "QUERO O AULÃO". Depois da data final vira "A promoção terminou. Valor atual: R$ 100".
- **Hero centralizado:** logo, selo escuro, título grande, frase grifada, linha da autora, botão.
- **Cartões de benefícios** (`.am-benefits`): ícone roxo com check; os destacados (`.is-hot`) em lilás.
- **Seção escura** (`.am-dark`, azul-marinho): lista numerada de partes (`.am-parts`).
- **Cartão de oferta** (`.am-offer`): benefícios, depois botão "Ver o preço" (`<details>`), que revela o preço, o botão de compra e o bônus.
- **Carrossel de fotos** (`.am-carousel`): rolagem com encaixe, setas e rolagem automática lenta.
- **FAQ** em `<details>`, **rodapé** com razão social e CNPJ.

## Regras de comportamento
- Coluna única de 640px; no celular tudo em 1 coluna; área segura do iPhone respeitada.
- Promoção: R$ 67 até 30/11 às 23h59 (horário de Brasília); depois R$ 100. A troca é automática no navegador (`aulao.js`, classes `.am-promo` e `.am-regular`).
- Bônus do 1º dia some às 23h59 de 23/11.
- Sem rolagem lateral; respeita "reduzir movimento".

## Pendências conhecidas
- Link do checkout: constante `CHECKOUT` em `build_aulao.py` (hoje aponta para `#oferta`).
- Confirmar: prazo de 1 ano, "+400 escritores", reembolso de 7 dias, autorização de uso das fotos.
