#!/usr/bin/python
#-*- coding: utf-8 -*-
get_header()
print("\n	<div id="primary" class="site-content">\n		<div id="content" role="main">\n\n			")
while :
  the_post()
  print("				")
  if has_post_thumbnail():
    print("					<div class="entry-page-image">\n						")
    the_post_thumbnail()
    print("					</div><!-- .entry-page-image -->\n				")
  print("\n				")
  get_template_part("content", "page")
  print("\n			")
print("\n\n		</div><!-- #content -->\n	</div><!-- #primary -->\n\n")
get_sidebar("front")
get_footer()
