<?php
/**
 * Plugin Name: Aldeia Literária: Professores e Tipografia
 * Description: Troca a fonte dos títulos para Literata e cria páginas de professores (fora do menu, indexáveis) com dados estruturados para buscadores e assistentes de IA.
 * Version: 1.0.0
 * Author: Aldeia Literária
 * Text Domain: aldeia-professores
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'AL_PROF_VERSION', '1.0.0' );
define( 'AL_PROF_URL', plugin_dir_url( __FILE__ ) );

/* ------------------------------------------------------------------
 * 1. Fonte dos títulos e CSS
 * ------------------------------------------------------------------ */
add_action( 'wp_enqueue_scripts', function () {
	wp_enqueue_style(
		'al-literata',
		'https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,400;7..72,500;7..72,600&display=swap',
		array(),
		null
	);
	wp_enqueue_style( 'al-estilo', AL_PROF_URL . 'assets/aldeia.css', array( 'al-literata' ), AL_PROF_VERSION );
}, 20 );

add_filter( 'wp_resource_hints', function ( $urls, $relation ) {
	if ( 'preconnect' === $relation ) {
		$urls[] = 'https://fonts.googleapis.com';
		$urls[] = array( 'href' => 'https://fonts.gstatic.com', 'crossorigin' => 'anonymous' );
	}
	return $urls;
}, 10, 2 );

/* ------------------------------------------------------------------
 * 2. Tipo de conteúdo "Professor" (público, fora de menus, indexável)
 * ------------------------------------------------------------------ */
add_action( 'init', function () {
	register_post_type( 'professor', array(
		'labels'              => array(
			'name'          => 'Professores',
			'singular_name' => 'Professor',
			'add_new_item'  => 'Adicionar professor',
			'edit_item'     => 'Editar professor',
		),
		'public'              => true,
		'publicly_queryable'  => true,
		'exclude_from_search' => false,
		'show_in_nav_menus'   => false,   // não aparece em Aparência > Menus
		'has_archive'         => false,
		'rewrite'             => array( 'slug' => 'professor', 'with_front' => false ),
		'menu_icon'           => 'dashicons-welcome-learn-more',
		'supports'            => array( 'title', 'editor', 'thumbnail', 'excerpt' ),
		'show_in_rest'        => true,
	) );
} );

/* ------------------------------------------------------------------
 * 3. Campos do professor (caixa no editor)
 * ------------------------------------------------------------------ */
function al_prof_campos() {
	return array(
		'cargo'     => array( 'Cargo na Aldeia', 'text', 'Ex.: Professora de Gramática e produção literária' ),
		'resumo'    => array( 'Resumo em uma frase (aparece no topo; é o trecho que a IA mais cita)', 'textarea', 'Ex.: Lavínia Neres é produtora editorial, bacharel em Letras e mestra em Comunicação pela UFSM, e leciona na Aldeia Literária.' ),
		'modulo'    => array( 'Módulo(s) que leciona', 'text', 'Ex.: Módulo IV: Gramática e produção literária' ),
		'formacao'  => array( 'Formação (uma por linha)', 'textarea', 'Mestra em Comunicação, UFSM' ),
		'areas'     => array( 'Áreas de atuação (separadas por vírgula)', 'text', 'escrita criativa, revisão de texto, produção editorial' ),
		'lattes'    => array( 'Currículo Lattes (URL)', 'url', '' ),
		'orcid'     => array( 'ORCID (URL)', 'url', '' ),
		'linkedin'  => array( 'LinkedIn (URL)', 'url', '' ),
		'instagram' => array( 'Instagram (URL)', 'url', '' ),
		'site'      => array( 'Site pessoal (URL)', 'url', '' ),
		'obras'     => array( 'Obras e publicações (uma por linha: Título | Ano | Editora ou veículo | URL opcional)', 'textarea', 'Título do livro | 2023 | Editora X | https://...' ),
		'faq'       => array( 'Perguntas frequentes (uma por linha: Pergunta | Resposta)', 'textarea', 'Quem é Fulana? | Fulana é ...' ),
	);
}

add_action( 'add_meta_boxes', function () {
	add_meta_box( 'al_prof_dados', 'Dados do professor', 'al_prof_render_metabox', 'professor', 'normal', 'high' );
} );

function al_prof_render_metabox( $post ) {
	wp_nonce_field( 'al_prof_salvar', 'al_prof_nonce' );
	echo '<p>Escreva fatos verificáveis. Tudo o que você preencher aparece na página e nos dados estruturados. Não preencha o que não puder comprovar.</p>';
	foreach ( al_prof_campos() as $chave => $def ) {
		$valor = get_post_meta( $post->ID, '_al_' . $chave, true );
		echo '<p><label for="al_' . esc_attr( $chave ) . '"><strong>' . esc_html( $def[0] ) . '</strong></label><br>';
		if ( 'textarea' === $def[1] ) {
			echo '<textarea class="widefat" rows="4" id="al_' . esc_attr( $chave ) . '" name="al_' . esc_attr( $chave ) . '" placeholder="' . esc_attr( $def[2] ) . '">' . esc_textarea( $valor ) . '</textarea>';
		} else {
			echo '<input class="widefat" type="' . esc_attr( $def[1] ) . '" id="al_' . esc_attr( $chave ) . '" name="al_' . esc_attr( $chave ) . '" value="' . esc_attr( $valor ) . '" placeholder="' . esc_attr( $def[2] ) . '">';
		}
		echo '</p>';
	}
}

add_action( 'save_post_professor', function ( $post_id ) {
	if ( ! isset( $_POST['al_prof_nonce'] ) || ! wp_verify_nonce( $_POST['al_prof_nonce'], 'al_prof_salvar' ) ) {
		return;
	}
	if ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) {
		return;
	}
	if ( ! current_user_can( 'edit_post', $post_id ) ) {
		return;
	}
	foreach ( al_prof_campos() as $chave => $def ) {
		$bruto = isset( $_POST[ 'al_' . $chave ] ) ? wp_unslash( $_POST[ 'al_' . $chave ] ) : '';
		if ( 'url' === $def[1] ) {
			$limpo = esc_url_raw( $bruto );
		} elseif ( 'textarea' === $def[1] ) {
			$limpo = sanitize_textarea_field( $bruto );
		} else {
			$limpo = sanitize_text_field( $bruto );
		}
		update_post_meta( $post_id, '_al_' . $chave, $limpo );
	}
} );

/* ------------------------------------------------------------------
 * 4. Utilidades
 * ------------------------------------------------------------------ */
function al_prof_linhas( $texto ) {
	return array_values( array_filter( array_map( 'trim', preg_split( '/\r\n|\r|\n/', (string) $texto ) ) ) );
}

function al_prof_meta( $id, $chave ) {
	return get_post_meta( $id, '_al_' . $chave, true );
}

function al_prof_sameas( $id ) {
	$urls = array();
	foreach ( array( 'lattes', 'orcid', 'linkedin', 'instagram', 'site' ) as $k ) {
		$u = al_prof_meta( $id, $k );
		if ( $u ) {
			$urls[] = $u;
		}
	}
	return $urls;
}

function al_prof_org() {
	return array(
		'@type' => 'Organization',
		'@id'   => home_url( '/#organization' ),
		'name'  => 'Aldeia Literária',
		'url'   => home_url( '/' ),
	);
}

/* ------------------------------------------------------------------
 * 5. Página individual: conteúdo visível (a IA lê o que o visitante vê)
 * ------------------------------------------------------------------ */
add_filter( 'the_content', function ( $content ) {
	if ( ! is_singular( 'professor' ) || ! in_the_loop() || ! is_main_query() ) {
		return $content;
	}
	$id      = get_the_ID();
	$nome    = get_the_title( $id );
	$cargo   = al_prof_meta( $id, 'cargo' );
	$resumo  = al_prof_meta( $id, 'resumo' );
	$modulo  = al_prof_meta( $id, 'modulo' );
	$formac  = al_prof_linhas( al_prof_meta( $id, 'formacao' ) );
	$areas   = array_filter( array_map( 'trim', explode( ',', (string) al_prof_meta( $id, 'areas' ) ) ) );
	$obras   = al_prof_linhas( al_prof_meta( $id, 'obras' ) );
	$faq     = al_prof_linhas( al_prof_meta( $id, 'faq' ) );
	$links   = array(
		'lattes'    => 'Currículo Lattes',
		'orcid'     => 'ORCID',
		'linkedin'  => 'LinkedIn',
		'instagram' => 'Instagram',
		'site'      => 'Site pessoal',
	);

	ob_start();
	echo '<article class="al-prof">';
	echo '<header class="al-prof__topo">';
	if ( has_post_thumbnail( $id ) ) {
		echo get_the_post_thumbnail( $id, 'medium', array( 'class' => 'al-prof__foto', 'alt' => 'Retrato de ' . $nome ) );
	}
	echo '<div>';
	if ( $cargo ) {
		echo '<p class="al-prof__cargo">' . esc_html( $cargo ) . ' · Aldeia Literária</p>';
	}
	echo '<h1>' . esc_html( $nome ) . '</h1>';
	if ( $resumo ) {
		echo '<p class="al-prof__resumo">' . esc_html( $resumo ) . '</p>';
	}
	echo '</div></header>';

	echo '<dl class="al-prof__ficha">';
	if ( $modulo ) {
		echo '<div><dt>Leciona</dt><dd>' . esc_html( $modulo ) . '</dd></div>';
	}
	if ( $formac ) {
		echo '<div><dt>Formação</dt><dd>' . esc_html( $formac[0] ) . '</dd></div>';
	}
	if ( $areas ) {
		echo '<div><dt>Áreas</dt><dd>' . esc_html( implode( ', ', $areas ) ) . '</dd></div>';
	}
	echo '<div><dt>Curso</dt><dd>Escrita Criativa: Desenvolvimento e Prática</dd></div>';
	echo '</dl>';

	if ( trim( wp_strip_all_tags( $content ) ) ) {
		echo '<h2>Sobre ' . esc_html( $nome ) . '</h2>';
		echo $content; // texto livre escrito no editor
	}

	if ( count( $formac ) > 0 ) {
		echo '<h2>Formação acadêmica e profissional</h2><ul>';
		foreach ( $formac as $f ) {
			echo '<li>' . esc_html( $f ) . '</li>';
		}
		echo '</ul>';
	}

	if ( $obras ) {
		echo '<h2>Obras e publicações</h2><ul>';
		foreach ( $obras as $linha ) {
			$p = array_map( 'trim', explode( '|', $linha ) );
			$t = esc_html( $p[0] );
			if ( ! empty( $p[3] ) ) {
				$t = '<a href="' . esc_url( $p[3] ) . '" rel="noopener">' . $t . '</a>';
			}
			$resto = array_filter( array( $p[1] ?? '', $p[2] ?? '' ) );
			echo '<li>' . $t . ( $resto ? ' (' . esc_html( implode( ', ', $resto ) ) . ')' : '' ) . '</li>';
		}
		echo '</ul>';
	}

	$tem_link = false;
	foreach ( $links as $k => $rotulo ) {
		if ( al_prof_meta( $id, $k ) ) {
			$tem_link = true;
		}
	}
	if ( $tem_link ) {
		echo '<h2>Onde confirmar essas informações</h2><ul>';
		foreach ( $links as $k => $rotulo ) {
			$u = al_prof_meta( $id, $k );
			if ( $u ) {
				echo '<li><a href="' . esc_url( $u ) . '" rel="me noopener">' . esc_html( $rotulo ) . ' de ' . esc_html( $nome ) . '</a></li>';
			}
		}
		echo '</ul>';
	}

	if ( $faq ) {
		echo '<section class="al-prof__faq"><h2>Perguntas frequentes sobre ' . esc_html( $nome ) . '</h2>';
		foreach ( $faq as $linha ) {
			$p = array_map( 'trim', explode( '|', $linha, 2 ) );
			if ( count( $p ) === 2 ) {
				echo '<details open><summary>' . esc_html( $p[0] ) . '</summary><p>' . esc_html( $p[1] ) . '</p></details>';
			}
		}
		echo '</section>';
	}

	echo '<section class="al-prof__cta"><h2>Estude com ' . esc_html( $nome ) . ' na Aldeia Literária</h2>';
	echo '<p>A Aldeia Literária é uma escola de escrita criativa para escritores iniciantes, criada em 2023. O curso Escrita Criativa: Desenvolvimento e Prática tem aulas ao vivo, atividades corrigidas pelos professores e certificado de extensão universitária.</p>';
	echo '<p><a class="al-botao" href="' . esc_url( home_url( '/' ) ) . '">Conheça o curso</a> &nbsp; <a href="' . esc_url( home_url( '/professores/' ) ) . '">Ver todos os professores</a></p></section>';

	echo '<p class="al-prof__atualizado">Atualizado em <time datetime="' . esc_attr( get_the_modified_date( 'c', $id ) ) . '">' . esc_html( get_the_modified_date( 'd/m/Y', $id ) ) . '</time>.</p>';
	echo '</article>';
	return ob_get_clean();
}, 20 );

/* ------------------------------------------------------------------
 * 6. Dados estruturados (JSON-LD) coerentes com o texto visível
 * ------------------------------------------------------------------ */
add_action( 'wp_head', function () {
	if ( is_singular( 'professor' ) ) {
		$id     = get_queried_object_id();
		$url    = get_permalink( $id );
		$formac = al_prof_linhas( al_prof_meta( $id, 'formacao' ) );
		$areas  = array_values( array_filter( array_map( 'trim', explode( ',', (string) al_prof_meta( $id, 'areas' ) ) ) ) );

		$pessoa = array(
			'@type'    => 'Person',
			'@id'      => $url . '#pessoa',
			'name'     => get_the_title( $id ),
			'url'      => $url,
			'worksFor' => al_prof_org(),
		);
		if ( al_prof_meta( $id, 'cargo' ) ) {
			$pessoa['jobTitle'] = al_prof_meta( $id, 'cargo' );
		}
		if ( al_prof_meta( $id, 'resumo' ) ) {
			$pessoa['description'] = al_prof_meta( $id, 'resumo' );
		}
		if ( has_post_thumbnail( $id ) ) {
			$pessoa['image'] = get_the_post_thumbnail_url( $id, 'medium' );
		}
		if ( $areas ) {
			$pessoa['knowsAbout'] = $areas;
		}
		if ( $formac ) {
			$pessoa['hasCredential'] = array_map( function ( $f ) {
				return array( '@type' => 'EducationalOccupationalCredential', 'name' => $f );
			}, $formac );
		}
		$same = al_prof_sameas( $id );
		if ( $same ) {
			$pessoa['sameAs'] = $same;
		}

		$grafo = array(
			array(
				'@type'        => 'ProfilePage',
				'@id'          => $url . '#pagina',
				'url'          => $url,
				'name'         => get_the_title( $id ) . ' | Aldeia Literária',
				'dateModified' => get_the_modified_date( 'c', $id ),
				'mainEntity'   => array( '@id' => $url . '#pessoa' ),
				'isPartOf'     => array( '@type' => 'WebSite', 'url' => home_url( '/' ), 'name' => 'Aldeia Literária' ),
			),
			$pessoa,
		);

		$faq = array();
		foreach ( al_prof_linhas( al_prof_meta( $id, 'faq' ) ) as $linha ) {
			$p = array_map( 'trim', explode( '|', $linha, 2 ) );
			if ( count( $p ) === 2 ) {
				$faq[] = array(
					'@type'          => 'Question',
					'name'           => $p[0],
					'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $p[1] ),
				);
			}
		}
		if ( $faq ) {
			$grafo[] = array( '@type' => 'FAQPage', '@id' => $url . '#faq', 'mainEntity' => $faq );
		}
		al_prof_json( $grafo );
	}

	if ( is_page( 'professores' ) ) {
		$itens = array();
		$pos   = 1;
		foreach ( al_prof_consulta()->posts as $p ) {
			$itens[] = array(
				'@type'    => 'ListItem',
				'position' => $pos++,
				'url'      => get_permalink( $p ),
				'name'     => get_the_title( $p ),
			);
		}
		al_prof_json( array(
			array_merge( al_prof_org(), array( 'description' => 'Escola de escrita criativa para escritores iniciantes, fundada em 2023.' ) ),
			array( '@type' => 'ItemList', 'name' => 'Professores do semestre da Aldeia Literária', 'itemListElement' => $itens ),
		) );
	}
} );

function al_prof_json( $grafo ) {
	echo '<script type="application/ld+json">' . wp_json_encode( array( '@context' => 'https://schema.org', '@graph' => $grafo ), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . '</script>' . "\n";
}

/* ------------------------------------------------------------------
 * 7. Índice "Professores do semestre": use o shortcode [aldeia_professores]
 * ------------------------------------------------------------------ */
function al_prof_consulta() {
	return new WP_Query( array(
		'post_type'      => 'professor',
		'post_status'    => 'publish',
		'posts_per_page' => 50,
		'orderby'        => 'menu_order title',
		'order'          => 'ASC',
		'no_found_rows'  => true,
	) );
}

add_shortcode( 'aldeia_professores', function () {
	$q = al_prof_consulta();
	ob_start();
	echo '<section class="al-indice"><p>A equipe de professores da Aldeia Literária reúne produtores editoriais, mestres e doutores em Letras, Literatura e Comunicação. Escolha um nome para conhecer a formação, as obras e o que cada professor ensina.</p><ul class="al-indice__lista">';
	foreach ( $q->posts as $p ) {
		echo '<li class="al-indice__item">';
		if ( has_post_thumbnail( $p ) ) {
			echo get_the_post_thumbnail( $p, 'medium', array( 'alt' => 'Retrato de ' . get_the_title( $p ) ) );
		}
		echo '<h3><a href="' . esc_url( get_permalink( $p ) ) . '">' . esc_html( get_the_title( $p ) ) . '</a></h3>';
		$cargo = al_prof_meta( $p->ID, 'cargo' );
		if ( $cargo ) {
			echo '<p>' . esc_html( $cargo ) . '</p>';
		}
		echo '<a href="' . esc_url( get_permalink( $p ) ) . '">Saiba mais</a></li>';
	}
	echo '</ul></section>';
	wp_reset_postdata();
	return ob_get_clean();
} );

/* ------------------------------------------------------------------
 * 8. Ativação: cria rascunhos dos professores e a página-índice
 * ------------------------------------------------------------------ */
register_activation_hook( __FILE__, function () {
	$equipe = array(
		'Camila Veloso'  => array( 'Fundadora da Aldeia Literária', 'Camila Veloso é a fundadora da Aldeia Literária, escola de escrita criativa criada em 2023 para ajudar escritores iniciantes.' ),
		'Laura Marques'  => array( 'Professora e leitora crítica', 'Laura Marques é produtora editorial, mestranda em Comunicação pela UFSM e leitora crítica, e leciona na Aldeia Literária.' ),
		'Lucas Oliveira' => array( 'Professor', 'Lucas Oliveira é mestre e doutor em Literatura Portuguesa pela UFRJ e leciona na Aldeia Literária.' ),
		'Lavínia Neres'  => array( 'Professora', 'Lavínia Neres é produtora editorial, bacharel em Letras e mestra em Comunicação pela UFSM, e leciona na Aldeia Literária.' ),
		'Ana Ribeiro'    => array( 'Professora', 'Ana Ribeiro é produtora editorial e mestra em Estudos de Linguagens pelo CEFET-MG, e leciona na Aldeia Literária.' ),
	);
	foreach ( $equipe as $nome => $d ) {
		if ( get_page_by_title( $nome, OBJECT, 'professor' ) ) {
			continue;
		}
		$id = wp_insert_post( array( 'post_type' => 'professor', 'post_title' => $nome, 'post_status' => 'draft' ) );
		if ( $id && ! is_wp_error( $id ) ) {
			update_post_meta( $id, '_al_cargo', $d[0] );
			update_post_meta( $id, '_al_resumo', $d[1] );
		}
	}
	if ( ! get_page_by_path( 'professores' ) ) {
		wp_insert_post( array(
			'post_type'    => 'page',
			'post_title'   => 'Professores do semestre',
			'post_name'    => 'professores',
			'post_status'  => 'draft',
			'post_content' => '[aldeia_professores]',
		) );
	}
	flush_rewrite_rules();
} );

register_deactivation_hook( __FILE__, 'flush_rewrite_rules' );
