<?php
/** Artigo individual do blog. */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
the_post();
$cats  = get_the_category();
$cat   = $cats ? $cats[0] : null;
$blog  = get_option( 'page_for_posts' ) ? get_permalink( (int) get_option( 'page_for_posts' ) ) : home_url( '/blog/' );
$bio   = get_the_author_meta( 'description' );
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
<article <?php post_class( 'av-post' ); ?>>
<section class="av-hero av-hero--prof"><div class="av-wrap av-hero__grid" style="grid-template-columns:1fr">
  <div class="av-reveal">
    <p class="av-breadcrumb"><a href="<?php echo esc_url( home_url( '/' ) ); ?>">Início</a> · <a href="<?php echo esc_url( $blog ); ?>">Blog</a><?php if ( $cat ) : ?> · <a href="<?php echo esc_url( get_category_link( $cat->term_id ) ); ?>"><?php echo esc_html( $cat->name ); ?></a><?php endif; ?></p>
    <h1 class="av-h1"><?php the_title(); ?></h1>
    <p class="av-post__meta">Por <?php echo esc_html( get_the_author() ); ?> · <time datetime="<?php echo esc_attr( get_the_date( 'c' ) ); ?>"><?php echo esc_html( get_the_date( 'j \d\e F \d\e Y' ) ); ?></time> · <?php echo (int) aldeia_blog_tempo_leitura(); ?> min de leitura</p>
  </div>
</div></section>

<section class="av-section av-section--tight"><div class="av-wrap">
	<?php if ( has_post_thumbnail() ) : ?>
  <figure class="av-post__cover"><?php the_post_thumbnail( 'large' ); ?></figure>
	<?php endif; ?>
  <div class="av-prose av-post__content"><?php the_content(); ?></div>
  <p class="av-updated">Atualizado em <?php echo esc_html( get_the_modified_date( 'j \d\e F \d\e Y' ) ); ?></p>
  <aside class="av-author">
    <strong><?php echo esc_html( get_the_author() ); ?></strong>
	<?php if ( $bio ) : ?>
    <p><?php echo esc_html( $bio ); ?></p>
	<?php endif; ?>
  </aside>
</div></section>

	<?php
	$rel = new WP_Query( array(
		'post_type'           => 'post',
		'posts_per_page'      => 3,
		'post__not_in'        => array( get_the_ID() ),
		'category__in'        => $cats ? wp_list_pluck( $cats, 'term_id' ) : array(),
		'ignore_sticky_posts' => true,
	) );
	if ( $rel->have_posts() ) :
		?>
<section class="av-section av-section--soft"><div class="av-wrap">
  <h2 class="av-h2 av-reveal">Continue lendo</h2>
  <div class="av-posts">
		<?php
		while ( $rel->have_posts() ) {
			$rel->the_post();
			aldeia_blog_cartao();
		}
		wp_reset_postdata();
		?>
  </div>
</div></section>
	<?php endif; ?>
</article>
</main>
<?php aldeia_blog_chamada(); ?>
<?php aldeia_blog_footer(); ?>
<?php wp_footer(); ?>
</body>
</html>
