#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./wp-load.php")
header("Content-Type: text/xml; charset="+get_option("blog_charset"), True)
link_cat = ""
if !empty(_GET["link_cat"]):
  link_cat = _GET["link_cat"]
  if !in_array(link_cat, ["all", "0"]):
    link_cat = absint(urldecode(link_cat))
print("<?xml version="1.0"?"+">\n")
print("<opml version="1.0">\n	<head>\n		<title>")
printf(__("Links for %s"), esc_attr(get_bloginfo("name", "display")))
print("</title>\n		<dateCreated>")
print(gmdate("D, d M Y H:i:s"))
print(" GMT</dateCreated>\n		")
do_action("opml_head")
print("	</head>\n	<body>\n")
if empty(link_cat):
  cats = get_categories({"taxonomy":"link_category", "hierarchical":0})
else:
  cats = get_categories({"taxonomy":"link_category", "hierarchical":0, "include":link_cat})
for cat in cats:
  catname = apply_filters("link_category", cat.name)
  print("<outline type="category" title="")
  print(esc_attr(catname))
  print("">\n")
  bookmarks = get_bookmarks({"category":cat.term_id})
  for bookmark in bookmarks:
    title = apply_filters("link_title", bookmark.link_name)
    print("	<outline text="")
    print(esc_attr(title))
    print("" type="link" xmlUrl="")
    print(esc_attr(bookmark.link_rss))
    print("" htmlUrl="")
    print(esc_attr(bookmark.link_url))
    print("" updated="")
    if "0000-00-00 00:00:00"!=bookmark.link_updated:
      print(bookmark.link_updated)
    print("" />\n")
  print("</outline>\n")
print("</body>\n</opml>")
