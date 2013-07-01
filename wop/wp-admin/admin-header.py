#!/usr/bin/python
#-*- coding: utf-8 -*-
header("Content-Type: "+get_option("html_type")+"; charset="+get_option("blog_charset"))
if !defined("WP_ADMIN"):
  require_once("./admin.php")
titlehook_suffixcurrent_screenwp_localepagenowwp_versioncurrent_siteupdate_titletotal_update_countparent_fileif empty(current_screen):
  set_current_screen()
get_admin_page_title()
title = esc_html(strip_tags(title))
if is_network_admin():
  admin_title = __("Network Admin")
elif is_user_admin():
  admin_title = __("Global Dashboard")
else:
  admin_title = get_bloginfo("name")
if admin_title==title:
  admin_title = sprintf(__("%1$s &#8212; WordPress"), title)
else:
  admin_title = sprintf(__("%1$s &lsaquo; %2$s &#8212; WordPress"), title, admin_title)
admin_title = apply_filters("admin_title", admin_title, title)
wp_user_settings()
_wp_admin_html_begin()
print("<title>")
print(admin_title)
print("</title>\n")
wp_enqueue_style("colors")
wp_enqueue_style("ie")
wp_enqueue_script("utils")
admin_body_class = preg_replace("/[^a-z0-9_-]+/i", "-", hook_suffix)
print("<script type="text/javascript">\naddLoadEvent = function(func){if(typeof jQuery!="undefined")jQuery(document).ready(func);else if(typeof wpOnload!='function'){wpOnload=func;}else{var oldonload=wpOnload;wpOnload=function(){oldonload();func();}}};\nvar ajaxurl = '")
print(admin_url("admin-ajax.php", "relative"))
print("',\n	pagenow = '")
print(current_screen.id)
print("',\n	typenow = '")
print(current_screen.post_type)
print("',\n	adminpage = '")
print(admin_body_class)
print("',\n	thousandsSeparator = '")
print(addslashes(wp_locale.number_format["thousands_sep"]))
print("',\n	decimalPoint = '")
print(addslashes(wp_locale.number_format["decimal_point"]))
print("',\n	isRtl = ")
print(is_rtl())
print(";\n</script>\n")
do_action("admin_enqueue_scripts", hook_suffix)
do_action("admin_print_styles-"+hook_suffix+"")
do_action("admin_print_styles")
do_action("admin_print_scripts-"+hook_suffix+"")
do_action("admin_print_scripts")
do_action("admin_head-"+hook_suffix+"")
do_action("admin_head")
if get_user_setting("mfold")=="f":
  admin_body_class+=" folded"
if !get_user_setting("unfold"):
  admin_body_class+=" auto-fold"
if is_admin_bar_showing():
  admin_body_class+=" admin-bar"
if is_rtl():
  admin_body_class+=" rtl"
admin_body_class+=" branch-"+str_replace([".", ","], "-", floatval(wp_version))
admin_body_class+=" version-"+str_replace(".", "-", preg_replace("/^([.0-9]+).*/", "$1", wp_version))
admin_body_class+=" admin-color-"+sanitize_html_class(get_user_option("admin_color"), "fresh")
admin_body_class+=" locale-"+sanitize_html_class(strtolower(str_replace("_", "-", get_locale())))
if wp_is_mobile():
  admin_body_class+=" mobile"
admin_body_class+=" no-customize-support"
print("</head>\n<body class="wp-admin wp-core-ui no-js ")
print(apply_filters("admin_body_class", "")+" "+admin_body_class+"")
print("">\n<script type="text/javascript">\n	document.body.className = document.body.className.replace('no-js','js');\n</script>\n\n")
if wp_script_is("customize-loader", "queue")&&current_user_can("edit_theme_options"):
  wp_customize_support_script()
print("\n<div id="wpwrap">\n<a tabindex="1" href="#wpbody-content" class="screen-reader-shortcut">")
_e("Skip to main content")
print("</a>\n")
require(ABSPATH+"wp-admin/menu-header.php")
print("<div id="wpcontent">\n\n")
do_action("in_admin_header")
print("\n<div id="wpbody">\n")
unset(title_class, blog_name, total_update_count, update_title)
current_screen.set_parentage(parent_file)
print("\n<div id="wpbody-content" aria-label="")
esc_attr_e("Main content")
print("" tabindex="0">\n")
current_screen.render_screen_meta()
if is_network_admin():
  do_action("network_admin_notices")
elif is_user_admin():
  do_action("user_admin_notices")
else:
  do_action("admin_notices")
do_action("all_admin_notices")
if parent_file=="options-general.php":
  require(ABSPATH+"wp-admin/options-head.php")
