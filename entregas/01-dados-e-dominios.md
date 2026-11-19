# Tarefa 1 — Dados que se contradizem (verificado em 19/11/2026)

Nada foi alterado em produção. Tudo abaixo é leitura (curl e API REST pública) + proposta.

## 0. Acesso que tenho

| Recurso | Situação | Consequência |
|---|---|---|
| Repositório `camilaveloso-hue/Projetos` | Sim (branch `claude/inspiring-cori-lurrv4`) | Tem os modelos Elementor, o plugin `aldeia-vendas` e as ferramentas de build. **Não é uma cópia do site no ar.** |
| API REST do WordPress, leitura | Sim, pública (páginas, posts, sitemap, `/wp-json/`) | Consigo auditar conteúdo e HTML publicado. |
| API REST do WordPress, escrita | **Não** (POST sem login → 401; não tenho senha de aplicação) | Não crio rascunho nem edito nada direto no site. |
| WP-CLI / SSH / banco / painel do servidor | **Não** | Não aplico redirecionamento no servidor, não edito `.htaccess` nem `functions.php` / mu-plugin. |
| Yoast / Elementor por dentro | Não | Edição de título, meta e Elementor continua com você (colar), ou com o plugin que você instala. |

Resultado: entrego **arquivos prontos para colar** em `./entregas/` e o plugin `aldeia-vendas.zip`.
Se você quiser que eu publique rascunhos direto, o caminho seguro é criar uma *senha de aplicação* (Usuários → Perfil) para um usuário Editor; só vale se você decidir isso.

Mudou algo desde o seu texto de 19/11? Não. Confirmei no ar: 35 vagas por módulo, 18 meses, 18 × R$ 199, matrícula R$ 105, lista de espera com Tally `0QNWPy`.

## 1. Preço: onde está a contradição

| Onde | O que diz |
|---|---|
| Home, tabela do plano, linha "Mensalidade" | `18x de R$ 199` e embaixo **`R$ 3.582 no total`** |
| Home, tabela, linha "Taxa de matrícula" | `R$ 105 com 40% de desconto…` (linha separada, sem somar) |
| Home, FAQ "Quanto custa…" | "…R$ 105 + 18 parcelas de R$ 199, totalizando **R$ 3.687**" |
| Home, JSON-LD (Course/Offer) | `price 199`, descrição com "Total: R$ 3.687" |
| Guia `/como-escolher-curso-de-escrita-criativa/` (2 lugares) | R$ 3.687 (correto, mas sem mostrar a conta) |

Causa: "R$ 3.582 no total" é só a soma das parcelas (18 × 199). A matrícula (R$ 105) vem depois. Quem lê só a tabela entende que o curso custa R$ 3.582.

### Texto proposto — tabela da home

- Linha **Mensalidade**: `18x de R$ 199` / subtexto **`18 × R$ 199 = R$ 3.582 em parcelas`** (some "no total").
- Linha **Taxa de matrícula**: `R$ 105` / subtexto `com 40% de desconto para os primeiros inscritos` **[CONFIRMAR: o R$ 105 já é o valor com desconto?]**
- **Nova linha "Total do curso"**: **`R$ 3.687`** / subtexto `18 × R$ 199 + R$ 105 de matrícula`.

### Texto proposto — FAQ da home e do guia (mesma frase nos dois)

> Em 2027, o curso terá uma taxa de matrícula de R$ 105 e 18 parcelas de R$ 199. A conta é: 18 × R$ 199 = R$ 3.582, mais R$ 105 de matrícula, o que dá **R$ 3.687 no total**. A matrícula tem 40% de desconto para os primeiros inscritos. As parcelas são pagas no Pix, sem usar o limite do cartão, com recorrência mensal.

O JSON-LD (FAQPage) da home é gerado a partir da FAQ visível, então se atualiza junto. A descrição do `Offer` já diz "Total: R$ 3.687" e fica como está.

Como desfazer: os modelos anteriores estão no git (`wordpress/entrega/home-v29.json`) e o Elementor guarda revisões (Histórico → Revisões).

## 2. Formulários e páginas antigas (contrato anual / escolha de módulos)

- **No site:** varri as 10 páginas e 2 posts publicados (API REST). **Nenhuma** menção a contrato anual, a escolher quantos módulos cursar ou a "Inscrição 2026/2". O único link de inscrição é `https://tally.so/r/0QNWPy` (home, guia, imprensa, cancelamento, professores, fundadora, novo-sobre).
- **Tally `0QNWPy` (ativo):** título "entre na lista da próxima turma", turma de janeiro de 2027, campos nome, e-mail, WhatsApp, fase do livro, consentimento + Política de Privacidade. Sem contrato anual, sem módulos, sem preços. A página 2 do formulário não apareceu na leitura; confira no painel.
- **Tally "Inscrição 2026/2":** **não encontrei na web aberta** (busca e links do site). Tally não lista formulários de uma conta, então só você vê isso. **Preciso de você:** no painel do Tally, abra cada formulário antigo e (a) feche as respostas ("Fechar formulário") ou (b) edite o texto. Tire também o link de lá de: bio do Instagram/TikTok, links fixados, mensagens salvas do WhatsApp e assinatura de e-mail.
- **Fora do seu controle:** matérias de 2024 (PublishNews, Jornal O Candeeiro, HojePR, Jornal do Belém) descrevem o formato antigo. Não dá para editar; a página /imprensa/ já as data como 2024.
- **Páginas internas a rever:** `/novo-sobre/` (título "Sobre a Aldeia Literária — história e equipe", está no sitemap e é o destino do menu "Sobre") e `/sobre-a-fundadora/`. `/sobre` redireciona para a fundadora. Não é contradição de preço, mas são duas portas para "sobre"; decidiremos na tarefa 3.

## 3. Variantes do domínio

| URL testada | Resultado | Canonical |
|---|---|---|
| `http://aaldeialiteraria.com.br/` | 301 → `https://aaldeialiteraria.com.br/` | `https://aaldeialiteraria.com.br/` |
| `http://www.aaldeialiteraria.com.br/` | 301 → `https://aaldeialiteraria.com.br/` | idem |
| `https://aaldeialiteraria.com.br/` | 200 | idem (versão oficial) |
| `https://www.aaldeialiteraria.com.br/` | 301 → `https://aaldeialiteraria.com.br/` | idem |
| `https://aaldeialiteraria.com.br/index.php`, `/?utm_source=x` | 200 | idem (aponta para a raiz) |
| **`http://aaldeialiteraria.com.br/<subpágina>/`** | **200, sem redirecionar** | aponta para a `https` |
| `http://www.aaldeialiteraria.com.br/blog/` | 301 → **`http://`** sem www (depois 200 em http) | aponta para a `https` |
| `aldeialiteraria.com.br` (sem o "a" duplo) | **não existe no DNS (NXDOMAIN)** | — |
| `https://aldeialiteraria.com` | 404, página de erro do **Wix** ("ConnectYourDomain Error") | sem canonical, `noindex` |
| `https://www.aldeialiteraria.com` | 404 (Wix, via Cloudflare) | — |

Leitura:
1. A home já termina num único canonical. O buraco é **http em subpáginas**: elas abrem em http com 200 (o redirecionamento da home é feito pelo WordPress, só na raiz). O canonical protege, mas o http duplicado fica rastreável e o `www` faz 2 saltos.
2. `aldeialiteraria.com.br` não está registrado/apontado. Se alguém registrar, pode se passar pela marca.
3. `aldeialiteraria.com` aponta para um site Wix que mostra erro. Se for seu, quem digitar esse endereço vê um 404.

### Regras 301 propostas (NÃO aplicadas)

Servidor: LiteSpeed (aceita `.htaccess`). Colar **acima** de `# BEGIN WordPress` e do bloco do WP Rocket, depois de fazer cópia do arquivo:

```apache
# BEGIN Aldeia - versão única do domínio (https + sem www)
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteCond %{HTTPS} !=on [OR]
RewriteCond %{HTTP_HOST} ^www\.aaldeialiteraria\.com\.br$ [NC]
RewriteRule ^(.*)$ https://aaldeialiteraria.com.br/$1 [R=301,L]
</IfModule>
# END Aldeia - versão única do domínio
```

- Efeito: qualquer http ou www vai em **um** salto para `https://aaldeialiteraria.com.br/…` mantendo o caminho.
- Testar depois: `curl -sI http://aaldeialiteraria.com.br/como-escolher-curso-de-escrita-criativa/` deve dar `301` com `location: https://aaldeialiteraria.com.br/como-escolher-curso-de-escrita-criativa/`; o mesmo para `http://www…/blog/` e `https://www…/`.
- Desfazer: apagar o bloco ou restaurar a cópia do `.htaccess`; limpar o cache do WP Rocket.
- Alternativa sem editar arquivo: no WP Rocket (aba Avançado) ou no host, ligar "forçar HTTPS"; ou o plugin Redirection. A regra acima é a mais enxuta.

Para os outros domínios (depende de você, ver perguntas):
- `aldeialiteraria.com.br`: se for seu, registrar em registro.br e apontar para o mesmo servidor com 301 para o domínio oficial; se não for, nada a fazer.
- `aldeialiteraria.com`: se for seu, no registrador/Wix apontar o DNS para o servidor do site e incluir a regra `RewriteCond %{HTTP_HOST} ^(www\.)?aldeialiteraria\.com$ [NC]` → `https://aaldeialiteraria.com.br/`; se não for seu, ignorar.

## 4. Pronto quando

- [ ] Preço igual em todo o site: precisa do seu OK no texto + resposta sobre o R$ 105. Depois eu gero o novo `home-v30.json` e o guia, para você colar.
- [ ] Toda variante termina em um canonical: hoje só falta o http em subpáginas e a decisão sobre os dois outros domínios.
