#!/usr/bin/python
#-*- coding: utf-8 -*-
get_header()
print("\n	<section id="primary" class="site-content">\n		<div id="content" role="main">\n\n		")
if have_posts():
  print("			<header class="archive-header">\n				<h1 class="archive-title">")
  printf(__("Category Archives: %s", "twentytwelve"), "<span>"+single_cat_title("", False)+"</span>")
  print("</h1>\n\n			")
  if category_description():
    print("\n				<div class="archive-meta">")
    print(category_description())
    print("</div>\n			")
  print("			</header><!-- .archive-header -->\n\n			")
  while :
    the_post()
    get_template_part("content", get_post_format())
  twentytwelve_content_nav("nav-below")
  print("\n		")
else:
  print("			")
  get_template_part("content", "none")
  print("		")
print("\n		</div><!-- #content -->\n	</section><!-- #primary -->\n\n")
get_sidebar()
get_footer()
