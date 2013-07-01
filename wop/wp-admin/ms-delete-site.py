#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if !is_multisite():
  wp_die(__("Multisite support is not enabled."))
if !current_user_can("manage_options"):
  wp_die(__("You do not have sufficient permissions to delete this site."))
if isset(_GET["h"])&&_GET["h"]!=""&&get_option("delete_blog_hash")!=False:
  if get_option("delete_blog_hash")==_GET["h"]:
    wpmu_delete_blog(wpdb.blogid)
    wp_die(sprintf(__("Thank you for using %s, your site has been deleted. Happy trails to you until we meet again."), current_site.site_name))
  else:
    wp_die(__("I'm sorry, the link you clicked is stale. Please select another option."))
blog = get_blog_details()
title = __("Delete Site")
parent_file = "tools.php"
require_once("./admin-header.php")
print("<div class="wrap">")
screen_icon()
print("<h2>"+esc_html(title)+"</h2>")
if isset(_POST["action"])&&_POST["action"]=="deleteblog"&&isset(_POST["confirmdelete"])&&_POST["confirmdelete"]=="1":
  check_admin_referer("delete-blog")
  hash = wp_generate_password(20, False)
  update_option("delete_blog_hash", hash)
  url_delete = esc_url(admin_url("ms-delete-site.php?h="+hash))
  content = apply_filters("delete_site_email_content", __("Dear User,\nYou recently clicked the 'Delete Site' link on your site and filled in a\nform on that page.\nIf you really want to delete your site, click the link below. You will not\nbe asked to confirm again so only click this link if you are absolutely certain:\n###URL_DELETE###\n\nIf you delete your site, please consider opening a new site here\nsome time in the future! (But remember your current site and username\nare gone forever.)\n\nThanks for using the site,\nWebmaster\n###SITE_NAME###"))
  content = str_replace("###URL_DELETE###", url_delete, content)
  content = str_replace("###SITE_NAME###", current_site.site_name, content)
  wp_mail(get_option("admin_email"), "[ "+get_option("blogname")+" ] "+__("Delete My Site"), content)
  print("\n	<p>")
  _e("Thank you. Please check your email for a link to confirm your action. Your site will not be deleted until this link is clicked. ")
  print("</p>\n\n")
else:
  print("	<p>")
  printf(__("If you do not want to use your %s site any more, you can delete it using the form below. When you click <strong>Delete My Site Permanently</strong> you will be sent an email with a link in it. Click on this link to delete your site."), current_site.site_name)
  print("</p>\n	<p>")
  _e("Remember, once deleted your site cannot be restored.")
  print("</p>\n\n	<form method="post" name="deletedirect">\n		")
  wp_nonce_field("delete-blog")
  print("		<input type="hidden" name="action" value="deleteblog" />\n		<p><input id="confirmdelete" type="checkbox" name="confirmdelete" value="1" /> <label for="confirmdelete"><strong>")
  printf(__("I'm sure I want to permanently disable my site, and I am aware I can never get it back or use %s again."), blog.domain if is_subdomain_install() else blog.domain+blog.path)
  print("</strong></label></p>\n		")
  submit_button(__("Delete My Site Permanently"))
  print("	</form>\n 	")
print("</div>")
include("./admin-footer.php")
