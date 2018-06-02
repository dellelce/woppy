#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if !is_multisite():
  wp_die(__("Multisite support is not enabled."))
if !current_user_can("manage_sites"):
  wp_die(__("You do not have sufficient permissions to add sites to this network."))
get_current_screen()
get_current_screen()
if isset(_REQUEST["action"])&&"add-site"==_REQUEST["action"]:
  check_admin_referer("add-blog", "_wpnonce_add-blog")
  if !current_user_can("manage_sites"):
    wp_die(__("You do not have permission to access this page."))
  if !is_array(_POST["blog"]):
    wp_die(__("Can&#8217;t create an empty site."))
  blog = _POST["blog"]
  domain = ""
  if preg_match("|^([a-zA-Z0-9-])+$|", blog["domain"]):
    domain = strtolower(blog["domain"])
  if !is_subdomain_install():
    subdirectory_reserved_names = apply_filters("subdirectory_reserved_names", ["page", "comments", "blog", "files", "feed"])
    if in_array(domain, subdirectory_reserved_names):
      wp_die(sprintf(__("The following words are reserved for use by WordPress functions and cannot be used as blog names: <code>%s</code>"), implode("</code>, <code>", subdirectory_reserved_names)))
  email = sanitize_email(blog["email"])
  title = blog["title"]
  if empty(domain):
    wp_die(__("Missing or invalid site address."))
  if empty(email):
    wp_die(__("Missing email address."))
  if !is_email(email):
    wp_die(__("Invalid email address."))
  if is_subdomain_install():
    newdomain = domain+"."+preg_replace("|^www\.|", "", current_site.domain)
    path = current_site.path
  else:
    newdomain = current_site.domain
    path = current_site.path+domain+"/"
  password = "N/A"
  user_id = email_exists(email)
  if !user_id:
    password = wp_generate_password(12, False)
    user_id = wpmu_create_user(domain, password, email)
    if False==user_id:
      wp_die(__("There was an error creating the user."))
    else:
      wp_new_user_notification(user_id, password)
  wpdb.hide_errors()
  id = wpmu_create_blog(newdomain, path, title, user_id, {"public":1}, current_site.id)
  wpdb.show_errors()
  if !is_wp_error(id):
    if !is_super_admin(user_id)&&!get_user_option("primary_blog", user_id):
      update_user_option(user_id, "primary_blog", id, True)
    content_mail = sprintf(__("New site created by %1$s\n\nAddress: %2$s\nName: %3$s"), current_user.user_login, get_site_url(id), stripslashes(title))
    wp_mail(get_site_option("admin_email"), sprintf(__("[%s] New Site Created"), current_site.site_name), content_mail, "From: "Site Admin" <"+get_site_option("admin_email")+">")
    wpmu_welcome_notification(id, user_id, password, title, {"public":1})
    wp_redirect(add_query_arg({"update":"added", "id":id}, "site-new.php"))
    exit(0)
  else:
    wp_die(id.get_error_message())
if isset(_GET["update"]):
  messages = []
  if "added"==_GET["update"]:
    messages[] = sprintf(__("Site added. <a href="%1$s">Visit Dashboard</a> or <a href="%2$s">Edit Site</a>"), esc_url(get_admin_url(absint(_GET["id"]))), network_admin_url("site-info.php?id="+absint(_GET["id"])))
title = __("Add New Site")
parent_file = "sites.php"
require("../admin-header.php")
print("\n<div class="wrap">\n")
screen_icon("ms-admin")
print("<h2 id="add-new-site">")
_e("Add New Site")
print("</h2>\n")
if !empty(messages):
  for msg in messages:
    print("<div id="message" class="updated"><p>"+msg+"</p></div>")
print("<form method="post" action="")
print(network_admin_url("site-new.php?action=add-site"))
print("">\n")
wp_nonce_field("add-blog", "_wpnonce_add-blog")
print("	<table class="form-table">\n		<tr class="form-field form-required">\n			<th scope="row">")
_e("Site Address")
print("</th>\n			<td>\n			")
if is_subdomain_install():
  print("				<input name="blog[domain]" type="text" class="regular-text" title="")
  esc_attr_e("Domain")
  print(""/><span class="no-break">.")
  print(preg_replace("|^www\.|", "", current_site.domain))
  print("</span>\n			")
else:
  print(current_site.domain+current_site.path)
  print("<input name="blog[domain]" class="regular-text" type="text" title="")
  esc_attr_e("Domain")
  print(""/>\n			")
print("<p>"+__("Only lowercase letters (a-z) and numbers are allowed.")+"</p>")
print("			</td>\n		</tr>\n		<tr class="form-field form-required">\n			<th scope="row">")
_e("Site Title")
print("</th>\n			<td><input name="blog[title]" type="text" class="regular-text" title="")
esc_attr_e("Title")
print(""/></td>\n		</tr>\n		<tr class="form-field form-required">\n			<th scope="row">")
_e("Admin Email")
print("</th>\n			<td><input name="blog[email]" type="text" class="regular-text" title="")
esc_attr_e("Email")
print(""/></td>\n		</tr>\n		<tr class="form-field">\n			<td colspan="2">")
_e("A new user will be created if the above email address is not in the database.")
print("<br />")
_e("The username and password will be mailed to this email address.")
print("</td>\n		</tr>\n	</table>\n	")
submit_button(__("Add Site"), "primary", "add-site")
print("	</form>\n</div>\n")
require("../admin-footer.php")
