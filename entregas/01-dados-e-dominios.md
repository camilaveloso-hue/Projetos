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

### Decisão (confirmada por você em 19/11)

- Matrícula sem desconto: **R$ 105**. O "40% para os primeiros inscritos" **sai do site**.
- Desconto de **R$ 70 na matrícula para quem comprar o Aulão Universal** (matrícula de R$ 35 para esse grupo). Você vai atualizar a página do Aulão, que ainda diz "50% de desconto na matrícula se comprar até 23/11".
- **O desconto do Aulão não entra no site do curso por enquanto**: o site não tem página nem descrição do Aulão, e você não definiu prazo. Quando a página do Aulão estiver no ar, incluo uma frase com link.

### Texto aplicado nos modelos novos (home v30 e guia)

- Tabela da home: `Mensalidade 18x de R$ 199` / `R$ 3.582 em 18 parcelas` · `Taxa de matrícula R$ 105` · nova linha **`Total do curso R$ 3.687`** / `18 × R$ 199 + R$ 105 de matrícula`.
- FAQ da home e do guia (mesma frase): "Em 2027, o curso terá uma taxa de matrícula de R$ 105 e 18 parcelas de R$ 199. A conta é: 18 × R$ 199 = R$ 3.582, mais R$ 105 de matrícula, o que dá R$ 3.687 no total. …"
- FAQ "O que é a taxa de matrícula?": "A taxa é de R$ 105. Ela cobre a formulação do seu contrato e a sua entrada na comunidade da Aldeia Literária."
- JSON-LD: o FAQPage é gerado do texto visível (atualiza junto) e a descrição do `Offer` perdeu o trecho dos 40%. Preço nos dois lugares: R$ 3.687.

Arquivos: `wordpress/entrega/home-v30.json` (+ `home-v30-colar-no-widget-html.html`) e `wordpress/entrega/paginas/guia.json` (+ `guia-colar-no-widget-html.html`). Tocados no repositório: `tools/src/body.html`, `tools/build_planb.py`, `tools/build_paginas.py`.

Como testar depois de colar: abrir a home e o guia e procurar "3.582" e "3.687" (a primeira só aparece como "R$ 3.582 em 18 parcelas" e dentro da conta; nenhuma frase pode dizer "no total" ao lado de R$ 3.582) e "40%" (não pode aparecer). Como desfazer: Elementor → Histórico → Revisões, ou colar o modelo anterior (`home-v29.json` está no git).

Fora do site, procure e troque "40%" / "primeiros inscritos" em: bio do Instagram/TikTok, posts fixados, mensagens salvas do WhatsApp, a página do Aulão e o texto do Tally.

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

- [ ] Preço igual em todo o site: modelos prontos (home v30 e guia); falta você colar e testar (seção 1).
- [ ] Toda variante termina em um canonical: hoje só falta o http em subpáginas e a decisão sobre os dois outros domínios.
