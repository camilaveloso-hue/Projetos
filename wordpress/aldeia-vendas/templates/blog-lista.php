<?php
/** Página de artigos (Blog), categorias e etiquetas. */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
if ( is_category() ) {
	$titulo = single_cat_title( '', false );
	$resumo = trim( wp_strip_all_tags( category_description() ) );
} elseif ( is_tag() ) {
	$titulo = single_tag_title( '', false );
	$resumo = trim( wp_strip_all_tags( tag_description() ) );
} else {
	$titulo = 'Blog da Aldeia Literária';
	$resumo = '';
}
if ( '' === $resumo ) {
	$resumo = 'Artigos sobre escrita criativa, mercado editorial e a jornada de quem quer escrever e terminar o próprio livro.';
}
?><!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<?php wp_head(); ?>
</head>
<body <?php body_class( 'av-page' ); ?> id="top">
<?php wp_body_open(); ?>
<?php aldeia_blog_header(); ?>
<main id="topo">
<section class="av-hero av-hero--prof"><div class="av-wrap av-hero__grid" style="grid-template-columns:1fr">
  <div class="av-reveal">
    <h1 class="av-h1"><?php echo esc_html( $titulo ); ?></h1>
    <p class="av-prof__summary"><?php echo esc_html( $resumo ); ?></p>
  </div>
</div></section>

<section class="av-section"><div class="av-wrap">
<?php if ( have_posts() ) : ?>
  <div class="av-posts">
	<?php
	while ( have_posts() ) {
		the_post();
		aldeia_blog_cartao();
	}
	?>
  </div>
	<?php
	$links = paginate_links( array( 'type' => 'array', 'prev_text' => '←', 'next_text' => '→', 'mid_size' => 1 ) );
	if ( $links ) :
		?>
  <nav class="av-pagination" aria-label="Páginas de artigos"><?php echo wp_kses_post( implode( '', $links ) ); ?></nav>
	<?php endif; ?>
<?php else : ?>
  <p class="av-lead">Ainda não há artigos publicados aqui. Volte em breve.</p>
<?php endif; ?>
</div></section>
</main>
<?php aldeia_blog_chamada(); ?>
<?php aldeia_blog_footer(); ?>
<?php wp_footer(); ?>
</body>
</html>
