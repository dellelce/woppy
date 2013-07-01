#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("admin.php")
if !current_user_can("manage_links"):
  wp_die(__("You do not have sufficient permissions to edit the links for this site."))
wp_list_table = _get_list_table("WP_Links_List_Table")
doaction = wp_list_table.current_action()
if doaction&&isset(_REQUEST["linkcheck"]):
  check_admin_referer("bulk-bookmarks")
  if "delete"==doaction:
    bulklinks = _REQUEST["linkcheck"]
    for link_id in bulklinks:
      link_id = link_id
      wp_delete_link(link_id)
    wp_redirect(add_query_arg("deleted", count(bulklinks), admin_url("link-manager.php")))
    exit(0)
elif !empty(_GET["_wp_http_referer"]):
  wp_redirect(remove_query_arg(["_wp_http_referer", "_wpnonce"], stripslashes(_SERVER["REQUEST_URI"])))
  exit(0)
wp_list_table.prepare_items()
title = __("Links")
self_file = parent_file = "link-manager.php"
get_current_screen()
get_current_screen()
get_current_screen()
include_once("./admin-header.php")
if !current_user_can("manage_links"):
  wp_die(__("You do not have sufficient permissions to edit the links for this site."))
print("\n<div class="wrap nosubsub">\n")
screen_icon()
print("<h2>")
print(esc_html(title))
print(" <a href="link-add.php" class="add-new-h2">")
print(esc_html_x("Add New", "link"))
print("</a> ")
if !empty(_REQUEST["s"]):
  printf("<span class="subtitle">"+__("Search results for &#8220;%s&#8221;")+"</span>", esc_html(stripslashes(_REQUEST["s"])))
print("</h2>\n\n")
if isset(_REQUEST["deleted"]):
  print("<div id="message" class="updated"><p>")
  deleted = _REQUEST["deleted"]
  printf(_n("%s link deleted.", "%s links deleted", deleted), deleted)
  print("</p></div>")
  _SERVER["REQUEST_URI"] = remove_query_arg(["deleted"], _SERVER["REQUEST_URI"])
print("\n<form id="posts-filter" action="" method="get">\n\n")
wp_list_table.search_box(__("Search Links"), "link")
print("\n")
wp_list_table.display()
print("\n<div id="ajax-response"></div>\n</form>\n\n</div>\n\n")
include("./admin-footer.php")
