# Como colocar a página de vendas no ar (WordPress + Elementor)

Você recebeu 3 arquivos (mais um plano B):

| Arquivo | Para que serve |
|---|---|
| `aldeia-vendas.zip` | **Plugin** com o visual da página (cores, fontes, animações, imagens). Instala uma vez. |
| `pagina-vendas-elementor.json` | **Modelo de página do Elementor**: a página completa, montada com widgets normais (títulos, textos, botões, imagens, abas, FAQ), 100% editável. |
| `plano-b-pagina-html-unico.html` | Só se o modelo acima não importar (veja o fim). |

Tempo estimado: 20 a 30 minutos. Você não precisa escrever código.

---

## Antes de começar

1. **Faça um backup do site** (plugin de backup que você já use, ou o do seu provedor de hospedagem). É só segurança: nada nos passos abaixo mexe nas páginas que já existem.
2. Confirme que o **Elementor Pro está ativo** (já está, pelo que vi no site: Elementor 4.1.4 e Pro 3.34).
3. Tenha o login de administrador do WordPress.

---

## Passo 1 — Instalar o plugin

1. No painel do WordPress: **Plugins → Adicionar novo → Enviar plugin**.
2. Clique em **Escolher arquivo**, selecione `aldeia-vendas.zip` e clique em **Instalar agora**.
3. Clique em **Ativar plugin**.

> Faça este passo **antes** do Passo 2: o modelo usa imagens que estão dentro do plugin (capas de livros, fotos, medalhão).

O plugin só carrega o visual nas páginas que usam o modelo. O resto do site não muda.

## Passo 2 — Importar o modelo no Elementor

1. No painel: **Modelos → Modelos salvos** (em inglês: *Templates → Saved Templates*).
2. Clique em **Importar modelos**, escolha `pagina-vendas-elementor.json` e clique em **Importar agora**.
3. O modelo **"Aldeia Literária — Página de vendas (turma 2027) v2"** aparece na lista. (Se existir um modelo antigo sem o "v2", ignore-o ou apague-o: a versão antiga não aplica o visual nos blocos.) O Elementor também copia as imagens para a sua Biblioteca de Mídia (é normal).

## Passo 3 — Criar a página

1. **Páginas → Adicionar nova**. Título sugerido: `Escrita Criativa — Turma 2027` (o endereço fica `.../escrita-criativa-turma-2027/`; você pode editar o endereço depois).
2. Clique em **Editar com Elementor**.
3. Na área de edição, clique no ícone de **pasta** (Adicionar modelo) → aba **Meus modelos** → ao lado de "Aldeia Literária — Página de vendas (turma 2027) v2", clique em **Inserir**. Se o Elementor perguntar sobre aplicar as configurações da página, responda **Sim**.
4. A página aparece montada. Clique em **Publicar** (canto inferior esquerdo) quando terminar os passos abaixo. Para ir testando, use **Salvar rascunho**.

## Passo 4 — Ajustar o layout da página

1. No Elementor, clique na **engrenagem** (Configurações da página, canto inferior esquerdo).
2. Em **Layout da página**, escolha **Elementor Canvas** (sem cabeçalho/rodapé do tema). A página já traz o próprio menu, rodapé e botão de WhatsApp.
3. Deixe **Ocultar título** ligado.

> Se preferir usar o cabeçalho que já existe no seu site, escolha "Elementor Largura total" e apague o bloco do menu no topo da página (container "av-header").

## Passo 5 — Preencher o que ainda está em amarelo

Tudo o que ainda depende de você aparece com **fundo amarelo**. Exemplos: taxa de matrícula, número de parcelas, garantia, contrato e multa, depoimentos, "quanto tempo ficam as aulas gravadas", foto da Camila.

Para trocar um trecho amarelo:
1. Clique no texto e **apague o trecho amarelo por inteiro**.
2. Para tirar o marcador, use a aba **Texto** (HTML) do editor, ou cole o novo texto com **Ctrl+Shift+V** (colar sem formatação).
3. Nos blocos de **Abas** e de **Acordeão** (FAQ), clique no item e use o mesmo editor.

Quando **tudo** estiver preenchido, se sobrar algum marcador, é só procurá-lo: em **Configurações da página → Avançado → CSS personalizado** você pode colar `.av-ph{background:none!important}` para tirar a cor de todos de uma vez.

**Números que precisam da sua confirmação:**
- Total do investimento usa **11 parcelas** (R$ 2.046 e R$ 2.882). Se forem 12, os totais mudam (R$ 2.232 e R$ 3.144). Eles aparecem em 3 lugares: tabela "Seu resumo", cartão "Seu investimento" e pergunta "Quanto custa?" do FAQ.
- Taxa de matrícula (aparece nos mesmos lugares).

## Passo 6 — Trocar as imagens provisórias

- **Foto da Camila** (seção "Quem conduz"): clique na imagem → **Escolher imagem** → envie a foto.
- **Professores**: hoje aparecem com as iniciais (LM, LO, LN, AR). Para usar foto, apague o círculo com as iniciais e arraste um widget **Imagem** para o lugar (ou me peça uma versão com fotos).
- **Depoimentos**: escreva as frases reais, com nome e cidade. O bloco "Vídeo curto" pode ser trocado por um widget **Vídeo**.
- Capas de livros e fotos da comunidade: já são do seu site. Para trocar, clique na imagem e escolha outra.

## Passo 7 — Testar e publicar

1. Clique em **Pré-visualizar alterações** (ícone de olho) e confira no computador **e no celular** (botão de telas, embaixo à esquerda no Elementor).
2. Se você usa **WP Rocket**: **Configurações → Limpar cache**. Se algo animado não funcionar (carrossel de problemas, faixa de capas), vá em **WP Rocket → Otimização de arquivos** e, em *Excluir arquivos JavaScript do atraso / da minificação*, adicione `/wp-content/plugins/aldeia-vendas/`. Depois limpe o cache de novo.
3. Clique em **Publicar**.
4. Abra o endereço da página em uma **janela anônima** (para ver como o visitante vê) e teste os botões "Lista de espera".

## Passo 8 (opcional) — Colocar essa página como início do site

O site hoje tem as páginas **Home** e **Sobre**. Sugestão segura: publique primeiro no endereço novo, teste por alguns dias, e depois troque:
1. **Configurações → Leitura → Sua página inicial exibe → Uma página estática**.
2. Em **Página inicial**, escolha a nova página. Salve.
3. Se quiser guardar a Home antiga, ela continua existindo (só deixa de ser a inicial). Para voltar atrás, repita o passo escolhendo a Home antiga.

---

## Como editar depois (mapa rápido)

Clique no elemento e edite no painel da esquerda, como em qualquer página do Elementor.

| Quero mudar... | Onde |
|---|---|
| Qualquer título ou texto | Clique no texto e digite |
| Link dos botões "Lista de espera" | Clique no botão → **Link**. São vários; use a busca de elementos (**Navegador**, ícone de camadas) para achar todos os botões |
| Números do topo (+500, 4h30, 9h, 30) | Cada número é um widget **Contador**: número final, prefixo (+) e sufixo (h30) |
| Módulos (5 abas) | Widget **Abas** da seção "Do chamado ao ponto final". Cada aba tem título e texto |
| Perguntas frequentes | Widget **Acordeão**: adicione, remova ou edite itens |
| Frases do carrossel "Você tem a ideia" | Quatro blocos (containers) com um texto cada. Para adicionar uma frase, **duplique** um bloco (botão direito → Duplicar). Os pontos do carrossel se ajustam sozinhos |
| Capas de livros | Faixa de imagens. Duplique ou apague imagens; o movimento é automático |
| Tabela de preços ("Seu resumo") | Widget **HTML** (código simples). Troque só os números entre `<td>` e `</td>`, por exemplo `<td>R$ 186</td>` |
| Equipe | Cartões. Para adicionar alguém, duplique um cartão |
| Cores e fontes | Ficam no plugin. Não precisa mexer |

**O que não apagar:** o campo **Avançado → Classes CSS** de cada bloco (nomes que começam com `av-`). É ele que aplica o visual. Pode editar tudo à vontade, só não apague esses nomes.

### Quando as matrículas abrirem (janeiro de 2027)
1. Troque o link dos botões "Lista de espera" pelo endereço do checkout.
2. Troque o texto dos botões (por exemplo, "Quero minha vaga").
3. Apague o aviso azul "Matrículas abrem em janeiro de 2027…" do cartão de investimento e a pergunta "Já posso me matricular?" do FAQ.
4. Atualize o aviso do topo da página.

---

## Se algo não sair como o esperado

| Problema | O que fazer |
|---|---|
| A página aparece sem cores, sem fontes (visual "cru"): botões verdes, títulos vermelhos | Confirme que você inseriu o modelo **v2**. Depois: o plugin não está ativo, ou há cache. Ative em **Plugins**, limpe o cache (WP Rocket, plugin de cache e o do navegador). Confirme também que o container principal tem a classe `av-page` (Avançado → Classes CSS) |
| A importação do modelo deu erro | Tente de novo pelo Elementor: **Modelos → Modelos salvos → Importar**. Se persistir, use o **Plano B** abaixo |
| Imagens não aparecem | Confirme que o plugin está ativo (as imagens ficam em `/wp-content/plugins/aldeia-vendas/assets/img/`). O nome da pasta do plugin precisa ser exatamente `aldeia-vendas` |
| Carrossel dos problemas ou faixa de capas parados | Veja o item de WP Rocket no Passo 7 |
| No editor do Elementor os blocos aparecem empilhados/sem animação | É proposital: dentro do editor as animações ficam desligadas para você editar com tudo visível. No site publicado elas funcionam |
| Quero desfazer tudo | Mova a página para a lixeira e desative o plugin. Nada mais no site foi alterado |

### Plano B (se o modelo não importar)
1. Crie uma página, abra no Elementor, arraste **um** widget **HTML** e cole todo o conteúdo de `plano-b-pagina-html-unico.html`. Use o layout **Elementor Canvas**.
2. O visual é idêntico, mas os textos ficam dentro do código (menos fácil de editar).

---

## Checklist antes de divulgar

- [ ] Nenhum trecho amarelo sobrando
- [ ] Número de parcelas, totais e taxa de matrícula conferidos
- [ ] Garantia, contrato e multa de cancelamento preenchidos (e revisados por quem cuida do jurídico)
- [ ] Todos os botões levam para o formulário/checkout certo
- [ ] Foto da Camila e depoimentos reais com autorização
- [ ] Testado no celular e no computador, em janela anônima
- [ ] Menu "Sobre" abre a página Sobre
- [ ] Cache limpo

Dúvidas ou ajustes: me mande o que viu (de preferência com um print) que eu corrijo o plugin ou o modelo e gero uma nova versão.
