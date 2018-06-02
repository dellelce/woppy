#!/usr/bin/python
#-*- coding: utf-8 -*-
get_header()
print("\n		<section id="primary">\n			<div id="content" role="main">\n\n			")
if have_posts():
  print("\n				<header class="page-header">\n					<h1 class="page-title">\n						")
  if is_day():
    print("							")
    printf(__("Daily Archives: %s", "twentyeleven"), "<span>"+get_the_date()+"</span>")
    print("						")
  elif is_month():
    print("							")
    printf(__("Monthly Archives: %s", "twentyeleven"), "<span>"+get_the_date(_x("F Y", "monthly archives date format", "twentyeleven"))+"</span>")
    print("						")
  elif is_year():
    print("							")
    printf(__("Yearly Archives: %s", "twentyeleven"), "<span>"+get_the_date(_x("Y", "yearly archives date format", "twentyeleven"))+"</span>")
    print("						")
  else:
    print("							")
    _e("Blog Archives", "twentyeleven")
    print("						")
  print("					</h1>\n				</header>\n\n				")
  twentyeleven_content_nav("nav-above")
  print("\n				")
  print("				")
  while :
    the_post()
    print("\n					")
    get_template_part("content", get_post_format())
    print("\n				")
  print("\n				")
  twentyeleven_content_nav("nav-below")
  print("\n			")
else:
  print("\n				<article id="post-0" class="post no-results not-found">\n					<header class="entry-header">\n						<h1 class="entry-title">")
  _e("Nothing Found", "twentyeleven")
  print("</h1>\n					</header><!-- .entry-header -->\n\n					<div class="entry-content">\n						<p>")
  _e("Apologies, but no results were found for the requested archive. Perhaps searching will help find a related post.", "twentyeleven")
  print("</p>\n						")
  get_search_form()
  print("					</div><!-- .entry-content -->\n				</article><!-- #post-0 -->\n\n			")
print("\n			</div><!-- #content -->\n		</section><!-- #primary -->\n\n")
get_sidebar()
get_footer()
