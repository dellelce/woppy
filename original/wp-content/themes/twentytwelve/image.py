#!/usr/bin/python
#-*- coding: utf-8 -*-
get_header()
print("\n	<div id="primary" class="site-content">\n		<div id="content" role="main">\n\n		")
while attachment.ID==post.ID:
  the_post()
  print("\n				<article id="post-")
  the_ID()
  print("" ")
  post_class("image-attachment")
  print(">\n					<header class="entry-header">\n						<h1 class="entry-title">")
  the_title()
  print("</h1>\n\n						<footer class="entry-meta">\n							")
  metadata = wp_get_attachment_metadata()
  printf(__("<span class="meta-prep meta-prep-entry-date">Published </span> <span class="entry-date"><time class="entry-date" datetime="%1$s">%2$s</time></span> at <a href="%3$s" title="Link to full-size image">%4$s &times; %5$s</a> in <a href="%6$s" title="Return to %7$s" rel="gallery">%8$s</a>.", "twentytwelve"), esc_attr(get_the_date("c")), esc_html(get_the_date()), esc_url(wp_get_attachment_url()), metadata["width"], metadata["height"], esc_url(get_permalink(post.post_parent)), esc_attr(strip_tags(get_the_title(post.post_parent))), get_the_title(post.post_parent))
  print("							")
  edit_post_link(__("Edit", "twentytwelve"), "<span class="edit-link">", "</span>")
  print("						</footer><!-- .entry-meta -->\n\n						<nav id="image-navigation" class="navigation" role="navigation">\n							<span class="previous-image">")
  previous_image_link(False, __("&larr; Previous", "twentytwelve"))
  print("</span>\n							<span class="next-image">")
  next_image_link(False, __("Next &rarr;", "twentytwelve"))
  print("</span>\n						</nav><!-- #image-navigation -->\n					</header><!-- .entry-header -->\n\n					<div class="entry-content">\n\n						<div class="entry-attachment">\n							<div class="attachment">\n")
  attachments = array_values(get_children({"post_parent":post.post_parent, "post_status":"inherit", "post_type":"attachment", "post_mime_type":"image", "order":"ASC", "orderby":"menu_order ID"}))
  for attachment in attachments:
    if attachment.ID==post.ID:
  k+=1
  if count(attachments)>1:
    if isset(attachments[k]):
      next_attachment_url = get_attachment_link(attachments[k].ID)
    else:
      next_attachment_url = get_attachment_link(attachments[0].ID)
  else:
    next_attachment_url = wp_get_attachment_url()
  print("								<a href="")
  print(esc_url(next_attachment_url))
  print("" title="")
  the_title_attribute()
  print("" rel="attachment">")
  attachment_size = apply_filters("twentytwelve_attachment_size", [960, 960])
  print(wp_get_attachment_image(post.ID, attachment_size))
  print("</a>\n\n								")
  if !empty(post.post_excerpt):
    print("								<div class="entry-caption">\n									")
    the_excerpt()
    print("								</div>\n								")
  print("							</div><!-- .attachment -->\n\n						</div><!-- .entry-attachment -->\n\n						<div class="entry-description">\n							")
  the_content()
  print("							")
  wp_link_pages({"before":"<div class="page-links">"+__("Pages:", "twentytwelve"), "after":"</div>"})
  print("						</div><!-- .entry-description -->\n\n					</div><!-- .entry-content -->\n\n				</article><!-- #post -->\n\n				")
  comments_template()
  print("\n			")
print("\n\n		</div><!-- #content -->\n	</div><!-- #primary -->\n\n")
get_footer()
