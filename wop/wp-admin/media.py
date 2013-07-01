#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
parent_file = "upload.php"
submenu_file = "upload.php"
wp_reset_vars(["action"])
if action=="editattachment":
  attachment_id = _POST["attachment_id"]
  check_admin_referer("media-form")
  if !current_user_can("edit_post", attachment_id):
    wp_die(__("You are not allowed to edit this attachment."))
  errors = media_upload_form_handler()
  if empty(errors):
    location = "media.php"
    if referer = wp_get_original_referer():
      if False!==strpos(referer, "upload.php")||url_to_postid(referer)==attachment_id:
        location = referer
    if False!==strpos(location, "upload.php"):
      location = remove_query_arg("message", location)
      location = add_query_arg("posted", attachment_id, location)
    elif False!==strpos(location, "media.php"):
      location = add_query_arg("message", "updated", location)
    wp_redirect(location)
    exit(0)
elif action=="edit":
  title = __("Edit Media")
  if empty(errors):
    errors = 
  if empty(_GET["attachment_id"]):
    wp_redirect(admin_url("upload.php"))
    exit(0)
  att_id = _GET["attachment_id"]
  if !current_user_can("edit_post", att_id):
    wp_die(__("You are not allowed to edit this attachment."))
  att = get_post(att_id)
  if empty(att.ID):
    wp_die(__("You attempted to edit an attachment that doesn&#8217;t exist. Perhaps it was deleted?"))
  if "attachment"!==att.post_type:
    wp_die(__("You attempted to edit an item that isn&#8217;t an attachment. Please go back and try again."))
  if att.post_status=="trash":
    wp_die(__("You can&#8217;t edit this attachment because it is in the Trash. Please move it out of the Trash and try again."))
  add_filter("attachment_fields_to_edit", "media_single_attachment_fields_to_edit", 10, 2)
  wp_enqueue_script("wp-ajax-response")
  wp_enqueue_script("image-edit")
  wp_enqueue_style("imgareaselect")
  get_current_screen()
  get_current_screen()
  require("./admin-header.php")
  parent_file = "upload.php"
  message = ""
  class = ""
  if isset(_GET["message"]):
    if _GET["message"]=="updated":
      message = __("Media attachment updated.")
      class = "updated"
  if message:
    print("<div id='message' class='"+class+"'><p>"+message+"</p></div>\n")
  print("\n<div class="wrap">\n")
  screen_icon()
  print("<h2>\n")
  print(esc_html(title))
  if current_user_can("upload_files"):
    print("	<a href="media-new.php" class="add-new-h2">")
    print(esc_html_x("Add New", "file"))
    print("</a>\n")
  print("</h2>\n\n<form method="post" action="" class="media-upload-form" id="media-single-form">\n<p class="submit" style="padding-bottom: 0;">\n")
  submit_button(__("Update Media"), "primary", "save", False)
  print("</p>\n\n<div class="media-single">\n<div id='media-item-")
  print(att_id)
  print("' class='media-item'>\n")
  print(get_media_item(att_id, {"toggle":False, "send":False, "delete":False, "show_title":False, "errors":errors[att_id] if !empty(errors[att_id]) else }))
  print("</div>\n</div>\n\n")
  submit_button(__("Update Media"), "primary", "save")
  print("<input type="hidden" name="post_id" id="post_id" value="")
  print(esc_attr(post_id) if isset(post_id) else "")
  print("" />\n<input type="hidden" name="attachment_id" id="attachment_id" value="")
  print(esc_attr(att_id))
  print("" />\n<input type="hidden" name="action" value="editattachment" />\n")
  wp_original_referer_field(True, "previous")
  wp_nonce_field("media-form")
  print("\n</form>\n\n</div>\n\n")
  require("./admin-footer.php")
  exit(0)
else:
  wp_redirect(admin_url("upload.php"))
  exit(0)
