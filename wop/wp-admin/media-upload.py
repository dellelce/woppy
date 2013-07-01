#!/usr/bin/python
#-*- coding: utf-8 -*-
if !isset(_GET["inline"]):
  define("IFRAME_REQUEST", True)
require_once("./admin.php")
if !current_user_can("upload_files"):
  wp_die(__("You do not have permission to upload files."))
wp_enqueue_script("plupload-handlers")
wp_enqueue_script("image-edit")
wp_enqueue_script("set-post-thumbnail")
wp_enqueue_style("imgareaselect")
wp_enqueue_script("media-gallery")
header("Content-Type: "+get_option("html_type")+"; charset="+get_option("blog_charset"))
ID = ID if isset(ID) else 0
post_id = post_id if isset(post_id) else 0
if isset(action)&&action=="edit"&&!ID:
  wp_die(__("Cheatin&#8217; uh?"))
if !empty(_REQUEST["post_id"])&&!current_user_can("edit_post", _REQUEST["post_id"]):
  wp_die(__("Cheatin&#8217; uh?"))
if isset(_GET["type"]):
  type = strval(_GET["type"])
else:
  type = apply_filters("media_upload_default_type", "file")
if isset(_GET["tab"]):
  tab = strval(_GET["tab"])
else:
  tab = apply_filters("media_upload_default_tab", "type")
body_id = "media-upload"
if tab=="type"||tab=="type_url"||!array_key_exists(tab, media_upload_tabs()):
  do_action("media_upload_"+type+"")
else:
  do_action("media_upload_"+tab+"")
