#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if !is_multisite():
  wp_die(__("Multisite support is not enabled."))
if !current_user_can("manage_sites"):
  wp_die(__("You do not have sufficient permissions to manage themes for this site."))
get_current_screen()
get_current_screen()
wp_list_table = _get_list_table("WP_MS_Themes_List_Table")
action = wp_list_table.current_action()
s = _REQUEST["s"] if isset(_REQUEST["s"]) else ""
temp_args = ["enabled", "disabled", "error"]
_SERVER["REQUEST_URI"] = remove_query_arg(temp_args, _SERVER["REQUEST_URI"])
referer = remove_query_arg(temp_args, wp_get_referer())
id = intval(_REQUEST["id"]) if isset(_REQUEST["id"]) else 0
if !id:
  wp_die(__("Invalid site ID."))
wp_list_table.prepare_items()
details = get_blog_details(id)
if !can_edit_network(details.site_id):
  wp_die(__("You do not have permission to access this page."))
is_main_site = is_main_site(id)
if action:
  switch_to_blog(id)
  allowed_themes = get_option("allowedthemes")
  if action=="enable":
    check_admin_referer("enable-theme_"+_GET["theme"])
    theme = _GET["theme"]
    action = "enabled"
    n = 1
    if !allowed_themes:
      allowed_themes = {theme:True}
    else:
      allowed_themes[theme] = True
  elif action=="disable":
    check_admin_referer("disable-theme_"+_GET["theme"])
    theme = _GET["theme"]
    action = "disabled"
    n = 1
    if !allowed_themes:
      allowed_themes = []
    else:
      unset(allowed_themes[theme])
  elif action=="enable-selected":
    check_admin_referer("bulk-themes")
    if isset(_POST["checked"]):
      themes = _POST["checked"]
      action = "enabled"
      n = count(themes)
      for theme in themes:
        allowed_themes[theme] = True
    else:
      action = "error"
      n = "none"
  elif action=="disable-selected":
    check_admin_referer("bulk-themes")
    if isset(_POST["checked"]):
      themes = _POST["checked"]
      action = "disabled"
      n = count(themes)
      for theme in themes:
        unset(allowed_themes[theme])
    else:
      action = "error"
      n = "none"
  update_option("allowedthemes", allowed_themes)
  restore_current_blog()
  wp_safe_redirect(add_query_arg({"id":id, action:n}, referer))
  exit(0)
if isset(_GET["action"])&&"update-site"==_GET["action"]:
  wp_safe_redirect(referer)
  exit(0)
add_thickbox()
add_screen_option("per_page", {"label":_x("Themes", "themes per page (screen options)")})
site_url_no_http = preg_replace("#^http(s)?://#", "", get_blogaddress_by_id(id))
title_site_url_linked = sprintf(__("Edit Site: <a href="%1$s">%2$s</a>"), get_blogaddress_by_id(id), site_url_no_http)
title = sprintf(__("Edit Site: %s"), site_url_no_http)
parent_file = "sites.php"
submenu_file = "sites.php"
require("../admin-header.php")
print("\n<div class="wrap">\n")
screen_icon("ms-admin")
print("<h2 id="edit-site">")
print(title_site_url_linked)
print("</h2>\n<h3 class="nav-tab-wrapper">\n")
tabs = {"site-info":{"label":__("Info"), "url":"site-info.php"}, "site-users":{"label":__("Users"), "url":"site-users.php"}, "site-themes":{"label":__("Themes"), "url":"site-themes.php"}, "site-settings":{"label":__("Settings"), "url":"site-settings.php"}}
for tab in tabs:
  class = " nav-tab-active" if tab["url"]==pagenow else ""
  print("<a href=""+tab["url"]+"?id="+id+"" class="nav-tab"+class+"">"+esc_html(tab["label"])+"</a>")
print("</h3>")
if isset(_GET["enabled"]):
  _GET["enabled"] = absint(_GET["enabled"])
  print("<div id="message" class="updated"><p>"+sprintf(_n("Theme enabled.", "%s themes enabled.", _GET["enabled"]), number_format_i18n(_GET["enabled"]))+"</p></div>")
elif isset(_GET["disabled"]):
  _GET["disabled"] = absint(_GET["disabled"])
  print("<div id="message" class="updated"><p>"+sprintf(_n("Theme disabled.", "%s themes disabled.", _GET["disabled"]), number_format_i18n(_GET["disabled"]))+"</p></div>")
elif isset(_GET["error"])&&"none"==_GET["error"]:
  print("<div id="message" class="error"><p>"+__("No theme selected.")+"</p></div>")
print("\n<p>")
_e("Network enabled themes are not shown on this screen.")
print("</p>\n\n<form method="get" action="">\n")
wp_list_table.search_box(__("Search Installed Themes"), "theme")
print("<input type="hidden" name="id" value="")
print(esc_attr(id))
print("" />\n</form>\n\n")
wp_list_table.views()
print("\n<form method="post" action="site-themes.php?action=update-site">\n	<input type="hidden" name="id" value="")
print(esc_attr(id))
print("" />\n\n")
wp_list_table.display()
print("\n</form>\n\n</div>\n")
include(ABSPATH+"wp-admin/admin-footer.php")
