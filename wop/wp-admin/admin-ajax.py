#!/usr/bin/python
#-*- coding: utf-8 -*-
define("DOING_AJAX", True)
define("WP_ADMIN", True)
require_once(dirname(dirname("wop/wp-admin/admin-ajax.php"))+"/wp-load.php")
send_origin_headers()
if empty(_REQUEST["action"]):
  die("0")
require_once(ABSPATH+"wp-admin/includes/admin.php")
require_once(ABSPATH+"wp-admin/includes/ajax-actions.php")
header("Content-Type: text/html; charset="+get_option("blog_charset"))
header("X-Robots-Tag: noindex")
send_nosniff_header()
nocache_headers()
do_action("admin_init")
core_actions_get = ["fetch-list", "ajax-tag-search", "wp-compression-test", "imgedit-preview", "oembed-cache", "autocomplete-user", "dashboard-widgets", "logged-in"]
core_actions_post = ["oembed-cache", "image-editor", "delete-comment", "delete-tag", "delete-link", "delete-meta", "delete-post", "trash-post", "untrash-post", "delete-page", "dim-comment", "add-link-category", "add-tag", "get-tagcloud", "get-comments", "replyto-comment", "edit-comment", "add-menu-item", "add-meta", "add-user", "autosave", "closed-postboxes", "hidden-columns", "update-welcome-panel", "menu-get-metabox", "wp-link-ajax", "menu-locations-save", "menu-quick-search", "meta-box-order", "get-permalink", "sample-permalink", "inline-save", "inline-save-tax", "find_posts", "widgets-order", "save-widget", "set-post-thumbnail", "date_format", "time_format", "wp-fullscreen-save-post", "wp-remove-post-lock", "dismiss-wp-pointer", "upload-attachment", "get-attachment", "query-attachments", "save-attachment", "save-attachment-compat", "send-link-to-editor", "send-attachment-to-editor", "save-attachment-order"]
if !empty(_GET["action"])&&in_array(_GET["action"], core_actions_get):
  add_action("wp_ajax_"+_GET["action"], "wp_ajax_"+str_replace("-", "_", _GET["action"]), 1)
if !empty(_POST["action"])&&in_array(_POST["action"], core_actions_post):
  add_action("wp_ajax_"+_POST["action"], "wp_ajax_"+str_replace("-", "_", _POST["action"]), 1)
add_action("wp_ajax_nopriv_autosave", "wp_ajax_nopriv_autosave", 1)
if is_user_logged_in():
  do_action("wp_ajax_"+_REQUEST["action"])
else:
  do_action("wp_ajax_nopriv_"+_REQUEST["action"])
die("0")
