#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("admin.php")
wp_reset_vars(["action", "cat_id", "linkurl", "name", "image", "description", "visible", "target", "category", "link_id", "submit", "order_by", "links_show_cat_id", "rating", "rel", "notes", "linkcheck[]"])
if !current_user_can("manage_links"):
  wp_link_manager_disabled_message()
if !empty(_POST["deletebookmarks"]):
  action = "deletebookmarks"
if !empty(_POST["move"]):
  action = "move"
if !empty(_POST["linkcheck"]):
  linkcheck = _POST["linkcheck"]
self_file = admin_url("link-manager.php")
if action=="deletebookmarks":
  check_admin_referer("bulk-bookmarks")
  if count(linkcheck)==0:
    wp_redirect(self_file)
    exit(0)
  deleted = 0
  for link_id in linkcheck:
    link_id = link_id
    if wp_delete_link(link_id):
      deleted+=1
  wp_redirect(""+self_file+"?deleted="+deleted+"")
  exit(0)
elif action=="move":
  check_admin_referer("bulk-bookmarks")
  if count(linkcheck)==0:
    wp_redirect(self_file)
    exit(0)
  all_links = join(",", linkcheck)
  wp_redirect(self_file)
  exit(0)
elif action=="add":
  check_admin_referer("add-bookmark")
  redir = wp_get_referer()
  if add_link():
    redir = add_query_arg("added", "true", redir)
  wp_redirect(redir)
  exit(0)
elif action=="save":
  link_id = _POST["link_id"]
  check_admin_referer("update-bookmark_"+link_id)
  edit_link(link_id)
  wp_redirect(self_file)
  exit(0)
elif action=="delete":
  link_id = _GET["link_id"]
  check_admin_referer("delete-bookmark_"+link_id)
  wp_delete_link(link_id)
  wp_redirect(self_file)
  exit(0)
elif action=="edit":
  wp_enqueue_script("link")
  wp_enqueue_script("xfn")
  if wp_is_mobile():
    wp_enqueue_script("jquery-touch-punch")
  parent_file = "link-manager.php"
  submenu_file = "link-manager.php"
  title = __("Edit Link")
  link_id = _GET["link_id"]
  if !link = get_link_to_edit(link_id):
    wp_die(__("Link not found."))
  include("edit-link-form.php")
  include("admin-footer.php")
else:
