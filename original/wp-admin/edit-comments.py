#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if !current_user_can("edit_posts"):
  wp_die(__("Cheatin&#8217; uh?"))
wp_list_table = _get_list_table("WP_Comments_List_Table")
pagenum = wp_list_table.get_pagenum()
doaction = wp_list_table.current_action()
if doaction:
  check_admin_referer("bulk-comments")
  if "delete_all"==doaction&&!empty(_REQUEST["pagegen_timestamp"]):
    comment_status = wpdb.escape(_REQUEST["comment_status"])
    delete_time = wpdb.escape(_REQUEST["pagegen_timestamp"])
    comment_ids = wpdb.get_col("SELECT comment_ID FROM "+wpdb.comments+" WHERE comment_approved = '"+comment_status+"' AND '"+delete_time+"' > comment_date_gmt")
    doaction = "delete"
  elif isset(_REQUEST["delete_comments"]):
    comment_ids = _REQUEST["delete_comments"]
    doaction = _REQUEST["action"] if _REQUEST["action"]!=-1 else _REQUEST["action2"]
  elif isset(_REQUEST["ids"]):
    comment_ids = array_map("absint", explode(",", _REQUEST["ids"]))
  elif wp_get_referer():
    wp_safe_redirect(wp_get_referer())
    exit(0)
  approved = unapproved = spammed = unspammed = trashed = untrashed = deleted = 0
  redirect_to = remove_query_arg(["trashed", "untrashed", "deleted", "spammed", "unspammed", "approved", "unapproved", "ids"], wp_get_referer())
  redirect_to = add_query_arg("paged", pagenum, redirect_to)
  for comment_id in comment_ids:
    if !current_user_can("edit_comment", comment_id):
    if doaction=="approve":
      wp_set_comment_status(comment_id, "approve")
      approved+=1
    elif doaction=="unapprove":
      wp_set_comment_status(comment_id, "hold")
      unapproved+=1
    elif doaction=="spam":
      wp_spam_comment(comment_id)
      spammed+=1
    elif doaction=="unspam":
      wp_unspam_comment(comment_id)
      unspammed+=1
    elif doaction=="trash":
      wp_trash_comment(comment_id)
      trashed+=1
    elif doaction=="untrash":
      wp_untrash_comment(comment_id)
      untrashed+=1
    elif doaction=="delete":
      wp_delete_comment(comment_id)
      deleted+=1
  if approved:
    redirect_to = add_query_arg("approved", approved, redirect_to)
  if unapproved:
    redirect_to = add_query_arg("unapproved", unapproved, redirect_to)
  if spammed:
    redirect_to = add_query_arg("spammed", spammed, redirect_to)
  if unspammed:
    redirect_to = add_query_arg("unspammed", unspammed, redirect_to)
  if trashed:
    redirect_to = add_query_arg("trashed", trashed, redirect_to)
  if untrashed:
    redirect_to = add_query_arg("untrashed", untrashed, redirect_to)
  if deleted:
    redirect_to = add_query_arg("deleted", deleted, redirect_to)
  if trashed||spammed:
    redirect_to = add_query_arg("ids", join(",", comment_ids), redirect_to)
  wp_safe_redirect(redirect_to)
  exit(0)
elif !empty(_GET["_wp_http_referer"]):
  wp_redirect(remove_query_arg(["_wp_http_referer", "_wpnonce"], stripslashes(_SERVER["REQUEST_URI"])))
  exit(0)
wp_list_table.prepare_items()
wp_enqueue_script("admin-comments")
enqueue_comment_hotkeys_js()
if post_id:
  title = sprintf(__("Comments on &#8220;%s&#8221;"), wp_html_excerpt(_draft_or_post_title(post_id), 50))
else:
  title = __("Comments")
add_screen_option("per_page", {"label":_x("Comments", "comments per page (screen options)")})
get_current_screen()
get_current_screen()
get_current_screen()
require_once("./admin-header.php")
print("\n<div class="wrap">\n")
screen_icon()
print("<h2>")
if post_id:
  print(sprintf(__("Comments on &#8220;%s&#8221;"), sprintf("<a href="%s">%s</a>", get_edit_post_link(post_id), wp_html_excerpt(_draft_or_post_title(post_id), 50))))
else:
  print(__("Comments"))
if isset(_REQUEST["s"])&&_REQUEST["s"]:
  printf("<span class="subtitle">"+sprintf(__("Search results for &#8220;%s&#8221;"), wp_html_excerpt(esc_html(stripslashes(_REQUEST["s"])), 50))+"</span>")
print("</h2>\n\n")
if isset(_REQUEST["error"]):
  error = _REQUEST["error"]
  error_msg = ""
  if error==1:
    error_msg = __("Oops, no comment with this ID.")
  elif error==2:
    error_msg = __("You are not allowed to edit comments on this post.")
  if error_msg:
    print("<div id="moderated" class="error"><p>"+error_msg+"</p></div>")
if isset(_REQUEST["approved"])||isset(_REQUEST["deleted"])||isset(_REQUEST["trashed"])||isset(_REQUEST["untrashed"])||isset(_REQUEST["spammed"])||isset(_REQUEST["unspammed"])||isset(_REQUEST["same"]):
  approved = _REQUEST["approved"] if isset(_REQUEST["approved"]) else 0
  deleted = _REQUEST["deleted"] if isset(_REQUEST["deleted"]) else 0
  trashed = _REQUEST["trashed"] if isset(_REQUEST["trashed"]) else 0
  untrashed = _REQUEST["untrashed"] if isset(_REQUEST["untrashed"]) else 0
  spammed = _REQUEST["spammed"] if isset(_REQUEST["spammed"]) else 0
  unspammed = _REQUEST["unspammed"] if isset(_REQUEST["unspammed"]) else 0
  same = _REQUEST["same"] if isset(_REQUEST["same"]) else 0
  if approved>0||deleted>0||trashed>0||untrashed>0||spammed>0||unspammed>0||same>0:
    if approved>0:
      messages[] = sprintf(_n("%s comment approved", "%s comments approved", approved), approved)
    if spammed>0:
      ids = _REQUEST["ids"] if isset(_REQUEST["ids"]) else 0
      messages[] = sprintf(_n("%s comment marked as spam.", "%s comments marked as spam.", spammed), spammed)+" <a href=""+esc_url(wp_nonce_url("edit-comments.php?doaction=undo&action=unspam&ids="+ids+"", "bulk-comments"))+"">"+__("Undo")+"</a><br />"
    if unspammed>0:
      messages[] = sprintf(_n("%s comment restored from the spam", "%s comments restored from the spam", unspammed), unspammed)
    if trashed>0:
      ids = _REQUEST["ids"] if isset(_REQUEST["ids"]) else 0
      messages[] = sprintf(_n("%s comment moved to the Trash.", "%s comments moved to the Trash.", trashed), trashed)+" <a href=""+esc_url(wp_nonce_url("edit-comments.php?doaction=undo&action=untrash&ids="+ids+"", "bulk-comments"))+"">"+__("Undo")+"</a><br />"
    if untrashed>0:
      messages[] = sprintf(_n("%s comment restored from the Trash", "%s comments restored from the Trash", untrashed), untrashed)
    if deleted>0:
      messages[] = sprintf(_n("%s comment permanently deleted", "%s comments permanently deleted", deleted), deleted)
    if same>0&&comment = get_comment(same):
      if comment.comment_approved=="1":
        messages[] = __("This comment is already approved.")+" <a href=""+esc_url(admin_url("comment.php?action=editcomment&c="+same+""))+"">"+__("Edit comment")+"</a>"
      elif comment.comment_approved=="trash":
        messages[] = __("This comment is already in the Trash.")+" <a href=""+esc_url(admin_url("edit-comments.php?comment_status=trash"))+""> "+__("View Trash")+"</a>"
      elif comment.comment_approved=="spam":
        messages[] = __("This comment is already marked as spam.")+" <a href=""+esc_url(admin_url("comment.php?action=editcomment&c="+same+""))+"">"+__("Edit comment")+"</a>"
    print("<div id="moderated" class="updated"><p>"+implode("<br/>\n", messages)+"</p></div>")
print("\n")
wp_list_table.views()
print("\n<form id="comments-form" action="" method="get">\n\n")
wp_list_table.search_box(__("Search Comments"), "comment")
print("\n")
if post_id:
  print("<input type="hidden" name="p" value="")
  print(esc_attr(intval(post_id)))
  print("" />\n")
print("<input type="hidden" name="comment_status" value="")
print(esc_attr(comment_status))
print("" />\n<input type="hidden" name="pagegen_timestamp" value="")
print(esc_attr(current_time("mysql", 1)))
print("" />\n\n<input type="hidden" name="_total" value="")
print(esc_attr(wp_list_table.get_pagination_arg("total_items")))
print("" />\n<input type="hidden" name="_per_page" value="")
print(esc_attr(wp_list_table.get_pagination_arg("per_page")))
print("" />\n<input type="hidden" name="_page" value="")
print(esc_attr(wp_list_table.get_pagination_arg("page")))
print("" />\n\n")
if isset(_REQUEST["paged"]):
  print("	<input type="hidden" name="paged" value="")
  print(esc_attr(absint(_REQUEST["paged"])))
  print("" />\n")
print("\n")
wp_list_table.display()
print("</form>\n</div>\n\n<div id="ajax-response"></div>\n\n")
wp_comment_reply("-1", True, "detail")
wp_comment_trashnotice()
include("./admin-footer.php")
