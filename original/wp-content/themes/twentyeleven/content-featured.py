#!/usr/bin/python
#-*- coding: utf-8 -*-
feature_classprint("<article id="post-")
the_ID()
print("" ")
post_class(feature_class)
print(">\n	<header class="entry-header">\n		<h2 class="entry-title"><a href="")
the_permalink()
print("" title="")
print(esc_attr(sprintf(__("Permalink to %s", "twentyeleven"), the_title_attribute("echo=0"))))
print("" rel="bookmark">")
the_title()
print("</a></h2>\n\n		<div class="entry-meta">\n			")
twentyeleven_posted_on()
print("		</div><!-- .entry-meta -->\n	</header><!-- .entry-header -->\n\n	<div class="entry-summary">\n		")
the_excerpt()
print("		")
wp_link_pages({"before":"<div class="page-link"><span>"+__("Pages:", "twentyeleven")+"</span>", "after":"</div>"})
print("	</div><!-- .entry-content -->\n\n	<footer class="entry-meta">\n		")
tag_list = get_the_tag_list("", __(", ", "twentyeleven"))
if ""!=tag_list:
  utility_text = __("This entry was posted in %1$s and tagged %2$s. Bookmark the <a href="%3$s" title="Permalink to %4$s" rel="bookmark">permalink</a>.", "twentyeleven")
else:
  utility_text = __("This entry was posted in %1$s. Bookmark the <a href="%3$s" title="Permalink to %4$s" rel="bookmark">permalink</a>.", "twentyeleven")
printf(utility_text, get_the_category_list(__(", ", "twentyeleven")), tag_list, esc_url(get_permalink()), the_title_attribute("echo=0"))
print("\n		")
edit_post_link(__("Edit", "twentyeleven"), "<span class="edit-link">", "</span>")
print("	</footer><!-- .entry-meta -->\n</article><!-- #post-")
the_ID()
print(" -->\n")
