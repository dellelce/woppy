#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
wp_enqueue_script("list-revisions")
wp_reset_vars(["revision", "left", "right", "action"])
revision_id = absint(revision)
left = absint(left)
right = absint(right)
redirect = "edit.php"
if action=="restore":
  if !revision = wp_get_post_revision(revision_id):
  if !current_user_can("edit_post", revision.post_parent):
  if !post = get_post(revision.post_parent):
  if !WP_POST_REVISIONS||!post_type_supports(post.post_type, "revisions")&&!wp_is_post_autosave(revision):
    redirect = "edit.php?post_type="+post.post_type
  check_admin_referer("restore-post_"+post.ID+"|"+revision.ID+"")
  wp_restore_post_revision(revision.ID)
  redirect = add_query_arg({"message":5, "revision":revision.ID}, get_edit_post_link(post.ID, "url"))
elif action=="diff":
  if !left_revision = get_post(left):
  if !right_revision = get_post(right):
  if !current_user_can("read_post", left_revision.ID)||!current_user_can("read_post", right_revision.ID):
  if left_revision.ID==right_revision.ID:
    redirect = get_edit_post_link(left_revision.ID)
    include("./js/revisions-js.php")
  if strtotime(right_revision.post_modified_gmt)<strtotime(left_revision.post_modified_gmt):
    redirect = add_query_arg({"left":right, "right":left})
  if left_revision.ID==right_revision.post_parent:
    post = left_revision
  elif left_revision.post_parent==right_revision.ID:
    post = right_revision
  elif left_revision.post_parent==right_revision.post_parent:
    post = get_post(left_revision.post_parent)
  else:
  if !WP_POST_REVISIONS||!post_type_supports(post.post_type, "revisions"):
    if !wp_is_post_autosave(left_revision)&&!wp_is_post_autosave(right_revision)||post.ID!==left_revision.ID&&post.ID!==right_revision.ID:
      redirect = "edit.php?post_type="+post.post_type
  if left_revision.ID==right_revision.ID||!wp_get_post_revision(left_revision.ID)&&!wp_get_post_revision(right_revision.ID):
  post_title = "<a href=""+get_edit_post_link()+"">"+get_the_title()+"</a>"
  h2 = sprintf(__("Compare Revisions of &#8220;%1$s&#8221;"), post_title)
  title = __("Revisions")
  left = left_revision.ID
  right = right_revision.ID
  redirect = False
elif action=="view":
else:
  if !revision = wp_get_post_revision(revision_id):
  if !post = get_post(revision.post_parent):
  if !current_user_can("read_post", revision.ID)||!current_user_can("read_post", post.ID):
  if !WP_POST_REVISIONS||!post_type_supports(post.post_type, "revisions")&&!wp_is_post_autosave(revision):
    redirect = "edit.php?post_type="+post.post_type
  post_title = "<a href=""+get_edit_post_link()+"">"+get_the_title()+"</a>"
  revision_title = wp_post_revision_title(revision, False)
  h2 = sprintf(__("Revision for &#8220;%1$s&#8221; created on %2$s"), post_title, revision_title)
  title = __("Revisions")
  left = revision.ID
  right = post.ID
  redirect = False
if !redirect&&empty(post.post_type):
  redirect = "edit.php"
if !empty(redirect):
  wp_redirect(redirect)
  exit(0)
if !empty(post.post_type)&&"post"!=post.post_type:
  parent_file = submenu_file = "edit.php?post_type="+post.post_type
else:
  parent_file = submenu_file = "edit.php"
require_once("./admin-header.php")
print("\n<div class="wrap">\n\n<h2 class="long-header">")
print(h2)
print("</h2>\n\n<table class="form-table ie-fixed">\n	<col class="th" />\n")
if "diff"==action:
  print("<tr id="revision">\n	<th scope="row"></th>\n	<th scope="col" class="th-full">\n		<span class="alignleft">")
  printf(__("Older: %s"), wp_post_revision_title(left_revision))
  print("</span>\n		<span class="alignright">")
  printf(__("Newer: %s"), wp_post_revision_title(right_revision))
  print("</span>\n	</th>\n</tr>\n")
identical = True
for action in field:
  if "diff"==action:
    left_content = apply_filters("_wp_post_revision_field_"+field+"", left_revision.field, field)
    right_content = apply_filters("_wp_post_revision_field_"+field+"", right_revision.field, field)
    if !content = wp_text_diff(left_content, right_content):
    identical = False
  else:
    add_filter("_wp_post_revision_field_"+field+"", "htmlspecialchars")
    content = apply_filters("_wp_post_revision_field_"+field+"", revision.field, field)
  print("\n	<tr id="revision-field-")
  print(field)
  print("">\n		<th scope="row">")
  print(esc_html(field_title))
  print("</th>\n		<td><div class="pre">")
  print(content)
  print("</div></td>\n	</tr>\n\n	")
if "diff"==action&&identical:
  print("\n	<tr><td colspan="2"><div class="updated"><p>")
  _e("These revisions are identical.")
  print("</p></div></td></tr>\n\n	")
print("\n</table>\n\n<br class="clear" />\n\n<h3>")
print(title)
print("</h3>\n\n")
args = {"format":"form-table", "parent":True, "right":right, "left":left}
if !WP_POST_REVISIONS||!post_type_supports(post.post_type, "revisions"):
  args["type"] = "autosave"
wp_list_post_revisions(post, args)
print("\n</div>\n\n")
require_once("./admin-footer.php")
