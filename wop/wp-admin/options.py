#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
title = __("Settings")
self_file = "options.php"
parent_file = "options-general.php"
wp_reset_vars(["action", "option_page"])
capability = "manage_options"
if empty(option_page):
  option_page = "options"
else:
  capability = apply_filters("option_page_capability_"+option_page+"", capability)
if !current_user_can(capability):
  wp_die(__("Cheatin&#8217; uh?"))
if is_multisite():
  if !empty(_GET["adminhash"]):
    new_admin_details = get_option("adminhash")
    redirect = "options-general.php?updated=false"
    if is_array(new_admin_details)&&new_admin_details["hash"]==_GET["adminhash"]&&!empty(new_admin_details["newemail"]):
      update_option("admin_email", new_admin_details["newemail"])
      delete_option("adminhash")
      delete_option("new_admin_email")
      redirect = "options-general.php?updated=true"
    wp_redirect(admin_url(redirect))
    exit(0)
  elif !empty(_GET["dismiss"])&&"new_admin_email"==_GET["dismiss"]:
    delete_option("adminhash")
    delete_option("new_admin_email")
    wp_redirect(admin_url("options-general.php?updated=true"))
    exit(0)
if is_multisite()&&!is_super_admin()&&"update"!=action:
  wp_die(__("Cheatin&#8217; uh?"))
whitelist_options = {"general":["blogname", "blogdescription", "gmt_offset", "date_format", "time_format", "start_of_week", "timezone_string"], "discussion":["default_pingback_flag", "default_ping_status", "default_comment_status", "comments_notify", "moderation_notify", "comment_moderation", "require_name_email", "comment_whitelist", "comment_max_links", "moderation_keys", "blacklist_keys", "show_avatars", "avatar_rating", "avatar_default", "close_comments_for_old_posts", "close_comments_days_old", "thread_comments", "thread_comments_depth", "page_comments", "comments_per_page", "default_comments_page", "comment_order", "comment_registration"], "media":["thumbnail_size_w", "thumbnail_size_h", "thumbnail_crop", "medium_size_w", "medium_size_h", "large_size_w", "large_size_h", "image_default_size", "image_default_align", "image_default_link_type"], "reading":["posts_per_page", "posts_per_rss", "rss_use_excerpt", "show_on_front", "page_on_front", "page_for_posts", "blog_public"], "writing":["use_smilies", "default_category", "default_email_category", "use_balanceTags", "default_link_category", "default_post_format"]}
whitelist_options["misc"] = whitelist_options["options"] = whitelist_options["privacy"] = []
mail_options = ["mailserver_url", "mailserver_port", "mailserver_login", "mailserver_pass"]
if !in_array(get_option("blog_charset"), ["utf8", "utf-8", "UTF8", "UTF-8"]):
  whitelist_options["reading"][] = "blog_charset"
if !is_multisite():
  if !defined("WP_SITEURL"):
    whitelist_options["general"][] = "siteurl"
  if !defined("WP_HOME"):
    whitelist_options["general"][] = "home"
  whitelist_options["general"][] = "admin_email"
  whitelist_options["general"][] = "users_can_register"
  whitelist_options["general"][] = "default_role"
  whitelist_options["writing"] = array_merge(whitelist_options["writing"], mail_options)
  whitelist_options["writing"][] = "ping_sites"
  whitelist_options["media"][] = "uploads_use_yearmonth_folders"
  if get_option("upload_url_path")||get_option("upload_path")!="wp-content/uploads"&&get_option("upload_path"):
    whitelist_options["media"][] = "upload_path"
    whitelist_options["media"][] = "upload_url_path"
else:
  whitelist_options["general"][] = "new_admin_email"
  whitelist_options["general"][] = "WPLANG"
  if apply_filters("enable_post_by_email_configuration", True):
    whitelist_options["writing"] = array_merge(whitelist_options["writing"], mail_options)
whitelist_options = apply_filters("whitelist_options", whitelist_options)
if "update"==action:
  if "options"==option_page&&!isset(_POST["option_page"]):
    unregistered = True
    check_admin_referer("update-options")
  else:
    unregistered = False
    check_admin_referer(option_page+"-options")
  if !isset(whitelist_options[option_page]):
    wp_die(__("<strong>ERROR</strong>: options page not found."))
  if "options"==option_page:
    if is_multisite()&&!is_super_admin():
      wp_die(__("You do not have sufficient permissions to modify unregistered settings for this site."))
    options = explode(",", stripslashes(_POST["page_options"]))
  else:
    options = whitelist_options[option_page]
  if "general"==option_page:
    if !empty(_POST["date_format"])&&isset(_POST["date_format_custom"])&&"\c\u\s\t\o\m"==stripslashes(_POST["date_format"]):
      _POST["date_format"] = _POST["date_format_custom"]
    if !empty(_POST["time_format"])&&isset(_POST["time_format_custom"])&&"\c\u\s\t\o\m"==stripslashes(_POST["time_format"]):
      _POST["time_format"] = _POST["time_format_custom"]
    if !empty(_POST["timezone_string"])&&preg_match("/^UTC[+-]/", _POST["timezone_string"]):
      _POST["gmt_offset"] = _POST["timezone_string"]
      _POST["gmt_offset"] = preg_replace("/UTC\+?/", "", _POST["gmt_offset"])
      _POST["timezone_string"] = ""
  if options:
    for option in options:
      if unregistered:
        _deprecated_argument("options.php", "2.7", sprintf(__("The <code>%1$s</code> setting is unregistered. Unregistered settings are deprecated. See http://codex.wordpress.org/Settings_API"), option, option_page))
      option = trim(option)
      value = 
      if isset(_POST[option]):
        value = _POST[option]
        if !is_array(value):
          value = trim(value)
        value = stripslashes_deep(value)
      update_option(option, value)
  if !count(get_settings_errors()):
    add_settings_error("general", "settings_updated", __("Settings saved."), "updated")
  set_transient("settings_errors", get_settings_errors(), 30)
  goback = add_query_arg("settings-updated", "true", wp_get_referer())
  wp_redirect(goback)
  exit(0)
include("./admin-header.php")
print("\n<div class="wrap">\n")
screen_icon()
print("  <h2>")
esc_html_e("All Settings")
print("</h2>\n  <form name="form" action="options.php" method="post" id="all-options">\n  ")
wp_nonce_field("options-options")
print("  <input type="hidden" name="action" value="update" />\n  <input type='hidden' name='option_page' value='options' />\n  <table class="form-table">\n")
options = wpdb.get_results("SELECT * FROM "+wpdb.options+" ORDER BY option_name")
for option in options:
  disabled = False
  if option.option_name=="":
  if is_serialized(option.option_value):
    if is_serialized_string(option.option_value):
      value = maybe_unserialize(option.option_value)
      options_to_update[] = option.option_name
      class = "all-options"
    else:
      value = "SERIALIZED DATA"
      disabled = True
      class = "all-options disabled"
  else:
    value = option.option_value
    options_to_update[] = option.option_name
    class = "all-options"
  name = esc_attr(option.option_name)
  print("\n<tr>\n	<th scope='row'><label for='"+name+"'>"+esc_html(option.option_name)+"</label></th>\n<td>")
  if strpos(value, "\n")!==False:
    print("<textarea class='"+class+"' name='"+name+"' id='"+name+"' cols='30' rows='5'>"+esc_textarea(value)+"</textarea>")
  else:
    print("<input class='regular-text "+class+"' type='text' name='"+name+"' id='"+name+"' value='"+esc_attr(value)+"'"+disabled(disabled, True, False)+" />")
  print("</td>\n</tr>")
print("  </table>\n\n<input type="hidden" name="page_options" value="")
print(esc_attr(implode(",", options_to_update)))
print("" />\n\n")
submit_button(__("Save Changes"), "primary", "Update")
print("\n  </form>\n</div>\n\n")
include("./admin-footer.php")
