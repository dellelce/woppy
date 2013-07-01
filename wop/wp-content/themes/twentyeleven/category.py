#!/usr/bin/python
#-*- coding: utf-8 -*-
get_header()
print("\n		<section id="primary">\n			<div id="content" role="main">\n\n			")
if have_posts():
  print("\n				<header class="page-header">\n					<h1 class="page-title">")
  printf(__("Category Archives: %s", "twentyeleven"), "<span>"+single_cat_title("", False)+"</span>")
  print("</h1>\n\n					")
  category_description = category_description()
  if !empty(category_description):
    print(apply_filters("category_archive_meta", "<div class="category-archive-meta">"+category_description+"</div>"))
  print("				</header>\n\n				")
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
