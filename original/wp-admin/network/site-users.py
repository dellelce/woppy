#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if !is_multisite():
  wp_die(__("Multisite support is not enabled."))
if !current_user_can("manage_sites"):
  wp_die(__("You do not have sufficient permissions to edit this site."))
wp_list_table = _get_list_table("WP_Users_List_Table")
wp_list_table.prepare_items()
get_current_screen()
get_current_screen()
_SERVER["REQUEST_URI"] = remove_query_arg("update", _SERVER["REQUEST_URI"])
referer = remove_query_arg("update", wp_get_referer())
id = intval(_REQUEST["id"]) if isset(_REQUEST["id"]) else 0
if !id:
  wp_die(__("Invalid site ID."))
details = get_blog_details(id)
if !can_edit_network(details.site_id):
  wp_die(__("You do not have permission to access this page."))
is_main_site = is_main_site(id)
switch_to_blog(id)
editblog_roles = wp_roles.roles
default_role = get_option("default_role")
action = wp_list_table.current_action()
if action:
  if action=="newuser":
    check_admin_referer("add-user", "_wpnonce_add-new-user")
    user = _POST["user"]
    if !is_array(_POST["user"])||empty(user["username"])||empty(user["email"]):
      update = "err_new"
    else:
      password = wp_generate_password(12, False)
      user_id = wpmu_create_user(esc_html(strtolower(user["username"])), password, esc_html(user["email"]))
      if False==user_id:
        update = "err_new_dup"
      else:
        wp_new_user_notification(user_id, password)
        add_user_to_blog(id, user_id, _POST["new_role"])
        update = "newuser"
  elif action=="adduser":
    check_admin_referer("add-user", "_wpnonce_add-user")
    if !empty(_POST["newuser"]):
      update = "adduser"
      newuser = _POST["newuser"]
      userid = wpdb.get_var(wpdb.prepare("SELECT ID FROM "+wpdb.users+" WHERE user_login = %s", newuser))
      if userid:
        blog_prefix = wpdb.get_blog_prefix(id)
        user = wpdb.get_var("SELECT user_id FROM "+wpdb.usermeta+" WHERE user_id='"+userid+"' AND meta_key='"+blog_prefix+"capabilities'")
        if user==False:
          add_user_to_blog(id, userid, _POST["new_role"])
        else:
          update = "err_add_member"
      else:
        update = "err_add_notfound"
    else:
      update = "err_add_notfound"
  elif action=="remove":
    if !current_user_can("remove_users"):
      die(__("You can&#8217;t remove users."))
    check_admin_referer("bulk-users")
    update = "remove"
    if isset(_REQUEST["users"]):
      userids = _REQUEST["users"]
      for user_id in userids:
        user_id = user_id
        remove_user_from_blog(user_id, id)
    elif isset(_GET["user"]):
      remove_user_from_blog(_GET["user"])
    else:
      update = "err_remove"
  elif action=="promote":
    check_admin_referer("bulk-users")
    editable_roles = get_editable_roles()
    if empty(editable_roles[_REQUEST["new_role"]]):
      wp_die(__("You can&#8217;t give users that role."))
    if isset(_REQUEST["users"]):
      userids = _REQUEST["users"]
      update = "promote"
      for user_id in userids:
        user_id = user_id
        if !is_user_member_of_blog(user_id):
          wp_die(__("Cheatin&#8217; uh?"))
        user = get_userdata(user_id)
        user.set_role(_REQUEST["new_role"])
    else:
      update = "err_promote"
  wp_safe_redirect(add_query_arg("update", update, referer))
  exit(0)
restore_current_blog()
if isset(_GET["action"])&&"update-site"==_GET["action"]:
  wp_safe_redirect(referer)
  exit(0)
add_screen_option("per_page", {"label":_x("Users", "users per page (screen options)")})
site_url_no_http = preg_replace("#^http(s)?://#", "", get_blogaddress_by_id(id))
title_site_url_linked = sprintf(__("Edit Site: <a href="%1$s">%2$s</a>"), get_blogaddress_by_id(id), site_url_no_http)
title = sprintf(__("Edit Site: %s"), site_url_no_http)
parent_file = "sites.php"
submenu_file = "sites.php"
if !wp_is_large_network("users")&&apply_filters("show_network_site_users_add_existing_form", True):
  wp_enqueue_script("user-suggest")
require("../admin-header.php")
print("\n<script type='text/javascript'>\n/* <![CDATA[ */\nvar current_site_id = ")
print(id)
print(";\n/* ]]> */\n</script>\n\n\n<div class="wrap">\n")
screen_icon("ms-admin")
print("<h2 id="edit-site">")
print(title_site_url_linked)
print("</h2>\n<h3 class="nav-tab-wrapper">\n")
tabs = {"site-info":{"label":__("Info"), "url":"site-info.php"}, "site-users":{"label":__("Users"), "url":"site-users.php"}, "site-themes":{"label":__("Themes"), "url":"site-themes.php"}, "site-settings":{"label":__("Settings"), "url":"site-settings.php"}}
for tab in tabs:
  class = " nav-tab-active" if tab["url"]==pagenow else ""
  print("<a href=""+tab["url"]+"?id="+id+"" class="nav-tab"+class+"">"+esc_html(tab["label"])+"</a>")
print("</h3>")
if isset(_GET["update"]):
  if _GET["update"]=="adduser":
    print("<div id="message" class="updated"><p>"+__("User added.")+"</p></div>")
  elif _GET["update"]=="err_add_member":
    print("<div id="message" class="error"><p>"+__("User is already a member of this site.")+"</p></div>")
  elif _GET["update"]=="err_add_notfound":
    print("<div id="message" class="error"><p>"+__("Enter the username of an existing user.")+"</p></div>")
  elif _GET["update"]=="promote":
    print("<div id="message" class="updated"><p>"+__("Changed roles.")+"</p></div>")
  elif _GET["update"]=="err_promote":
    print("<div id="message" class="error"><p>"+__("Select a user to change role.")+"</p></div>")
  elif _GET["update"]=="remove":
    print("<div id="message" class="updated"><p>"+__("User removed from this site.")+"</p></div>")
  elif _GET["update"]=="err_remove":
    print("<div id="message" class="error"><p>"+__("Select a user to remove.")+"</p></div>")
  elif _GET["update"]=="newuser":
    print("<div id="message" class="updated"><p>"+__("User created.")+"</p></div>")
  elif _GET["update"]=="err_new":
    print("<div id="message" class="error"><p>"+__("Enter the username and email.")+"</p></div>")
  elif _GET["update"]=="err_new_dup":
    print("<div id="message" class="error"><p>"+__("Duplicated username or email address.")+"</p></div>")
print("\n<form class="search-form" action="" method="get">\n")
wp_list_table.search_box(__("Search Users"), "user")
print("<input type="hidden" name="id" value="")
print(esc_attr(id))
print("" />\n</form>\n\n")
wp_list_table.views()
print("\n<form method="post" action="site-users.php?action=update-site">\n	<input type="hidden" name="id" value="")
print(esc_attr(id))
print("" />\n\n")
wp_list_table.display()
print("\n</form>\n\n")
do_action("network_site_users_after_list_table", "")
print("\n")
if current_user_can("promote_users")&&apply_filters("show_network_site_users_add_existing_form", True):
  print("<h3 id="add-existing-user">")
  _e("Add Existing User")
  print("</h3>\n<form action="site-users.php?action=adduser" id="adduser" method="post">\n	<input type="hidden" name="id" value="")
  print(esc_attr(id))
  print("" />\n	<table class="form-table">\n		<tr>\n			<th scope="row">")
  _e("Username")
  print("</th>\n			<td><input type="text" class="regular-text wp-suggest-user" name="newuser" id="newuser" /></td>\n		</tr>\n		<tr>\n			<th scope="row">")
  _e("Role")
  print("</th>\n			<td><select name="new_role" id="new_role_0">\n			")
  reset(editblog_roles)
  for role_assoc in editblog_roles:
    name = translate_user_role(role_assoc["name"])
    print("<option "+selected(default_role, role, False)+" value=""+esc_attr(role)+"">"+esc_html(name)+"</option>")
  print("			</select></td>\n		</tr>\n	</table>\n	")
  wp_nonce_field("add-user", "_wpnonce_add-user")
  print("	")
  submit_button(__("Add User"), "primary", "add-user", True, {"id":"submit-add-existing-user"})
  print("</form>\n")
print("\n")
if current_user_can("create_users")&&apply_filters("show_network_site_users_add_new_form", True):
  print("<h3 id="add-new-user">")
  _e("Add New User")
  print("</h3>\n<form action="")
  print(network_admin_url("site-users.php?action=newuser"))
  print("" id="newuser" method="post">\n	<input type="hidden" name="id" value="")
  print(esc_attr(id))
  print("" />\n	<table class="form-table">\n		<tr>\n			<th scope="row">")
  _e("Username")
  print("</th>\n			<td><input type="text" class="regular-text" name="user[username]" /></td>\n		</tr>\n		<tr>\n			<th scope="row">")
  _e("Email")
  print("</th>\n			<td><input type="text" class="regular-text" name="user[email]" /></td>\n		</tr>\n		<tr>\n			<th scope="row">")
  _e("Role")
  print("</th>\n			<td><select name="new_role" id="new_role_0">\n			")
  reset(editblog_roles)
  for role_assoc in editblog_roles:
    name = translate_user_role(role_assoc["name"])
    print("<option "+selected(default_role, role, False)+" value=""+esc_attr(role)+"">"+esc_html(name)+"</option>")
  print("			</select></td>\n		</tr>\n		<tr class="form-field">\n			<td colspan="2">")
  _e("Username and password will be mailed to the above email address.")
  print("</td>\n		</tr>\n	</table>\n	")
  wp_nonce_field("add-user", "_wpnonce_add-new-user")
  print("	")
  submit_button(__("Add New User"), "primary", "add-user", True, {"id":"submit-add-user"})
  print("</form>\n")
print("</div>\n")
require("../admin-footer.php")
