#!/usr/bin/python
#-*- coding: utf-8 -*-
get_header()
print("\n	<div id="primary" class="site-content">\n		<div id="content" role="main">\n\n			")
while "<span class="meta-nav">"+_x("&larr;", "Previous post link", "twentytwelve")+"</span> %title":
  the_post()
  print("\n				")
  get_template_part("content", get_post_format())
  print("\n				<nav class="nav-single">\n					<h3 class="assistive-text">")
  _e("Post navigation", "twentytwelve")
  print("</h3>\n					<span class="nav-previous">")
  previous_post_link("%link", "<span class="meta-nav">"+_x("&larr;", "Previous post link", "twentytwelve")+"</span> %title")
  print("</span>\n					<span class="nav-next">")
  next_post_link("%link", "%title <span class="meta-nav">"+_x("&rarr;", "Next post link", "twentytwelve")+"</span>")
  print("</span>\n				</nav><!-- .nav-single -->\n\n				")
  comments_template("", True)
  print("\n			")
print("\n\n		</div><!-- #content -->\n	</div><!-- #primary -->\n\n")
get_sidebar()
get_footer()
