#!/usr/bin/python
#-*- coding: utf-8 -*-
print("\n	<article id="post-")
the_ID()
print("" ")
post_class()
print(">\n		<div class="entry-content">\n			")
the_content(__("Continue reading <span class="meta-nav">&rarr;</span>", "twentytwelve"))
print("		</div><!-- .entry-content -->\n\n		<footer class="entry-meta">\n			<a href="")
the_permalink()
print("" title="")
print(esc_attr(sprintf(__("Permalink to %s", "twentytwelve"), the_title_attribute("echo=0"))))
print("" rel="bookmark">\n				<h1>")
the_title()
print("</h1>\n				<h2><time class="entry-date" datetime="")
print(esc_attr(get_the_date("c")))
print("">")
print(get_the_date())
print("</time></h2>\n			</a>\n			")
if comments_open():
  print("			<div class="comments-link">\n				")
  comments_popup_link("<span class="leave-reply">"+__("Leave a reply", "twentytwelve")+"</span>", __("1 Reply", "twentytwelve"), __("% Replies", "twentytwelve"))
  print("			</div><!-- .comments-link -->\n			")
print("\n			")
edit_post_link(__("Edit", "twentytwelve"), "<span class="edit-link">", "</span>")
print("		</footer><!-- .entry-meta -->\n	</article><!-- #post -->\n")
