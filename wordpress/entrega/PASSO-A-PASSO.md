# Como colocar no ar: Home, Sobre e páginas dos professores

Tudo o que você precisa subir está nesta pasta (`wordpress/entrega/`). Faça as etapas **na ordem**. Cada etapa diz o que clicar e como saber se deu certo.

## Os arquivos

| Arquivo | Para que serve |
|---|---|
| `aldeia-vendas.zip` | **Plugin** (versão 1.1.0). Guarda as fontes (agora a Libre Caslon), as imagens e o estilo. Reinstale por cima do atual. |
| `home-v17.json` | Modelo do Elementor da **Home** (página de vendas), já com os botões "Saiba mais". |
| `sobre-v7.json` | Modelo do Elementor da página **Sobre**, com a nova fonte. |
| `professores/lista-professores.json` | Modelo da página **/professores/** (lista com os cinco professores). |
| `professores/camila-veloso.json`, `laura-marques.json`, `lucas-oliveira.json`, `lavinia-neres.json` | Modelos das **páginas individuais**. |
| arquivos `…-colar-no-widget-html.html` | O mesmo conteúdo para **colar** num widget HTML. É o **Plano B** se a importação do modelo falhar. |

**Ana Ribeiro:** a página dela só entra quando eu receber o Lattes e o texto de "Função no curso". Por isso o card dela na Home ainda **não** tem o botão "Saiba mais", e ela aparece na lista sem link.

---

## Etapa 1 — Backup
Faça um backup do site (plugin de backup ou o da hospedagem). Nada abaixo apaga páginas, mas é segurança.

## Etapa 2 — Reinstalar o plugin
1. Painel do WordPress → **Plugins → Adicionar plugin → Enviar plugin**.
2. Escolha `aldeia-vendas.zip` → **Instalar agora**.
3. Quando aparecer "o plugin já existe", clique em **Substituir o atual pelo enviado**.
4. Confirme que o plugin está **Ativo** e que a versão é **1.1.0**.

## Etapa 3 — Importar os modelos
1. Abra `https://aaldeialiteraria.com.br/wp-admin/edit.php?post_type=elementor_library&tabs_group=library` (ou **Elementor → Modelos → Modelos salvos**).
2. Clique em **Importar modelos** e envie os 7 arquivos `.json` (pode ser um de cada vez).
3. Devem aparecer:
   - **ALDEIA Home v17 — Página de vendas**
   - **ALDEIA Sobre v7 — Página Sobre**
   - **ALDEIA Professor v1 — Lista de professores**
   - **ALDEIA Professor v1 — Camila Veloso**, **Laura Marques**, **Lucas Oliveira**, **Lavínia Neres**
4. **Apague os modelos antigos** (Home v16, Sobre v6 e anteriores). Assim não dá para inserir o errado.

## Etapa 4 — Conferir o endereço das páginas (uma vez só)
Os links entre as páginas dependem de endereços sem número. Vá em **Configurações → Links permanentes** e confirme que está **Nome do post**. Se estiver outra opção, escolha essa e clique em **Salvar alterações**.

## Etapa 5 — Criar as páginas dos professores
Faça **primeiro a página-mãe** (a lista) e depois as individuais.

### 5.1 Página-mãe: a lista
1. **Páginas → Adicionar nova**. Título: `Professores da Aldeia Literária`.
2. No painel da direita (**Resumo** ou **Endereço**), deixe o **slug** exatamente `professores`.
3. Clique em **Editar com Elementor**.
4. Na área vazia, clique na **pasta preta** (Adicionar modelo) → **Meus modelos** → **Inserir** ao lado de **ALDEIA Professor v1 — Lista de professores**.
5. **Engrenagem (Configurações da página) → Layout da página → Elementor Canvas**. Isso tira o menu duplicado do tema, porque a página já traz o cabeçalho.
6. Clique em **Publicar**.
7. Abra `https://aaldeialiteraria.com.br/professores/`. A lista deve aparecer, com quatro botões **Ver perfil** (a Ana ainda não tem).

### 5.2 Páginas individuais (repita 4 vezes)
Use esta tabela. O **slug** precisa ser **idêntico**, porque a Home e a lista já apontam para esses endereços.

| Título da página | Slug | Modelo a inserir |
|---|---|---|
| Camila Veloso | `camila-veloso` | ALDEIA Professor v1 — Camila Veloso |
| Laura Marques | `laura-marques` | ALDEIA Professor v1 — Laura Marques |
| Lucas Oliveira | `lucas-oliveira` | ALDEIA Professor v1 — Lucas Oliveira |
| Lavínia Neres | `lavinia-neres` | ALDEIA Professor v1 — Lavínia Neres |

Para cada uma:
1. **Páginas → Adicionar nova**, digite o título.
2. No painel da direita, em **Atributos da página** (ou **Página**), escolha **Página-mãe: Professores da Aldeia Literária**. Assim o endereço fica `/professores/lucas-oliveira/`.
3. Confira o **slug** (veja a tabela).
4. **Editar com Elementor** → pasta preta → **Meus modelos → Inserir** o modelo da linha.
5. **Engrenagem → Layout da página → Elementor Canvas**.
6. **Publicar**.
7. Abra o endereço (por exemplo `https://aaldeialiteraria.com.br/professores/lucas-oliveira/`) e confira a foto, o nome e as perguntas frequentes.

### 5.3 Deixar as páginas fora do menu (mas públicas)
- **Não** adicione essas páginas em **Aparência → Menus**.
- Em **Aparência → Menus**, desmarque **"Adicionar automaticamente novas páginas de nível superior a este menu"**, se estiver marcado. Como as páginas individuais têm página-mãe, normalmente isso não as afeta; a mãe (lista) sim.
- Em **Publicar → Visibilidade**, deixe **Pública** (não "Protegida por senha" nem "Privada"). Elas precisam ser públicas para o Google e as IAs lerem.

## Etapa 6 — Atualizar a Home e a Sobre
### 6.1 Home (v17)
1. Abra a página da Home nova (a que usa o modelo v16, "Escrita Criativa — Turma 2027") no **Elementor**. Se ainda não existe, crie **Páginas → Adicionar nova** com esse título.
2. Abra o **Histórico** (ícone de relógio) e confirme que há uma versão guardada, para poder voltar atrás.
3. No **Navegador** (camadas), apague todo o conteúdo: botão direito em cada bloco → **Excluir**. O modelo é **adicionado**, não substitui.
4. **Pasta preta → Meus modelos → Inserir** **ALDEIA Home v17**.
5. **Engrenagem → Layout da página → Elementor Canvas**.
6. Clique em **Atualizar** (numa página já publicada só esse botão muda o que está no ar).

### 6.2 Sobre (v7)
Mesmo procedimento, na página **Sobre** (hoje em `/novo-sobre/`), com o modelo **ALDEIA Sobre v7**.

### 6.3 (Opcional) Home como página inicial do site
**Configurações → Leitura → Sua página inicial exibe → Uma página estática** → escolha a Home nova → **Salvar alterações**. Assim o link "Início" das páginas dos professores leva à Home nova.

## Etapa 7 — Conferir tudo
Abra tudo numa **janela anônima** (e limpe o cache: **WP Rocket → Limpar cache**, se usar).

- [ ] Home: os títulos aparecem na fonte nova, os cards dos professores têm **Saiba mais** (menos a Ana) e cada botão abre a página certa.
- [ ] A Home e as demais páginas **não** mostram nenhuma linha de "versão".
- [ ] Sobre: títulos na fonte nova e link **Sobre** do menu funcionando.
- [ ] `/professores/`: lista com cinco cartões.
- [ ] As 4 páginas individuais: foto, resumo, tabela, trajetória, perguntas frequentes e "Conheça também".
- [ ] Teste no **celular** e no computador.
- [ ] Se o carrossel, as abas ou as fotos não se mexerem: **WP Rocket → Otimização de arquivos** e adicione `/wp-content/plugins/aldeia-vendas/` às exclusões de JavaScript (atraso e minificação). Limpe o cache de novo.

## Etapa 8 — Fazer o Google e as IAs encontrarem as páginas
Publicar não basta: o buscador precisa **indexar**. Faça isto:

1. **Não bloquear a indexação:** **Configurações → Leitura** → deixe **desmarcada** a caixa *"Pedir aos mecanismos de busca para não indexarem este site"*.
2. **Mapa do site:** abra `https://aaldeialiteraria.com.br/wp-sitemap.xml`, entre em `wp-sitemap-posts-page-1.xml` e confira que as páginas `/professores/…` aparecem. Se você usa Yoast, Rank Math ou SEOPress, o mapa deles é outro (por exemplo `/sitemap_index.xml`).
3. **robots.txt:** abra `https://aaldeialiteraria.com.br/robots.txt` e confira que **não** há `Disallow: /professores` nem bloqueio ao `Googlebot` e ao `OAI-SearchBot` (o robô de busca do ChatGPT).
4. **Google Search Console:** adicione o site (se ainda não estiver), cole cada endereço no campo de cima (**Inspeção de URL**) e clique em **Solicitar indexação**: as 5 páginas dos professores, a Home e a Sobre.
5. **Título e descrição de cada página:** o WordPress sozinho não tem esses campos. Instale um plugin gratuito de SEO (Yoast SEO, Rank Math ou SEOPress) e preencha, em cada página, o **título SEO** e a **meta descrição**. Sugestões:

| Página | Título SEO | Meta descrição |
|---|---|---|
| Home | Curso de escrita criativa para iniciantes — Aldeia Literária | Curso on-line de escrita criativa para iniciantes, com aulas ao vivo e feedback de mestres e doutores. Matrículas abrem em janeiro de 2027. |
| Sobre | Sobre a Aldeia Literária — nossa história e equipe | Conheça a história da Aldeia Literária, fundada em 2023 por Camila Veloso, e a equipe que ajuda escritores iniciantes a transformar a ideia em livro. |
| Lista | Professores da Aldeia Literária — curso de escrita criativa | Conheça os professores da Aldeia Literária, curso on-line de escrita criativa para iniciantes: mestres, doutores e produtoras editoriais. |
| Camila | Camila Veloso — fundadora da Aldeia Literária | Camila Veloso é Produtora Editorial formada pela UFSM e fundadora da Aldeia Literária, curso de escrita criativa para escritores iniciantes. |
| Laura | Laura Marques — professora de escrita criativa | Laura Marques é graduada em Produção Editorial pela UFSM, leitora crítica e professora de escrita criativa na Aldeia Literária. |
| Lucas | Lucas Oliveira — doutor em Literatura Portuguesa (UFRJ) | Lucas Oliveira é Doutor em Letras pela UFRJ, na área de Literatura Portuguesa, com pesquisa sobre Jorge de Sena. Professor na Aldeia Literária. |
| Lavínia | Lavínia Neres — mestra em Comunicação (UFSM) | Lavínia Neres é mestra em Comunicação pela UFSM, com pesquisa sobre leitura de livros digitais. Professora na Aldeia Literária. |

6. **Dados estruturados:** cada página dos professores já traz, no código, os dados que os buscadores leem (nome, formação, link do Lattes, escola). Se o plugin de SEO tiver a opção de **desligar o schema** daquela página, desligue, para não duplicar. Para conferir, cole o endereço em `validator.schema.org`.
7. **Paciência:** a indexação leva de dias a semanas. Aparecer nas respostas de IA depende também de outros sites falarem dos professores (entrevistas, perfis, citações). Não há como garantir ou acelerar isso só pelo site.

## Como editar depois
Cada página é **um único bloco HTML**: o texto não se edita clicando nele. No Elementor, clique na página (seleciona o bloco), use o campo **Código HTML** no painel da esquerda e **Ctrl+F** para achar o trecho. Troque **só o texto**, sem apagar nada entre `<` e `>` nem os nomes que começam com `av-`.

| Quero mudar | Procure por |
|---|---|
| A data de atualização da página do professor | `Página atualizada em` (e `dateModified` nos dados estruturados no fim do código) |
| Função, formação ou trajetória de um professor | `av-facts` e `av-prose` |
| As perguntas frequentes | `<summary>` |
| Link do formulário | `tally.so/r/0QNWPy` |
| Endereço da Sobre | `/novo-sobre/` |

**Atualize a data "Página atualizada em" a cada semestre.** Páginas com data recente passam mais confiança a buscadores e IAs.

**Guarde os arquivos originais.** Se algo quebrar, importe ou cole de novo. O **Histórico** do Elementor (relógio) volta a versões anteriores.

## Se algo não sair como o esperado

| Problema | O que fazer |
|---|---|
| Página sem cores, botões verdes ou títulos em fonte comum | O plugin não está ativo ou há cache. Confirme em **Plugins** (versão 1.1.0), limpe o cache e teste em janela anônima |
| O botão "Saiba mais" leva a uma página "não encontrada" | O slug ou a página-mãe está diferente da tabela da Etapa 5. Confira o endereço e os **Links permanentes** (Etapa 4) |
| Menu duplicado no topo | Falta o layout **Elementor Canvas** na página |
| Imagens não aparecem | O plugin precisa estar ativo e a pasta se chama exatamente `aldeia-vendas` |
| A importação do modelo deu erro | **Plano B:** crie a página, arraste **um** widget **HTML**, cole todo o conteúdo do arquivo `…-colar-no-widget-html.html` e escolha **Elementor Canvas** |
| No editor do Elementor as animações ficam paradas | É proposital. No site publicado funcionam |
| Quero desfazer | Mande a página para a lixeira (ou volte pelo Histórico) e reinstale o plugin antigo, se for o caso |

## Antes de divulgar, decida
- [ ] **Laura:** o card da Home/lista diz "mestranda em comunicação (UFSM)" e a página diz "mestranda em Produção Editorial (UFSM)". Deixe igual nos dois lugares.
- [ ] **Camila:** a Home diz "+500 escritores"; o Lattes dela diz "mais de 400". Confirme qual vale.
- [ ] **Ana Ribeiro:** mande o Lattes e o texto de "Função no curso" para eu gerar a página e reativar o botão na Home.
- [ ] **Foto da seção de certificados** e **links dos livros**, ainda pendentes na Home.
- [ ] Peça ao **Lucas** para atualizar o resumo do Lattes (ainda diz "Doutorando"; a titulação já consta como doutor, 2025).
- [ ] Confirme se todos autorizaram o uso das fotos e dos dados dos currículos.
