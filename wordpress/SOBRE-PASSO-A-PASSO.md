# Página Sobre — como colocar no ar

Arquivos:

| Arquivo | Para que serve |
|---|---|
| `aldeia-vendas.zip` | Plugin (versão **1.0.6**). **Reinstale por cima**: ele traz as imagens e o estilo novos da página Sobre. |
| `aldeia-sobre-v1.json` | Modelo de página do Elementor da página Sobre. |
| `aldeia-sobre-v1-colar-no-widget-html.html` | O mesmo conteúdo, para colar num widget HTML (plano B). |

## Passo 1 — Reinstalar o plugin
**Plugins → Adicionar plugin → Enviar plugin** → `aldeia-vendas.zip` → **Substituir o atual pelo enviado**. Confirme que continua **Ativo**.

## Passo 2 — Importar o modelo
Abra `https://aaldeialiteraria.com.br/wp-admin/edit.php?post_type=elementor_library&tabs_group=library` → **Importar modelos** → `aldeia-sobre-v1.json`. Deve aparecer **"ALDEIA Sobre v1 — Página Sobre"**.

## Passo 3 — Colocar na página Sobre
Duas opções. A **A** mantém o endereço `/sobre/` e é a mais simples.

**A. Substituir o conteúdo da página Sobre atual**
1. **Páginas → Sobre → Editar com Elementor**.
2. Antes de mexer, abra o **Histórico** (ícone de relógio) e confirme que existe uma versão guardada, para poder voltar atrás.
3. No **Navegador** (ícone de camadas), apague todo o conteúdo: botão direito em cada bloco → **Excluir**.
4. Clique na **pasta preta** → **Meus modelos** → **Inserir** em **ALDEIA Sobre v1**.
5. **Engrenagem (Configurações da página) → Layout da página → Elementor Canvas** (a página já traz o próprio cabeçalho e rodapé).
6. Clique em **Atualizar** (o botão grande, no canto inferior esquerdo).

**B. Testar numa página nova antes**
Crie **Páginas → Adicionar nova** (título "Sobre — novo", rascunho), insira o modelo, use o layout **Elementor Canvas** e veja a pré-visualização. Quando aprovar, repita a opção A na página Sobre.

## Passo 4 — Conferir
1. Limpe o cache (**WP Rocket → Limpar cache**) e abra `aaldeialiteraria.com.br/sobre/` numa janela anônima.
2. Role até o fim: a última linha deve dizer **"versão sobre v1"**.
3. Teste no celular e no computador. Se a faixa de palestrantes ou de fotos não se mexer, adicione `/wp-content/plugins/aldeia-vendas/` nas exclusões de JavaScript do WP Rocket e limpe o cache.
4. Depois de conferir, apague a linha "versão sobre v1" (no código do bloco, procure `av-ver`).

## Como editar
Como na página de vendas: clique no bloco e edite o **Código HTML** no painel da esquerda (Ctrl+F para achar o trecho). Troque só o texto, sem apagar nada entre `<` e `>` nem os nomes que começam com `av-`.

| Quero mudar | Procure por |
|---|---|
| Os marcos da linha do tempo | `av-tl__item` |
| Nome ou cargo de um palestrante | `av-gcard` |
| Os 4 itens de "Oferecemos" | `av-offer-item` |
| Link dos botões | `tally.so/r/0QNWPy` |

**Desfazer:** Histórico do Elementor, ou volte à versão antiga da página Sobre.
