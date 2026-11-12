<?php
/** Comentários dos artigos do blog. */
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
if ( post_password_required() ) {
	return;
}
?>
<section class="av-section av-section--soft" id="comentarios"><div class="av-wrap"><div class="av-comments">
  <h2 class="av-h2">Comentários<?php if ( get_comments_number() ) : ?> (<?php echo (int) get_comments_number(); ?>)<?php endif; ?></h2>
<?php if ( have_comments() ) : ?>
  <ol class="av-comment-list">
	<?php wp_list_comments( array( 'style' => 'ol', 'short_ping' => true, 'callback' => 'aldeia_blog_comentario' ) ); ?>
  </ol>
	<?php the_comments_pagination( array( 'prev_text' => '←', 'next_text' => '→' ) ); ?>
<?php else : ?>
  <p class="av-lead">Ainda não há comentários. Seja a primeira pessoa a comentar.</p>
<?php endif; ?>

<?php if ( comments_open() ) : ?>
	<?php
	comment_form( array(
		'title_reply_before'   => '<h3 id="reply-title" class="comment-reply-title">',
		'title_reply_after'    => '</h3>',
		'title_reply'          => 'Deixe um comentário',
		'title_reply_to'       => 'Responder a %s',
		'cancel_reply_link'    => 'Cancelar resposta',
		'label_submit'         => 'Publicar comentário',
		'class_submit'         => 'av-btn',
		'submit_button'        => '<button name="%1$s" type="submit" id="%2$s" class="%3$s">%4$s</button>',
		'comment_notes_before' => '<p class="comment-notes">Seu e-mail não será publicado. Os campos marcados com * são obrigatórios.</p>',
		'comment_notes_after'  => '<p class="comment-notes">Ao comentar, o seu nome e o seu comentário ficam visíveis para todos. Os comentários passam por aprovação antes de aparecer.</p>',
		'comment_field'        => '<p class="comment-form-comment"><label for="comment">Comentário *</label><textarea id="comment" name="comment" cols="45" rows="6" maxlength="3000" required></textarea></p>',
	) );
	?>
<?php else : ?>
  <p class="av-lead">Os comentários deste artigo estão fechados.</p>
<?php endif; ?>
</div></div></section>
