#!/usr/bin/python
#-*- coding: utf-8 -*-
if !defined("IFRAME_REQUEST")&&isset(_GET["tab"])&&"plugin-information"==_GET["tab"]:
  define("IFRAME_REQUEST", True)
require_once("./admin.php")
if !current_user_can("install_plugins"):
  wp_die(__("You do not have sufficient permissions to install plugins on this site."))
if is_multisite()&&!is_network_admin():
  wp_redirect(network_admin_url("plugin-install.php"))
  exit(0)
wp_list_table = _get_list_table("WP_Plugin_Install_List_Table")
pagenum = wp_list_table.get_pagenum()
wp_list_table.prepare_items()
title = __("Install Plugins")
parent_file = "plugins.php"
wp_enqueue_script("plugin-install")
if "plugin-information"!=tab:
  add_thickbox()
body_id = tab
do_action("install_plugins_pre_"+tab)
get_current_screen()
get_current_screen()
get_current_screen()
include(ABSPATH+"wp-admin/admin-header.php")
print("<div class="wrap">\n")
screen_icon("plugins")
print("<h2>")
print(esc_html(title))
print("</h2>\n\n")
wp_list_table.views()
print("\n<br class="clear" />\n")
do_action("install_plugins_"+tab, paged)
print("</div>\n")
include(ABSPATH+"wp-admin/admin-footer.php")
