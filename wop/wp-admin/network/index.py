#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
require_once(ABSPATH+"wp-admin/includes/dashboard.php")
if !is_multisite():
  wp_die(__("Multisite support is not enabled."))
if !current_user_can("manage_network"):
  wp_die(__("You do not have permission to access this page."))
title = __("Dashboard")
parent_file = "index.php"
get_current_screen()
get_current_screen()
wp_dashboard_setup()
wp_enqueue_script("dashboard")
wp_enqueue_script("plugin-install")
add_thickbox()
add_screen_option("layout_columns", {"max":4, "default":2})
require_once("../admin-header.php")
print("\n<div class="wrap">\n")
screen_icon()
print("<h2>")
print(esc_html(title))
print("</h2>\n\n<div id="dashboard-widgets-wrap">\n\n")
wp_dashboard()
print("\n<div class="clear"></div>\n</div><!-- dashboard-widgets-wrap -->\n\n</div><!-- wrap -->\n\n")
include("../admin-footer.php")
