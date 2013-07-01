#!/usr/bin/python
#-*- coding: utf-8 -*-
print("\n<article id="post-")
the_ID()
print("" ")
post_class()
print(">\n	<header class="entry-header">\n		<hgroup>\n			<h2 class="entry-title"><a href="")
the_permalink()
print("" title="")
print(esc_attr(sprintf(__("Permalink to %s", "twentyeleven"), the_title_attribute("echo=0"))))
print("" rel="bookmark">")
the_title()
print("</a></h2>\n			<h3 class="entry-format">")
_e("Gallery", "twentyeleven")
print("</h3>\n		</hgroup>\n\n		<div class="entry-meta">\n			")
twentyeleven_posted_on()
print("		</div><!-- .entry-meta -->\n	</header><!-- .entry-header -->\n\n	")
if is_search():
  print("\n		<div class="entry-summary">\n			")
  the_excerpt()
  print("		</div><!-- .entry-summary -->\n		")
else:
  print("		<div class="entry-content">\n			")
  if post_password_required():
    print("				")
    the_content(__("Continue reading <span class="meta-nav">&rarr;</span>", "twentyeleven"))
    print("\n			")
  else:
    print("				")
    images = get_children({"post_parent":post.ID, "post_type":"attachment", "post_mime_type":"image", "orderby":"menu_order", "order":"ASC", "numberposts":999})
    if images:
      total_images = count(images)
      image = array_shift(images)
      image_img_tag = wp_get_attachment_image(image.ID, "thumbnail")
      print("\n				<figure class="gallery-thumb">\n					<a href="")
      the_permalink()
      print("">")
      print(image_img_tag)
      print("</a>\n				</figure><!-- .gallery-thumb -->\n\n				<p><em>")
      printf(_n("This gallery contains <a %1$s>%2$s photo</a>.", "This gallery contains <a %1$s>%2$s photos</a>.", total_images, "twentyeleven"), "href=""+esc_url(get_permalink())+"" title=""+esc_attr(sprintf(__("Permalink to %s", "twentyeleven"), the_title_attribute("echo=0")))+"" rel="bookmark"", number_format_i18n(total_images))
      print("</em></p>\n			")
    print("			")
    the_excerpt()
    print("		")
  print("		")
  wp_link_pages({"before":"<div class="page-link"><span>"+__("Pages:", "twentyeleven")+"</span>", "after":"</div>"})
  print("	</div><!-- .entry-content -->\n	")
print("\n	<footer class="entry-meta">\n		")
show_sep = False
print("		")
categories_list = get_the_category_list(__(", ", "twentyeleven"))
if categories_list:
  print("		<span class="cat-links">\n			")
  printf(__("<span class="%1$s">Posted in</span> %2$s", "twentyeleven"), "entry-utility-prep entry-utility-prep-cat-links", categories_list)
  show_sep = True
  print("		</span>\n		")
print("\n		")
tags_list = get_the_tag_list("", __(", ", "twentyeleven"))
if tags_list:
  if show_sep:
    print("		<span class="sep"> | </span>\n			")
  print("\n		<span class="tag-links">\n			")
  printf(__("<span class="%1$s">Tagged</span> %2$s", "twentyeleven"), "entry-utility-prep entry-utility-prep-tag-links", tags_list)
  show_sep = True
  print("		</span>\n		")
print("\n\n		")
if comments_open():
  print("		")
  if show_sep:
    print("		<span class="sep"> | </span>\n		")
  print("\n		<span class="comments-link">")
  comments_popup_link("<span class="leave-reply">"+__("Leave a reply", "twentyeleven")+"</span>", __("<b>1</b> Reply", "twentyeleven"), __("<b>%</b> Replies", "twentyeleven"))
  print("</span>\n		")
print("\n\n		")
edit_post_link(__("Edit", "twentyeleven"), "<span class="edit-link">", "</span>")
print("	</footer><!-- .entry-meta -->\n</article><!-- #post-")
the_ID()
print(" -->\n")
