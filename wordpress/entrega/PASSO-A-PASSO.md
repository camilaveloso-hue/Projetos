# Como colocar no ar: Home, Sobre e páginas dos professores

Tudo o que você precisa subir está nesta pasta (`wordpress/entrega/`). Faça as etapas **na ordem**. Cada etapa diz o que clicar e como saber se deu certo.

## Os arquivos

| Arquivo | Para que serve |
|---|---|
| `aldeia-vendas.zip` | **Plugin** (versão 1.2.4). Guarda as fontes (agora a Libre Caslon), as imagens e o estilo. Reinstale por cima do atual. |
| `home-v29.json` | Modelo do Elementor da **Home** (página de vendas), com plano único de 1 aula por semana e botões "Saiba mais". |
| `sobre-v10.json` | Modelo do Elementor da página **Sobre**, com a nova fonte. |
| `professores/camila-veloso.json`, `laura-marques.json`, `lucas-oliveira.json`, `lavinia-neres.json` | Modelos (v6) das **páginas individuais** dos professores, já com os endereços reais. |
| arquivos `…-colar-no-widget-html.html` | O mesmo conteúdo para **colar** num widget HTML. É o **Plano B** se a importação do modelo falhar. |

**Ana Ribeiro:** a página dela ainda não existe (falta o Lattes e o texto de "Função no curso"). Por isso a Home v29 está **sem** o botão "Saiba mais" dela.

---

## Novidades desta versão (leia primeiro)
- Texto padronizado: **1 aula por semana (quartas, 19h30)**, **18 meses**, **18x de R$ 199 no Pix + matrícula de R$ 105**, "**mais de 400** escritores", "professores **mestres, doutores e mestrandos**". "Certificado MEC" saiu de todo o site: agora é "curso de extensão universitária, com certificado emitido pela Anhanguera" (e o texto avisa que não é diploma).
- Rodapé com razão social e CNPJ em todas as páginas. **Confirme a grafia da razão social** ("CAMILA VELOSO. CO LTDA") no cartão CNPJ.
- **Cancelamento:** nova página **Política de cancelamento e reembolso** (`/politica-de-cancelamento-e-reembolso/`), feita a partir da cláusula 4 do contrato. Todos os rodapés têm o link para ela.
- **Certificado:** o texto agora segue o que você escreveu (extensão universitária de 120h, reconhecida pelo MEC, certificado emitido pela Anhanguera).
- **Páginas novas** em `paginas/`: **Guia** (`/como-escolher-curso-de-escrita-criativa/`) e **Imprensa** (`/imprensa/`). Crie 3 páginas (Guia, Imprensa e Cancelamento) com esses endereços, insira o modelo, **Elementor Canvas**, **Publicar**.
- Home com dados estruturados novos (Curso, Oferta, FAQ). Veja `SEO-TECNICO.md` (títulos, descrições, domínio, robots) e `KIT-AUTORIDADE-EXTERNA.md`.

## Etapa 1 — Backup
Faça um backup do site (plugin de backup ou o da hospedagem). Nada abaixo apaga páginas, mas é segurança.

## Etapa 2 — Reinstalar o plugin
1. Painel do WordPress → **Plugins → Adicionar plugin → Enviar plugin**.
2. Escolha `aldeia-vendas.zip` → **Instalar agora**.
3. Quando aparecer "o plugin já existe", clique em **Substituir o atual pelo enviado**.
4. Confirme que o plugin está **Ativo** e que a versão é **1.2.4**.

## Etapa 3 — Importar os modelos
1. Abra `https://aaldeialiteraria.com.br/wp-admin/edit.php?post_type=elementor_library&tabs_group=library` (ou **Elementor → Modelos → Modelos salvos**).
2. Clique em **Importar modelos** e envie os arquivos `.json` (pode ser um de cada vez).
3. Devem aparecer:
   - **ALDEIA Home v29 — Página de vendas**
   - **ALDEIA Sobre v10 — Página Sobre**
   - **ALDEIA Professor v6 — Camila Veloso**, **Laura Marques**, **Lucas Oliveira**, **Lavínia Neres**
4. **Apague os modelos antigos** (Home v16, Sobre v6 e anteriores). Assim não dá para inserir o errado.

## Etapa 4 — Conferir o endereço das páginas (uma vez só)
Os links entre as páginas dependem de endereços sem número. Vá em **Configurações → Links permanentes** e confirme que está **Nome do post**. Se estiver outra opção, escolha essa e clique em **Salvar alterações**.

## Etapa 5 — Páginas dos professores (endereços que já existem no site)
As páginas já foram criadas com estes endereços. Os links da Home e das páginas usam **exatamente** estes endereços, então **não mude os slugs**:

| Professor | Endereço | Modelo (versão 6) |
|---|---|---|
| Camila Veloso | `/sobre-a-fundadora/` | ALDEIA Professor v6 — Camila Veloso |
| Laura Marques | `/professores-laura-marques/` | ALDEIA Professor v6 — Laura Marques |
| Lucas Oliveira | `/professores-lucas-oliveira/` | ALDEIA Professor v6 — Lucas Oliveira |
| Lavínia Neres | `/professora-lavinia/` | ALDEIA Professor v6 — Lavínia Neres |

**Atualize cada uma das 4 páginas com o modelo v6** (o conteúdo das versões anteriores tinha links para endereços que não existem):
1. Abra a página no **Elementor**.
2. No **Navegador** (camadas), apague todo o conteúdo e **Excluir**.
3. Pasta preta → **Meus modelos** → **Inserir** o modelo da linha.
4. **Engrenagem → Layout da página → Elementor Canvas**.
5. Clique em **Atualizar**.

Não coloque essas páginas em **Aparência → Menus** e deixe a visibilidade **Pública**.

**Página-lista dos professores:** ainda não existe, e por isso nenhuma página aponta para ela. Quando quiser criá-la, me diga o endereço e eu gero o modelo e atualizo os links.

**Ana Ribeiro:** a página dela ainda não existe. A Home v29 está **sem** o botão dela; quando a página estiver pronta, eu gero a versão com o botão.

## Etapa 6 — Atualizar a Home e a Sobre
### 6.1 Home (v29)
1. Abra a página da Home nova (a que usa o modelo v16, "Escrita Criativa — Turma 2027") no **Elementor**. Se ainda não existe, crie **Páginas → Adicionar nova** com esse título.
2. Abra o **Histórico** (ícone de relógio) e confirme que há uma versão guardada, para poder voltar atrás.
3. No **Navegador** (camadas), apague todo o conteúdo: botão direito em cada bloco → **Excluir**. O modelo é **adicionado**, não substitui.
4. **Pasta preta → Meus modelos → Inserir** **ALDEIA Home v29**.
5. **Engrenagem → Layout da página → Elementor Canvas**.
6. Clique em **Atualizar** (numa página já publicada só esse botão muda o que está no ar).

### 6.2 Sobre (v8)
Mesmo procedimento, na página **Sobre** (hoje em `/novo-sobre/`), com o modelo **ALDEIA Sobre v10**.

### 6.3 (Opcional) Home como página inicial do site
**Configurações → Leitura → Sua página inicial exibe → Uma página estática** → escolha a Home nova → **Salvar alterações**. Assim o link "Início" das páginas dos professores leva à Home nova.

## Etapa 7 — Conferir tudo
Abra tudo numa **janela anônima** (e limpe o cache: **WP Rocket → Limpar cache**, se usar).

- [ ] Home: títulos na fonte nova; faixa dos professores **antes** da fundadora; tabela com **18x de R$ 199** (total R$ 3.582), **4 atividades por mês com feedback individual** e **18 meses**; módulos com **12 aulas** e **Quarta, 19h30**; cada **Saiba mais** abre a página certa (a da Ana ainda não existe).
- [ ] A Home e as demais páginas **não** mostram nenhuma linha de "versão".
- [ ] Sobre: títulos na fonte nova e link **Sobre** do menu funcionando.
- [ ] As 4 páginas individuais: foto, resumo, tabela, trajetória, perguntas frequentes e "Conheça também".
- [ ] Teste no **celular** e no computador.
- [ ] Se o carrossel, as abas ou as fotos não se mexerem: **WP Rocket → Otimização de arquivos** e adicione `/wp-content/plugins/aldeia-vendas/` às exclusões de JavaScript (atraso e minificação). Limpe o cache de novo.

## Etapa 8 — Fazer o Google e as IAs encontrarem as páginas
Publicar não basta: o buscador precisa **indexar**. Faça isto:

1. **Não bloquear a indexação:** **Configurações → Leitura** → deixe **desmarcada** a caixa *"Pedir aos mecanismos de busca para não indexarem este site"*.
2. **Mapa do site:** abra `https://aaldeialiteraria.com.br/wp-sitemap.xml`, entre em `wp-sitemap-posts-page-1.xml` e confira que as páginas dos professores (`/sobre-a-fundadora/`, `/professores-laura-marques/`, `/professores-lucas-oliveira/`, `/professora-lavinia/`) aparecem. Se você usa Yoast, Rank Math ou SEOPress, o mapa deles é outro (por exemplo `/sitemap_index.xml`).
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
| Página sem cores, botões verdes ou títulos em fonte comum | O plugin não está ativo ou há cache. Confirme em **Plugins** (versão 1.2.4), limpe o cache e teste em janela anônima |
| O botão "Saiba mais" leva a uma página "não encontrada" | O slug ou a página-mãe está diferente da tabela da Etapa 5. Confira o endereço e os **Links permanentes** (Etapa 4) |
| Menu duplicado no topo | Falta o layout **Elementor Canvas** na página |
| Imagens não aparecem | O plugin precisa estar ativo e a pasta se chama exatamente `aldeia-vendas` |
| A importação do modelo deu erro | **Plano B:** crie a página, arraste **um** widget **HTML**, cole todo o conteúdo do arquivo `…-colar-no-widget-html.html` e escolha **Elementor Canvas** |
| No editor do Elementor as animações ficam paradas | É proposital. No site publicado funcionam |
| Quero desfazer | Mande a página para a lixeira (ou volte pelo Histórico) e reinstale o plugin antigo, se for o caso |

## Se você já tinha publicado a versão anterior
Importe os modelos novos (Home v29, Sobre v10 e Professor v6), apague os antigos e, em **cada página já publicada**, repita o procedimento da Etapa 6.1: apague o conteúdo, insira o modelo novo, Elementor Canvas e **Atualizar**. Vale para a Home, a Sobre e as 4 páginas dos professores (o texto sobre o curso mudou em todas).

## Antes de divulgar, decida
- [ ] **Foto da seção "Certificado emitido pela Anhanguera":** a foto atual mostra um certificado "do Módulo I". Troque por uma foto do certificado final, se tiver.
- [ ] **Laura:** o card da Home/lista diz "mestranda em comunicação (UFSM)" e a página diz "mestranda em Produção Editorial (UFSM)". Deixe igual nos dois lugares.
- [ ] **Camila:** a Home diz "+500 escritores"; o Lattes dela diz "mais de 400". Confirme qual vale.
- [ ] **Ana Ribeiro:** mande o Lattes e o texto de "Função no curso" para eu gerar a página e reativar o botão na Home.
- [ ] **Foto da seção de certificados** e **links dos livros**, ainda pendentes na Home.
- [ ] Peça ao **Lucas** para atualizar o resumo do Lattes (ainda diz "Doutorando"; a titulação já consta como doutor, 2025).
- [ ] Confirme se todos autorizaram o uso das fotos e dos dados dos currículos.
