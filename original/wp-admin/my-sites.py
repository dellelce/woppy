#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if !is_multisite():
  wp_die(__("Multisite support is not enabled."))
if !current_user_can("read"):
  wp_die(__("You do not have sufficient permissions to view this page."))
action = _POST["action"] if isset(_POST["action"]) else "splash"
blogs = get_blogs_of_user(current_user.ID)
updated = False
if "updateblogsettings"==action&&isset(_POST["primary_blog"]):
  check_admin_referer("update-my-sites")
  blog = get_blog_details(_POST["primary_blog"])
  if blog&&isset(blog.domain):
    update_user_option(current_user.ID, "primary_blog", _POST["primary_blog"], True)
    updated = True
  else:
    wp_die(__("The primary site you chose does not exist."))
title = __("My Sites")
parent_file = "index.php"
get_current_screen()
get_current_screen()
require_once("./admin-header.php")
if updated:
  print("	<div id="message" class="updated"><p><strong>")
  _e("Settings saved.")
  print("</strong></p></div>\n")
print("\n<div class="wrap">\n")
screen_icon()
print("<h2>")
print(esc_html(title))
print("</h2>\n")
if empty(blogs):
  print("<p>")
  _e("You must be a member of at least one site to use this page.")
  print("</p>")
else:
  print("<form id="myblogs" action="" method="post">\n	")
  choose_primary_blog()
  do_action("myblogs_allblogs_options")
  print("	<br clear="all" />\n	<table class="widefat fixed">\n	")
  settings_html = apply_filters("myblogs_options", "", "global")
  if settings_html!="":
    print("<tr><td valign="top"><h3>"+__("Global Settings")+"</h3></td><td>")
    print(settings_html)
    print("</td></tr>")
  reset(blogs)
  num = count(blogs)
  cols = 1
  if num>=20:
    cols = 4
  elif num>=10:
    cols = 2
  num_rows = ceil(num/cols)
  split = 0
  i = 1
  while i<=num_rows:
    rows[] = array_slice(blogs, split, cols)
    split = split+cols
    i+=1
  c = ""
  for row in rows:
    c = "" if c=="alternate" else "alternate"
    print("<tr class='"+c+"'>")
    i = 0
    for user_blog in row:
      s = "" if i==3 else "border-right: 1px solid #ccc;"
      print("<td valign='top' style='"+s+"'>")
      print("<h3>"+user_blog.blogname+"</h3>")
      print("<p>"+apply_filters("myblogs_blog_actions", "<a href='"+esc_url(get_home_url(user_blog.userblog_id))+"'>"+__("Visit")+"</a> | <a href='"+esc_url(get_admin_url(user_blog.userblog_id))+"'>"+__("Dashboard")+"</a>", user_blog)+"</p>")
      print(apply_filters("myblogs_options", "", user_blog))
      print("</td>")
      i+=1
    print("</tr>")
  print("	</table>\n	<input type="hidden" name="action" value="updateblogsettings" />\n	")
  wp_nonce_field("update-my-sites")
  print("	")
  submit_button()
  print("	</form>\n")
print("	</div>\n")
include("./admin-footer.php")
