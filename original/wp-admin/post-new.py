#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if !isset(_GET["post_type"]):
  post_type = "post"
elif in_array(_GET["post_type"], get_post_types({"show_ui":True})):
  post_type = _GET["post_type"]
else:
  wp_die(__("Invalid post type"))
post_type_object = get_post_type_object(post_type)
if "post"==post_type:
  parent_file = "edit.php"
  submenu_file = "post-new.php"
elif "attachment"==post_type:
  wp_redirect(admin_url("media-new.php"))
  exit(0)
else:
  submenu_file = "post-new.php?post_type="+post_type+""
  if isset(post_type_object)&&post_type_object.show_in_menu&&post_type_object.show_in_menu!==True:
    parent_file = post_type_object.show_in_menu
    if !isset(_registered_pages[get_plugin_page_hookname("post-new.php?post_type="+post_type+"", post_type_object.show_in_menu)]):
      submenu_file = parent_file
  else:
    parent_file = "edit.php?post_type="+post_type+""
title = post_type_object.labels.add_new_item
editing = True
if !current_user_can(post_type_object.cap.edit_posts)||!current_user_can(post_type_object.cap.create_posts):
  wp_die(__("Cheatin&#8217; uh?"))
if !wp_next_scheduled("wp_scheduled_auto_draft_delete"):
  wp_schedule_event(time(), "daily", "wp_scheduled_auto_draft_delete")
wp_enqueue_script("autosave")
post = get_default_post_to_edit(post_type, True)
post_ID = post.ID
include("edit-form-advanced.php")
include("./admin-footer.php")
