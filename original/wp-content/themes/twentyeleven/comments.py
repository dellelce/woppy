#!/usr/bin/python
#-*- coding: utf-8 -*-
print("	<div id="comments">\n	")
if post_password_required():
  print("		<p class="nopassword">")
  _e("This post is password protected. Enter the password to view any comments.", "twentyeleven")
  print("</p>\n	</div><!-- #comments -->\n	")
  return 
print("\n	")
print("\n\n	")
if have_comments():
  print("		<h2 id="comments-title">\n			")
  printf(_n("One thought on &ldquo;%2$s&rdquo;", "%1$s thoughts on &ldquo;%2$s&rdquo;", get_comments_number(), "twentyeleven"), number_format_i18n(get_comments_number()), "<span>"+get_the_title()+"</span>")
  print("		</h2>\n\n		")
  if get_comment_pages_count()>1&&get_option("page_comments"):
    print("\n		<nav id="comment-nav-above">\n			<h1 class="assistive-text">")
    _e("Comment navigation", "twentyeleven")
    print("</h1>\n			<div class="nav-previous">")
    previous_comments_link(__("&larr; Older Comments", "twentyeleven"))
    print("</div>\n			<div class="nav-next">")
    next_comments_link(__("Newer Comments &rarr;", "twentyeleven"))
    print("</div>\n		</nav>\n		")
  print("\n\n		<ol class="commentlist">\n			")
  wp_list_comments({"callback":"twentyeleven_comment"})
  print("		</ol>\n\n		")
  if get_comment_pages_count()>1&&get_option("page_comments"):
    print("\n		<nav id="comment-nav-below">\n			<h1 class="assistive-text">")
    _e("Comment navigation", "twentyeleven")
    print("</h1>\n			<div class="nav-previous">")
    previous_comments_link(__("&larr; Older Comments", "twentyeleven"))
    print("</div>\n			<div class="nav-next">")
    next_comments_link(__("Newer Comments &rarr;", "twentyeleven"))
    print("</div>\n		</nav>\n		")
  print("\n\n		")
  if !comments_open()&&get_comments_number():
    print("		<p class="nocomments">")
    _e("Comments are closed.", "twentyeleven")
    print("</p>\n		")
  print("\n	")
print("\n\n	")
comment_form()
print("\n</div><!-- #comments -->\n")
