#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if is_multisite()&&!is_network_admin():
  wp_redirect(network_admin_url("theme-editor.php"))
  exit(0)
if !current_user_can("edit_themes"):
  wp_die("<p>"+__("You do not have sufficient permissions to edit templates for this site.")+"</p>")
title = __("Edit Themes")
parent_file = "themes.php"
get_current_screen()
get_current_screen()
wp_reset_vars(["action", "error", "file", "theme"])
if theme:
  stylesheet = theme
else:
  stylesheet = get_stylesheet()
theme = wp_get_theme(stylesheet)
if !theme.exists():
  wp_die(__("The requested theme does not exist."))
if theme.errors()&&"theme_no_stylesheet"==errors():
  wp_die(__("The requested theme does not exist.")+" "+errors())
allowed_files = theme.get_files("php", 1)
has_templates = !empty(allowed_files)
style_files = theme.get_files("css")
allowed_files["style.css"] = style_files["style.css"]
allowed_files+=style_files
if empty(file):
  relative_file = "style.css"
  file = allowed_files["style.css"]
else:
  relative_file = stripslashes(file)
  file = theme.get_stylesheet_directory()+"/"+relative_file
validate_file_to_edit(file, allowed_files)
scrollto = _REQUEST["scrollto"] if isset(_REQUEST["scrollto"]) else 0
if action=="update":
  check_admin_referer("edit-theme_"+file+stylesheet)
  newcontent = stripslashes(_POST["newcontent"])
  location = "theme-editor.php?file="+urlencode(relative_file)+"&theme="+urlencode(stylesheet)+"&scrollto="+scrollto
  if is_writeable(file):
    f = fopen(file, "w+")
    if f!==False:
      fwrite(f, newcontent)
      fclose(f)
      location+="&updated=true"
      theme.cache_delete()
  wp_redirect(location)
  exit(0)
else:
  require_once(ABSPATH+"wp-admin/admin-header.php")
  update_recently_edited(file)
  if !is_file(file):
    error = True
  content = ""
  if !error&&filesize(file)>0:
    f = fopen(file, "r")
    content = fread(f, filesize(file))
    if ".php"==substr(file, strrpos(file, ".")):
      functions = wp_doc_link_parse(content)
      docs_select = "<select name="docs-list" id="docs-list">"
      docs_select+="<option value="">"+esc_attr__("Function Name...")+"</option>"
      for function in functions:
        docs_select+="<option value=""+esc_attr(urlencode(function))+"">"+htmlspecialchars(function)+"()</option>"
      docs_select+="</select>"
    content = esc_textarea(content)
  if isset(_GET["updated"]):
    print(" <div id="message" class="updated"><p>")
    _e("File edited successfully.")
    print("</p></div>\n")
  description = get_file_description(file)
  file_show = array_search(file, array_filter(allowed_files))
  if description!=file_show:
    description+=" <span>("+file_show+")</span>"
  print("<div class="wrap">\n")
  screen_icon()
  print("<h2>")
  print(esc_html(title))
  print("</h2>\n\n<div class="fileedit-sub">\n<div class="alignleft">\n<h3>")
  print(theme.display("Name"))
  if description:
    print(": "+description)
  print("</h3>\n</div>\n<div class="alignright">\n	<form action="theme-editor.php" method="post">\n		<strong><label for="theme">")
  _e("Select theme to edit:")
  print(" </label></strong>\n		<select name="theme" id="theme">\n")
  for a_theme in a_stylesheet:
    if a_theme.errors()&&"theme_no_stylesheet"==errors():
    selected = " selected="selected"" if a_stylesheet==stylesheet else ""
    print("\n	"+"<option value=""+esc_attr(a_stylesheet)+"""+selected+">"+a_theme.display("Name")+"</option>")
  print("		</select>\n		")
  submit_button(__("Select"), "button", "Submit", False)
  print("	</form>\n</div>\n<br class="clear" />\n</div>\n")
  if theme.errors():
    print("<div class="error"><p><strong>"+__("This theme is broken.")+"</strong> "+errors()+"</p></div>")
  print("	<div id="templateside">\n")
  if allowed_files:
    if has_templates||theme.parent():
      print("	<h3>")
      _e("Templates")
      print("</h3>\n	")
      if theme.parent():
        print("	<p class="howto">")
        printf(__("This child theme inherits templates from a parent theme, %s."), "<a href=""+self_admin_url("theme-editor.php?theme="+urlencode(theme.get_template()))+"">"+parent()+"</a>")
        print("</p>\n	")
      print("	<ul>\n")
    for absolute_filename in allowed_files:
      if "style.css"==filename:
        print("	</ul>\n	<h3>"+_x("Styles", "Theme stylesheets in theme editor")+"</h3>\n	<ul>\n")
      file_description = get_file_description(absolute_filename)
      if file_description!=basename(filename):
        file_description+="<br /><span class="nonessential">("+filename+")</span>"
      if absolute_filename==file:
        file_description = "<span class="highlight">"+file_description+"</span>"
      print("		<li><a href="theme-editor.php?file=")
      print(urlencode(filename))
      print("&amp;theme=")
      print(urlencode(stylesheet))
      print("">")
      print(file_description)
      print("</a></li>\n")
    print("</ul>\n")
  print("</div>\n")
  if error:
    print("<div class="error"><p>"+__("Oops, no such file exists! Double check the name and try again, merci.")+"</p></div>")
  else:
    print("	<form name="template" id="template" action="theme-editor.php" method="post">\n	")
    wp_nonce_field("edit-theme_"+file+stylesheet)
    print("		<div><textarea cols="70" rows="30" name="newcontent" id="newcontent" aria-describedby="newcontent-description">")
    print(content)
    print("</textarea>\n		<input type="hidden" name="action" value="update" />\n		<input type="hidden" name="file" value="")
    print(esc_attr(relative_file))
    print("" />\n		<input type="hidden" name="theme" value="")
    print(esc_attr(theme.get_stylesheet()))
    print("" />\n		<input type="hidden" name="scrollto" id="scrollto" value="")
    print(scrollto)
    print("" />\n		</div>\n	")
    if !empty(functions):
      print("		<div id="documentation" class="hide-if-no-js">\n		<label for="docs-list">")
      _e("Documentation:")
      print("</label>\n		")
      print(docs_select)
      print("		<input type="button" class="button" value=" ")
      esc_attr_e("Lookup")
      print(" " onclick="if ( '' != jQuery('#docs-list').val() ) { window.open( 'http://api.wordpress.org/core/handbook/1.0/?function=' + escape( jQuery( '#docs-list' ).val() ) + '&amp;locale=")
      print(urlencode(get_locale()))
      print("&amp;version=")
      print(urlencode(wp_version))
      print("&amp;redirect=true'); }" />\n		</div>\n	")
    print("\n		<div>\n		")
    if is_child_theme()&&theme.get_stylesheet()==get_template():
      print("			<p>")
      if is_writeable(file):
        print("<strong>")
        _e("Caution:")
        print("</strong>")
      print("			")
      _e("This is a file in your current parent theme.")
      print("</p>\n		")
    if is_writeable(file):
      submit_button(__("Update File"), "primary", "submit", True)
    else:
      print("<p><em>")
      _e("You need to make this file writable before you can save your changes. See <a href="http://codex.wordpress.org/Changing_File_Permissions">the Codex</a> for more information.")
      print("</em></p>\n")
    print("		</div>\n	</form>\n")
  print("<br class="clear" />\n</div>\n<script type="text/javascript">\n/* <![CDATA[ */\njQuery(document).ready(function($){\n	$('#template').submit(function(){ $('#scrollto').val( $('#newcontent').scrollTop() ); });\n	$('#newcontent').scrollTop( $('#scrollto').val() );\n});\n/* ]]> */\n</script>\n")
include(ABSPATH+"wp-admin/admin-footer.php")
