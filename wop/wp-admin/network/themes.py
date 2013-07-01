#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if !is_multisite():
  wp_die(__("Multisite support is not enabled."))
if !current_user_can("manage_network_themes"):
  wp_die(__("You do not have sufficient permissions to manage network themes."))
wp_list_table = _get_list_table("WP_MS_Themes_List_Table")
pagenum = wp_list_table.get_pagenum()
action = wp_list_table.current_action()
s = _REQUEST["s"] if isset(_REQUEST["s"]) else ""
temp_args = ["enabled", "disabled", "deleted", "error"]
_SERVER["REQUEST_URI"] = remove_query_arg(temp_args, _SERVER["REQUEST_URI"])
referer = remove_query_arg(temp_args, wp_get_referer())
if action:
  allowed_themes = get_site_option("allowedthemes")
  if action=="enable":
    check_admin_referer("enable-theme_"+_GET["theme"])
    allowed_themes[_GET["theme"]] = True
    update_site_option("allowedthemes", allowed_themes)
    if False===strpos(referer, "/network/themes.php"):
      wp_redirect(network_admin_url("themes.php?enabled=1"))
    else:
      wp_safe_redirect(add_query_arg("enabled", 1, referer))
    exit(0)
  elif action=="disable":
    check_admin_referer("disable-theme_"+_GET["theme"])
    unset(allowed_themes[_GET["theme"]])
    update_site_option("allowedthemes", allowed_themes)
    wp_safe_redirect(add_query_arg("disabled", "1", referer))
    exit(0)
  elif action=="enable-selected":
    check_admin_referer("bulk-themes")
    themes = _POST["checked"] if isset(_POST["checked"]) else []
    if empty(themes):
      wp_safe_redirect(add_query_arg("error", "none", referer))
      exit(0)
    for theme in themes:
      allowed_themes[theme] = True
    update_site_option("allowedthemes", allowed_themes)
    wp_safe_redirect(add_query_arg("enabled", count(themes), referer))
    exit(0)
  elif action=="disable-selected":
    check_admin_referer("bulk-themes")
    themes = _POST["checked"] if isset(_POST["checked"]) else []
    if empty(themes):
      wp_safe_redirect(add_query_arg("error", "none", referer))
      exit(0)
    for theme in themes:
      unset(allowed_themes[theme])
    update_site_option("allowedthemes", allowed_themes)
    wp_safe_redirect(add_query_arg("disabled", count(themes), referer))
    exit(0)
  elif action=="update-selected":
    check_admin_referer("bulk-themes")
    if isset(_GET["themes"]):
      themes = explode(",", _GET["themes"])
    elif isset(_POST["checked"]):
      themes = _POST["checked"]
    else:
      themes = []
    title = __("Update Themes")
    parent_file = "themes.php"
    require_once(ABSPATH+"wp-admin/admin-header.php")
    print("<div class="wrap">")
    screen_icon()
    print("<h2>"+esc_html(title)+"</h2>")
    url = self_admin_url("update.php?action=update-selected-themes&amp;themes="+urlencode(join(",", themes)))
    url = wp_nonce_url(url, "bulk-update-themes")
    print("<iframe src='"+url+"' style='width: 100%; height:100%; min-height:850px;'></iframe>")
    print("</div>")
    require_once(ABSPATH+"wp-admin/admin-footer.php")
    exit(0)
  elif action=="delete-selected":
    if !current_user_can("delete_themes"):
      wp_die(__("You do not have sufficient permissions to delete themes for this site."))
    check_admin_referer("bulk-themes")
    themes = _REQUEST["checked"] if isset(_REQUEST["checked"]) else []
    unset(themes[get_option("stylesheet")], themes[get_option("template")])
    if empty(themes):
      wp_safe_redirect(add_query_arg("error", "none", referer))
      exit(0)
    files_to_delete = theme_info = []
    for theme in themes:
      theme_info[theme] = wp_get_theme(theme)
      files_to_delete = array_merge(files_to_delete, list_files(theme_info[theme].get_stylesheet_directory()))
    if empty(themes):
      wp_safe_redirect(add_query_arg("error", "main", referer))
      exit(0)
    include(ABSPATH+"wp-admin/update.php")
    parent_file = "themes.php"
    if !isset(_REQUEST["verify-delete"]):
      wp_enqueue_script("jquery")
      require_once(ABSPATH+"wp-admin/admin-header.php")
      print("			<div class="wrap">\n				")
      themes_to_delete = count(themes)
      screen_icon()
      print("<h2>"+_n("Delete Theme", "Delete Themes", themes_to_delete)+"</h2>")
      print("				<div class="error"><p><strong>")
      _e("Caution:")
      print("</strong> ")
      print(_n("This theme may be active on other sites in the network.", "These themes may be active on other sites in the network.", themes_to_delete))
      print("</p></div>\n				<p>")
      print(_n("You are about to remove the following theme:", "You are about to remove the following themes:", themes_to_delete))
      print("</p>\n					<ul class="ul-disc">\n						")
      for theme in theme_info:
        print("<li>", sprintf(__("<strong>%1$s</strong> by <em>%2$s</em>"), theme.display("Name"), theme.display("Author")), "</li>")
      print("					</ul>\n				<p>")
      _e("Are you sure you wish to delete these themes?")
      print("</p>\n				<form method="post" action="")
      print(esc_url(_SERVER["REQUEST_URI"]))
      print("" style="display:inline;">\n					<input type="hidden" name="verify-delete" value="1" />\n					<input type="hidden" name="action" value="delete-selected" />\n					")
      for theme in themes:
        print("<input type="hidden" name="checked[]" value=""+esc_attr(theme)+"" />")
      print("					")
      wp_nonce_field("bulk-themes")
      print("					")
      submit_button(_n("Yes, Delete this theme", "Yes, Delete these themes", themes_to_delete), "button", "submit", False)
      print("				</form>\n				<form method="post" action="")
      print(esc_url(wp_get_referer()))
      print("" style="display:inline;">\n					")
      submit_button(__("No, Return me to the theme list"), "button", "submit", False)
      print("				</form>\n\n				<p><a href="#" onclick="jQuery('#files-list').toggle(); return false;">")
      _e("Click to view entire list of files which will be deleted")
      print("</a></p>\n				<div id="files-list" style="display:none;">\n					<ul class="code">\n					")
      for file in files_to_delete:
        print("<li>"+esc_html(str_replace(WP_CONTENT_DIR+"/themes", "", file))+"</li>")
      print("					</ul>\n				</div>\n			</div>\n				")
      require_once(ABSPATH+"wp-admin/admin-footer.php")
      exit(0)
    for theme in themes:
      delete_result = delete_theme(theme, esc_url(add_query_arg({"verify-delete":1, "action":"delete-selected", "checked":_REQUEST["checked"], "_wpnonce":_REQUEST["_wpnonce"]}, network_admin_url("themes.php"))))
    paged = _REQUEST["paged"] if _REQUEST["paged"] else 1
    wp_redirect(add_query_arg({"deleted":count(themes), "paged":paged, "s":s}, network_admin_url("themes.php")))
    exit(0)
wp_list_table.prepare_items()
add_thickbox()
add_screen_option("per_page", {"label":_x("Themes", "themes per page (screen options)")})
get_current_screen()
get_current_screen()
title = __("Themes")
parent_file = "themes.php"
require_once(ABSPATH+"wp-admin/admin-header.php")
print("\n<div class="wrap">\n")
screen_icon("themes")
print("<h2>")
print(esc_html(title))
if current_user_can("install_themes"):
  print(" <a href="theme-install.php" class="add-new-h2">")
  print(esc_html_x("Add New", "theme"))
  print("</a>")
if s:
  printf("<span class="subtitle">"+__("Search results for &#8220;%s&#8221;")+"</span>", esc_html(s))
print("</h2>\n\n")
if isset(_GET["enabled"]):
  _GET["enabled"] = absint(_GET["enabled"])
  print("<div id="message" class="updated"><p>"+sprintf(_n("Theme enabled.", "%s themes enabled.", _GET["enabled"]), number_format_i18n(_GET["enabled"]))+"</p></div>")
elif isset(_GET["disabled"]):
  _GET["disabled"] = absint(_GET["disabled"])
  print("<div id="message" class="updated"><p>"+sprintf(_n("Theme disabled.", "%s themes disabled.", _GET["disabled"]), number_format_i18n(_GET["disabled"]))+"</p></div>")
elif isset(_GET["deleted"]):
  _GET["deleted"] = absint(_GET["deleted"])
  print("<div id="message" class="updated"><p>"+sprintf(_nx("Theme deleted.", "%s themes deleted.", _GET["deleted"], "network"), number_format_i18n(_GET["deleted"]))+"</p></div>")
elif isset(_GET["error"])&&"none"==_GET["error"]:
  print("<div id="message" class="error"><p>"+__("No theme selected.")+"</p></div>")
elif isset(_GET["error"])&&"main"==_GET["error"]:
  print("<div class="error"><p>"+__("You cannot delete a theme while it is active on the main site.")+"</p></div>")
print("\n<form method="get" action="">\n")
wp_list_table.search_box(__("Search Installed Themes"), "theme")
print("</form>\n\n")
wp_list_table.views()
if "broken"==status:
  print("<p class="clear">"+__("The following themes are installed but incomplete. Themes must have a stylesheet and a template.")+"</p>")
print("\n<form method="post" action="">\n<input type="hidden" name="theme_status" value="")
print(esc_attr(status))
print("" />\n<input type="hidden" name="paged" value="")
print(esc_attr(page))
print("" />\n\n")
wp_list_table.display()
print("</form>\n\n</div>\n\n")
include(ABSPATH+"wp-admin/admin-footer.php")
