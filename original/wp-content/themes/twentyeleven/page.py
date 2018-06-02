#!/usr/bin/python
#-*- coding: utf-8 -*-
get_header()
print("\n		<div id="primary">\n			<div id="content" role="main">\n\n				")
while :
  the_post()
  print("\n					")
  get_template_part("content", "page")
  print("\n					")
  comments_template("", True)
  print("\n				")
print("\n\n			</div><!-- #content -->\n		</div><!-- #primary -->\n\n")
get_footer()
