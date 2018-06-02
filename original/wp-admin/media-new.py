#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if !current_user_can("upload_files"):
  wp_die(__("You do not have permission to upload files."))
wp_enqueue_script("plupload-handlers")
post_id = 0
if isset(_REQUEST["post_id"]):
  post_id = absint(_REQUEST["post_id"])
  if !get_post(post_id)||!current_user_can("edit_post", post_id):
    post_id = 0
if _POST:
  location = "upload.php"
  if isset(_POST["html-upload"])&&!empty(_FILES):
    check_admin_referer("media-form")
    id = media_handle_upload("async-upload", post_id)
    if is_wp_error(id):
      location+="?message=3"
  wp_redirect(admin_url(location))
  exit(0)
title = __("Upload New Media")
parent_file = "upload.php"
get_current_screen()
get_current_screen()
require_once(ABSPATH+"wp-admin/admin-header.php")
form_class = "media-upload-form type-form validate"
if get_user_setting("uploader")||isset(_GET["browser-uploader"]):
  form_class+=" html-uploader"
print("<div class="wrap">\n	")
screen_icon()
print("	<h2>")
print(esc_html(title))
print("</h2>\n\n	<form enctype="multipart/form-data" method="post" action="")
print(admin_url("media-new.php"))
print("" class="")
print(form_class)
print("" id="file-form">\n\n	")
media_upload_form()
print("\n	<script type="text/javascript">\n	var post_id = ")
print(post_id)
print(", shortform = 3;\n	</script>\n	<input type="hidden" name="post_id" id="post_id" value="")
print(post_id)
print("" />\n	")
wp_nonce_field("media-form")
print("	<div id="media-items" class="hide-if-no-js"></div>\n	</form>\n</div>\n\n")
include(ABSPATH+"wp-admin/admin-footer.php")
