<?php
/**
 * Blog da Aldeia Literária: lista de artigos, categorias e artigo individual, na identidade visual do site.
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

/* 9 artigos por página (3 colunas x 3 linhas). */
add_action( 'pre_get_posts', function ( $q ) {
	if ( is_admin() || ! $q->is_main_query() || ! apply_filters( 'aldeia_blog_ativo', true ) ) {
		return;
	}
	if ( ( $q->is_home() && ! $q->is_front_page() ) || $q->is_category() || $q->is_tag() ) {
		$q->set( 'posts_per_page', 9 );
	}
} );

function aldeia_blog_url( $path ) {
	return home_url( $path );
}

/* Cabeçalho igual ao das outras páginas do site. */
function aldeia_blog_header() {
	$home  = esc_url( home_url( '/' ) );
	$blog  = get_option( 'page_for_posts' ) ? esc_url( get_permalink( (int) get_option( 'page_for_posts' ) ) ) : esc_url( home_url( '/blog/' ) );
	?>
<header class="av-header"><div class="av-wrap">
  <a class="av-logo" href="<?php echo $home; ?>"><span>Aldeia Literária</span></a>
  <nav class="av-nav" aria-label="Principal"><a class="av-nav__keep" href="<?php echo $home; ?>">Início</a><a href="<?php echo esc_url( aldeia_blog_url( '/novo-sobre/' ) ); ?>">Sobre</a><a href="<?php echo esc_url( aldeia_blog_url( '/como-escolher-curso-de-escrita-criativa/' ) ); ?>">Guia</a><a href="<?php echo $blog; ?>">Blog</a></nav>
  <a class="av-btn" href="https://tally.so/r/0QNWPy">Entrar na lista de espera</a>
</div></header>
	<?php
}

/* Rodapé igual ao da Home (redes sociais, "na mídia", razão social e CNPJ). */
function aldeia_blog_footer() {
	?>
<footer class="av-footer">
  <div class="av-footer__social" aria-label="Redes sociais da Aldeia Literária">
    <a class="av-footer__ico" href="https://www.instagram.com/aldeialiteraria.oficial/" target="_blank" rel="noopener noreferrer me" aria-label="Instagram da Aldeia Literária"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1" fill="currentColor" stroke="none"/></svg></a>
    <a class="av-footer__ico" href="https://www.tiktok.com/@aldeialiteraria" target="_blank" rel="noopener noreferrer me" aria-label="TikTok da Aldeia Literária"><svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor" aria-hidden="true"><path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg></a>
  </div>
  <p class="av-footer__media"><a class="av-footer__mediabtn" href="<?php echo esc_url( aldeia_blog_url( '/imprensa/' ) ); ?>">Aldeia Literária na mídia</a></p>
  <a href="<?php echo esc_url( home_url( '/' ) ); ?>">Home</a> · <a href="<?php echo esc_url( aldeia_blog_url( '/novo-sobre/' ) ); ?>">Sobre</a><br>© Aldeia Literária · Curso de escrita para iniciantes · Todos os direitos reservados · <a href="<?php echo esc_url( aldeia_blog_url( '/politica-de-cancelamento-e-reembolso/' ) ); ?>">Cancelamento e reembolso</a><br>CAMILA VELOSO. CO LTDA · CNPJ 47.277.682/0001-48
</footer>
	<?php
}

/* Tempo de leitura (200 palavras por minuto). */
function aldeia_blog_tempo_leitura( $post_id = 0 ) {
	$txt   = wp_strip_all_tags( get_post_field( 'post_content', $post_id ?: get_the_ID() ) );
	$words = str_word_count( $txt, 0, 'ÀÁÂÃÇÉÊÍÓÔÕÚàáâãçéêíóôõú' );
	return max( 1, (int) ceil( $words / 200 ) );
}

/* Cartão de um artigo, dentro do loop. */
function aldeia_blog_cartao() {
	$cats = get_the_category();
	$cat  = $cats ? $cats[0] : null;
	?>
<article class="av-post-card av-reveal">
  <a class="av-post-card__img" href="<?php the_permalink(); ?>" tabindex="-1" aria-hidden="true">
	<?php if ( has_post_thumbnail() ) : ?>
		<?php the_post_thumbnail( 'medium_large', array( 'loading' => 'lazy', 'alt' => '' ) ); ?>
	<?php else : ?>
		<span class="av-post-card__ph"></span>
	<?php endif; ?>
  </a>
  <div class="av-post-card__body">
	<?php if ( $cat ) : ?>
	<a class="av-tag" href="<?php echo esc_url( get_category_link( $cat->term_id ) ); ?>"><?php echo esc_html( $cat->name ); ?></a>
	<?php endif; ?>
	<h2 class="av-post-card__title"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
	<p class="av-post-card__meta"><time datetime="<?php echo esc_attr( get_the_date( 'c' ) ); ?>"><?php echo esc_html( get_the_date( 'j \d\e F \d\e Y' ) ); ?></time> · <?php echo (int) aldeia_blog_tempo_leitura(); ?> min de leitura</p>
	<p class="av-post-card__excerpt"><?php echo esc_html( wp_trim_words( get_the_excerpt(), 28 ) ); ?></p>
	<a class="av-tmore" href="<?php the_permalink(); ?>">Ler artigo</a>
  </div>
</article>
	<?php
}

/* Chamada final para a lista de espera. */
function aldeia_blog_chamada() {
	?>
<section class="av-final av-mark av-mark--left"><div class="av-meander av-meander--top"></div><div class="av-wrap">
  <h2 class="av-h2">Quer escrever o seu livro?</h2>
  <p>A Aldeia Literária é um curso on-line de escrita criativa para iniciantes. As matrículas abrem em janeiro de 2027. Por enquanto, temos apenas a lista de espera.</p>
  <p style="margin:32px auto 18px"><a class="av-btn" href="https://tally.so/r/0QNWPy">Entrar na lista de espera</a></p>
</div></section>
	<?php
}
