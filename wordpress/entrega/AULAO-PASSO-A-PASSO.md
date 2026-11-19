# Como colocar o AULÃO UNIVERSAL no site (página escondida)

Faça as etapas **na ordem**. Cada uma diz o que clicar e como saber se deu certo.

## Os arquivos (pasta `wordpress/entrega/`)
| Arquivo | Para que serve |
|---|---|
| `aldeia-vendas.zip` | **Plugin versão 1.4.0.** Guarda as fotos e as fontes da página do aulão. Reinstale por cima do atual. |
| `aulao-universal-v1.json` | **Modelo do Elementor** da página. |
| `aulao-universal-v1-colar-no-widget-html.html` | **Plano B:** o mesmo conteúdo para colar num widget HTML, se a importação do modelo falhar. |

O plugin novo **não muda** nenhuma outra página do site (Home, Sobre, professores e blog continuam iguais).

## Etapa 1: Backup
Faça um backup do site (plugin de backup ou o da hospedagem).

## Etapa 2: Reinstalar o plugin
1. **Plugins → Adicionar plugin → Enviar plugin** → escolha `aldeia-vendas.zip` → **Instalar agora**.
2. Quando aparecer "o plugin já existe", clique em **Substituir o atual pelo enviado**.
3. Confirme que está **Ativo** e que a versão é **1.4.0**.

## Etapa 3: Importar o modelo
1. **Elementor → Modelos → Modelos salvos** → **Importar modelos** → envie `aulao-universal-v1.json`.
2. Deve aparecer **ALDEIA Aulão Universal v1**.

## Etapa 4: Criar a página (escondida)
1. **Páginas → Adicionar nova**. Título: `AULÃO UNIVERSAL`.
2. Em **Link permanente**, deixe o endereço **`aulao-universal`**. A página fica em `https://aaldeialiteraria.com.br/aulao-universal/`.
3. Clique em **Editar com o Elementor**.
4. Pasta preta → **Meus modelos** → **Inserir** o modelo **ALDEIA Aulão Universal v1**.
5. **Engrenagem (configurações da página) → Layout da página → Elementor Canvas**. Sem isso aparece o menu do tema por cima.
6. **Publicar**.

**Para a página ficar escondida, não faça estas coisas:**
- não coloque a página em **Aparência → Menus** nem em widgets do rodapé;
- não coloque o endereço na Home, no blog nem em outras páginas;
- não escolha esta página em **Configurações → Leitura**.

A página fica pública para quem tiver o link (use o link nas redes sociais), mas ninguém chega a ela navegando pelo site.

## Etapa 5: Link de compra (já está no modelo)
Os 4 botões de compra ("QUERO O AULÃO" na faixa do topo e "Quero o AULÃO UNIVERSAL" no começo, no cartão de oferta e na chamada final) já apontam para `https://pay.kiwify.com.br/TyiiZBm`. **Não precisa trocar nada.** Para mudar o link no futuro, use **Ctrl+F** no campo **Código HTML** do Elementor e troque todos os `https://pay.kiwify.com.br/TyiiZBm` pelo novo endereço.

## Etapa 6: Título e descrição para o Google e as IAs (Yoast)
Na página, role até a caixa do **Yoast SEO** e preencha:
- **Título SEO:** `AULÃO UNIVERSAL: como escrever um livro | Camila Veloso`
- **Meta descrição:** `Aula gravada de Camila Veloso, fundadora da Aldeia Literária, para quem quer escrever um livro e não sabe por onde começar. Promoção de Black Friday até 30/11.`
- **Endereço (slug):** `aulao-universal`

**Decisão sua:** em **Avançado → Permitir que mecanismos de busca mostrem esta página**, deixe **Sim** se quiser que o Google e as IAs possam recomendar a página. Escolha **Não** apenas se quiser a página **totalmente invisível** para buscadores; nesse caso as IAs não vão encontrá-la.

A página já traz, no código, os dados estruturados (Curso, Oferta e Perguntas frequentes). Se o Yoast tiver a opção de desligar o schema desta página, desligue para não duplicar.

## Etapa 7: Conferir (janela anônima e celular)
- [ ] Abre no celular, sem menu do tema por cima, com o fundo creme.
- [ ] A faixa preta no topo mostra "A promoção acaba em:" com o cronômetro andando e o botão **QUERO O AULÃO**.
- [ ] O botão **Ver o preço** abre o preço de **R$ 70** (riscado R$ 100), o botão de compra e o bônus de R$ 70 na matrícula.
- [ ] Os 4 botões de compra abrem a página de compra da Kiwify, com o produto e o preço certos.
- [ ] As fotos do carrossel e as capas aparecem; as setas funcionam.
- [ ] A página **não** aparece no menu nem na Home.
- [ ] Se o cronômetro ficar parado em "7d 00h 00min 00s": em **WP Rocket → Otimização de arquivos**, desative o **Atraso de JavaScript** para esta página (ou exclua `data-count`), e limpe o cache.
- [ ] Se as fotos ou as fontes não aparecerem: confirme que o plugin está na versão **1.4.0** e limpe o cache.

## O que muda sozinho (sem você mexer)
- **Até 30/11, 23h59 (horário de Brasília):** preço de **R$ 70**, riscado R$ 100, com cronômetro, e o bônus de **R$ 70 de desconto na matrícula da Aldeia Literária** para todos que comprarem.
- **Depois de 30/11:** a página **continua no ar** e passa a mostrar **R$ 100**, sem cronômetro, sem o bônus e sem a palavra "promoção". A troca acontece no navegador de quem abre a página, então não precisa republicar nem limpar cache.

## Antes de divulgar, confirme
- [ ] **Formas de pagamento** aceitas na Kiwify e o **preço cadastrado lá (R$ 70)**. Depois de 30/11 a página mostra R$ 100, então o valor no checkout precisa mudar também.
- [ ] **Prazo de 1 ano** de acesso e **reembolso de 7 dias** valem para o aulão.
- [ ] **"+400 escritores"** é o número correto (seus arquivos antigos falavam em +500).
- [ ] Todos os alunos das fotos do carrossel **autorizaram** o uso na página.
- [ ] **Material de apoio + atividade** existem e serão entregues.

## Se algo não sair como o esperado
| Problema | O que fazer |
|---|---|
| Menu do tema por cima da página | Falta o layout **Elementor Canvas** (Etapa 4, passo 5) |
| Página sem cores ou com letras comuns | Plugin sem a versão 1.4.0 ou cache. Reinstale e limpe o cache |
| A importação do modelo deu erro | **Plano B:** crie a página, arraste **um** widget **HTML**, cole todo o conteúdo de `aulao-universal-v1-colar-no-widget-html.html` e escolha **Elementor Canvas** |
| Faixa do topo não fica fixa | Raro. Desative temporariamente plugins de otimização de CSS e teste de novo |
| Quero desfazer | Mande a página para a lixeira |
