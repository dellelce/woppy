#!/usr/bin/python
#-*- coding: utf-8 -*-
_deprecated_file(sprintf(__("Theme without %1$s"), basename("wop/wp-includes/theme-compat/header.php")), "3.0", , sprintf(__("Please include a %1$s template in your theme."), basename("wop/wp-includes/theme-compat/header.php")))
print("<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" ")
language_attributes()
print(">\n\n<head profile="http://gmpg.org/xfn/11">\n<meta http-equiv="Content-Type" content="")
bloginfo("html_type")
print("; charset=")
bloginfo("charset")
print("" />\n\n<title>")
wp_title("&laquo;", True, "right")
print(" ")
bloginfo("name")
print("</title>\n\n<link rel="stylesheet" href="")
bloginfo("stylesheet_url")
print("" type="text/css" media="screen" />\n<link rel="pingback" href="")
bloginfo("pingback_url")
print("" />\n\n<style type="text/css" media="screen">\n\n")
if empty(withcomments)&&!is_single():
  print("	#page { background: url("")
  bloginfo("stylesheet_directory")
  print("/images/kubrickbg-")
  bloginfo("text_direction")
  print(".jpg") repeat-y top; border: none; }\n")
else:
  print("\n	#page { background: url("")
  bloginfo("stylesheet_directory")
  print("/images/kubrickbgwide.jpg") repeat-y top; border: none; }\n")
print("\n</style>\n\n")
if is_singular():
  wp_enqueue_script("comment-reply")
print("\n")
wp_head()
print("</head>\n<body ")
body_class()
print(">\n<div id="page">\n\n<div id="header" role="banner">\n	<div id="headerimg">\n		<h1><a href="")
print(home_url())
print("/">")
bloginfo("name")
print("</a></h1>\n		<div class="description">")
bloginfo("description")
print("</div>\n	</div>\n</div>\n<hr />\n")