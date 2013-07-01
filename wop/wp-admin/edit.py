#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if !typenow:
  wp_die(__("Invalid post type"))
post_type = typenow
post_type_object = get_post_type_object(post_type)
if !post_type_object:
  wp_die(__("Invalid post type"))
if !current_user_can(post_type_object.cap.edit_posts):
  wp_die(__("Cheatin&#8217; uh?"))
wp_list_table = _get_list_table("WP_Posts_List_Table")
pagenum = wp_list_table.get_pagenum()
for _REQUEST[_redirect] in :
  if !empty(_REQUEST[_redirect]):
    wp_redirect(admin_url("edit-comments.php?p="+absint(_REQUEST[_redirect])))
    exit(0)
unset(_redirect)
if "post"!=post_type:
  parent_file = "edit.php?post_type="+post_type+""
  submenu_file = "edit.php?post_type="+post_type+""
  post_new_file = "post-new.php?post_type="+post_type+""
else:
  parent_file = "edit.php"
  submenu_file = "edit.php"
  post_new_file = "post-new.php"
doaction = wp_list_table.current_action()
if doaction:
  check_admin_referer("bulk-posts")
  sendback = remove_query_arg(["trashed", "untrashed", "deleted", "ids"], wp_get_referer())
  if !sendback:
    sendback = admin_url(parent_file)
  sendback = add_query_arg("paged", pagenum, sendback)
  if strpos(sendback, "post.php")!==False:
    sendback = admin_url(post_new_file)
  if "delete_all"==doaction:
    post_status = preg_replace("/[^a-z0-9_-]+/i", "", _REQUEST["post_status"])
    if get_post_status_object(post_status):
      post_ids = wpdb.get_col(wpdb.prepare("SELECT ID FROM "+wpdb.posts+" WHERE post_type=%s AND post_status = %s", post_type, post_status))
    doaction = "delete"
  elif isset(_REQUEST["media"]):
    post_ids = _REQUEST["media"]
  elif isset(_REQUEST["ids"]):
    post_ids = explode(",", _REQUEST["ids"])
  elif !empty(_REQUEST["post"]):
    post_ids = array_map("intval", _REQUEST["post"])
  if !isset(post_ids):
    wp_redirect(sendback)
    exit(0)
  if doaction=="trash":
    trashed = 0
    for post_id in post_ids:
      if !current_user_can(post_type_object.cap.delete_post, post_id):
        wp_die(__("You are not allowed to move this item to the Trash."))
      if !wp_trash_post(post_id):
        wp_die(__("Error in moving to Trash."))
      trashed+=1
    sendback = add_query_arg({"trashed":trashed, "ids":join(",", post_ids)}, sendback)
  elif doaction=="untrash":
    untrashed = 0
    for post_id in post_ids:
      if !current_user_can(post_type_object.cap.delete_post, post_id):
        wp_die(__("You are not allowed to restore this item from the Trash."))
      if !wp_untrash_post(post_id):
        wp_die(__("Error in restoring from Trash."))
      untrashed+=1
    sendback = add_query_arg("untrashed", untrashed, sendback)
  elif doaction=="delete":
    deleted = 0
    for post_id in post_ids:
      post_del = get_post(post_id)
      if !current_user_can(post_type_object.cap.delete_post, post_id):
        wp_die(__("You are not allowed to delete this item."))
      if post_del.post_type=="attachment":
        if !wp_delete_attachment(post_id):
          wp_die(__("Error in deleting..."))
      elif !wp_delete_post(post_id):
        wp_die(__("Error in deleting..."))
      deleted+=1
    sendback = add_query_arg("deleted", deleted, sendback)
  elif doaction=="edit":
    if isset(_REQUEST["bulk_edit"]):
      done = bulk_edit_posts(_REQUEST)
      if is_array(done):
        done["updated"] = count(done["updated"])
        done["skipped"] = count(done["skipped"])
        done["locked"] = count(done["locked"])
        sendback = add_query_arg(done, sendback)
  sendback = remove_query_arg(["action", "action2", "tags_input", "post_author", "comment_status", "ping_status", "_status", "post", "bulk_edit", "post_view"], sendback)
  wp_redirect(sendback)
  exit(0)
elif !empty(_REQUEST["_wp_http_referer"]):
  wp_redirect(remove_query_arg(["_wp_http_referer", "_wpnonce"], stripslashes(_SERVER["REQUEST_URI"])))
  exit(0)
wp_list_table.prepare_items()
wp_enqueue_script("inline-edit-post")
title = post_type_object.labels.name
if "post"==post_type:
  get_current_screen()
  get_current_screen()
  get_current_screen()
  get_current_screen()
  get_current_screen()
elif "page"==post_type:
  get_current_screen()
  get_current_screen()
  get_current_screen()
add_screen_option("per_page", {"label":title, "default":20, "option":"edit_"+post_type+"_per_page"})
require_once("./admin-header.php")
print("<div class="wrap">\n")
screen_icon()
print("<h2>")
print(esc_html(post_type_object.labels.name))
if current_user_can(post_type_object.cap.create_posts):
  print(" <a href=""+esc_url(post_new_file)+"" class="add-new-h2">"+esc_html(post_type_object.labels.add_new)+"</a>")
if !empty(_REQUEST["s"]):
  printf(" <span class="subtitle">"+__("Search results for &#8220;%s&#8221;")+"</span>", get_search_query())
print("</h2>\n\n")
if isset(_REQUEST["locked"])||isset(_REQUEST["updated"])||isset(_REQUEST["deleted"])||isset(_REQUEST["trashed"])||isset(_REQUEST["untrashed"]):
  messages = []
  print("<div id="message" class="updated"><p>\n")
  if isset(_REQUEST["updated"])&&updated = absint(_REQUEST["updated"]):
    messages[] = sprintf(_n("%s post updated.", "%s posts updated.", updated), number_format_i18n(updated))
  if isset(_REQUEST["locked"])&&locked = absint(_REQUEST["locked"]):
    messages[] = sprintf(_n("%s item not updated, somebody is editing it.", "%s items not updated, somebody is editing them.", locked), number_format_i18n(locked))
  if isset(_REQUEST["deleted"])&&deleted = absint(_REQUEST["deleted"]):
    messages[] = sprintf(_n("Item permanently deleted.", "%s items permanently deleted.", deleted), number_format_i18n(deleted))
  if isset(_REQUEST["trashed"])&&trashed = absint(_REQUEST["trashed"]):
    messages[] = sprintf(_n("Item moved to the Trash.", "%s items moved to the Trash.", trashed), number_format_i18n(trashed))
    ids = _REQUEST["ids"] if isset(_REQUEST["ids"]) else 0
    messages[] = "<a href=""+esc_url(wp_nonce_url("edit.php?post_type="+post_type+"&doaction=undo&action=untrash&ids="+ids+"", "bulk-posts"))+"">"+__("Undo")+"</a>"
  if isset(_REQUEST["untrashed"])&&untrashed = absint(_REQUEST["untrashed"]):
    messages[] = sprintf(_n("Item restored from the Trash.", "%s items restored from the Trash.", untrashed), number_format_i18n(untrashed))
  if messages:
    print(join(" ", messages))
  unset(messages)
  _SERVER["REQUEST_URI"] = remove_query_arg(["locked", "skipped", "updated", "deleted", "trashed", "untrashed"], _SERVER["REQUEST_URI"])
  print("</p></div>\n")
print("\n")
wp_list_table.views()
print("\n<form id="posts-filter" action="" method="get">\n\n")
wp_list_table.search_box(post_type_object.labels.search_items, "post")
print("\n<input type="hidden" name="post_status" class="post_status_page" value="")
print(esc_attr(_REQUEST["post_status"]) if !empty(_REQUEST["post_status"]) else "all")
print("" />\n<input type="hidden" name="post_type" class="post_type_page" value="")
print(post_type)
print("" />\n")
if !empty(_REQUEST["show_sticky"]):
  print("<input type="hidden" name="show_sticky" value="1" />\n")
print("\n")
wp_list_table.display()
print("\n</form>\n\n")
if wp_list_table.has_items():
  wp_list_table.inline_edit()
print("\n<div id="ajax-response"></div>\n<br class="clear" />\n</div>\n\n")
include("./admin-footer.php")
