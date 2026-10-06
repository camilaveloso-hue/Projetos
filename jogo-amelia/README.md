# Fuga da Seita (inspirado em O Diário de Amélia)

Jogo de plataforma 2D (estilo Mario) que roda direto no navegador, no PC e no celular. Sem instalação, sem build: é só `index.html` + a pasta `assets/`.

## Rodar localmente
```
cd jogo-amelia && python3 -m http.server 8000   # abra http://localhost:8000
```
Atalho para testar fases: `?fase=3` (começa na fase 3), `&boss` (vai direto ao chefão), `&god` (invencível).

## Fases e chefões
1. Presa em Casa, **O Porteiro** (2 pisões; sem balões ainda)
2. Um Emprego Escondido, **O Tesoureiro** (libera os balões de opinião, tecla X)
3. Ronda da Noite (furtiva), **O Vigia**
4. Antes do Beijo (correr antes que o Lucca beije a Michelle), **O Medo** (a sombra da própria Amélia)
5. Mesa para Dois (restaurante onde Lucca e Michelle estão), **O Fiscal da Seita**, com final em cliffhanger e botão para o livro

## Personalizar
No topo do `<script>` do `index.html`: `CFG.BOOK_URL` (link de compra), `CFG.SHARE_TEXT` e o array `LEVELS` (nomes, textos do diário, chefões).

## Arte
Amélia, crush, coração, estrela, coroa e brilhos foram recortados da capa/guardas do livro (`assets/`). Pernas, inimigos e chefões são desenhados em código com a paleta do livro.
