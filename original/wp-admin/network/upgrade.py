#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if !is_multisite():
  wp_die(__("Multisite support is not enabled."))
require_once(ABSPATH+WPINC+"/http.php")
title = __("Update Network")
parent_file = "upgrade.php"
get_current_screen()
get_current_screen()
require_once("../admin-header.php")
if !current_user_can("manage_network"):
  wp_die(__("You do not have permission to access this page."))
print("<div class="wrap">")
screen_icon("tools")
print("<h2>"+__("Update Network")+"</h2>")
action = _GET["action"] if isset(_GET["action"]) else "show"
if action=="upgrade":
  n = intval(_GET["n"]) if isset(_GET["n"]) else 0
  if n<5:
    wp_db_versionupdate_site_option("wpmu_upgrade_site", wp_db_version)
  blogs = wpdb.get_results("SELECT * FROM "+wpdb.blogs+" WHERE site_id = '"+wpdb.siteid+"' AND spam = '0' AND deleted = '0' AND archived = '0' ORDER BY registered DESC LIMIT "+n+", 5", ARRAY_A)
  if empty(blogs):
    print("<p>"+__("All done!")+"</p>")
  print("<ul>")
  for details in blogs:
    switch_to_blog(details["blog_id"])
    siteurl = site_url()
    upgrade_url = admin_url("upgrade.php?step=upgrade_db")
    restore_current_blog()
    print("<li>"+siteurl+"</li>")
    response = wp_remote_get(upgrade_url, {"timeout":120, "httpversion":"1.1"})
    if is_wp_error(response):
      wp_die(sprintf(__("Warning! Problem updating %1$s. Your server may not be able to connect to sites running on it. Error message: <em>%2$s</em>"), siteurl, response.get_error_message()))
    do_action("after_mu_upgrade", response)
    do_action("wpmu_upgrade_site", details["blog_id"])
  print("</ul>")
  print("<p>")
  _e("If your browser doesn&#8217;t start loading the next page automatically, click this link:")
  print(" <a class="button" href="upgrade.php?action=upgrade&amp;n=")
  print(n+5)
  print("">")
  _e("Next Sites")
  print("</a></p>\n		<script type='text/javascript'>\n		<!--\n		function nextpage() {\n			location.href = "upgrade.php?action=upgrade&n=")
  print(n+5)
  print("";\n		}\n		setTimeout( "nextpage()", 250 );\n		//-->\n		</script>")
elif action=="show":
else:
  print("<p>")
  _e("You can update all the sites on your network through this page. It works by calling the update script of each site automatically. Hit the link below to update.")
  print("</p>\n		<p><a class="button" href="upgrade.php?action=upgrade">")
  _e("Update Network")
  print("</a></p>")
  do_action("wpmu_upgrade_page")
print("</div>\n\n")
include("../admin-footer.php")
