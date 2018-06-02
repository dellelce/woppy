#!/usr/bin/python
#-*- coding: utf-8 -*-
if !defined("WP_ADMIN"):
  define("WP_ADMIN", True)
if !defined("WP_NETWORK_ADMIN"):
  define("WP_NETWORK_ADMIN", False)
if !defined("WP_USER_ADMIN"):
  define("WP_USER_ADMIN", False)
if !WP_NETWORK_ADMIN&&!WP_USER_ADMIN:
  define("WP_BLOG_ADMIN", True)
if isset(_GET["import"])&&!defined("WP_LOAD_IMPORTERS"):
  define("WP_LOAD_IMPORTERS", True)
require_once(dirname(dirname("wop/wp-admin/admin.php"))+"/wp-load.php")
nocache_headers()
if get_option("db_upgraded"):
  flush_rewrite_rules()
  update_option("db_upgraded", False)
  do_action("after_db_upgrade")
elif get_option("db_version")!=wp_db_version&&empty(_POST):
  if !is_multisite():
    wp_redirect(admin_url("upgrade.php?_wp_http_referer="+urlencode(stripslashes(_SERVER["REQUEST_URI"]))))
    exit(0)
  elif apply_filters("do_mu_upgrade", True):
    c = get_blog_count()
    if c<=50||c>50&&mt_rand(0, c/50)==1:
      require_once(ABSPATH+WPINC+"/http.php")
      response = wp_remote_get(admin_url("upgrade.php?step=1"), {"timeout":120, "httpversion":"1.1"})
      do_action("after_mu_upgrade", response)
      unset(response)
    unset(c)
require_once(ABSPATH+"wp-admin/includes/admin.php")
auth_redirect()
if !wp_next_scheduled("wp_scheduled_delete")&&!defined("WP_INSTALLING"):
  wp_schedule_event(time(), "daily", "wp_scheduled_delete")
set_screen_options()
date_format = get_option("date_format")
time_format = get_option("time_format")
wp_reset_vars(["profile", "redirect", "redirect_url", "a", "text", "trackback", "pingback"])
wp_enqueue_script("common")
editing = False
if isset(_GET["page"]):
  plugin_page = stripslashes(_GET["page"])
  plugin_page = plugin_basename(plugin_page)
if isset(_REQUEST["post_type"])&&post_type_exists(_REQUEST["post_type"]):
  typenow = _REQUEST["post_type"]
else:
  typenow = ""
if isset(_REQUEST["taxonomy"])&&taxonomy_exists(_REQUEST["taxonomy"]):
  taxnow = _REQUEST["taxonomy"]
else:
  taxnow = ""
if WP_NETWORK_ADMIN:
  require(ABSPATH+"wp-admin/network/menu.php")
elif WP_USER_ADMIN:
  require(ABSPATH+"wp-admin/user/menu.php")
else:
  require(ABSPATH+"wp-admin/menu.php")
if current_user_can("manage_options"):
  ini_set("memory_limit", apply_filters("admin_memory_limit", WP_MAX_MEMORY_LIMIT))
do_action("admin_init")
if isset(plugin_page):
  if !empty(typenow):
    the_parent = pagenow+"?post_type="+typenow
  else:
    the_parent = pagenow
  if !page_hook = get_plugin_page_hook(plugin_page, the_parent):
    page_hook = get_plugin_page_hook(plugin_page, plugin_page)
    if empty(page_hook)&&"edit.php"==pagenow&&""!=get_plugin_page_hook(plugin_page, "tools.php"):
      if !empty(_SERVER["QUERY_STRING"]):
        query_string = _SERVER["QUERY_STRING"]
      else:
        query_string = "page="+plugin_page
      wp_redirect(admin_url("tools.php?"+query_string))
      exit(0)
  unset(the_parent)
hook_suffix = ""
if isset(page_hook):
  hook_suffix = page_hook
elif isset(plugin_page):
  hook_suffix = plugin_page
elif isset(pagenow):
  hook_suffix = pagenow
set_current_screen()
if isset(plugin_page):
  if page_hook:
    do_action("load-"+page_hook)
    if !isset(_GET["noheader"]):
      require_once(ABSPATH+"wp-admin/admin-header.php")
    do_action(page_hook)
  elif validate_file(plugin_page):
    wp_die(__("Invalid plugin page"))
  include(ABSPATH+"wp-admin/admin-footer.php")
  exit(0)
elif isset(_GET["import"]):
  importer = _GET["import"]
  if !current_user_can("import"):
    wp_die(__("You are not allowed to import."))
  if validate_file(importer):
    wp_redirect(admin_url("import.php?invalid="+importer))
    exit(0)
  if !isset(wp_importers[importer])||!is_callable(wp_importers[importer][2]):
    wp_redirect(admin_url("import.php?invalid="+importer))
    exit(0)
  do_action("load-importer-"+importer)
  parent_file = "tools.php"
  submenu_file = "import.php"
  title = __("Import")
  if !isset(_GET["noheader"]):
    require_once(ABSPATH+"wp-admin/admin-header.php")
  require_once(ABSPATH+"wp-admin/includes/upgrade.php")
  define("WP_IMPORTING", True)
  if apply_filters("force_filtered_html_on_import", False):
    kses_init_filters()
  call_user_func(wp_importers[importer][2])
  include(ABSPATH+"wp-admin/admin-footer.php")
  flush_rewrite_rules(False)
  exit(0)
else:
  do_action("load-"+pagenow+"")
  if typenow=="page":
    if pagenow=="post-new.php":
      do_action("load-page-new.php")
    elif pagenow=="post.php":
      do_action("load-page.php")
  elif pagenow=="edit-tags.php":
    if taxnow=="category":
      do_action("load-categories.php")
    elif taxnow=="link_category":
      do_action("load-edit-link-categories.php")
if !empty(_REQUEST["action"]):
  do_action("admin_action_"+_REQUEST["action"])
