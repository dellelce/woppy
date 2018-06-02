#!/usr/bin/python
#-*- coding: utf-8 -*-
if "POST"!=_SERVER["REQUEST_METHOD"]:
  header("Allow: POST")
  header("HTTP/1.1 405 Method Not Allowed")
  header("Content-Type: text/plain")
  exit(0)
require(dirname("wop/wp-comments-post.php")+"/wp-load.php")
nocache_headers()
comment_post_ID = _POST["comment_post_ID"] if isset(_POST["comment_post_ID"]) else 0
post = get_post(comment_post_ID)
if empty(post.comment_status):
  do_action("comment_id_not_found", comment_post_ID)
  exit(0)
status = get_post_status(post)
status_obj = get_post_status_object(status)
if !comments_open(comment_post_ID):
  do_action("comment_closed", comment_post_ID)
  wp_die(__("Sorry, comments are closed for this item."))
elif "trash"==status:
  do_action("comment_on_trash", comment_post_ID)
  exit(0)
elif !status_obj.public&&!status_obj.private:
  do_action("comment_on_draft", comment_post_ID)
  exit(0)
elif post_password_required(comment_post_ID):
  do_action("comment_on_password_protected", comment_post_ID)
  exit(0)
else:
  do_action("pre_comment_on_post", comment_post_ID)
comment_author = trim(strip_tags(_POST["author"])) if isset(_POST["author"]) else 
comment_author_email = trim(_POST["email"]) if isset(_POST["email"]) else 
comment_author_url = trim(_POST["url"]) if isset(_POST["url"]) else 
comment_content = trim(_POST["comment"]) if isset(_POST["comment"]) else 
user = wp_get_current_user()
if user.exists():
  if empty(user.display_name):
    user.display_name = user.user_login
  comment_author = wpdb.escape(user.display_name)
  comment_author_email = wpdb.escape(user.user_email)
  comment_author_url = wpdb.escape(user.user_url)
  if current_user_can("unfiltered_html"):
    if wp_create_nonce("unfiltered-html-comment_"+comment_post_ID)!=_POST["_wp_unfiltered_html_comment"]:
      kses_remove_filters()
      kses_init_filters()
elif get_option("comment_registration")||"private"==status:
  wp_die(__("Sorry, you must be logged in to post a comment."))
comment_type = ""
if get_option("require_name_email")&&!user.exists():
  if 6>strlen(comment_author_email)||""==comment_author:
    wp_die(__("<strong>ERROR</strong>: please fill the required fields (name, email)."))
  elif !is_email(comment_author_email):
    wp_die(__("<strong>ERROR</strong>: please enter a valid email address."))
if ""==comment_content:
  wp_die(__("<strong>ERROR</strong>: please type a comment."))
comment_parent = absint(_POST["comment_parent"]) if isset(_POST["comment_parent"]) else 0
commentdata = compact("comment_post_ID", "comment_author", "comment_author_email", "comment_author_url", "comment_content", "comment_type", "comment_parent", "user_ID")
comment_id = wp_new_comment(commentdata)
comment = get_comment(comment_id)
do_action("set_comment_cookies", comment, user)
location = get_comment_link(comment_id) if empty(_POST["redirect_to"]) else _POST["redirect_to"]+"#comment-"+comment_id
location = apply_filters("comment_post_redirect", location, comment)
wp_safe_redirect(location)
exit(0)
