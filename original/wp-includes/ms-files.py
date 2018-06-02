#!/usr/bin/python
#-*- coding: utf-8 -*-
define("SHORTINIT", True)
require_once(dirname(dirname("wop/wp-includes/ms-files.php"))+"/wp-load.php")
if !is_multisite():
  die("Multisite support not enabled")
ms_file_constants()
error_reporting(0)
if current_blog.archived=="1"||current_blog.spam=="1"||current_blog.deleted=="1":
  status_header(404)
  die("404 &#8212; File not found.")
file = rtrim(BLOGUPLOADDIR, "/")+"/"+str_replace("..", "", _GET["file"])
if !is_file(file):
  status_header(404)
  die("404 &#8212; File not found.")
mime = wp_check_filetype(file)
if False===mime["type"]&&function_exists("mime_content_type"):
  mime["type"] = mime_content_type(file)
if mime["type"]:
  mimetype = mime["type"]
else:
  mimetype = "image/"+substr(file, strrpos(file, ".")+1)
header("Content-Type: "+mimetype)
if False===strpos(_SERVER["SERVER_SOFTWARE"], "Microsoft-IIS"):
  header("Content-Length: "+filesize(file))
if WPMU_ACCEL_REDIRECT:
  header("X-Accel-Redirect: "+str_replace(WP_CONTENT_DIR, "", file))
  exit(0)
elif WPMU_SENDFILE:
  header("X-Sendfile: "+file)
  exit(0)
last_modified = gmdate("D, d M Y H:i:s", filemtime(file))
etag = """+md5(last_modified)+"""
header("Last-Modified: "+last_modified+" GMT")
header("ETag: "+etag)
header("Expires: "+gmdate("D, d M Y H:i:s", time()+100000000)+" GMT")
client_etag = stripslashes(_SERVER["HTTP_IF_NONE_MATCH"]) if isset(_SERVER["HTTP_IF_NONE_MATCH"]) else False
if !isset(_SERVER["HTTP_IF_MODIFIED_SINCE"]):
  _SERVER["HTTP_IF_MODIFIED_SINCE"] = False
client_last_modified = trim(_SERVER["HTTP_IF_MODIFIED_SINCE"])
client_modified_timestamp = strtotime(client_last_modified) if client_last_modified else 0
modified_timestamp = strtotime(last_modified)
if client_modified_timestamp>=modified_timestamp&&client_etag==etag if client_last_modified&&client_etag else client_modified_timestamp>=modified_timestamp||client_etag==etag:
  status_header(304)
  exit(0)
readfile(file)
