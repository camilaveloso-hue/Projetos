# Aldeia Literária: Professores e Tipografia

Plugin de WordPress que faz duas coisas.

1. Troca a fonte dos títulos do site inteiro (home, Sobre e demais páginas) para **Literata**.
2. Cria páginas de professores, fora do menu mas indexáveis, com dados estruturados para Google e assistentes de IA.

## Instalação
1. Compacte a pasta `aldeia-literaria-professores` em .zip.
2. No WordPress: Plugins > Adicionar novo > Enviar plugin > ative.
3. Na ativação são criados 5 professores **em rascunho** (com a bio que está hoje no site) e a página "Professores do semestre" (rascunho, com o shortcode `[aldeia_professores]`).
4. Em **Professores** no menu lateral, abra cada um, preencha os campos (Lattes, ORCID, LinkedIn, obras, perguntas frequentes), adicione a foto em "Imagem destacada" e publique.
5. Publique a página "Professores do semestre".
6. No Elementor, em cada card da home, ligue o botão "Saiba mais" ao link `/professor/nome-do-professor/`.
7. Não adicione essas páginas ao menu. Não marque noindex em plugin de SEO.

## Por que essa estrutura
- Resumo em uma frase no topo, porque o início da página é o trecho mais citado por IAs.
- Hierarquia H1 > H2 > H3, FAQ visível e dados estruturados `ProfilePage`, `Person` e `FAQPage` que repetem o que está na tela.
- `sameAs` com Lattes, ORCID e redes confirma que o professor é uma pessoa real e única.
- Fatos verificáveis (formação, obras com ano e editora) em vez de adjetivos.
- A documentação do Google diz que não há marcação especial para IA; a página só precisa estar indexada e com texto legível.

## Observação sobre LGPD
A fonte é carregada do Google Fonts. Para evitar o envio de IP do visitante ao Google, hospede a Literata no próprio servidor (plugin "OMGF" faz isso).
