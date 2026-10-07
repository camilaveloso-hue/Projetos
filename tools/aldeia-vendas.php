<?php
/**
 * Plugin Name: Aldeia Literária — Página de vendas
 * Description: Estilo (CSS), comportamentos (JS), fontes e imagens da página de vendas da turma 2027. Funciona junto com o modelo de página importado no Elementor.
 * Version: 1.0.10
 * Author: Aldeia Literária
 * Requires PHP: 7.2
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'ALDEIA_VENDAS_VERSION', '1.0.10' );

/**
 * Carrega o CSS/JS só nas páginas que usam a página de vendas
 * (as que têm o container principal com a classe "av-page").
 */
function aldeia_vendas_precisa_carregar() {
	// Dentro do editor do Elementor (iframe de pré-visualização), carrega sempre:
	// a página pode ainda não ter sido salva com o conteúdo.
	if ( isset( $_GET['elementor-preview'] ) ) { // phpcs:ignore WordPress.Security.NonceVerification
		return true;
	}
	if ( ! is_singular() ) {
		return false;
	}
	$id   = get_queried_object_id();
	$data = $id ? get_post_meta( $id, '_elementor_data', true ) : '';
	if ( is_array( $data ) ) {
		$data = wp_json_encode( $data );
	}
	return is_string( $data ) && false !== strpos( $data, 'av-page' );
}

add_action( 'wp_enqueue_scripts', function () {
	if ( ! aldeia_vendas_precisa_carregar() ) {
		return;
	}
	wp_enqueue_style(
		'aldeia-vendas',
		plugins_url( 'assets/css/aldeia-vendas.css', __FILE__ ),
		array( 'elementor-frontend' ),
		ALDEIA_VENDAS_VERSION
	);
	wp_enqueue_script(
		'aldeia-vendas',
		plugins_url( 'assets/js/aldeia-vendas.js', __FILE__ ),
		array(),
		ALDEIA_VENDAS_VERSION,
		true
	);
}, 20 );

/* Faz o navegador baixar as fontes principais cedo (ajuda no tempo de carregamento). */
add_action( 'wp_head', function () {
	if ( ! aldeia_vendas_precisa_carregar() ) {
		return;
	}
	foreach ( array( 'Cinzel-700-normal.woff2', 'EBGaramond-400-normal.woff2', 'Montserrat-600-normal.woff2' ) as $f ) {
		printf(
			'<link rel="preload" href="%s" as="font" type="font/woff2" crossorigin>' . "\n",
			esc_url( plugins_url( 'assets/fonts/' . $f, __FILE__ ) )
		);
	}
}, 1 );
