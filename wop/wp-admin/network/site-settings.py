#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if !is_multisite():
  wp_die(__("Multisite support is not enabled."))
if !current_user_can("manage_sites"):
  wp_die(__("You do not have sufficient permissions to edit this site."))
get_current_screen()
get_current_screen()
id = intval(_REQUEST["id"]) if isset(_REQUEST["id"]) else 0
if !id:
  wp_die(__("Invalid site ID."))
details = get_blog_details(id)
if !can_edit_network(details.site_id):
  wp_die(__("You do not have permission to access this page."))
is_main_site = is_main_site(id)
if isset(_REQUEST["action"])&&"update-site"==_REQUEST["action"]&&is_array(_POST["option"]):
  check_admin_referer("edit-site")
  switch_to_blog(id)
  c = 1
  count = count(_POST["option"])
  skip_options = ["allowedthemes"]
  for val in _POST["option"]:
    if key===0||is_array(val)||in_array(key, skip_options):
    if c==count:
      update_option(key, stripslashes(val))
    else:
      update_option(key, stripslashes(val), False)
    c+=1
  do_action("wpmu_update_blog_options")
  restore_current_blog()
  wp_redirect(add_query_arg({"update":"updated", "id":id}, "site-settings.php"))
  exit(0)
if isset(_GET["update"]):
  messages = []
  if "updated"==_GET["update"]:
    messages[] = __("Site options updated.")
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
print("</h3>\n")
if !empty(messages):
  for msg in messages:
    print("<div id="message" class="updated"><p>"+msg+"</p></div>")
print("<form method="post" action="site-settings.php?action=update-site">\n	")
wp_nonce_field("edit-site")
print("	<input type="hidden" name="id" value="")
print(esc_attr(id))
print("" />\n	<table class="form-table">\n		")
blog_prefix = wpdb.get_blog_prefix(id)
options = wpdb.get_results("SELECT * FROM "+blog_prefix+"options WHERE option_name NOT LIKE '\_%' AND option_name NOT LIKE '%user_roles'")
for option in options:
  if option.option_name=="default_role":
    editblog_default_role = option.option_value
  disabled = False
  class = "all-options"
  if is_serialized(option.option_value):
    if is_serialized_string(option.option_value):
      option.option_value = esc_html(maybe_unserialize(option.option_value), "single")
    else:
      option.option_value = "SERIALIZED DATA"
      disabled = True
      class = "all-options disabled"
  if strpos(option.option_value, "\n")!==False:
    print("				<tr class="form-field">\n					<th scope="row">")
    print(ucwords(str_replace("_", " ", option.option_name)))
    print("</th>\n					<td><textarea class="")
    print(class)
    print("" rows="5" cols="40" name="option[")
    print(esc_attr(option.option_name))
    print("]" id="")
    print(esc_attr(option.option_name))
    print(""")
    disabled(disabled)
    print(">")
    print(esc_textarea(option.option_value))
    print("</textarea></td>\n				</tr>\n			")
  else:
    print("				<tr class="form-field">\n					<th scope="row">")
    print(esc_html(ucwords(str_replace("_", " ", option.option_name))))
    print("</th>\n					")
    if is_main_site&&in_array(option.option_name, ["siteurl", "home"]):
      print("					<td><code>")
      print(esc_html(option.option_value))
      print("</code></td>\n					")
    else:
      print("					<td><input class="")
      print(class)
      print("" name="option[")
      print(esc_attr(option.option_name))
      print("]" type="text" id="")
      print(esc_attr(option.option_name))
      print("" value="")
      print(esc_attr(option.option_value))
      print("" size="40" ")
      disabled(disabled)
      print(" /></td>\n					")
    print("				</tr>\n			")
do_action("wpmueditblogaction", id)
print("	</table>\n	")
submit_button()
print("</form>\n\n</div>\n")
require("../admin-footer.php")
