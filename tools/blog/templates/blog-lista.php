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
	$resumo = 'Textos sobre escrita criativa, mercado editorial e a jornada de quem quer escrever e terminar o próprio livro.';
}
?><!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<?php wp_head(); ?>
</head>
<body <?php body_class( 'ab-page' ); ?>>
<?php wp_body_open(); ?>
<?php aldeia_blog_header(); ?>
<main id="topo" class="ab-wrap">
  <section class="ab-mast">
    <h1><?php echo esc_html( $titulo ); ?></h1>
    <p class="ab-mast__sub"><?php echo esc_html( $resumo ); ?></p>
  </section>
<?php if ( have_posts() ) : ?>
  <div class="ab-list">
	<?php
	while ( have_posts() ) {
		the_post();
		aldeia_blog_cartao();
	}
	?>
  </div>
	<?php
	$links = paginate_links( array( 'type' => 'array', 'prev_text' => '← Mais novos', 'next_text' => 'Mais antigos →', 'mid_size' => 0, 'show_all' => false ) );
	if ( $links ) :
		?>
  <nav class="ab-pager" aria-label="Páginas de artigos"><?php echo wp_kses_post( implode( '', $links ) ); ?></nav>
	<?php endif; ?>
<?php else : ?>
  <p class="ab-empty">Ainda não há textos publicados aqui. Volte em breve.</p>
<?php endif; ?>
  <?php aldeia_blog_chamada(); ?>
</main>
<?php aldeia_blog_footer(); ?>
<?php wp_footer(); ?>
</body>
</html>
