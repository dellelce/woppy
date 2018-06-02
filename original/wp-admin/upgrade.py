#!/usr/bin/python
#-*- coding: utf-8 -*-
define("WP_INSTALLING", True)
require("../wp-load.php")
nocache_headers()
timer_start()
require_once(ABSPATH+"wp-admin/includes/upgrade.php")
delete_site_transient("update_core")
if isset(_GET["step"]):
  step = _GET["step"]
else:
  step = 0
if "upgrade_db"===step:
  wp_upgrade()
  die("0")
step = step
php_version = phpversion()
mysql_version = wpdb.db_version()
php_compat = version_compare(php_version, required_php_version, ">=")
if file_exists(WP_CONTENT_DIR+"/db.php")&&empty(wpdb.is_mysql):
  mysql_compat = True
else:
  mysql_compat = version_compare(mysql_version, required_mysql_version, ">=")
header("Content-Type: "+get_option("html_type")+"; charset="+get_option("blog_charset"))
print("<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" ")
language_attributes()
print(">\n<head>\n	<meta http-equiv="Content-Type" content="")
bloginfo("html_type")
print("; charset=")
print(get_option("blog_charset"))
print("" />\n	<title>")
_e("WordPress &rsaquo; Update")
print("</title>\n	")
wp_admin_css("install", True)
wp_admin_css("ie", True)
print("</head>\n<body class="wp-core-ui">\n<h1 id="logo"><a href="")
esc_attr_e("http://wordpress.org/")
print("">")
_e("WordPress")
print("</a></h1>\n\n")
if get_option("db_version")==wp_db_version||!is_blog_installed():
  print("\n<h2>")
  _e("No Update Required")
  print("</h2>\n<p>")
  _e("Your WordPress database is already up-to-date!")
  print("</p>\n<p class="step"><a class="button button-large" href="")
  print(get_option("home"))
  print("/">")
  _e("Continue")
  print("</a></p>\n\n")
elif !php_compat||!mysql_compat:
  if !mysql_compat&&!php_compat:
    printf(__("You cannot update because <a href="http://codex.wordpress.org/Version_%1$s">WordPress %1$s</a> requires PHP version %2$s or higher and MySQL version %3$s or higher. You are running PHP version %4$s and MySQL version %5$s."), wp_version, required_php_version, required_mysql_version, php_version, mysql_version)
  elif !php_compat:
    printf(__("You cannot update because <a href="http://codex.wordpress.org/Version_%1$s">WordPress %1$s</a> requires PHP version %2$s or higher. You are running version %3$s."), wp_version, required_php_version, php_version)
  elif !mysql_compat:
    printf(__("You cannot update because <a href="http://codex.wordpress.org/Version_%1$s">WordPress %1$s</a> requires MySQL version %2$s or higher. You are running version %3$s."), wp_version, required_mysql_version, mysql_version)
else:
  if step==0:
    goback = stripslashes(wp_get_referer())
    goback = esc_url_raw(goback)
    goback = urlencode(goback)
    print("<h2>")
    _e("Database Update Required")
    print("</h2>\n<p>")
    _e("WordPress has been updated! Before we send you on your way, we have to update your database to the newest version.")
    print("</p>\n<p>")
    _e("The update process may take a little while, so please be patient.")
    print("</p>\n<p class="step"><a class="button button-large" href="upgrade.php?step=1&amp;backto=")
    print(goback)
    print("">")
    _e("Update WordPress Database")
    print("</a></p>\n")
  elif step==1:
    wp_upgrade()
    backto = stripslashes(urldecode(_GET["backto"])) if !empty(_GET["backto"]) else __get_option("home")+"/"
    backto = esc_url(backto)
    backto = wp_validate_redirect(backto, __get_option("home")+"/")
    print("<h2>")
    _e("Update Complete")
    print("</h2>\n	<p>")
    _e("Your WordPress database has been successfully updated!")
    print("</p>\n	<p class="step"><a class="button button-large" href="")
    print(backto)
    print("">")
    _e("Continue")
    print("</a></p>\n\n<!--\n<pre>\n")
    printf(__("%s queries"), wpdb.num_queries)
    print("\n")
    printf(__("%s seconds"), timer_stop(0))
    print("</pre>\n-->\n\n")
print("</body>\n</html>\n")
