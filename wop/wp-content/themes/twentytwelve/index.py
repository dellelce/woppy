#!/usr/bin/python
#-*- coding: utf-8 -*-
get_header()
print("\n	<div id="primary" class="site-content">\n		<div id="content" role="main">\n		")
if have_posts():
  print("\n			")
  print("			")
  while :
    the_post()
    print("				")
    get_template_part("content", get_post_format())
    print("			")
  print("\n			")
  twentytwelve_content_nav("nav-below")
  print("\n		")
else:
  print("\n			<article id="post-0" class="post no-results not-found">\n\n			")
  if current_user_can("edit_posts"):
    print("				<header class="entry-header">\n					<h1 class="entry-title">")
    _e("No posts to display", "twentytwelve")
    print("</h1>\n				</header>\n\n				<div class="entry-content">\n					<p>")
    printf(__("Ready to publish your first post? <a href="%s">Get started here</a>.", "twentytwelve"), admin_url("post-new.php"))
    print("</p>\n				</div><!-- .entry-content -->\n\n			")
  else:
    print("				<header class="entry-header">\n					<h1 class="entry-title">")
    _e("Nothing Found", "twentytwelve")
    print("</h1>\n				</header>\n\n				<div class="entry-content">\n					<p>")
    _e("Apologies, but no results were found. Perhaps searching will help find a related post.", "twentytwelve")
    print("</p>\n					")
    get_search_form()
    print("				</div><!-- .entry-content -->\n			")
  print("\n\n			</article><!-- #post-0 -->\n\n		")
print("\n\n		</div><!-- #content -->\n	</div><!-- #primary -->\n\n")
get_sidebar()
get_footer()
