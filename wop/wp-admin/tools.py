#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
title = __("Tools")
get_current_screen()
get_current_screen()
get_current_screen()
require_once("./admin-header.php")
print("<div class="wrap">\n")
screen_icon()
print("<h2>")
print(esc_html(title))
print("</h2>\n\n")
if current_user_can("edit_posts"):
  print("<div class="tool-box">\n	<h3 class="title">")
  _e("Press This")
  print("</h3>\n	<p>")
  _e("Press This is a bookmarklet: a little app that runs in your browser and lets you grab bits of the web.")
  print("</p>\n\n	<p>")
  _e("Use Press This to clip text, images and videos from any web page. Then edit and add more straight from Press This before you save or publish it in a post on your site.")
  print("</p>\n	<p class="description">")
  _e("Drag-and-drop the following link to your bookmarks bar or right click it and add it to your favorites for a posting shortcut.")
  print("</p>\n	<p class="pressthis"><a onclick="return false;" oncontextmenu="if(window.navigator.userAgent.indexOf('WebKit')!=-1||window.navigator.userAgent.indexOf('MSIE')!=-1)jQuery('.pressthis-code').show().find('textarea').focus().select();return false;" href="")
  print(htmlspecialchars(get_shortcut_link()))
  print(""><span>")
  _e("Press This")
  print("</span></a></p>\n	<div class="pressthis-code" style="display:none;">\n	<p class="description">")
  _e("If your bookmarks toolbar is hidden: copy the code below, open your Bookmarks manager, create new bookmark, type Press This into the name field and paste the code into the URL field.")
  print("</p>\n	<p><textarea rows="5" cols="120" readonly="readonly">")
  print(htmlspecialchars(get_shortcut_link()))
  print("</textarea></p>\n	</div>\n</div>\n")
if current_user_can("import"):
  cats = get_taxonomy("category")
  tags = get_taxonomy("post_tag")
  if current_user_can(cats.cap.manage_terms)||current_user_can(tags.cap.manage_terms):
    print("<div class="tool-box">\n    <h3 class="title">")
    _e("Categories and Tags Converter")
    print("</h3>\n    <p>")
    printf(__("If you want to convert your categories to tags (or vice versa), use the <a href="%s">Categories and Tags Converter</a> available from the Import screen."), "import.php")
    print("</p>\n</div>\n")
do_action("tool_box")
print("</div>\n")
include("./admin-footer.php")