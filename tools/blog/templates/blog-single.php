<?php
/** Artigo individual do blog. */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
the_post();
$bio = aldeia_blog_autor_bio();
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
<article <?php post_class( 'ab-art' ); ?>>
  <p class="ab-back"><a href="<?php echo esc_url( aldeia_blog_pagina_blog() ); ?>">← Blog</a></p>
  <h1><?php the_title(); ?></h1>
  <p class="ab-byline"><strong><?php echo esc_html( aldeia_blog_autor() ); ?></strong> · <time datetime="<?php echo esc_attr( get_the_date( 'c' ) ); ?>"><?php echo esc_html( get_the_date( 'j \d\e F \d\e Y' ) ); ?></time> · <?php echo (int) aldeia_blog_tempo_leitura(); ?> min de leitura</p>
	<?php if ( has_post_thumbnail() ) : ?>
  <figure class="ab-cover"><?php the_post_thumbnail( 'large' ); ?></figure>
	<?php endif; ?>
  <div class="ab-body"><?php the_content(); ?></div>
  <p class="ab-updated">Atualizado em <?php echo esc_html( get_the_modified_date( 'j \d\e F \d\e Y' ) ); ?></p>
	<?php if ( $bio ) : ?>
  <p class="ab-author"><strong><?php echo esc_html( aldeia_blog_autor() ); ?></strong>. <?php echo esc_html( $bio ); ?></p>
	<?php endif; ?>
</article>

	<?php if ( comments_open() || get_comments_number() ) { comments_template(); } ?>

	<?php
	$cats = get_the_category();
	$rel  = new WP_Query( array(
		'post_type'           => 'post',
		'posts_per_page'      => 3,
		'post__not_in'        => array( get_the_ID() ),
		'category__in'        => $cats ? wp_list_pluck( $cats, 'term_id' ) : array(),
		'ignore_sticky_posts' => true,
	) );
	if ( $rel->have_posts() ) :
		?>
  <section class="ab-more">
    <h2>Mais do blog</h2>
		<?php
		while ( $rel->have_posts() ) {
			$rel->the_post();
			?>
    <div class="ab-more__it"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a><p class="ab-meta"><?php echo esc_html( get_the_date( 'j \d\e F \d\e Y' ) ); ?> · <?php echo (int) aldeia_blog_tempo_leitura(); ?> min de leitura</p></div>
			<?php
		}
		wp_reset_postdata();
		?>
  </section>
	<?php endif; ?>

  <?php aldeia_blog_chamada(); ?>
</main>
<?php aldeia_blog_footer(); ?>
<?php wp_footer(); ?>
</body>
</html>
