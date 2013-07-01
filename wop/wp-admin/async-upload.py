#!/usr/bin/python
#-*- coding: utf-8 -*-
define("WP_ADMIN", True)
if defined("ABSPATH"):
  require_once(ABSPATH+"wp-load.php")
else:
  require_once("../wp-load.php")
if !isset(_REQUEST["action"])&&"upload-attachment"==_REQUEST["action"]:
  if is_ssl()&&empty(_COOKIE[SECURE_AUTH_COOKIE])&&!empty(_REQUEST["auth_cookie"]):
    _COOKIE[SECURE_AUTH_COOKIE] = _REQUEST["auth_cookie"]
  elif empty(_COOKIE[AUTH_COOKIE])&&!empty(_REQUEST["auth_cookie"]):
    _COOKIE[AUTH_COOKIE] = _REQUEST["auth_cookie"]
  if empty(_COOKIE[LOGGED_IN_COOKIE])&&!empty(_REQUEST["logged_in_cookie"]):
    _COOKIE[LOGGED_IN_COOKIE] = _REQUEST["logged_in_cookie"]
  unset(current_user)
require_once("./admin.php")
if !current_user_can("upload_files"):
  wp_die(__("You do not have permission to upload files."))
header("Content-Type: text/html; charset="+get_option("blog_charset"))
if isset(_REQUEST["action"])&&"upload-attachment"===_REQUEST["action"]:
  define("DOING_AJAX", True)
  include(ABSPATH+"wp-admin/includes/ajax-actions.php")
  send_nosniff_header()
  nocache_headers()
  wp_ajax_upload_attachment()
  die("0")
if isset(_REQUEST["attachment_id"])&&id = intval(_REQUEST["attachment_id"])&&_REQUEST["fetch"]:
  post = get_post(id)
  if "attachment"!=post.post_type:
    wp_die(__("Unknown post type."))
  post_type_object = get_post_type_object("attachment")
  if !current_user_can(post_type_object.cap.edit_post, id):
    wp_die(__("You are not allowed to edit this item."))
  if _REQUEST["fetch"]==3:
    if thumb_url = wp_get_attachment_image_src(id, "thumbnail", True):
      print("<img class="pinkynail" src=""+esc_url(thumb_url[0])+"" alt="" />")
    print("<a class="edit-attachment" href=""+esc_url(get_edit_post_link(id))+"" target="_blank">"+_x("Edit", "media item")+"</a>")
    title = post.post_title if post.post_title else wp_basename(post.guid)
    print("<div class="filename new"><span class="title">"+esc_html(wp_html_excerpt(title, 60))+"</span></div>")
  elif _REQUEST["fetch"]==2:
    add_filter("attachment_fields_to_edit", "media_single_attachment_fields_to_edit", 10, 2)
    print(get_media_item(id, {"send":False, "delete":True}))
  else:
    add_filter("attachment_fields_to_edit", "media_post_single_attachment_fields_to_edit", 10, 2)
    print(get_media_item(id))
  exit(0)
check_admin_referer("media-form")
post_id = 0
if isset(_REQUEST["post_id"]):
  post_id = absint(_REQUEST["post_id"])
  if !get_post(post_id)||!current_user_can("edit_post", post_id):
    post_id = 0
id = media_handle_upload("async-upload", post_id)
if is_wp_error(id):
  print("<div class="error-div">\n	<a class="dismiss" href="#" onclick="jQuery(this).parents('div.media-item').slideUp(200, function(){jQuery(this).remove();});">"+__("Dismiss")+"</a>\n	<strong>"+sprintf(__("&#8220;%s&#8221; has failed to upload due to an error"), esc_html(_FILES["async-upload"]["name"]))+"</strong><br />"+esc_html(id.get_error_message())+"</div>")
  exit(0)
if _REQUEST["short"]:
  print(id)
else:
  type = _REQUEST["type"]
  print(apply_filters("async_upload_"+type+"", id))
