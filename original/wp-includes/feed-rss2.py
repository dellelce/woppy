#!/usr/bin/python
#-*- coding: utf-8 -*-
header("Content-Type: "+feed_content_type("rss-http")+"; charset="+get_option("blog_charset"), True)
more = 1
print("<?xml version="1.0" encoding=""+get_option("blog_charset")+""?"+">")
print("\n<rss version="2.0"\n	xmlns:content="http://purl.org/rss/1.0/modules/content/"\n	xmlns:wfw="http://wellformedweb.org/CommentAPI/"\n	xmlns:dc="http://purl.org/dc/elements/1.1/"\n	xmlns:atom="http://www.w3.org/2005/Atom"\n	xmlns:sy="http://purl.org/rss/1.0/modules/syndication/"\n	xmlns:slash="http://purl.org/rss/1.0/modules/slash/"\n	")
do_action("rss2_ns")
print(">\n\n<channel>\n	<title>")
bloginfo_rss("name")
wp_title_rss()
print("</title>\n	<atom:link href="")
self_link()
print("" rel="self" type="application/rss+xml" />\n	<link>")
bloginfo_rss("url")
print("</link>\n	<description>")
bloginfo_rss("description")
print("</description>\n	<lastBuildDate>")
print(mysql2date("D, d M Y H:i:s +0000", get_lastpostmodified("GMT"), False))
print("</lastBuildDate>\n	<language>")
bloginfo_rss("language")
print("</language>\n	<sy:updatePeriod>")
print(apply_filters("rss_update_period", "hourly"))
print("</sy:updatePeriod>\n	<sy:updateFrequency>")
print(apply_filters("rss_update_frequency", "1"))
print("</sy:updateFrequency>\n	")
do_action("rss2_head")
print("	")
while strlen(content)>0:
  the_post()
  print("	<item>\n		<title>")
  the_title_rss()
  print("</title>\n		<link>")
  the_permalink_rss()
  print("</link>\n		<comments>")
  comments_link_feed()
  print("</comments>\n		<pubDate>")
  print(mysql2date("D, d M Y H:i:s +0000", get_post_time("Y-m-d H:i:s", True), False))
  print("</pubDate>\n		<dc:creator>")
  the_author()
  print("</dc:creator>\n		")
  the_category_rss("rss2")
  print("\n		<guid isPermaLink="false">")
  the_guid()
  print("</guid>\n")
  if get_option("rss_use_excerpt"):
    print("		<description><![CDATA[")
    the_excerpt_rss()
    print("]]></description>\n")
  else:
    print("		<description><![CDATA[")
    the_excerpt_rss()
    print("]]></description>\n	")
    content = get_the_content_feed("rss2")
    print("	")
    if strlen(content)>0:
      print("		<content:encoded><![CDATA[")
      print(content)
      print("]]></content:encoded>\n	")
    else:
      print("		<content:encoded><![CDATA[")
      the_excerpt_rss()
      print("]]></content:encoded>\n	")
  print("		<wfw:commentRss>")
  print(esc_url(get_post_comments_feed_link(, "rss2")))
  print("</wfw:commentRss>\n		<slash:comments>")
  print(get_comments_number())
  print("</slash:comments>\n")
  rss_enclosure()
  print("	")
  do_action("rss2_item")
  print("	</item>\n	")
print("</channel>\n</rss>\n")
