# Como colocar a página de vendas no ar (versão final v16)

Você recebeu 3 arquivos:

| Arquivo | Para que serve |
|---|---|
| `aldeia-vendas.zip` | **Plugin**: guarda as fontes, as imagens (capas, fotos, brasão) e o estilo. Instala uma vez. |
| `aldeia-pagina-v16.json` | **Modelo de página do Elementor**: a página inteira, pronta. |
| `aldeia-pagina-v16-colar-no-widget-html.html` | O mesmo conteúdo, para **colar** num widget HTML. Plano B se o modelo não funcionar. |

A página nova nasce num endereço próprio. **A Home atual continua no ar** até você decidir trocar.

---

## Passo 1 — Backup
Faça um backup do site (plugin de backup ou o da hospedagem). Nada abaixo mexe nas páginas existentes, é só segurança.

## Passo 2 — Instalar o plugin
1. Painel do WordPress → **Plugins → Adicionar plugin → Enviar plugin**.
2. Escolha `aldeia-vendas.zip` → **Instalar agora**.
3. Se aparecer "o plugin já existe", clique em **Substituir o atual pelo enviado**.
4. Clique em **Ativar plugin**.

## Passo 3 — Importar o modelo
1. Abra: `https://aaldeialiteraria.com.br/wp-admin/edit.php?post_type=elementor_library&tabs_group=library`
   (ou pelo menu **Elementor**, no painel, procure **Modelos** / **Modelos salvos**).
2. Clique em **Importar modelos**, escolha `aldeia-pagina-v16.json` → **Importar agora**.
3. Confirme que aparece **"ALDEIA v16 — Página de vendas (final)"**.
4. **Apague os modelos antigos** da lista (v3, v4, v5, v6, v7, "Página de vendas"…). Assim não dá para inserir o errado.

## Passo 4 — Criar a página e inserir o modelo
1. **Páginas → Adicionar nova**. Título sugerido: `Escrita Criativa — Turma 2027`.
2. Clique em **Editar com Elementor**.
3. Na área vazia, clique no círculo da **pasta preta** (Adicionar modelo) → aba **Meus modelos** → **Inserir** ao lado de **ALDEIA v16**.
4. Se a página já tinha conteúdo, apague tudo antes: abra o **Navegador** (ícone de camadas, na barra de cima), clique com o botão direito em cada bloco → **Excluir**. O modelo é **adicionado**, não substitui.
5. Clique no ícone da **folha com engrenagem** (Configurações da página) → **Layout da página** → **Elementor Canvas**. Isso tira o menu duplicado do tema, porque a página já traz o próprio cabeçalho.
6. Clique em **Publicar** (ou **Atualizar**, se a página já estava publicada).

> **Importante:** numa página já publicada, só o botão **Atualizar** muda o que está no ar. "Salvar rascunho" (pela setinha) guarda só no editor.

## Passo 5 — Conferir
1. Abra o endereço da página numa **janela anônima**.
2. Confira no rodapé que **não** aparece nenhuma linha de versão e que o link **Sobre** (no menu do topo e no rodapé) leva à nova página Sobre. Se ainda aparecer "versão…", há conteúdo antigo na página (volte ao Passo 4, item 4).
3. Se o site usa **WP Rocket**: **WP Rocket → Limpar cache**. Se o carrossel dos problemas, a faixa de capas ou as abas dos módulos não se mexerem, vá em **WP Rocket → Otimização de arquivos** e adicione `/wp-content/plugins/aldeia-vendas/` nas exclusões de JavaScript (atraso e minificação). Limpe o cache de novo.
4. Teste no **celular** e no computador, e clique nos botões "Entrar na lista de espera".

## Passo 6 (opcional) — Colocar essa página como início do site
1. **Configurações → Leitura → Sua página inicial exibe → Uma página estática**.
2. Em **Página inicial**, escolha a nova página → **Salvar alterações**.
3. Limpe o cache. A Home antiga continua existindo e dá para voltar atrás repetindo o passo.

---

## Como editar depois
A página é **um único bloco HTML**: o texto não se edita clicando nele, como nas outras páginas do Elementor. Para ajustes pequenos:

1. Abra a página no Elementor e clique em qualquer parte dela (isso seleciona o bloco).
2. No painel da esquerda, a caixa **Código HTML** mostra tudo. Use **Ctrl+F** para achar o trecho.
3. Troque **só o texto**, sem apagar nada entre `<` e `>`.

| Quero mudar | Como |
|---|---|
| Uma frase | Troque as palavras dentro de `<p>…</p>`, `<h2>…</h2>` etc. |
| Link dos botões "Entrar na lista de espera" | Troque o endereço em `href="https://tally.so/r/0QNWPy"` (aparece em vários lugares: use Ctrl+F) |
| **Links dos livros** | Procure `Abrir a página do livro` e, na mesma linha, troque `href="#"` pelo endereço do livro. Cada capa abre em nova janela. A segunda cópia de cada livro é criada pelo próprio código |
| Valores, parcelas, taxa | Procure `R$ 186`, `R$ 262`, `R$ 105`… e troque os números |
| Tempo de curso e duração dos módulos | Procure `Tempo de curso` e `duração de 6 meses` |
| Foto de um professor | Troque o endereço em `src="…/prof-….jpg"` pelo da imagem na sua Biblioteca de Mídia |
| Endereço da página Sobre | Procure `/novo-sobre/` (aparece no menu do topo e no rodapé) e troque pelo endereço da sua página Sobre |

**Cuidados**
- Nunca apague os nomes que começam com `av-`: é o que aplica o visual.
- **Guarde o arquivo original** `aldeia-pagina-v16-colar-no-widget-html.html`. Se algo quebrar, cole tudo de novo.
- O **Histórico** do Elementor (ícone de relógio) permite voltar a uma versão anterior.
- Mudanças grandes: faça como rascunho e confira na pré-visualização antes de publicar.

### Quando as matrículas abrirem (janeiro de 2027)
1. Troque o link e o texto dos botões "Entrar na lista de espera" pelo do checkout.
2. Atualize "Matrículas abrem em janeiro de 2027" e "Próxima turma em janeiro de 2027".
3. Atualize ou apague a pergunta "Já posso me matricular?" do FAQ.

---

## Se algo não sair como o esperado

| Problema | O que fazer |
|---|---|
| Página sem cores, botões verdes e títulos vermelhos | O plugin não está ativo, ou há cache. Confirme em **Plugins**, limpe o cache e teste em janela anônima |
| A página mostra conteúdo antigo | Veja se clicou em **Atualizar** e se há **dois blocos** no Navegador. Confira se o rodapé ainda mostra alguma linha "versão…" (a versão certa não mostra) |
| Imagens não aparecem | Confirme que o plugin está ativo. A pasta dele precisa se chamar exatamente `aldeia-vendas` |
| Carrossel/abas parados | WP Rocket: veja o Passo 5, item 3 |
| No editor do Elementor tudo aparece parado | É proposital: as animações ficam desligadas dentro do editor. No site publicado funcionam |
| A importação do modelo deu erro | Use o **Plano B**: crie a página, arraste **um** widget **HTML**, cole todo o conteúdo de `aldeia-pagina-v16-colar-no-widget-html.html` e escolha o layout **Elementor Canvas** |
| Quero desfazer tudo | Mande a página para a lixeira e desative o plugin. Nada mais no site foi alterado |

---

## Checklist antes de divulgar
- [ ] O rodapé não mostra nenhuma linha de versão
- [ ] Botões levam ao formulário/checkout certo
- [ ] Links dos livros preenchidos (ou capas sem link, se preferir)
- [ ] Alunos das fotos da comunidade autorizaram o uso das imagens
- [ ] Tempo de curso, valores, parcelas e taxa conferidos
- [ ] Testado no celular e no computador, em janela anônima
- [ ] Menu "Sobre" abre a página Sobre
- [ ] Cache limpo

---

## Qual versão está no ar?
A página não mostra mais nenhuma linha de versão. Para saber qual está no ar, abra o código do bloco HTML no Elementor: a primeira linha é um comentário (invisível no site) com o nome, por exemplo `aldeia-vendas-v16`.

## Link para a página Sobre
O menu do topo e o rodapé apontam para `https://aaldeialiteraria.com.br/novo-sobre/`. No celular, o menu mostra só o link "Sobre". Se um dia a nova Sobre passar a ficar em `/sobre/`, troque `/novo-sobre/` por `/sobre/` no código (use Ctrl+F).
