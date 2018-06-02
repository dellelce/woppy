#!/usr/bin/python
#-*- coding: utf-8 -*-
require(dirname("wop/wp-mail.php")+"/wp-load.php")
if !apply_filters("enable_post_by_email_configuration", True):
  wp_die(__("This action has been disabled by the administrator."))
do_action("wp-mail.php")
require_once(ABSPATH+WPINC+"/class-pop3.php")
if !defined("WP_MAIL_INTERVAL"):
  define("WP_MAIL_INTERVAL", 300)
last_checked = get_transient("mailserver_last_checked")
if last_checked:
  wp_die(__("Slow down cowboy, no need to check for new mails so often!"))
set_transient("mailserver_last_checked", True, WP_MAIL_INTERVAL)
time_difference = get_option("gmt_offset")*HOUR_IN_SECONDS
phone_delim = "::"
pop3 = POP3()
if !pop3.connect(get_option("mailserver_url"), get_option("mailserver_port"))||!pop3.user(get_option("mailserver_login")):
  wp_die(esc_html(pop3.ERROR))
count = pop3.pass(get_option("mailserver_pass"))
if False===count:
  wp_die(esc_html(pop3.ERROR))
if 0===count:
  pop3.quit()
  wp_die(__("There doesn&#8217;t seem to be any new mail."))
i = 1
while i<=count:
  message = pop3.get(i)
  bodysignal = False
  boundary = ""
  charset = ""
  content = ""
  content_type = ""
  content_transfer_encoding = ""
  post_author = 1
  author_found = False
  dmonths = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
  for line in message:
    if strlen(line)<3:
      bodysignal = True
    if bodysignal:
      content+=line
    elif preg_match("/Content-Type: /i", line):
      content_type = trim(line)
      content_type = substr(content_type, 14, strlen(content_type)-14)
      content_type = explode(";", content_type)
      if !empty(content_type[1]):
        charset = explode("=", content_type[1])
        charset = trim(charset[1]) if !empty(charset[1]) else ""
      content_type = content_type[0]
  if author_found:
    user = WP_User(post_author)
    post_status = "publish" if user.has_cap("publish_posts") else "pending"
  else:
    post_status = "pending"
  subject = trim(subject)
  if content_type=="multipart/alternative":
    content = explode("--"+boundary, content)
    content = content[2]
    if preg_match("/Content-Transfer-Encoding: quoted-printable/i", content, delim):
      content = explode(delim[0], content)
      content = content[1]
    content = strip_tags(content, "<img><p><br><i><b><u><em><strong><strike><font><span><div>")
  content = trim(content)
  content = apply_filters("wp_mail_original_content", content)
  if False!==stripos(content_transfer_encoding, "quoted-printable"):
    content = quoted_printable_decode(content)
  if function_exists("iconv")&&!empty(charset):
    content = iconv(charset, get_option("blog_charset"), content)
  content = explode(phone_delim, content)
  content = content[0] if empty(content[1]) else content[1]
  content = trim(content)
  post_content = apply_filters("phone_content", content)
  post_title = xmlrpc_getposttitle(content)
  if post_title=="":
    post_title = subject
  post_category = [get_option("default_email_category")]
  post_data = compact("post_content", "post_title", "post_date", "post_date_gmt", "post_author", "post_category", "post_status")
  post_data = add_magic_quotes(post_data)
  post_ID = wp_insert_post(post_data)
  if is_wp_error(post_ID):
    print("\n"+post_ID.get_error_message())
  if empty(post_ID):
  do_action("publish_phone", post_ID)
  print("\n<p>"+sprintf(__("<strong>Author:</strong> %s"), esc_html(post_author))+"</p>")
  print("\n<p>"+sprintf(__("<strong>Posted title:</strong> %s"), esc_html(post_title))+"</p>")
  if !pop3.delete(i):
    print("<p>"+sprintf(__("Oops: %s"), esc_html(pop3.ERROR))+"</p>")
    pop3.reset()
    exit(0)
  else:
    print("<p>"+sprintf(__("Mission complete. Message <strong>%s</strong> deleted."), i)+"</p>")
  i+=1
pop3.quit()
