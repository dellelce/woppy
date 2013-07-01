#!/usr/bin/python
#-*- coding: utf-8 -*-
print("<!DOCTYPE html>\n<!--[if IE 6]>\n<html id="ie6" ")
language_attributes()
print(">\n<![endif]-->\n<!--[if IE 7]>\n<html id="ie7" ")
language_attributes()
print(">\n<![endif]-->\n<!--[if IE 8]>\n<html id="ie8" ")
language_attributes()
print(">\n<![endif]-->\n<!--[if !(IE 6) | !(IE 7) | !(IE 8)  ]><!-->\n<html ")
language_attributes()
print(">\n<!--<![endif]-->\n<head>\n<meta charset="")
bloginfo("charset")
print("" />\n<meta name="viewport" content="width=device-width" />\n<title>")
pagepagedwp_title("|", True, "right")
bloginfo("name")
site_description = get_bloginfo("description", "display")
if site_description&&is_home()||is_front_page():
  print(" | "+site_description+"")
if paged>=2||page>=2:
  print(" | "+sprintf(__("Page %s", "twentyeleven"), max(paged, page)))
print("</title>\n<link rel="profile" href="http://gmpg.org/xfn/11" />\n<link rel="stylesheet" type="text/css" media="all" href="")
bloginfo("stylesheet_url")
print("" />\n<link rel="pingback" href="")
bloginfo("pingback_url")
print("" />\n<!--[if lt IE 9]>\n<script src="")
print(get_template_directory_uri())
print("/js/html5.js" type="text/javascript"></script>\n<![endif]-->\n")
if is_singular()&&get_option("thread_comments"):
  wp_enqueue_script("comment-reply")
wp_head()
print("</head>\n\n<body ")
body_class()
print(">\n<div id="page" class="hfeed">\n	<header id="branding" role="banner">\n			<hgroup>\n				<h1 id="site-title"><span><a href="")
print(esc_url(home_url("/")))
print("" title="")
print(esc_attr(get_bloginfo("name", "display")))
print("" rel="home">")
bloginfo("name")
print("</a></span></h1>\n				<h2 id="site-description">")
bloginfo("description")
print("</h2>\n			</hgroup>\n\n			")
header_image = get_header_image()
if header_image:
  if function_exists("get_custom_header"):
    header_image_width = get_theme_support("custom-header", "width")
  else:
    header_image_width = HEADER_IMAGE_WIDTH
  print("			<a href="")
  print(esc_url(home_url("/")))
  print("">\n				")
  if is_singular()&&has_post_thumbnail(post.ID)&&image = wp_get_attachment_image_src(get_post_thumbnail_id(post.ID), [header_image_width, header_image_width])&&image[1]>=header_image_width:
    print(get_the_post_thumbnail(post.ID, "post-thumbnail"))
  elif function_exists("get_custom_header"):
    header_image_width = width
    header_image_height = height
  else:
    header_image_width = HEADER_IMAGE_WIDTH
    header_image_height = HEADER_IMAGE_HEIGHT
  print("\n			</a>\n			")
print("\n\n			")
if "blank"==get_header_textcolor():
  print("				<div class="only-search")
  if header_image:
    print(" with-image")
  print("">\n				")
  get_search_form()
  print("				</div>\n			")
else:
  print("				")
  get_search_form()
  print("			")
print("\n			<nav id="access" role="navigation">\n				<h3 class="assistive-text">")
_e("Main menu", "twentyeleven")
print("</h3>\n				")
print("				<div class="skip-link"><a class="assistive-text" href="#content" title="")
esc_attr_e("Skip to primary content", "twentyeleven")
print("">")
_e("Skip to primary content", "twentyeleven")
print("</a></div>\n				<div class="skip-link"><a class="assistive-text" href="#secondary" title="")
esc_attr_e("Skip to secondary content", "twentyeleven")
print("">")
_e("Skip to secondary content", "twentyeleven")
print("</a></div>\n				")
print("				")
wp_nav_menu({"theme_location":"primary"})
print("			</nav><!-- #access -->\n	</header><!-- #branding -->\n\n\n	<div id="main">\n")
