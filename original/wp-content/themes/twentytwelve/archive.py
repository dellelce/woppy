#!/usr/bin/python
#-*- coding: utf-8 -*-
get_header()
print("\n	<section id="primary" class="site-content">\n		<div id="content" role="main">\n\n		")
if have_posts():
  print("			<header class="archive-header">\n				<h1 class="archive-title">")
  if is_day():
    printf(__("Daily Archives: %s", "twentytwelve"), "<span>"+get_the_date()+"</span>")
  elif is_month():
    printf(__("Monthly Archives: %s", "twentytwelve"), "<span>"+get_the_date(_x("F Y", "monthly archives date format", "twentytwelve"))+"</span>")
  elif is_year():
    printf(__("Yearly Archives: %s", "twentytwelve"), "<span>"+get_the_date(_x("Y", "yearly archives date format", "twentytwelve"))+"</span>")
  else:
    _e("Archives", "twentytwelve")
  print("</h1>\n			</header><!-- .archive-header -->\n\n			")
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
