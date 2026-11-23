# AULÃO UNIVERSAL: identidade visual e estrutura (para reaproveitar em outros projetos)

Página de vendas curta, pensada para celular. Gerada por `build_aulao.py` (conteúdo e relevo), `aulao.css` (visual) e `aulao.js` (contagem, carrossel).
Prévia local: `preview/aulao-universal.html`. Para regenerar: `python3 tools/aulao-universal/build_aulao.py`.

## Identidade (a da versão curta, baseada na OliNews)
- Fundo creme `#fdfaec`, texto `#09090a`, seções escuras em preto.
- Azul escuro da Aldeia `#0D3756` nos ícones e detalhes; azul claro `#d9e8f5` nos cartões em destaque, no grifo e nas montanhas; amarelo `#ffd60a` nos botões e destaques sobre o escuro.
- Títulos em **Playfair Display** 900; texto em **DM Sans**. Fontes em `preview/aulao-v3/fonts/`.
- Frase-chave grifada em azul claro (`.am-hl`).

## Relevo de montanhas
Três cordilheiras sobrepostas, desenhadas em SVG pela função `mountains()` em `build_aulao.py` e embutidas no CSS como fundo (`{MTN_LIGHT}` e `{MTN_DARK}`).
- Versão clara (azul claro sobre creme): rodapé do topo da página.
- Versão escura (branco translúcido e traço azul claro sobre preto): seção "Na aula, 6 partes", carrossel de fotos e chamada final.
- Para usar em outra seção, adicione as classes `am-mtn am-mtn--light` ou `am-mtn am-mtn--dark`.
- Para mudar o desenho, altere os parâmetros (semente, base, altura, largura) em `mountains()`.

## Componentes
Faixa fixa do topo com cronômetro e botão, hero, cartões de benefícios, lista das 6 partes, cartão de oferta com "Ver o preço" (`<details>`), bio, carrossel, FAQ, chamada final e rodapé.

## Regras
- R$ 70 até 30/11 às 23h59 (Brasília); depois R$ 100, troca automática (`aulao.js`). O bônus (R$ 70 de desconto na matrícula da Aldeia) vale para quem comprar até 30/11 e some junto com a promoção.
- Coluna de 640px, sem rolagem lateral, respeita "reduzir movimento".

## Pendências
Link do checkout (`CHECKOUT` em `build_aulao.py`); confirmar prazo de 1 ano, "+400 escritores", reembolso de 7 dias e autorização das fotos.
