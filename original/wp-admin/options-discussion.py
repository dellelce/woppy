#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if !current_user_can("manage_options"):
  wp_die(__("You do not have sufficient permissions to manage options for this site."))
title = __("Discussion Settings")
parent_file = "options-general.php"
get_current_screen()
get_current_screen()
include("./admin-header.php")
print("\n<div class="wrap">\n")
screen_icon()
print("<h2>")
print(esc_html(title))
print("</h2>\n\n<form method="post" action="options.php">\n")
settings_fields("discussion")
print("\n<table class="form-table">\n<tr valign="top">\n<th scope="row">")
_e("Default article settings")
print("</th>\n<td><fieldset><legend class="screen-reader-text"><span>")
_e("Default article settings")
print("</span></legend>\n<label for="default_pingback_flag">\n<input name="default_pingback_flag" type="checkbox" id="default_pingback_flag" value="1" ")
checked("1", get_option("default_pingback_flag"))
print(" />\n")
_e("Attempt to notify any blogs linked to from the article")
print("</label>\n<br />\n<label for="default_ping_status">\n<input name="default_ping_status" type="checkbox" id="default_ping_status" value="open" ")
checked("open", get_option("default_ping_status"))
print(" />\n")
_e("Allow link notifications from other blogs (pingbacks and trackbacks)")
print("</label>\n<br />\n<label for="default_comment_status">\n<input name="default_comment_status" type="checkbox" id="default_comment_status" value="open" ")
checked("open", get_option("default_comment_status"))
print(" />\n")
_e("Allow people to post comments on new articles")
print("</label>\n<br />\n<small><em>")
print("("+__("These settings may be overridden for individual articles.")+")")
print("</em></small>\n</fieldset></td>\n</tr>\n<tr valign="top">\n<th scope="row">")
_e("Other comment settings")
print("</th>\n<td><fieldset><legend class="screen-reader-text"><span>")
_e("Other comment settings")
print("</span></legend>\n<label for="require_name_email"><input type="checkbox" name="require_name_email" id="require_name_email" value="1" ")
checked("1", get_option("require_name_email"))
print(" /> ")
_e("Comment author must fill out name and e-mail")
print("</label>\n<br />\n<label for="comment_registration">\n<input name="comment_registration" type="checkbox" id="comment_registration" value="1" ")
checked("1", get_option("comment_registration"))
print(" />\n")
_e("Users must be registered and logged in to comment")
if !get_option("users_can_register")&&is_multisite():
  print(" "+__("(Signup has been disabled. Only members of this site can comment.)"))
print("</label>\n<br />\n\n<label for="close_comments_for_old_posts">\n<input name="close_comments_for_old_posts" type="checkbox" id="close_comments_for_old_posts" value="1" ")
checked("1", get_option("close_comments_for_old_posts"))
print(" />\n")
printf(__("Automatically close comments on articles older than %s days"), "</label><label for="close_comments_days_old"><input name="close_comments_days_old" type="number" min="0" step="1" id="close_comments_days_old" value=""+esc_attr(get_option("close_comments_days_old"))+"" class="small-text" />")
print("</label>\n<br />\n<label for="thread_comments">\n<input name="thread_comments" type="checkbox" id="thread_comments" value="1" ")
checked("1", get_option("thread_comments"))
print(" />\n")
maxdeep = apply_filters("thread_comments_depth_max", 10)
thread_comments_depth = "</label><label for="thread_comments_depth"><select name="thread_comments_depth" id="thread_comments_depth">"
i = 2
while i<=maxdeep:
  thread_comments_depth+="<option value='"+esc_attr(i)+"'"
  if get_option("thread_comments_depth")==i:
    thread_comments_depth+=" selected='selected'"
  thread_comments_depth+=">"+i+"</option>"
  i+=1
thread_comments_depth+="</select>"
printf(__("Enable threaded (nested) comments %s levels deep"), thread_comments_depth)
print("</label>\n<br />\n<label for="page_comments">\n<input name="page_comments" type="checkbox" id="page_comments" value="1" ")
checked("1", get_option("page_comments"))
print(" />\n")
default_comments_page = "</label><label for="default_comments_page"><select name="default_comments_page" id="default_comments_page"><option value="newest""
if "newest"==get_option("default_comments_page"):
  default_comments_page+=" selected="selected""
default_comments_page+=">"+__("last")+"</option><option value="oldest""
if "oldest"==get_option("default_comments_page"):
  default_comments_page+=" selected="selected""
default_comments_page+=">"+__("first")+"</option></select>"
printf(__("Break comments into pages with %1$s top level comments per page and the %2$s page displayed by default"), "</label><label for="comments_per_page"><input name="comments_per_page" type="number" step="1" min="0" id="comments_per_page" value=""+esc_attr(get_option("comments_per_page"))+"" class="small-text" />", default_comments_page)
print("</label>\n<br />\n<label for="comment_order">")
comment_order = "<select name="comment_order" id="comment_order"><option value="asc""
if "asc"==get_option("comment_order"):
  comment_order+=" selected="selected""
comment_order+=">"+__("older")+"</option><option value="desc""
if "desc"==get_option("comment_order"):
  comment_order+=" selected="selected""
comment_order+=">"+__("newer")+"</option></select>"
printf(__("Comments should be displayed with the %s comments at the top of each page"), comment_order)
print("</label>\n</fieldset></td>\n</tr>\n<tr valign="top">\n<th scope="row">")
_e("E-mail me whenever")
print("</th>\n<td><fieldset><legend class="screen-reader-text"><span>")
_e("E-mail me whenever")
print("</span></legend>\n<label for="comments_notify">\n<input name="comments_notify" type="checkbox" id="comments_notify" value="1" ")
checked("1", get_option("comments_notify"))
print(" />\n")
_e("Anyone posts a comment")
print(" </label>\n<br />\n<label for="moderation_notify">\n<input name="moderation_notify" type="checkbox" id="moderation_notify" value="1" ")
checked("1", get_option("moderation_notify"))
print(" />\n")
_e("A comment is held for moderation")
print(" </label>\n</fieldset></td>\n</tr>\n<tr valign="top">\n<th scope="row">")
_e("Before a comment appears")
print("</th>\n<td><fieldset><legend class="screen-reader-text"><span>")
_e("Before a comment appears")
print("</span></legend>\n<label for="comment_moderation">\n<input name="comment_moderation" type="checkbox" id="comment_moderation" value="1" ")
checked("1", get_option("comment_moderation"))
print(" />\n")
_e("An administrator must always approve the comment")
print(" </label>\n<br />\n<label for="comment_whitelist"><input type="checkbox" name="comment_whitelist" id="comment_whitelist" value="1" ")
checked("1", get_option("comment_whitelist"))
print(" /> ")
_e("Comment author must have a previously approved comment")
print("</label>\n</fieldset></td>\n</tr>\n<tr valign="top">\n<th scope="row">")
_e("Comment Moderation")
print("</th>\n<td><fieldset><legend class="screen-reader-text"><span>")
_e("Comment Moderation")
print("</span></legend>\n<p><label for="comment_max_links">")
printf(__("Hold a comment in the queue if it contains %s or more links. (A common characteristic of comment spam is a large number of hyperlinks.)"), "<input name="comment_max_links" type="number" step="1" min="0" id="comment_max_links" value=""+esc_attr(get_option("comment_max_links"))+"" class="small-text" />")
print("</label></p>\n\n<p><label for="moderation_keys">")
_e("When a comment contains any of these words in its content, name, URL, e-mail, or IP, it will be held in the <a href="edit-comments.php?comment_status=moderated">moderation queue</a>. One word or IP per line. It will match inside words, so &#8220;press&#8221; will match &#8220;WordPress&#8221;.")
print("</label></p>\n<p>\n<textarea name="moderation_keys" rows="10" cols="50" id="moderation_keys" class="large-text code">")
print(esc_textarea(get_option("moderation_keys")))
print("</textarea>\n</p>\n</fieldset></td>\n</tr>\n<tr valign="top">\n<th scope="row">")
_e("Comment Blacklist")
print("</th>\n<td><fieldset><legend class="screen-reader-text"><span>")
_e("Comment Blacklist")
print("</span></legend>\n<p><label for="blacklist_keys">")
_e("When a comment contains any of these words in its content, name, URL, e-mail, or IP, it will be marked as spam. One word or IP per line. It will match inside words, so &#8220;press&#8221; will match &#8220;WordPress&#8221;.")
print("</label></p>\n<p>\n<textarea name="blacklist_keys" rows="10" cols="50" id="blacklist_keys" class="large-text code">")
print(esc_textarea(get_option("blacklist_keys")))
print("</textarea>\n</p>\n</fieldset></td>\n</tr>\n")
do_settings_fields("discussion", "default")
print("</table>\n\n<h3>")
_e("Avatars")
print("</h3>\n\n<p>")
_e("An avatar is an image that follows you from weblog to weblog appearing beside your name when you comment on avatar enabled sites. Here you can enable the display of avatars for people who comment on your site.")
print("</p>\n\n")
print("\n\n<table class="form-table">\n<tr valign="top">\n<th scope="row">")
_e("Avatar Display")
print("</th>\n<td><fieldset><legend class="screen-reader-text"><span>")
_e("Avatar Display")
print("</span></legend>\n	<label for="show_avatars">\n		<input type="checkbox" id="show_avatars" name="show_avatars" value="1" ")
checked(get_option("show_avatars"), 1)
print(" />\n		")
_e("Show Avatars")
print("	</label>\n</fieldset></td>\n</tr>\n<tr valign="top">\n<th scope="row">")
_e("Maximum Rating")
print("</th>\n<td><fieldset><legend class="screen-reader-text"><span>")
_e("Maximum Rating")
print("</span></legend>\n\n")
ratings = {"G":__("G &#8212; Suitable for all audiences"), "PG":__("PG &#8212; Possibly offensive, usually for audiences 13 and above"), "R":__("R &#8212; Intended for adult audiences above 17"), "X":__("X &#8212; Even more mature than above")}
for rating in ratings:
  selected = "checked="checked"" if get_option("avatar_rating")==key else ""
  print("\n	<label><input type='radio' name='avatar_rating' value='"+esc_attr(key)+"' "+selected+"/> "+rating+"</label><br />")
print("\n</fieldset></td>\n</tr>\n<tr valign="top">\n<th scope="row">")
_e("Default Avatar")
print("</th>\n<td class="defaultavatarpicker"><fieldset><legend class="screen-reader-text"><span>")
_e("Default Avatar")
print("</span></legend>\n\n")
_e("For users without a custom avatar of their own, you can either display a generic logo or a generated one based on their e-mail address.")
print("<br />\n\n")
avatar_defaults = {"mystery":__("Mystery Man"), "blank":__("Blank"), "gravatar_default":__("Gravatar Logo"), "identicon":__("Identicon (Generated)"), "wavatar":__("Wavatar (Generated)"), "monsterid":__("MonsterID (Generated)"), "retro":__("Retro (Generated)")}
avatar_defaults = apply_filters("avatar_defaults", avatar_defaults)
default = get_option("avatar_default")
if empty(default):
  default = "mystery"
size = 32
avatar_list = ""
for default_name in avatar_defaults:
  selected = "checked="checked" " if default==default_key else ""
  avatar_list+="\n	<label><input type='radio' name='avatar_default' id='avatar_"+default_key+"' value='"+esc_attr(default_key)+"' "+selected+"/> "
  avatar = get_avatar(user_email, size, default_key)
  avatar_list+=preg_replace("/src='(.+?)'/", "src='$1&amp;forcedefault=1'", avatar)
  avatar_list+=" "+default_name+"</label>"
  avatar_list+="<br />"
print(apply_filters("default_avatar_select", avatar_list))
print("\n</fieldset></td>\n</tr>\n")
do_settings_fields("discussion", "avatars")
print("</table>\n\n")
do_settings_sections("discussion")
print("\n")
submit_button()
print("</form>\n</div>\n\n")
include("./admin-footer.php")
