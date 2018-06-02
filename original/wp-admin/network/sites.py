#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if !is_multisite():
  wp_die(__("Multisite support is not enabled."))
if !current_user_can("manage_sites"):
  wp_die(__("You do not have permission to access this page."))
wp_list_table = _get_list_table("WP_MS_Sites_List_Table")
pagenum = wp_list_table.get_pagenum()
title = __("Sites")
parent_file = "sites.php"
add_screen_option("per_page", {"label":_x("Sites", "sites per page (screen options)")})
get_current_screen()
get_current_screen()
id = intval(_REQUEST["id"]) if isset(_REQUEST["id"]) else 0
if isset(_GET["action"]):
  do_action("wpmuadminedit", "")
  if "confirm"===_GET["action"]:
    check_admin_referer("confirm")
    if !headers_sent():
      nocache_headers()
      header("Content-Type: text/html; charset=utf-8")
    if current_site.blog_id==id:
      wp_die(__("You are not allowed to change the current site."))
    print("		<!DOCTYPE html>\n		<html xmlns="http://www.w3.org/1999/xhtml" ")
    language_attributes()
    print(">\n			<head>\n				<title>")
    _e("WordPress &rsaquo; Confirm your action")
    print("</title>\n\n				<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n				")
    wp_admin_css("install", True)
    wp_admin_css("ie", True)
    print("			</head>\n			<body class="wp-core-ui">\n				<h1 id="logo"><a href="")
    esc_attr_e("http://wordpress.org/")
    print("">")
    _e("WordPress")
    print("</a></h1>\n				<form action="sites.php?action=")
    print(esc_attr(_GET["action2"]))
    print("" method="post">\n					<input type="hidden" name="action" value="")
    print(esc_attr(_GET["action2"]))
    print("" />\n					<input type="hidden" name="id" value="")
    print(esc_attr(id))
    print("" />\n					<input type="hidden" name="_wp_http_referer" value="")
    print(esc_attr(wp_get_referer()))
    print("" />\n					")
    wp_nonce_field(_GET["action2"], "_wpnonce", False)
    print("					<p>")
    print(esc_html(stripslashes(_GET["msg"])))
    print("</p>\n					")
    submit_button(__("Confirm"), "button")
    print("				</form>\n			</body>\n		</html>\n		")
    exit(0)
  updated_action = ""
  manage_actions = ["deleteblog", "allblogs", "archiveblog", "unarchiveblog", "activateblog", "deactivateblog", "unspamblog", "spamblog", "unmatureblog", "matureblog"]
  if in_array(_GET["action"], manage_actions):
    action = _GET["action"]
    if "allblogs"===action:
      action = "bulk-sites"
    check_admin_referer(action)
  if _GET["action"]=="deleteblog":
    if !current_user_can("delete_sites"):
      wp_die(__("You do not have permission to access this page."))
    updated_action = "not_deleted"
    if id!="0"&&id!=current_site.blog_id&&current_user_can("delete_site", id):
      wpmu_delete_blog(id, True)
      updated_action = "delete"
  elif _GET["action"]=="allblogs":
    if isset(_POST["action"])||isset(_POST["action2"])&&isset(_POST["allblogs"]):
      doaction = _POST["action"] if _POST["action"]!=-1 else _POST["action2"]
      for val in _POST["allblogs"]:
        if val!="0"&&val!=current_site.blog_id:
          if doaction=="delete":
            if !current_user_can("delete_site", val):
              wp_die(__("You are not allowed to delete the site."))
            updated_action = "all_delete"
            wpmu_delete_blog(val, True)
          elif doaction=="spam":
          elif doaction=="notspam":
            updated_action = "all_spam" if "spam"===doaction else "all_notspam"
            update_blog_status(val, "spam", "1" if "spam"===doaction else "0")
        else:
          wp_die(__("You are not allowed to change the current site."))
    else:
      wp_redirect(network_admin_url("sites.php"))
      exit(0)
  elif _GET["action"]=="archiveblog":
  elif _GET["action"]=="unarchiveblog":
    update_blog_status(id, "archived", "1" if "archiveblog"===_GET["action"] else "0")
  elif _GET["action"]=="activateblog":
    update_blog_status(id, "deleted", "0")
    do_action("activate_blog", id)
  elif _GET["action"]=="deactivateblog":
    do_action("deactivate_blog", id)
    update_blog_status(id, "deleted", "1")
  elif _GET["action"]=="unspamblog":
  elif _GET["action"]=="spamblog":
    update_blog_status(id, "spam", "1" if "spamblog"===_GET["action"] else "0")
  elif _GET["action"]=="unmatureblog":
  elif _GET["action"]=="matureblog":
    update_blog_status(id, "mature", "1" if "matureblog"===_GET["action"] else "0")
  if empty(updated_action)&&in_array(_GET["action"], manage_actions):
    updated_action = _GET["action"]
  if !empty(updated_action):
    wp_safe_redirect(add_query_arg({"updated":updated_action}, wp_get_referer()))
    exit(0)
msg = ""
if isset(_GET["updated"]):
  if _GET["updated"]=="all_notspam":
    msg = __("Sites removed from spam.")
  elif _GET["updated"]=="all_spam":
    msg = __("Sites marked as spam.")
  elif _GET["updated"]=="all_delete":
    msg = __("Sites deleted.")
  elif _GET["updated"]=="delete":
    msg = __("Site deleted.")
  elif _GET["updated"]=="not_deleted":
    msg = __("You do not have permission to delete that site.")
  elif _GET["updated"]=="archiveblog":
    msg = __("Site archived.")
  elif _GET["updated"]=="unarchiveblog":
    msg = __("Site unarchived.")
  elif _GET["updated"]=="activateblog":
    msg = __("Site activated.")
  elif _GET["updated"]=="deactivateblog":
    msg = __("Site deactivated.")
  elif _GET["updated"]=="unspamblog":
    msg = __("Site removed from spam.")
  elif _GET["updated"]=="spamblog":
    msg = __("Site marked as spam.")
  else:
    msg = apply_filters("network_sites_updated_message_"+_GET["updated"], __("Settings saved."))
  if !empty(msg):
    msg = "<div class="updated" id="message"><p>"+msg+"</p></div>"
wp_list_table.prepare_items()
require_once("../admin-header.php")
print("\n<div class="wrap">\n")
screen_icon("ms-admin")
print("<h2>")
_e("Sites")
print("\n")
if current_user_can("create_sites"):
  print("	<a href="")
  print(network_admin_url("site-new.php"))
  print("" class="add-new-h2">")
  print(esc_html_x("Add New", "site"))
  print("</a>\n")
print("\n")
if isset(_REQUEST["s"])&&_REQUEST["s"]:
  printf("<span class="subtitle">"+__("Search results for &#8220;%s&#8221;")+"</span>", esc_html(s))
print("</h2>\n\n")
print(msg)
print("\n<form action="" method="get" id="ms-search">\n")
wp_list_table.search_box(__("Search Sites"), "site")
print("<input type="hidden" name="action" value="blogs" />\n</form>\n\n<form id="form-site-list" action="sites.php?action=allblogs" method="post">\n	")
wp_list_table.display()
print("</form>\n</div>\n")
require_once("../admin-footer.php")
