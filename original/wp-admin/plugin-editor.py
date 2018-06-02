#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if is_multisite()&&!is_network_admin():
  wp_redirect(network_admin_url("plugin-editor.php"))
  exit(0)
if !current_user_can("edit_plugins"):
  wp_die(__("You do not have sufficient permissions to edit plugins for this site."))
title = __("Edit Plugins")
parent_file = "plugins.php"
wp_reset_vars(["action", "redirect", "profile", "error", "warning", "a", "file", "plugin"])
plugins = get_plugins()
if empty(plugins):
  wp_die(__("There are no plugins installed on this site."))
if isset(_REQUEST["file"]):
  plugin = stripslashes(_REQUEST["file"])
if empty(plugin):
  plugin = array_keys(plugins)
  plugin = plugin[0]
plugin_files = get_plugin_files(plugin)
if empty(file):
  file = plugin_files[0]
else:
  file = stripslashes(file)
file = validate_file_to_edit(file, plugin_files)
real_file = WP_PLUGIN_DIR+"/"+file
scrollto = _REQUEST["scrollto"] if isset(_REQUEST["scrollto"]) else 0
if action=="update":
  check_admin_referer("edit-plugin_"+file)
  newcontent = stripslashes(_POST["newcontent"])
  if is_writeable(real_file):
    f = fopen(real_file, "w+")
    fwrite(f, newcontent)
    fclose(f)
    network_wide = is_plugin_active_for_network(file)
    if is_plugin_active(file)||isset(_POST["phperror"]):
      if is_plugin_active(file):
        deactivate_plugins(file, True)
      if !is_network_admin():
        update_option("recently_activated", {file:time()}+get_option("recently_activated"))
      wp_redirect(add_query_arg("_wpnonce", wp_create_nonce("edit-plugin-test_"+file), "plugin-editor.php?file="+file+"&liveupdate=1&scrollto="+scrollto+"&networkwide="+network_wide))
      exit(0)
    wp_redirect(self_admin_url("plugin-editor.php?file="+file+"&a=te&scrollto="+scrollto+""))
  else:
    wp_redirect(self_admin_url("plugin-editor.php?file="+file+"&scrollto="+scrollto+""))
  exit(0)
else:
  if isset(_GET["liveupdate"]):
    check_admin_referer("edit-plugin-test_"+file)
    error = validate_plugin(file)
    if is_wp_error(error):
      wp_die(error)
    if !empty(_GET["networkwide"])&&!is_plugin_active_for_network(file)||!is_plugin_active(file):
      activate_plugin(file, "plugin-editor.php?file="+file+"&phperror=1", !empty(_GET["networkwide"]))
    wp_redirect(self_admin_url("plugin-editor.php?file="+file+"&a=te&scrollto="+scrollto+""))
    exit(0)
  editable_extensions = ["php", "txt", "text", "js", "css", "html", "htm", "xml", "inc", "include"]
  editable_extensions = apply_filters("editable_extensions", editable_extensions)
  if !is_file(real_file):
    wp_die(sprintf("<p>%s</p>", __("No such file exists! Double check the name and try again.")))
  elif preg_match("/\.([^.]+)$/", real_file, matches):
    ext = strtolower(matches[1])
    if !in_array(ext, editable_extensions):
      wp_die(sprintf("<p>%s</p>", __("Files of this type are not editable.")))
  get_current_screen()
  get_current_screen()
  require_once(ABSPATH+"wp-admin/admin-header.php")
  update_recently_edited(WP_PLUGIN_DIR+"/"+file)
  content = file_get_contents(real_file)
  if ".php"==substr(real_file, strrpos(real_file, ".")):
    functions = wp_doc_link_parse(content)
    if !empty(functions):
      docs_select = "<select name="docs-list" id="docs-list">"
      docs_select+="<option value="">"+__("Function Name&hellip;")+"</option>"
      for function in functions:
        docs_select+="<option value=""+esc_attr(function)+"">"+esc_html(function)+"()</option>"
      docs_select+="</select>"
  content = esc_textarea(content)
  if isset(_GET["a"]):
    print(" <div id="message" class="updated"><p>")
    _e("File edited successfully.")
    print("</p></div>\n")
  elif isset(_GET["phperror"]):
    print(" <div id="message" class="updated"><p>")
    _e("This plugin has been deactivated because your changes resulted in a <strong>fatal error</strong>.")
    print("</p>\n	")
    if wp_verify_nonce(_GET["_error_nonce"], "plugin-activation-error_"+file):
      print("	<iframe style="border:0" width="100%" height="70px" src="")
      bloginfo("wpurl")
      print("/wp-admin/plugins.php?action=error_scrape&amp;plugin=")
      print(esc_attr(file))
      print("&amp;_wpnonce=")
      print(esc_attr(_GET["_error_nonce"]))
      print(""></iframe>\n	")
    print("</div>\n")
  print("<div class="wrap">\n")
  screen_icon()
  print("<h2>")
  print(esc_html(title))
  print("</h2>\n\n<div class="fileedit-sub">\n<div class="alignleft">\n<big>")
  if is_plugin_active(plugin):
    if is_writeable(real_file):
      print(sprintf(__("Editing <strong>%s</strong> (active)"), file))
    else:
      print(sprintf(__("Browsing <strong>%s</strong> (active)"), file))
  elif is_writeable(real_file):
    print(sprintf(__("Editing <strong>%s</strong> (inactive)"), file))
  else:
    print(sprintf(__("Browsing <strong>%s</strong> (inactive)"), file))
  print("</big>\n</div>\n<div class="alignright">\n	<form action="plugin-editor.php" method="post">\n		<strong><label for="plugin">")
  _e("Select plugin to edit:")
  print(" </label></strong>\n		<select name="plugin" id="plugin">\n")
  for a_plugin in plugins:
    plugin_name = a_plugin["Name"]
    if plugin_key==plugin:
      selected = " selected='selected'"
    else:
      selected = ""
    plugin_name = esc_attr(plugin_name)
    plugin_key = esc_attr(plugin_key)
    print("\n	<option value=""+plugin_key+"" "+selected+">"+plugin_name+"</option>")
  print("		</select>\n		")
  submit_button(__("Select"), "button", "Submit", False)
  print("	</form>\n</div>\n<br class="clear" />\n</div>\n\n<div id="templateside">\n	<h3>")
  _e("Plugin Files")
  print("</h3>\n\n	<ul>\n")
  for plugin_file in plugin_files:
    if preg_match("/\.([^.]+)$/", plugin_file, matches):
      ext = strtolower(matches[1])
      if !in_array(ext, editable_extensions):
    else:
    print("		<li")
    print(" class="highlight"" if file==plugin_file else "")
    print("><a href="plugin-editor.php?file=")
    print(urlencode(plugin_file))
    print("&amp;plugin=")
    print(urlencode(plugin))
    print("">")
    print(plugin_file)
    print("</a></li>\n")
  print("	</ul>\n</div>\n<form name="template" id="template" action="plugin-editor.php" method="post">\n	")
  wp_nonce_field("edit-plugin_"+file)
  print("		<div><textarea cols="70" rows="25" name="newcontent" id="newcontent" aria-describedby="newcontent-description">")
  print(content)
  print("</textarea>\n		<input type="hidden" name="action" value="update" />\n		<input type="hidden" name="file" value="")
  print(esc_attr(file))
  print("" />\n		<input type="hidden" name="plugin" value="")
  print(esc_attr(plugin))
  print("" />\n		<input type="hidden" name="scrollto" id="scrollto" value="")
  print(scrollto)
  print("" />\n		</div>\n		")
  if !empty(docs_select):
    print("		<div id="documentation" class="hide-if-no-js"><label for="docs-list">")
    _e("Documentation:")
    print("</label> ")
    print(docs_select)
    print(" <input type="button" class="button" value="")
    esc_attr_e("Lookup")
    print(" " onclick="if ( '' != jQuery('#docs-list').val() ) { window.open( 'http://api.wordpress.org/core/handbook/1.0/?function=' + escape( jQuery( '#docs-list' ).val() ) + '&amp;locale=")
    print(urlencode(get_locale()))
    print("&amp;version=")
    print(urlencode(wp_version))
    print("&amp;redirect=true'); }" /></div>\n		")
  if is_writeable(real_file):
    print("	")
    if in_array(file, get_option("active_plugins", [])):
      print("		<p>")
      _e("<strong>Warning:</strong> Making changes to active plugins is not recommended. If your changes cause a fatal error, the plugin will be automatically deactivated.")
      print("</p>\n	")
    print("	<p class="submit">\n	")
    if isset(_GET["phperror"]):
      print("<input type='hidden' name='phperror' value='1' />")
      submit_button(__("Update File and Attempt to Reactivate"), "primary", "submit", False)
    else:
      submit_button(__("Update File"), "primary", "submit", False)
    print("	</p>\n")
  else:
    print("	<p><em>")
    _e("You need to make this file writable before you can save your changes. See <a href="http://codex.wordpress.org/Changing_File_Permissions">the Codex</a> for more information.")
    print("</em></p>\n")
  print("</form>\n<br class="clear" />\n</div>\n<script type="text/javascript">\njQuery(document).ready(function($){\n	$('#template').submit(function(){ $('#scrollto').val( $('#newcontent').scrollTop() ); });\n	$('#newcontent').scrollTop( $('#scrollto').val() );\n});\n</script>\n")
include(ABSPATH+"wp-admin/admin-footer.php")
