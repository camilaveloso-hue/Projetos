# Site de Camila Veloso: O Diário de Amélia

Site estático (HTML + CSS + um arquivo de JavaScript, sem dependências). Funciona em qualquer hospedagem: Netlify, Vercel, Cloudflare Pages, GitHub Pages, Hostinger etc. Basta publicar esta pasta.

## Páginas
Home, **O Diário de Amélia** (venda: contagem regressiva, brindes, autógrafo, perguntas frequentes), Livros, Sobre, **Links** (para a bio das redes), Manifesto, Leituras (4 artigos para busca) e 404.

## Antes de publicar
1. **Domínio:** em `tools/build.py` troque `SITE["dominio"]` e rode `python3 tools/build.py`.
2. **Preço:** `PRECO` e `PRECO_DE` em `tools/build.py` aparecem em todo o site e nos dados estruturados. Têm que bater com a loja da Editora Fissura.
3. **Medição dos links:** veja a seção abaixo.
4. **Redes:** preencha `instagram`, `podcast` e `email` em `SITE`.
5. Peça à Fissura a capa em alta e substitua `assets/img/capa-diario-de-amelia-capa.jpg`.

## Medir cliques e origem (página /links/)
O painel é o do **GoatCounter** (grátis, sem cookies, só você entra com login):
1. Crie a conta em goatcounter.com e escolha um código (ex.: `camilaveloso`).
2. Escreva o código em `SITE["goatcounter"]` e rode `python3 tools/build.py`.
3. Em cada rede use um endereço diferente na bio, para saber de onde veio o clique:
   `https://SEUDOMINIO/links/?ref=instagram`, `?ref=tiktok`, `?ref=youtube`, `?ref=whatsapp`.
4. No painel, cada link aparece como evento (`link-pre-venda`, `link-newsletter`, `link-youtube`, `link-aldeia`) com a origem.
Os links de saída também levam `utm_source=camilaveloso&utm_medium=linkinbio`, o que mostra a origem no Substack e na loja da editora.

## Editar e gerar
Textos das páginas em `tools/paginas/*.html`, artigos e configuração em `tools/build.py`, visual em `assets/css/style.css`.
```
python3 tools/build.py        # regenera as páginas
python3 -m http.server 8000   # prévia em http://localhost:8000
```

## Depois do lançamento (23/10/2026)
Atualize preço e selos de pré-venda e o `availability` dos dados estruturados em `tools/build.py`.
