<?php
/**
 * Blog da Aldeia Literária: lista de artigos, categorias e artigo individual, em estilo simples de leitura (tipo Substack).
 * Usa os templates da pasta /templates e o CSS do plugin. Não altera o conteúdo dos artigos.
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Em que tela estamos: 'single' (um artigo), 'lista' (página de artigos, categoria ou etiqueta) ou '' (outras telas).
 * A página inicial do site NUNCA é trocada: só a "Página de posts" (Configurações > Leitura).
 */
function aldeia_blog_contexto() {
	if ( is_admin() || ! apply_filters( 'aldeia_blog_ativo', true ) ) {
		return '';
	}
	if ( is_singular( 'post' ) ) {
		return 'single';
	}
	if ( is_home() && ! is_front_page() ) {
		return 'lista';
	}
	if ( is_category() || is_tag() ) {
		return 'lista';
	}
	return '';
}

add_filter( 'template_include', function ( $template ) {
	$c = aldeia_blog_contexto();
	if ( '' === $c ) {
		return $template;
	}
	$file = dirname( __DIR__ ) . '/templates/' . ( 'single' === $c ? 'blog-single.php' : 'blog-lista.php' );
	return file_exists( $file ) ? $file : $template;
}, 99 );

/* 10 artigos por página (lista simples). */
add_action( 'pre_get_posts', function ( $q ) {
	if ( is_admin() || ! $q->is_main_query() || ! apply_filters( 'aldeia_blog_ativo', true ) ) {
		return;
	}
	if ( ( $q->is_home() && ! $q->is_front_page() ) || $q->is_category() || $q->is_tag() ) {
		$q->set( 'posts_per_page', 10 );
	}
} );

/**
 * Nome do autor. Se a conta do WordPress ainda mostra só o nome de usuário (sem espaço, como "aaldeial"),
 * usa o nome da fundadora. Para outro autor com nome completo, mostra o nome dele.
 */
function aldeia_blog_autor() {
	$n = trim( (string) get_the_author() );
	if ( '' === $n || false === strpos( $n, ' ' ) ) {
		$n = 'Camila Veloso';
	}
	return apply_filters( 'aldeia_blog_autor', $n );
}

function aldeia_blog_autor_bio() {
	$bio = trim( (string) get_the_author_meta( 'description' ) );
	if ( '' === $bio && 'Camila Veloso' === aldeia_blog_autor() ) {
		$bio = 'Fundadora da Aldeia Literária. Produtora Editorial formada pela UFSM.';
	}
	return $bio;
}

/* Comentários: usa o modelo do plugin, só nos artigos do blog. */
add_filter( 'comments_template', function ( $file ) {
	if ( 'single' === aldeia_blog_contexto() ) {
		$mine = dirname( __DIR__ ) . '/templates/blog-comentarios.php';
		if ( file_exists( $mine ) ) {
			return $mine;
		}
	}
	return $file;
} );

/* Um comentário na lista (usado por wp_list_comments). O WordPress fecha o <li> sozinho. */
function aldeia_blog_comentario( $comment, $args, $depth ) {
	$GLOBALS['comment'] = $comment; // phpcs:ignore WordPress.WP.GlobalVariablesOverride
	?>
<li id="comment-<?php comment_ID(); ?>" <?php comment_class( 'ab-comment' ); ?>>
  <article>
    <header class="ab-comment__head"><strong><?php comment_author(); ?></strong> <time datetime="<?php echo esc_attr( get_comment_date( 'c' ) ); ?>"><?php echo esc_html( get_comment_date( 'j \d\e F \d\e Y' ) ); ?></time></header>
	<?php if ( '0' === (string) $comment->comment_approved ) : ?>
    <p class="ab-comment__wait">Seu comentário está aguardando aprovação.</p>
	<?php endif; ?>
    <div class="ab-comment__text"><?php comment_text(); ?></div>
	<?php
	comment_reply_link( array_merge( $args, array(
		'depth'      => $depth,
		'max_depth'  => $args['max_depth'],
		'before'     => '<div class="ab-comment__reply">',
		'after'      => '</div>',
		'reply_text' => 'Responder',
	) ) );
	?>
  </article>
	<?php
}

function aldeia_blog_url( $path ) {
	return home_url( $path );
}

function aldeia_blog_pagina_blog() {
	return get_option( 'page_for_posts' ) ? get_permalink( (int) get_option( 'page_for_posts' ) ) : home_url( '/blog/' );
}

/* Topo simples: só o logo e os links. */
function aldeia_blog_header() {
	$logo = plugins_url( 'assets/img/logo-medalhao.png', dirname( __DIR__ ) . '/aldeia-vendas.php' );
	?>
<header class="ab-top"><div class="ab-wrap ab-top__in">
  <a class="ab-brand" href="<?php echo esc_url( home_url( '/' ) ); ?>" aria-label="Aldeia Literária, página inicial"><img src="<?php echo esc_url( $logo ); ?>" alt="" width="38" height="38"></a>
  <nav class="ab-nav" aria-label="Principal"><a href="<?php echo esc_url( home_url( '/' ) ); ?>">Início</a><a href="<?php echo esc_url( aldeia_blog_url( '/novo-sobre/' ) ); ?>">Sobre</a><a href="<?php echo esc_url( aldeia_blog_url( '/como-escolher-curso-de-escrita-criativa/' ) ); ?>">Guia</a><a class="is-on" href="<?php echo esc_url( aldeia_blog_pagina_blog() ); ?>">Blog</a><a class="ab-nav__cta" href="https://tally.so/r/0QNWPy">Lista de espera</a></nav>
</div></header>
	<?php
}

/* Rodapé discreto (sem o link de imprensa). */
function aldeia_blog_footer() {
	?>
<footer class="ab-foot"><div class="ab-wrap">
  <p><a href="<?php echo esc_url( home_url( '/' ) ); ?>">Início</a> · <a href="<?php echo esc_url( aldeia_blog_url( '/novo-sobre/' ) ); ?>">Sobre</a> · <a href="<?php echo esc_url( aldeia_blog_url( '/como-escolher-curso-de-escrita-criativa/' ) ); ?>">Guia</a> · <a href="https://www.instagram.com/aldeialiteraria.oficial/" target="_blank" rel="noopener noreferrer me">Instagram</a> · <a href="https://www.tiktok.com/@aldeialiteraria" target="_blank" rel="noopener noreferrer me">TikTok</a> · <a href="<?php echo esc_url( aldeia_blog_url( '/politica-de-cancelamento-e-reembolso/' ) ); ?>">Cancelamento e reembolso</a></p>
  <p class="ab-foot__small">© Aldeia Literária · CAMILA VELOSO. CO LTDA · CNPJ 47.277.682/0001-48</p>
</div></footer>
	<?php
}

/* Tempo de leitura (200 palavras por minuto). */
function aldeia_blog_tempo_leitura( $post_id = 0 ) {
	$txt   = wp_strip_all_tags( get_post_field( 'post_content', $post_id ?: get_the_ID() ) );
	$words = str_word_count( $txt, 0, 'ÀÁÂÃÇÉÊÍÓÔÕÚàáâãçéêíóôõú' );
	return max( 1, (int) ceil( $words / 200 ) );
}

/* Um artigo na lista: título, trecho, data e miniatura (se houver). Dentro do loop. */
function aldeia_blog_cartao() {
	?>
<article class="ab-item">
  <div class="ab-item__txt">
    <h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
    <p class="ab-item__ex"><?php echo esc_html( wp_trim_words( get_the_excerpt(), 34 ) ); ?></p>
    <p class="ab-meta"><time datetime="<?php echo esc_attr( get_the_date( 'c' ) ); ?>"><?php echo esc_html( get_the_date( 'j \d\e F \d\e Y' ) ); ?></time> · <?php echo (int) aldeia_blog_tempo_leitura(); ?> min de leitura</p>
  </div>
	<?php if ( has_post_thumbnail() ) : ?>
  <a class="ab-item__img" href="<?php the_permalink(); ?>" tabindex="-1" aria-hidden="true"><?php the_post_thumbnail( 'thumbnail', array( 'loading' => 'lazy', 'alt' => '' ) ); ?></a>
	<?php endif; ?>
</article>
	<?php
}

/* Convite para a lista de espera (caixa simples). */
function aldeia_blog_chamada() {
	?>
<aside class="ab-invite">
  <h2>Quer escrever o seu livro?</h2>
  <p>A Aldeia Literária é um curso on-line de escrita criativa para iniciantes. As matrículas abrem em janeiro de 2027. Por enquanto, temos apenas a lista de espera.</p>
  <a class="ab-btn" href="https://tally.so/r/0QNWPy">Entrar na lista de espera</a>
</aside>
	<?php
}
