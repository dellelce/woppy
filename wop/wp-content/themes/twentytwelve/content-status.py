#!/usr/bin/python
#-*- coding: utf-8 -*-
print("\n	<article id="post-")
the_ID()
print("" ")
post_class()
print(">\n		<div class="entry-header">\n			<header>\n				<h1>")
the_author()
print("</h1>\n				<h2><a href="")
the_permalink()
print("" title="")
print(esc_attr(sprintf(__("Permalink to %s", "twentytwelve"), the_title_attribute("echo=0"))))
print("" rel="bookmark">")
print(get_the_date())
print("</a></h2>\n			</header>\n			")
print(get_avatar(get_the_author_meta("ID"), apply_filters("twentytwelve_status_avatar", "48")))
print("		</div><!-- .entry-header -->\n\n		<div class="entry-content">\n			")
the_content(__("Continue reading <span class="meta-nav">&rarr;</span>", "twentytwelve"))
print("		</div><!-- .entry-content -->\n\n		<footer class="entry-meta">\n			")
if comments_open():
  print("			<div class="comments-link">\n				")
  comments_popup_link("<span class="leave-reply">"+__("Leave a reply", "twentytwelve")+"</span>", __("1 Reply", "twentytwelve"), __("% Replies", "twentytwelve"))
  print("			</div><!-- .comments-link -->\n			")
print("\n			")
edit_post_link(__("Edit", "twentytwelve"), "<span class="edit-link">", "</span>")
print("		</footer><!-- .entry-meta -->\n	</article><!-- #post -->\n")
