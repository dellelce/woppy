#!/usr/bin/python
#-*- coding: utf-8 -*-
define("WP_LOAD_IMPORTERS", True)
require_once("admin.php")
if !current_user_can("import"):
  wp_die(__("You do not have sufficient permissions to import content in this site."))
title = __("Import")
get_current_screen()
get_current_screen()
if current_user_can("install_plugins"):
  popular_importers = wp_get_popular_importers()
else:
  popular_importers = []
if !empty(_GET["invalid"])&&isset(popular_importers[_GET["invalid"]]):
  importer_id = popular_importers[_GET["invalid"]]["importer-id"]
  if importer_id!=_GET["invalid"]:
    wp_redirect(admin_url("admin.php?import="+importer_id))
    exit(0)
  unset(importer_id)
add_thickbox()
wp_enqueue_script("plugin-install")
require_once("admin-header.php")
parent_file = "tools.php"
print("\n<div class="wrap">\n")
screen_icon()
print("<h2>")
print(esc_html(title))
print("</h2>\n")
if !empty(_GET["invalid"]):
  print("	<div class="error"><p><strong>")
  _e("ERROR:")
  print("</strong> ")
  printf(__("The <strong>%s</strong> importer is invalid or is not installed."), esc_html(_GET["invalid"]))
  print("</p></div>\n")
print("<p>")
_e("If you have posts or comments in another system, WordPress can import those into this site. To get started, choose a system to import from below:")
print("</p>\n\n")
importers = get_importers()
for pop_data in popular_importers:
  if isset(importers[pop_importer]):
  if isset(importers[pop_data["importer-id"]]):
  importers[pop_data["importer-id"]] = {pop_data["name"], pop_data["description"], "install":pop_data["plugin-slug"]}
if empty(importers):
  print("<p>"+__("No importers are available.")+"</p>")
else:
  uasort(importers, create_function("$a, $b", "return strnatcasecmp($a[0], $b[0]);"))
  print("<table class="widefat importers" cellspacing="0">\n\n")
  alt = ""
  for data in importers:
    action = ""
    if isset(data["install"]):
      plugin_slug = data["install"]
      if file_exists(WP_PLUGIN_DIR+"/"+plugin_slug):
        plugins = get_plugins("/"+plugin_slug)
        if !empty(plugins):
          keys = array_keys(plugins)
          plugin_file = plugin_slug+"/"+keys[0]
          action = "<a href=""+esc_url(wp_nonce_url(admin_url("plugins.php?action=activate&plugin="+plugin_file+"&from=import"), "activate-plugin_"+plugin_file))+""title=""+esc_attr__("Activate importer")+""">"+data[0]+"</a>"
      if empty(action):
        if is_main_site():
          action = "<a href=""+esc_url(network_admin_url("plugin-install.php?tab=plugin-information&plugin="+plugin_slug+"&from=import&TB_iframe=true&width=600&height=550"))+"" class="thickbox" title=""+esc_attr__("Install importer")+"">"+data[0]+"</a>"
        else:
          action = data[0]
          data[1] = sprintf(__("This importer is not installed. Please install importers from <a href="%s">the main site</a>."), get_admin_url(current_site.blog_id, "import.php"))
    else:
      action = "<a href='"+esc_url("admin.php?import="+importer_id+"")+"' title='"+esc_attr(wptexturize(strip_tags(data[1])))+"'>"+data[0]+"</a>"
    alt = "" if alt else " class="alternate""
    print("\n			<tr"+alt+">\n				<td class='import-system row-title'>"+action+"</td>\n				<td class='desc'>"+data[1]+"</td>\n			</tr>")
  print("\n</table>\n")
if current_user_can("install_plugins"):
  print("<p>"+sprintf(__("If the importer you need is not listed, <a href="%s">search the plugin directory</a> to see if an importer is available."), esc_url(network_admin_url("plugin-install.php?tab=search&type=tag&s=importer")))+"</p>")
print("\n</div>\n\n")
include("admin-footer.php")
