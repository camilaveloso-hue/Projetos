# Site de Camila Veloso — O Diário de Amélia

Site estático (HTML + CSS, sem dependências). Funciona em qualquer hospedagem: Netlify, Vercel, Cloudflare Pages, GitHub Pages, Hostinger etc. Basta publicar esta pasta.

## O que já está pronto
- Home, **O Diário de Amélia** (página do livro com ficha, FAQ e dados estruturados `Book`/`FAQPage`), Livros, Manifesto, Sobre, Leituras (4 artigos pensados para busca) e 404.
- SEO técnico: `title`/`description` únicos, canonical, Open Graph, JSON-LD (Person, Book, Article, FAQ, Breadcrumb), `sitemap.xml`, `robots.txt`, HTML semântico, mobile-first, acessível.
- Identidade: cores e insígnias da sua marca (vermelho-sol, roxo, azul-vírgula, marinho).

## Antes de publicar (checklist)
1. **Domínio:** em `tools/build.py` troque `SITE["dominio"]` (hoje `https://www.camilaveloso.com.br`, um palpite) e rode `python3 tools/build.py`.
2. **Redes:** preencha `instagram`, `podcast`, `aldeia` e `email` em `SITE`; aparecem no rodapé e nos dados estruturados.
3. **Sua foto:** hoje há um espaço com a insígnia (home e Sobre). Salve a foto em `assets/img/` e troque o bloco `.foto-slot`.
4. **Capa em alta:** a capa usada veio da loja da editora (541 px). Peça o arquivo em alta à Fissura e substitua `assets/img/capa-diario-de-amelia.webp`.
5. **Outros livros:** adicione capa, sinopse e link de compra (lista `LIVROS` em `tools/build.py`).
6. Revise os textos dos artigos em `ARTIGOS` — são rascunhos; ajuste para a sua voz.

## Depois de publicar (o que ajuda a ranquear)
- Cadastre o site no **Google Search Console** e envie `https://SEUDOMINIO/sitemap.xml`.
- Peça indexação da home e da página do livro.
- Coloque o link do site no Instagram, no podcast, na página de autora da Amazon e na loja da editora (backlinks pesam).
- Publique textos novos em `ARTIGOS` com regularidade, mirando buscas como "livros sobre liberdade" ou "romance young adult sobre família opressora".
- Após o lançamento (23/10/2026) atualize os selos "Pré-venda" e o `availability` do JSON-LD.

## Editar e gerar
Conteúdo em `tools/build.py`, visual em `assets/css/style.css`.
```
python3 tools/build.py        # regenera as páginas
python3 -m http.server 8000   # prévia em http://localhost:8000
```
