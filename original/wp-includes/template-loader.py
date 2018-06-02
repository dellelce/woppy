#!/usr/bin/python
#-*- coding: utf-8 -*-
if defined("WP_USE_THEMES")&&WP_USE_THEMES:
  do_action("template_redirect")
if "HEAD"===_SERVER["REQUEST_METHOD"]&&apply_filters("exit_on_http_head", True):
  exit(0)
if is_robots():
  do_action("do_robots")
  return 
elif is_feed():
  do_feed()
  return 
elif is_trackback():
  include(ABSPATH+"wp-trackback.php")
  return 
if defined("WP_USE_THEMES")&&WP_USE_THEMES:
  template = False
  if is_404()&&template = get_404_template():
  elif is_search()&&template = get_search_template():
  elif is_tax()&&template = get_taxonomy_template():
  elif is_front_page()&&template = get_front_page_template():
  elif is_home()&&template = get_home_template():
  elif is_attachment()&&template = get_attachment_template():
    remove_filter("the_content", "prepend_attachment")
  elif is_single()&&template = get_single_template():
  elif is_page()&&template = get_page_template():
  elif is_category()&&template = get_category_template():
  elif is_tag()&&template = get_tag_template():
  elif is_author()&&template = get_author_template():
  elif is_date()&&template = get_date_template():
  elif is_archive()&&template = get_archive_template():
  elif is_comments_popup()&&template = get_comments_popup_template():
  elif is_paged()&&template = get_paged_template():
  else:
    template = get_index_template()
  if template = apply_filters("template_include", template):
    include(template)
  return 
