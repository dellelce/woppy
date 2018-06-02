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
if isset(_REQUEST["action"])&&"update-site"==_REQUEST["action"]:
  check_admin_referer("edit-site")
  switch_to_blog(id)
  if isset(_POST["update_home_url"])&&_POST["update_home_url"]=="update":
    blog_address = get_blogaddress_by_domain(_POST["blog"]["domain"], _POST["blog"]["path"])
    if get_option("siteurl")!=blog_address:
      update_option("siteurl", blog_address)
    if get_option("home")!=blog_address:
      update_option("home", blog_address)
  delete_option("rewrite_rules")
  blog_data = stripslashes_deep(_POST["blog"])
  existing_details = get_blog_details(id, False)
  blog_data_checkboxes = ["public", "archived", "spam", "mature", "deleted"]
  for c in blog_data_checkboxes:
    if !in_array(existing_details.c, [0, 1]):
      blog_data[c] = existing_details.c
    else:
      blog_data[c] = 1 if isset(_POST["blog"][c]) else 0
  update_blog_details(id, blog_data)
  restore_current_blog()
  wp_redirect(add_query_arg({"update":"updated", "id":id}, "site-info.php"))
  exit(0)
if isset(_GET["update"]):
  messages = []
  if "updated"==_GET["update"]:
    messages[] = __("Site info updated.")
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
print("<form method="post" action="site-info.php?action=update-site">\n	")
wp_nonce_field("edit-site")
print("	<input type="hidden" name="id" value="")
print(esc_attr(id))
print("" />\n	<table class="form-table">\n		<tr class="form-field form-required">\n			<th scope="row">")
_e("Domain")
print("</th>\n			")
protocol = "https://" if is_ssl() else "http://"
if is_main_site:
  print("			<td><code>")
  print(protocol)
  print(esc_attr(details.domain))
  print("</code></td>\n			")
else:
  print("			<td>")
  print(protocol)
  print("<input name="blog[domain]" type="text" id="domain" value="")
  print(esc_attr(details.domain))
  print("" size="33" /></td>\n			")
print("		</tr>\n		<tr class="form-field form-required">\n			<th scope="row">")
_e("Path")
print("</th>\n			")
if is_main_site:
  print("			<td><code>")
  print(esc_attr(details.path))
  print("</code></td>\n			")
else:
  switch_to_blog(id)
  print("			<td><input name="blog[path]" type="text" id="path" value="")
  print(esc_attr(details.path))
  print("" size="40" style='margin-bottom:5px;' />\n			<br /><input type="checkbox" style="width:20px;" name="update_home_url" value="update" ")
  if get_option("siteurl")==untrailingslashit(get_blogaddress_by_id(id))||get_option("home")==untrailingslashit(get_blogaddress_by_id(id)):
    print("checked="checked"")
  print(" /> ")
  _e("Update <code>siteurl</code> and <code>home</code> as well.")
  print("</td>\n			")
  restore_current_blog()
print("		</tr>\n		<tr class="form-field">\n			<th scope="row">")
_ex("Registered", "site")
print("</th>\n			<td><input name="blog[registered]" type="text" id="blog_registered" value="")
print(esc_attr(details.registered))
print("" size="40" /></td>\n		</tr>\n		<tr class="form-field">\n			<th scope="row">")
_e("Last Updated")
print("</th>\n			<td><input name="blog[last_updated]" type="text" id="blog_last_updated" value="")
print(esc_attr(details.last_updated))
print("" size="40" /></td>\n		</tr>\n		")
attribute_fields = {"public":__("Public")}
if !is_main_site:
  attribute_fields["archived"] = __("Archived")
  attribute_fields["spam"] = _x("Spam", "site")
  attribute_fields["deleted"] = __("Deleted")
attribute_fields["mature"] = __("Mature")
print("		<tr>\n			<th scope="row">")
_e("Attributes")
print("</th>\n			<td>\n			")
for field_label in attribute_fields:
  print("				<label><input type="checkbox" name="blog[")
  print(field_key)
  print("]" value="1" ")
  checked(details.field_key, True)
  disabled(!in_array(details.field_key, [0, 1]))
  print(" />\n				")
  print(field_label)
  print("</label><br/>\n			")
print("			</td>\n		</tr>\n	</table>\n	")
submit_button()
print("</form>\n\n</div>\n")
require("../admin-footer.php")
