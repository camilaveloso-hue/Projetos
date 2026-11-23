# AULÃO UNIVERSAL no site: atualização v2 (página para buscadores e IAs)

Esta versão **substitui** a anterior. Faça as etapas **na ordem**.

## Os arquivos (pasta `wordpress/entrega/`)
| Arquivo | Para que serve |
|---|---|
| `aldeia-vendas.zip` | **Plugin 1.4.1.** Fotos e fontes do aulão, e agora também o **título, a descrição e o tipo Open Graph** da página para o Yoast. Reinstale por cima do atual. |
| `aulao-universal-v2.json` | **Modelo para a Black Friday** (R$ 70, até 30/11). Use agora. |
| `aulao-universal-v2-pos-promocao.json` | **Modelo para depois de 30/11** (R$ 100, sem promoção). Só entra em **30/11, depois das 23h59**. |
| `…-colar-no-widget-html.html` | Plano B de cada modelo, para colar num widget HTML. |

## O que mudou na página
1. **Sem contradição de preço.** O HTML da Black Friday só tem **R$ 70** e "A promoção acaba em: 30/11". O R$ 100 e o texto "promoção terminou" não existem mais nele. Quem lê o código (inclusive IAs) vê uma oferta só.
2. **Definição citável** logo abaixo do título: "O AULÃO UNIVERSAL é uma aula gravada de escrita criativa para iniciantes…", com duração (cerca de 1 hora), formato, acesso de 1 ano e o que vem junto.
3. **Títulos descritivos** (H2): "O que é o AULÃO UNIVERSAL?", "O que você aprende nas 6 partes da aula", "Para quem é…", "Para quem não é", "O que está incluído e quanto custa", "Quem é a professora: Camila Veloso", "Perguntas frequentes". As chamadas de venda ficam nos botões.
4. **As 6 partes em H3**, cada uma com 2 a 3 linhas (com "três atos", "arco", "premissa" explicados em palavras simples).
5. **10 perguntas frequentes** (eram 5), com respostas curtas. Os dados estruturados espelham exatamente o que está na tela.
6. **Para quem é / Para quem não é**, com o caminho para o curso completo da Aldeia.
7. **14 fotos com texto alternativo único**.
8. **Datas visíveis:** "Publicado em 19/11/2026 · Atualizado em 23/11/2026".
9. **Links internos:** página inicial da Aldeia, lista de espera, página da Camila e 3 artigos do site.
10. **Dados estruturados:** Course (com preço e validade da oferta vigente), Person (Camila) e FAQPage. A organização "Aldeia Literária" já vem do Yoast e é só referenciada, para não duplicar.
11. **Título, descrição e og:type** definidos pelo plugin (og:type deixa de ser "article" e vira "website").

## Etapa 1: Backup do site.

## Etapa 2: Reinstalar o plugin
**Plugins → Adicionar plugin → Enviar plugin** → `aldeia-vendas.zip` → **Substituir o atual pelo enviado**. Confirme a versão **1.4.1**.

## Etapa 3: Trocar o conteúdo da página
1. **Elementor → Modelos → Importar modelos** → `aulao-universal-v2.json` e `aulao-universal-v2-pos-promocao.json`. Aparecem "ALDEIA Aulão Universal v2 (Black Friday)" e "… (pós-promoção, R$ 100)".
2. Abra a página `aulao-universal` no Elementor, apague o conteúdo e insira **ALDEIA Aulão Universal v2 (Black Friday)**. Layout **Elementor Canvas**. **Atualizar**.
3. **WP Rocket → Limpar cache.**

## Etapa 4: Conferir (janela anônima e celular)
- [ ] Faixa do topo: "A promoção acaba em:" com o cronômetro andando e **QUERO O AULÃO**.
- [ ] Só aparece **R$ 70** (depois de "Ver o preço" e no cartão "Promoção"). **Não** aparece R$ 100 nem "promoção terminou".
- [ ] Os 4 botões abrem a Kiwify.
- [ ] No Yoast, o título é "AULÃO UNIVERSAL: aula de escrita criativa para iniciantes | Aldeia Literária" (o plugin define sozinho).
- [ ] Em `view-source:`, procure `og:type`: deve ser **website**, e `og:description` deve ser a descrição curta, não o texto da página.
- [ ] Teste em `search.google.com/test/rich-results` e `validator.schema.org`: devem aparecer Course, Person e FAQPage.

## Etapa 5: Depois de 30/11 (às 23h59), troque o modelo
1. Abra a página no Elementor, apague o conteúdo e insira **ALDEIA Aulão Universal v2 (pós-promoção, R$ 100)**. **Atualizar** e limpe o cache.
2. **Mude o preço na Kiwify para R$ 100** (ou me mande um link novo de R$ 100, e eu gero os arquivos de novo).
3. Se você esquecer: depois das 23h59 a página **esconde sozinha** a contagem, o bônus e o preço de R$ 70, mas fica sem preço visível até a troca.

## Pendências
- **Prova social:** a página **não tem depoimentos nem livros de alunos**. Você mencionou prints de depoimentos de aulões, mas **eles não chegaram nesta conversa**. Mande os prints (com nome da pessoa e o que mudou) e eu incluo.
- **Data "Atualizado em":** está fixa em 23/11/2026. Ao mudar a página, me peça para atualizar ou troque a data no Código HTML.
- Confirme que valem para o aulão: **acesso de 1 ano, reembolso de 7 dias, duração de cerca de 1 hora, material de apoio + atividade**, e que ele **não inclui retorno individual sobre os textos** (está na seção "Para quem não é").
- Autorização dos alunos que aparecem nas fotos.
