#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if !is_multisite():
  wp_die(__("Multisite support is not enabled."))
if !current_user_can("create_users"):
  wp_die(__("You do not have sufficient permissions to add users to this network."))
get_current_screen()
get_current_screen()
if isset(_REQUEST["action"])&&"add-user"==_REQUEST["action"]:
  check_admin_referer("add-user", "_wpnonce_add-user")
  if !current_user_can("manage_network_users"):
    wp_die(__("You do not have permission to access this page."))
  if !is_array(_POST["user"]):
    wp_die(__("Cannot create an empty user."))
  user = _POST["user"]
  user_details = wpmu_validate_user_signup(user["username"], user["email"])
  if is_wp_error(user_details["errors"])&&!empty(user_details["errors"].errors):
    add_user_errors = user_details["errors"]
  else:
    password = wp_generate_password(12, False)
    user_id = wpmu_create_user(esc_html(strtolower(user["username"])), password, esc_html(user["email"]))
    if !user_id:
      add_user_errors = WP_Error("add_user_fail", __("Cannot add user."))
    else:
      wp_new_user_notification(user_id, password)
      wp_redirect(add_query_arg({"update":"added"}, "user-new.php"))
      exit(0)
if isset(_GET["update"]):
  messages = []
  if "added"==_GET["update"]:
    messages[] = __("User added.")
title = __("Add New User")
parent_file = "users.php"
require("../admin-header.php")
print("\n<div class="wrap">\n")
screen_icon()
print("<h2 id="add-new-user">")
_e("Add New User")
print("</h2>\n")
if !empty(messages):
  for msg in messages:
    print("<div id="message" class="updated"><p>"+msg+"</p></div>")
if isset(add_user_errors)&&is_wp_error(add_user_errors):
  print("	<div class="error">\n		")
  for message in add_user_errors:
    print("<p>"+message+"</p>")
  print("	</div>\n")
print("	<form action="")
print(network_admin_url("user-new.php?action=add-user"))
print("" id="adduser" method="post">\n	<table class="form-table">\n		<tr class="form-field form-required">\n			<th scope="row">")
_e("Username")
print("</th>\n			<td><input type="text" class="regular-text" name="user[username]" /></td>\n		</tr>\n		<tr class="form-field form-required">\n			<th scope="row">")
_e("Email")
print("</th>\n			<td><input type="text" class="regular-text" name="user[email]" /></td>\n		</tr>\n		<tr class="form-field">\n			<td colspan="2">")
_e("Username and password will be mailed to the above email address.")
print("</td>\n		</tr>\n	</table>\n	")
wp_nonce_field("add-user", "_wpnonce_add-user")
print("	")
submit_button(__("Add User"), "primary", "add-user")
print("	</form>\n</div>\n")
require("../admin-footer.php")
