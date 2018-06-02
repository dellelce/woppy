#!/usr/bin/python
#-*- coding: utf-8 -*-
if !defined("IFRAME_REQUEST")&&isset(_GET["action"])&&in_array(_GET["action"], ["update-selected", "activate-plugin", "update-selected-themes"]):
  define("IFRAME_REQUEST", True)
require_once("./admin.php")
include_once(ABSPATH+"wp-admin/includes/class-wp-upgrader.php")
if isset(_GET["action"]):
  plugin = trim(_REQUEST["plugin"]) if isset(_REQUEST["plugin"]) else ""
  theme = urldecode(_REQUEST["theme"]) if isset(_REQUEST["theme"]) else ""
  action = _REQUEST["action"] if isset(_REQUEST["action"]) else ""
  if "update-selected"==action:
    if !current_user_can("update_plugins"):
      wp_die(__("You do not have sufficient permissions to update plugins for this site."))
    check_admin_referer("bulk-update-plugins")
    if isset(_GET["plugins"]):
      plugins = explode(",", stripslashes(_GET["plugins"]))
    elif isset(_POST["checked"]):
      plugins = _POST["checked"]
    else:
      plugins = []
    plugins = array_map("urldecode", plugins)
    url = "update.php?action=update-selected&amp;plugins="+urlencode(implode(",", plugins))
    nonce = "bulk-update-plugins"
    wp_enqueue_script("jquery")
    iframe_header()
    upgrader = Plugin_Upgrader(Bulk_Plugin_Upgrader_Skin(compact("nonce", "url")))
    upgrader.bulk_upgrade(plugins)
    iframe_footer()
  elif "upgrade-plugin"==action:
    if !current_user_can("update_plugins"):
      wp_die(__("You do not have sufficient permissions to update plugins for this site."))
    check_admin_referer("upgrade-plugin_"+plugin)
    title = __("Update Plugin")
    parent_file = "plugins.php"
    submenu_file = "plugins.php"
    require_once(ABSPATH+"wp-admin/admin-header.php")
    nonce = "upgrade-plugin_"+plugin
    url = "update.php?action=upgrade-plugin&plugin="+plugin
    upgrader = Plugin_Upgrader(Plugin_Upgrader_Skin(compact("title", "nonce", "url", "plugin")))
    upgrader.upgrade(plugin)
    include(ABSPATH+"wp-admin/admin-footer.php")
  elif "activate-plugin"==action:
    if !current_user_can("update_plugins"):
      wp_die(__("You do not have sufficient permissions to update plugins for this site."))
    check_admin_referer("activate-plugin_"+plugin)
    if !isset(_GET["failure"])&&!isset(_GET["success"]):
      wp_redirect(admin_url("update.php?action=activate-plugin&failure=true&plugin="+plugin+"&_wpnonce="+_GET["_wpnonce"]))
      activate_plugin(plugin, "", !empty(_GET["networkwide"]), True)
      wp_redirect(admin_url("update.php?action=activate-plugin&success=true&plugin="+plugin+"&_wpnonce="+_GET["_wpnonce"]))
      die(0)
    iframe_header(__("Plugin Reactivation"), True)
    if isset(_GET["success"]):
      print("<p>"+__("Plugin reactivated successfully.")+"</p>")
    if isset(_GET["failure"]):
      print("<p>"+__("Plugin failed to reactivate due to a fatal error.")+"</p>")
      error_reporting(E_CORE_ERROR|E_CORE_WARNING|E_COMPILE_ERROR|E_ERROR|E_WARNING|E_PARSE|E_USER_ERROR|E_USER_WARNING|E_RECOVERABLE_ERROR)
      ini_set("display_errors", True)
      include(WP_PLUGIN_DIR+"/"+plugin)
    iframe_footer()
  elif "install-plugin"==action:
    if !current_user_can("install_plugins"):
      wp_die(__("You do not have sufficient permissions to install plugins on this site."))
    include_once(ABSPATH+"wp-admin/includes/plugin-install.php")
    check_admin_referer("install-plugin_"+plugin)
    api = plugins_api("plugin_information", {"slug":plugin, "fields":{"sections":False}})
    if is_wp_error(api):
      wp_die(api)
    title = __("Plugin Install")
    parent_file = "plugins.php"
    submenu_file = "plugin-install.php"
    require_once(ABSPATH+"wp-admin/admin-header.php")
    title = sprintf(__("Installing Plugin: %s"), api.name+" "+api.version)
    nonce = "install-plugin_"+plugin
    url = "update.php?action=install-plugin&plugin="+plugin
    if isset(_GET["from"]):
      url+="&from="+urlencode(stripslashes(_GET["from"]))
    type = "web"
    upgrader = Plugin_Upgrader(Plugin_Installer_Skin(compact("title", "url", "nonce", "plugin", "api")))
    upgrader.install(api.download_link)
    include(ABSPATH+"wp-admin/admin-footer.php")
  elif "upload-plugin"==action:
    if !current_user_can("install_plugins"):
      wp_die(__("You do not have sufficient permissions to install plugins on this site."))
    check_admin_referer("plugin-upload")
    file_upload = File_Upload_Upgrader("pluginzip", "package")
    title = __("Upload Plugin")
    parent_file = "plugins.php"
    submenu_file = "plugin-install.php"
    require_once(ABSPATH+"wp-admin/admin-header.php")
    title = sprintf(__("Installing Plugin from uploaded file: %s"), basename(file_upload.filename))
    nonce = "plugin-upload"
    url = add_query_arg({"package":file_upload.id}, "update.php?action=upload-plugin")
    type = "upload"
    upgrader = Plugin_Upgrader(Plugin_Installer_Skin(compact("type", "title", "nonce", "url")))
    result = upgrader.install(file_upload.package)
    if result||is_wp_error(result):
      file_upload.cleanup()
    include(ABSPATH+"wp-admin/admin-footer.php")
  elif "upgrade-theme"==action:
    if !current_user_can("update_themes"):
      wp_die(__("You do not have sufficient permissions to update themes for this site."))
    check_admin_referer("upgrade-theme_"+theme)
    wp_enqueue_script("customize-loader")
    title = __("Update Theme")
    parent_file = "themes.php"
    submenu_file = "themes.php"
    require_once(ABSPATH+"wp-admin/admin-header.php")
    nonce = "upgrade-theme_"+theme
    url = "update.php?action=upgrade-theme&theme="+theme
    upgrader = Theme_Upgrader(Theme_Upgrader_Skin(compact("title", "nonce", "url", "theme")))
    upgrader.upgrade(theme)
    include(ABSPATH+"wp-admin/admin-footer.php")
  elif "update-selected-themes"==action:
    if !current_user_can("update_themes"):
      wp_die(__("You do not have sufficient permissions to update themes for this site."))
    check_admin_referer("bulk-update-themes")
    if isset(_GET["themes"]):
      themes = explode(",", stripslashes(_GET["themes"]))
    elif isset(_POST["checked"]):
      themes = _POST["checked"]
    else:
      themes = []
    themes = array_map("urldecode", themes)
    url = "update.php?action=update-selected-themes&amp;themes="+urlencode(implode(",", themes))
    nonce = "bulk-update-themes"
    wp_enqueue_script("jquery")
    iframe_header()
    upgrader = Theme_Upgrader(Bulk_Theme_Upgrader_Skin(compact("nonce", "url")))
    upgrader.bulk_upgrade(themes)
    iframe_footer()
  elif "install-theme"==action:
    if !current_user_can("install_themes"):
      wp_die(__("You do not have sufficient permissions to install themes on this site."))
    include_once(ABSPATH+"wp-admin/includes/theme-install.php")
    check_admin_referer("install-theme_"+theme)
    api = themes_api("theme_information", {"slug":theme, "fields":{"sections":False, "tags":False}})
    if is_wp_error(api):
      wp_die(api)
    wp_enqueue_script("customize-loader")
    title = __("Install Themes")
    parent_file = "themes.php"
    submenu_file = "themes.php"
    require_once(ABSPATH+"wp-admin/admin-header.php")
    title = sprintf(__("Installing Theme: %s"), api.name+" "+api.version)
    nonce = "install-theme_"+theme
    url = "update.php?action=install-theme&theme="+theme
    type = "web"
    upgrader = Theme_Upgrader(Theme_Installer_Skin(compact("title", "url", "nonce", "plugin", "api")))
    upgrader.install(api.download_link)
    include(ABSPATH+"wp-admin/admin-footer.php")
  elif "upload-theme"==action:
    if !current_user_can("install_themes"):
      wp_die(__("You do not have sufficient permissions to install themes on this site."))
    check_admin_referer("theme-upload")
    file_upload = File_Upload_Upgrader("themezip", "package")
    wp_enqueue_script("customize-loader")
    title = __("Upload Theme")
    parent_file = "themes.php"
    submenu_file = "theme-install.php"
    require_once(ABSPATH+"wp-admin/admin-header.php")
    title = sprintf(__("Installing Theme from uploaded file: %s"), basename(file_upload.filename))
    nonce = "theme-upload"
    url = add_query_arg({"package":file_upload.id}, "update.php?action=upload-theme")
    type = "upload"
    upgrader = Theme_Upgrader(Theme_Installer_Skin(compact("type", "title", "nonce", "url")))
    result = upgrader.install(file_upload.package)
    if result||is_wp_error(result):
      file_upload.cleanup()
    include(ABSPATH+"wp-admin/admin-footer.php")
  else:
    do_action("update-custom_"+action)
