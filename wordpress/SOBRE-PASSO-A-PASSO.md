# Página Sobre (versão 3) — como colocar no ar

| Arquivo | Para que serve |
|---|---|
| `aldeia-vendas.zip` | Plugin (versão **1.0.8**). **Reinstale por cima**: traz o estilo e as imagens novas. |
| `aldeia-sobre-v4.json` | Modelo de página do Elementor da página Sobre. |
| `aldeia-sobre-v4-colar-no-widget-html.html` | O mesmo conteúdo, para colar num widget HTML (plano B). |

## Passo 1 — Reinstalar o plugin
**Plugins → Adicionar plugin → Enviar plugin** → `aldeia-vendas.zip` → **Substituir o atual pelo enviado**. Confirme que continua **Ativo**.

## Passo 2 — Importar o modelo
Abra `https://aaldeialiteraria.com.br/wp-admin/edit.php?post_type=elementor_library&tabs_group=library` → **Importar modelos** → `aldeia-sobre-v4.json`. Deve aparecer **"ALDEIA Sobre v4 — Página Sobre"**.

## Passo 3 — Colocar na página Sobre
**A. Substituir o conteúdo da página atual (mantém o endereço `/sobre/`)**
1. **Páginas → Sobre → Editar com Elementor**.
2. Abra o **Histórico** (ícone de relógio) e confirme que existe uma versão guardada, para poder voltar atrás.
3. No **Navegador** (camadas), apague todo o conteúdo (botão direito em cada bloco → **Excluir**).
4. **Pasta preta → Meus modelos → Inserir** em **ALDEIA Sobre v4**.
5. **Engrenagem → Layout da página → Elementor Canvas**.
6. Clique em **Atualizar** (botão grande, canto inferior esquerdo).

**B. Testar antes numa página nova:** crie **Páginas → Adicionar nova** ("Sobre — novo", rascunho), insira o modelo, escolha o layout **Elementor Canvas** e confira na pré-visualização. Depois repita a opção A.

## Passo 4 — Conferir
1. **WP Rocket → Limpar cache** e abra `aaldeialiteraria.com.br/sobre/` numa janela anônima.
2. Como a linha de versão foi retirada, confirme assim: o menu tem "Início, Nossa história, Quem somos, Comunidade", o título do fim da página é **"Faça parte deste movimento literário."** (acima das fotos) e **não existe** uma seção azul com botão depois das fotos.
3. Teste no celular e no computador. Se os carrosséis (palestrantes, livros, fotos) não se mexerem, adicione `/wp-content/plugins/aldeia-vendas/` nas exclusões de JavaScript do WP Rocket e limpe o cache.
4. Para saber qual versão está no ar, abra o código do bloco HTML: a primeira linha é um comentário `aldeia-sobre-v4`.

## Como editar
Clique no bloco e edite o **Código HTML** no painel da esquerda (Ctrl+F para achar o trecho). Troque só o texto, sem apagar nada entre `<` e `>` nem os nomes que começam com `av-`.

| Quero mudar | Procure por |
|---|---|
| Os 4 capítulos da história | `av-chapter` |
| Os 4 pilares do método | `av-pillar` |
| Nome ou cargo de professor | `av-tcard` |
| Palestrantes | `av-gcard` |
| Fotos da comunidade | `av-cphoto` |
| Link dos botões | `tally.so/r/0QNWPy` |

**Desfazer:** Histórico do Elementor ou a versão antiga da página Sobre.
