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

### Situação (atualizada com a sua resposta)

Você cancelou o "40% de desconto para os primeiros inscritos". A regra nova é: **R$ 70 de desconto na matrícula para quem comprar o "aulão universal"**. Ainda faltam dois dados, então **não escrevi nenhum preço novo no site**:

1. **Valor da matrícula sem desconto**: R$ 105, R$ 107 ou R$ 175? (Você citou "107"; o site diz 105; 105 + 70 = 175, que é o preço cheio antes dos 40%.)
2. **Descrição do aulão universal** (o que é, data, como compra, se o desconto vale para quem compra antes ou depois da matrícula). O site não menciona o aulão em nenhum lugar.

Estrutura do texto que vou usar assim que você confirmar (só a conta; os valores ficam em branco até lá):

- Tabela da home: linha "Mensalidade" → `18x de R$ 199` + `18 × R$ 199 = R$ 3.582 em parcelas` (some "no total"); linha "Taxa de matrícula" → `R$ [MATRÍCULA]`; nova linha "Total do curso" → `R$ [TOTAL]` + `18 × R$ 199 + R$ [MATRÍCULA]`.
- FAQ (home e guia, a mesma frase): "…taxa de matrícula de R$ [MATRÍCULA] e 18 parcelas de R$ 199. A conta é: 18 × R$ 199 = R$ 3.582, mais R$ [MATRÍCULA], total de R$ [TOTAL]."
- O desconto do aulão entra como frase separada, só quando houver a descrição.

Onde a frase "40% de desconto para os primeiros inscritos" precisa sair: home (tabela, 2 FAQs, JSON-LD) e guia (2 lugares), e o texto de abertura do Tally se citar. Como desfazer: `wordpress/entrega/home-v29.json` está no git e o Elementor guarda revisões (Histórico → Revisões).

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

### Regras 301 (NÃO aplicadas)

Servidor LiteSpeed (aceita `.htaccess`). A regra única, que cobre http, www e os outros dois domínios, está no fim da seção, em "Regra 301 final". Testes depois de aplicar: `curl -sI http://aaldeialiteraria.com.br/como-escolher-curso-de-escrita-criativa/` deve dar `301` com `location: https://aaldeialiteraria.com.br/como-escolher-curso-de-escrita-criativa/`; o mesmo para `http://www.aaldeialiteraria.com.br/blog/` e `https://www.aaldeialiteraria.com.br/`.

### Os outros dois domínios (você confirmou que são seus)

O que o DNS público mostra de `aldeialiteraria.com`:

- Nameservers: **Wix** (`ns10/ns11.wixdns.net`). O DNS é editado no painel do Wix.
- **E-mail: Google Workspace** (registros MX `aspmx.l.google.com` e SPF `include:_spf.google.com`). Estes registros **não podem ser apagados nem alterados**, senão o e-mail para de funcionar.
- Site: registros `A` na raiz e `CNAME` do `www` apontando para o Wix. Só estes dois são o problema (a página de erro do Wix).

Plano que **não derruba o e-mail** (você não precisa tirar o domínio do Wix): mexer apenas em dois registros no DNS avançado do Wix.

1. Na hospedagem do site (a mesma de `aaldeialiteraria.com.br`), adicionar `aldeialiteraria.com` e `www.aldeialiteraria.com` como **domínio alias/estacionado** (sem criar site novo) e ligar o SSL automático para eles. Pergunte ao suporte, se não achar.
2. No Wix: Domínios → aldeialiteraria.com → **Gerenciar registros DNS**. Alterar **só**: o registro `A` da raiz (@) para o IP do servidor do site (hoje `177.73.233.37` no DNS público; confirme no painel da hospedagem) e o `CNAME` do `www` para `aaldeialiteraria.com.br`. **Não tocar** em MX, TXT/SPF, DKIM nem em outros registros.
3. Colar a regra do bloco abaixo no `.htaccess` (versão com os 3 domínios).
4. Esperar propagação (de minutos a algumas horas) e testar: `curl -sI https://aldeialiteraria.com/` deve dar `301` para `https://aaldeialiteraria.com.br/`, e mandar um e-mail de teste para `@aldeialiteraria.com` para confirmar que o e-mail segue funcionando.
- Desfazer: no Wix, restaurar o registro `A`/`CNAME` anteriores (anote os valores atuais **antes** de editar: `A` 185.230.63.171, 185.230.63.186 e 185.230.63.107; `CNAME www` = `cdn3.wixdns.net`; confirme no painel).

`aldeialiteraria.com.br` (sem o "a" duplo) hoje **não responde no DNS (NXDOMAIN)**: o domínio existe no registro.br mas não tem DNS configurado. No registro.br → Editar DNS: usar o DNS do próprio registro.br e criar `A` (raiz) e `CNAME` (www) iguais ao item 2. Sem e-mail ali, não há risco. Depois, as mesmas etapas 1, 3 e 4.

### Regra 301 final (todos os domínios, um salto, mantém o caminho)

```apache
# BEGIN Aldeia - versão única do domínio (https + sem www + domínio oficial)
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteCond %{HTTP_HOST} !^aaldeialiteraria\.com\.br$ [NC,OR]
RewriteCond %{HTTPS} !=on
RewriteRule ^(.*)$ https://aaldeialiteraria.com.br/$1 [R=301,L]
</IfModule>
# END Aldeia - versão única do domínio
```

- Faça a **cópia do `.htaccess`** antes (Gerenciador de arquivos da hospedagem → baixar). Cole o bloco **acima** de `# BEGIN WordPress` e do bloco do WP Rocket.
- Cuidado com o `wp-admin`/`wp-login` se o seu servidor ficar atrás de proxy/CDN que termina o HTTPS: se o site entrar em loop de redirecionamento, remova a linha `RewriteCond %{HTTPS} !=on` (a regra de host continua valendo) e me avise.
- Depois de aplicar: limpar o cache do WP Rocket e rodar os testes da tabela da seção 3 (esperado: tudo `301` em um salto, ou `200` só em `https://aaldeialiteraria.com.br/`).

## 4. Pronto quando

- [ ] Preço igual em todo o site: **bloqueado** até você mandar (a) matrícula sem desconto e (b) a descrição do aulão universal. Depois eu gero `home-v30.json` e o guia para você colar.
- [ ] Toda variante termina em um canonical: hoje só falta o http em subpáginas e a decisão sobre os dois outros domínios.
