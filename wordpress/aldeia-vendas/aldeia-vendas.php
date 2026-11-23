<?php
/**
 * Plugin Name: Aldeia Literária — Página de vendas
 * Description: Estilo (CSS), comportamentos (JS), fontes e imagens das páginas da Aldeia Literária (Home, Sobre, professores e Aulão). Funciona junto com os modelos de página importados no Elementor.
 * Version: 1.4.1
 * Author: Aldeia Literária
 * Requires PHP: 7.2
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'ALDEIA_VENDAS_VERSION', '1.4.1' );

/* Blog da Aldeia (lista de artigos, categorias e artigo individual). */
if ( file_exists( plugin_dir_path( __FILE__ ) . 'includes/blog.php' ) ) {
	require_once plugin_dir_path( __FILE__ ) . 'includes/blog.php';
}

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
	// Telas do blog (lista, categoria e artigo) usam o mesmo visual.
	if ( function_exists( 'aldeia_blog_contexto' ) && '' !== aldeia_blog_contexto() ) {
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
	foreach ( array( 'LibreCaslonText-700-normal.woff2', 'EBGaramond-400-normal.woff2', 'Montserrat-600-normal.woff2' ) as $f ) {
		printf(
			'<link rel="preload" href="%s" as="font" type="font/woff2" crossorigin>' . "\n",
			esc_url( plugins_url( 'assets/fonts/' . $f, __FILE__ ) )
		);
	}
}, 1 );

/**
 * Página do AULÃO UNIVERSAL (endereço /aulao-universal/): título, descrição e tipo para buscadores e IAs.
 * Faz o Yoast usar estes textos (e não o texto solto da página) no <title>, na meta descrição e no Open Graph.
 * O tipo Open Graph passa de "article" para "website". Não mexe em nenhuma outra página.
 */
function aldeia_aulao_pagina() {
	return function_exists( 'is_page' ) && is_page( 'aulao-universal' );
}
function aldeia_aulao_titulo() {
	return 'AULÃO UNIVERSAL: aula de escrita criativa para iniciantes | Aldeia Literária';
}
function aldeia_aulao_descricao() {
	return 'Aula gravada de escrita criativa para iniciantes: aprenda como escrever um livro com três atos, premissa e checklist de 9 passos. Com Camila Veloso.';
}
foreach ( array( 'wpseo_title', 'wpseo_opengraph_title', 'wpseo_twitter_title' ) as $aldeia_hook ) {
	add_filter( $aldeia_hook, function ( $v ) {
		return aldeia_aulao_pagina() ? aldeia_aulao_titulo() : $v;
	} );
}
foreach ( array( 'wpseo_metadesc', 'wpseo_opengraph_desc', 'wpseo_twitter_description' ) as $aldeia_hook ) {
	add_filter( $aldeia_hook, function ( $v ) {
		return aldeia_aulao_pagina() ? aldeia_aulao_descricao() : $v;
	} );
}
add_filter( 'wpseo_opengraph_type', function ( $v ) {
	return aldeia_aulao_pagina() ? 'website' : $v;
} );
