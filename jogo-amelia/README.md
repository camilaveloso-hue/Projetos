# Fuga da Seita (inspirado em O Diário de Amélia)

Jogo de plataforma 2D (estilo Mario) que roda direto no navegador, no PC e no celular. Sem instalação, sem build: é só `index.html` + a pasta `assets/`.

## Rodar localmente
```
cd jogo-amelia && python3 -m http.server 8000   # abra http://localhost:8000
```
Atalho para testar fases: `?fase=3` (começa na fase 3), `&boss` (vai direto ao chefão), `&god` (invencível).

## Fases e chefões
1. Presa em Casa, **O Porteiro** (3 pisões; sem balões ainda)
2. Um Emprego Escondido, **O Gerente** (libera os balões de opinião, tecla X)
3. Janela do Quarto (fuga furtiva), **Mãe Radar & Pai Lanterna**
4. Os Olhos do Líder (fuga furtiva), **O Líder da Seita**
5. A Saída do Crush, **O Ciúme**
6. Um Beijo, Por Favor, **As Expectativas**, com final em cliffhanger e botão para o livro

## Personalizar
No topo do `<script>` do `index.html`: `CFG.BOOK_URL` (link de compra), `CFG.SHARE_TEXT` e o array `LEVELS` (nomes, textos do diário, chefões).

## Arte
Amélia, crush, coração, estrela, coroa e brilhos foram recortados da capa/guardas do livro (`assets/`). Pernas, inimigos e chefões são desenhados em código com a paleta do livro.
