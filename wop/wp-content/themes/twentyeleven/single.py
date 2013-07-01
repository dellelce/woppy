#!/usr/bin/python
#-*- coding: utf-8 -*-
get_header()
print("\n		<div id="primary">\n			<div id="content" role="main">\n\n				")
while :
  the_post()
  print("\n					<nav id="nav-single">\n						<h3 class="assistive-text">")
  _e("Post navigation", "twentyeleven")
  print("</h3>\n						<span class="nav-previous">")
  previous_post_link("%link", __("<span class="meta-nav">&larr;</span> Previous", "twentyeleven"))
  print("</span>\n						<span class="nav-next">")
  next_post_link("%link", __("Next <span class="meta-nav">&rarr;</span>", "twentyeleven"))
  print("</span>\n					</nav><!-- #nav-single -->\n\n					")
  get_template_part("content-single", get_post_format())
  print("\n					")
  comments_template("", True)
  print("\n				")
print("\n\n			</div><!-- #content -->\n		</div><!-- #primary -->\n\n")
get_footer()
