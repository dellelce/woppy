#!/usr/bin/python
#-*- coding: utf-8 -*-
print("	<article id="post-")
the_ID()
print("" ")
post_class("indexed")
print(">\n		<header class="entry-header">\n			<hgroup>\n				<h2 class="entry-title"><a href="")
the_permalink()
print("" title="")
print(esc_attr(sprintf(__("Permalink to %s", "twentyeleven"), the_title_attribute("echo=0"))))
print("" rel="bookmark">")
the_title()
print("</a></h2>\n				<h3 class="entry-format">")
_e("Image", "twentyeleven")
print("</h3>\n			</hgroup>\n\n			")
if comments_open()&&!post_password_required():
  print("			<div class="comments-link">\n				")
  comments_popup_link("<span class="leave-reply">"+__("Reply", "twentyeleven")+"</span>", _x("1", "comments number", "twentyeleven"), _x("%", "comments number", "twentyeleven"))
  print("			</div>\n			")
print("		</header><!-- .entry-header -->\n\n		<div class="entry-content">\n			")
the_content(__("Continue reading <span class="meta-nav">&rarr;</span>", "twentyeleven"))
print("			")
wp_link_pages({"before":"<div class="page-link"><span>"+__("Pages:", "twentyeleven")+"</span>", "after":"</div>"})
print("		</div><!-- .entry-content -->\n\n		<footer class="entry-meta">\n			<div class="entry-meta">\n				")
printf(__("<a href="%1$s" rel="bookmark"><time class="entry-date" datetime="%2$s">%3$s</time></a><span class="by-author"> <span class="sep"> by </span> <span class="author vcard"><a class="url fn n" href="%4$s" title="%5$s" rel="author">%6$s</a></span></span>", "twentyeleven"), esc_url(get_permalink()), get_the_date("c"), get_the_date(), esc_url(get_author_posts_url(get_the_author_meta("ID"))), esc_attr(sprintf(__("View all posts by %s", "twentyeleven"), get_the_author())), get_the_author())
print("			</div><!-- .entry-meta -->\n			<div class="entry-meta">\n				")
categories_list = get_the_category_list(__(", ", "twentyeleven"))
if categories_list:
  print("				<span class="cat-links">\n					")
  printf(__("<span class="%1$s">Posted in</span> %2$s", "twentyeleven"), "entry-utility-prep entry-utility-prep-cat-links", categories_list)
  print("				</span>\n				")
print("\n				")
tags_list = get_the_tag_list("", __(", ", "twentyeleven"))
if tags_list:
  print("				<span class="tag-links">\n					")
  printf(__("<span class="%1$s">Tagged</span> %2$s", "twentyeleven"), "entry-utility-prep entry-utility-prep-tag-links", tags_list)
  print("				</span>\n				")
print("\n\n				")
if comments_open():
  print("				<span class="comments-link">")
  comments_popup_link("<span class="leave-reply">"+__("Leave a reply", "twentyeleven")+"</span>", __("<b>1</b> Reply", "twentyeleven"), __("<b>%</b> Replies", "twentyeleven"))
  print("</span>\n				")
print("\n			</div><!-- .entry-meta -->\n\n			")
edit_post_link(__("Edit", "twentyeleven"), "<span class="edit-link">", "</span>")
print("		</footer><!-- .entry-meta -->\n	</article><!-- #post-")
the_ID()
print(" -->\n")
