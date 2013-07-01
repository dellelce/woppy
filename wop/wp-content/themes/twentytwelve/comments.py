#!/usr/bin/python
#-*- coding: utf-8 -*-
if post_password_required():
  return 
print("\n<div id="comments" class="comments-area">\n\n	")
print("\n\n	")
if have_comments():
  print("		<h2 class="comments-title">\n			")
  printf(_n("One thought on &ldquo;%2$s&rdquo;", "%1$s thoughts on &ldquo;%2$s&rdquo;", get_comments_number(), "twentytwelve"), number_format_i18n(get_comments_number()), "<span>"+get_the_title()+"</span>")
  print("		</h2>\n\n		<ol class="commentlist">\n			")
  wp_list_comments({"callback":"twentytwelve_comment", "style":"ol"})
  print("		</ol><!-- .commentlist -->\n\n		")
  if get_comment_pages_count()>1&&get_option("page_comments"):
    print("\n		<nav id="comment-nav-below" class="navigation" role="navigation">\n			<h1 class="assistive-text section-heading">")
    _e("Comment navigation", "twentytwelve")
    print("</h1>\n			<div class="nav-previous">")
    previous_comments_link(__("&larr; Older Comments", "twentytwelve"))
    print("</div>\n			<div class="nav-next">")
    next_comments_link(__("Newer Comments &rarr;", "twentytwelve"))
    print("</div>\n		</nav>\n		")
  print("\n\n		")
  if !comments_open()&&get_comments_number():
    print("		<p class="nocomments">")
    _e("Comments are closed.", "twentytwelve")
    print("</p>\n		")
  print("\n	")
print("\n\n	")
comment_form()
print("\n</div><!-- #comments .comments-area -->")
