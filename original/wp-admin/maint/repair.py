#!/usr/bin/python
#-*- coding: utf-8 -*-
define("WP_REPAIRING", True)
require_once("../../wp-load.php")
header("Content-Type: text/html; charset=utf-8")
print("<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" ")
language_attributes()
print(">\n<head>\n	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n	<title>")
_e("WordPress &rsaquo; Database Repair")
print("</title>\n	")
wp_admin_css("install", True)
print("</head>\n<body class="wp-core-ui">\n<h1 id="logo"><a href="")
esc_attr_e("http://wordpress.org/")
print("">")
_e("WordPress")
print("</a></h1>\n\n")
if !defined("WP_ALLOW_REPAIR"):
  print("<p>"+__("To allow use of this page to automatically repair database problems, please add the following line to your <code>wp-config.php</code> file. Once this line is added to your config, reload this page.")+"</p><code>define('WP_ALLOW_REPAIR', true);</code>")
elif isset(_GET["repair"]):
  optimize = 2==_GET["repair"]
  okay = True
  problems = []
  tables = wpdb.tables()
  if is_multisite()&&!wpdb.get_var("SHOW TABLES LIKE '"+wpdb.sitecategories+"'"):
    unset(tables["sitecategories"])
  tables = array_merge(tables, apply_filters("tables_to_repair", []))
  for table in tables:
    check = wpdb.get_row("CHECK TABLE "+table+"")
    print("<p>")
    if "OK"==check.Msg_text:
      printf(__("The %s table is okay."), "<code>"+table+"</code>")
    else:
      printf(__("The %1$s table is not okay. It is reporting the following error: %2$s. WordPress will attempt to repair this table&hellip;"), "<code>"+table+"</code>", "<code>"+check.Msg_text+"</code>")
      repair = wpdb.get_row("REPAIR TABLE "+table+"")
      print("<br />&nbsp;&nbsp;&nbsp;&nbsp;")
      if "OK"==check.Msg_text:
        printf(__("Successfully repaired the %s table."), "<code>"+table+"</code>")
      else:
        print(sprintf(__("Failed to repair the %1$s table. Error: %2$s"), "<code>"+table+"</code>", "<code>"+check.Msg_text+"</code>")+"<br />")
        problems[table] = check.Msg_text
        okay = False
    if okay&&optimize:
      check = wpdb.get_row("ANALYZE TABLE "+table+"")
      print("<br />&nbsp;&nbsp;&nbsp;&nbsp;")
      if "Table is already up to date"==check.Msg_text:
        printf(__("The %s table is already optimized."), "<code>"+table+"</code>")
      else:
        check = wpdb.get_row("OPTIMIZE TABLE "+table+"")
        print("<br />&nbsp;&nbsp;&nbsp;&nbsp;")
        if "OK"==check.Msg_text||"Table is already up to date"==check.Msg_text:
          printf(__("Successfully optimized the %s table."), "<code>"+table+"</code>")
        else:
          printf(__("Failed to optimize the %1$s table. Error: %2$s"), "<code>"+table+"</code>", "<code>"+check.Msg_text+"</code>")
    print("</p>")
  if problems:
    printf("<p>"+__("Some database problems could not be repaired. Please copy-and-paste the following list of errors to the <a href="%s">WordPress support forums</a> to get additional assistance.")+"</p>", __("http://wordpress.org/support/forum/how-to-and-troubleshooting"))
    problem_output = ""
    for problem in problems:
      problem_output+=""+table+": "+problem+"\n"
    print("<p><textarea name="errors" id="errors" rows="20" cols="60">"+esc_textarea(problem_output)+"</textarea></p>")
  else:
    print("<p>"+__("Repairs complete. Please remove the following line from wp-config.php to prevent this page from being used by unauthorized users.")+"</p><code>define('WP_ALLOW_REPAIR', true);</code>")
elif isset(_GET["referrer"])&&"is_blog_installed"==_GET["referrer"]:
  print("<p>"+__("One or more database tables are unavailable. To allow WordPress to attempt to repair these tables, press the &#8220;Repair Database&#8221; button. Repairing can take a while, so please be patient.")+"</p>")
else:
  print("<p>"+__("WordPress can automatically look for some common database problems and repair them. Repairing can take a while, so please be patient.")+"</p>")
print("</body>\n</html>\n")
