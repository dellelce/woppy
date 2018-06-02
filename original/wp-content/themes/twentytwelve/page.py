#!/usr/bin/python
#-*- coding: utf-8 -*-
get_header()
print("\n	<div id="primary" class="site-content">\n		<div id="content" role="main">\n\n			")
while :
  the_post()
  print("				")
  get_template_part("content", "page")
  print("				")
  comments_template("", True)
  print("			")
print("\n\n		</div><!-- #content -->\n	</div><!-- #primary -->\n\n")
get_sidebar()
get_footer()
