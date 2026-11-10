# Parte técnica: títulos, descrições, robots.txt, domínio e dados estruturados

## 1. Título e descrição de cada página (plugin de SEO: Yoast, Rank Math ou SEOPress)
O WordPress não tem esses campos sozinho. Instale um plugin gratuito e preencha **Título SEO** e **Meta descrição** em cada página (até ~60 e ~155 caracteres).

| Página | Título SEO | Meta descrição |
|---|---|---|
| Home | Curso de escrita criativa para iniciantes — Aldeia Literária | Curso on-line de escrita criativa para iniciantes: aula ao vivo toda quarta, feedback individual, 18x de R$ 199 no Pix. Extensão universitária, certificado Anhanguera. |
| Sobre (`/novo-sobre/`) | Sobre a Aldeia Literária — história e equipe | Conheça a história da Aldeia Literária, fundada em 2023 por Camila Veloso, e a equipe que ajuda escritores iniciantes a transformar a ideia em livro. |
| Camila (`/sobre-a-fundadora/`) | Camila Veloso — fundadora da Aldeia Literária | Camila Veloso é Produtora Editorial formada pela UFSM e fundadora da Aldeia Literária, curso de escrita criativa para escritores iniciantes. |
| Laura (`/professores-laura-marques/`) | Laura Marques — professora de escrita criativa | Laura Marques é graduada em Produção Editorial pela UFSM, leitora crítica e professora de escrita criativa na Aldeia Literária. |
| Lucas (`/professores-lucas-oliveira/`) | Lucas Oliveira — doutor em Literatura Portuguesa (UFRJ) | Lucas Oliveira é Doutor em Letras pela UFRJ, na área de Literatura Portuguesa, com pesquisa sobre Jorge de Sena. Professor na Aldeia Literária. |
| Lavínia (`/professora-lavinia/`) | Lavínia Neres — mestra em Comunicação (UFSM) | Lavínia Neres é mestra em Comunicação pela UFSM, com pesquisa sobre leitura de livros digitais. Professora na Aldeia Literária. |
| Guia | Como escolher um curso de escrita criativa — Aldeia Literária | Guia para escolher um curso de escrita criativa: feedback, professores, formato, certificado, preço. Quando vale a pena e para quem é a Aldeia Literária. |
| Cancelamento (`/politica-de-cancelamento-e-reembolso/`) | Política de cancelamento e reembolso — Aldeia Literária | Regras de cancelamento e reembolso do curso: arrependimento em 7 dias, antes e depois do início das aulas. |
| Imprensa | Aldeia Literária na imprensa | Matérias sobre a Aldeia Literária, curso de escrita criativa para iniciantes: PublishNews e outros veículos, com data e link. |

Troque o título "novo sobre" da página Sobre por o da tabela.

## 2. Domínio principal: `aaldeialiteraria.com.br`
Decidido: o domínio com "aa" é o principal.
1. **Configurações → Geral:** *Endereço do WordPress* e *Endereço do site* = `https://aaldeialiteraria.com.br`.
2. **Canonical:** o plugin de SEO gera `<link rel="canonical">` em cada página. Confira em *Ver código-fonte* (procure `canonical`) que aponta para `https://aaldeialiteraria.com.br/...`.
3. **Redirecionamento 301 dos outros domínios** (`aldeialiteraria.com`, `www`): o domínio precisa apontar para a mesma hospedagem. No `.htaccess` (antes do bloco `# BEGIN WordPress`; faça backup antes):
```
RewriteEngine On
RewriteCond %{HTTP_HOST} ^(www\.)?aldeialiteraria\.com$ [NC,OR]
RewriteCond %{HTTP_HOST} ^www\.aaldeialiteraria\.com\.br$ [NC]
RewriteRule ^(.*)$ https://aaldeialiteraria.com.br/$1 [R=301,L]
```
   Sem acesso ao `.htaccess`, use o plugin *Redirection* ou o painel da hospedagem ("Redirecionamentos"). O **e-mail** em `aldeialiteraria.com` continua funcionando: o redirecionamento é só do site.
4. Teste: abra `http://aldeialiteraria.com/` e confirme que vai para `https://aaldeialiteraria.com.br/` (use `redirectchecker` ou a aba Rede do navegador).

## 3. robots.txt e sitemap
Mantenha as IAs liberadas. Em **SEO → Ferramentas → Editor de arquivos** (ou na raiz do site), o `robots.txt` pode ficar assim:
```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /

Sitemap: https://aaldeialiteraria.com.br/wp-sitemap.xml
```
(Use a URL do sitemap do seu plugin de SEO, se ele tiver outro.) Para aparecer nas respostas de busca por IA, o essencial é o `OAI-SearchBot` e o `Googlebot` não estarem bloqueados.

## 4. Dados estruturados (já estão nos arquivos)
Tudo é gerado a partir do texto visível da página:
- **Home:** `EducationalOrganization` (com razão social e CNPJ), `Course` + `CourseInstance` (online, 35 vagas) + `Offer` (18 parcelas de R$ 199 no Pix, mais matrícula de R$ 105) e `FAQPage` (as 15 perguntas visíveis).
- **Páginas dos professores:** `ProfilePage` + `Person` (formação, Lattes/ORCID).
- **Guia:** `Article` + `FAQPage`. **Imprensa:** `CollectionPage` + `ItemList`.
Valide cada endereço em `validator.schema.org` e em `search.google.com/test/rich-results`. Se o plugin de SEO também gerar schema, desligue o dele nessas páginas para não duplicar.
Observação: o Google só mostra resultado ampliado de FAQ para alguns tipos de site; o marcador continua útil para outros buscadores e IAs.

## 5. Desempenho e conteúdo no HTML
- Preço, programa, horários e FAQ estão em texto HTML (nenhum só em imagem). As respostas da FAQ já ficam abertas no código.
- Imagens com `alt` já estão preenchidas nos modelos. Imagens que você subir na Biblioteca de Mídia precisam de texto alternativo.
- **WP Rocket:** ative cache de página, *Carregar CSS otimizado* e *Atraso do JavaScript* (exclua `/wp-content/plugins/aldeia-vendas/`, como no passo a passo). Teste em `pagespeed.web.dev` (celular).

## 6. Links internos
As páginas novas (Guia e Imprensa) já se ligam à Home, à Sobre e aos professores. Falta você: **Aparência → Menus** → adicionar *Guia* e *Imprensa* ao menu principal e ao rodapé do tema (as páginas em Canvas têm o próprio cabeçalho e rodapé, já com esses links).
