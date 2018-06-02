#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if !current_user_can("switch_themes")&&!current_user_can("edit_theme_options"):
  wp_die(__("Cheatin&#8217; uh?"))
wp_list_table = _get_list_table("WP_Themes_List_Table")
if current_user_can("switch_themes")&&isset(_GET["action"]):
  if "activate"==_GET["action"]:
    check_admin_referer("switch-theme_"+_GET["stylesheet"])
    theme = wp_get_theme(_GET["stylesheet"])
    if !theme.exists()||!theme.is_allowed():
      wp_die(__("Cheatin&#8217; uh?"))
    switch_theme(theme.get_stylesheet())
    wp_redirect(admin_url("themes.php?activated=true"))
    exit(0)
  elif "delete"==_GET["action"]:
    check_admin_referer("delete-theme_"+_GET["stylesheet"])
    theme = wp_get_theme(_GET["stylesheet"])
    if !current_user_can("delete_themes")||!theme.exists():
      wp_die(__("Cheatin&#8217; uh?"))
    delete_theme(_GET["stylesheet"])
    wp_redirect(admin_url("themes.php?deleted=true"))
    exit(0)
wp_list_table.prepare_items()
title = __("Manage Themes")
parent_file = "themes.php"
if current_user_can("switch_themes"):
  help_manage = "<p>"+__("Aside from the default theme included with your WordPress installation, themes are designed and developed by third parties.")+"</p>"+"<p>"+__("You can see your active theme at the top of the screen. Below are the other themes you have installed that are not currently in use. You can see what your site would look like with one of these themes by clicking the Live Preview link (see "Previewing and Customizing" help tab). To change themes, click the Activate link.")+"</p>"
  get_current_screen()
  if current_user_can("install_themes"):
    if is_multisite():
      help_install = "<p>"+__("Installing themes on Multisite can only be done from the Network Admin section.")+"</p>"
    else:
      help_install = "<p>"+sprintf(__("If you would like to see more themes to choose from, click on the &#8220;Install Themes&#8221; tab and you will be able to browse or search for additional themes from the <a href="%s" target="_blank">WordPress.org Theme Directory</a>. Themes in the WordPress.org Theme Directory are designed and developed by third parties, and are compatible with the license WordPress uses. Oh, and they&#8217;re free!"), "http://wordpress.org/extend/themes/")+"</p>"
    get_current_screen()
  add_thickbox()
if current_user_can("edit_theme_options"):
  help_customize = "<p>"+__("Click on the "Live Preview" link under any theme to preview that theme and change theme options in a separate, full-screen view. Any installed theme can be previewed and customized in this way.")+"</p>"+"<p>"+__("The theme being previewed is fully interactive &mdash; navigate to different pages to see how the theme handles posts, archives, and other page templates.")+"</p>"+"<p>"+__("In the left-hand pane you can edit the theme settings. The settings will differ, depending on what theme features the theme being previewed supports. To accept the new settings and activate the theme all in one step, click the "Save &amp; Activate" button at the top of the left-hand pane.")+"</p>"+"<p>"+__("When previewing on smaller monitors, you can use the "Collapse" icon at the bottom of the left-hand pane. This will hide the pane, giving you more room to preview your site in the new theme. To bring the pane back, click on the Collapse icon again.")+"</p>"
  get_current_screen()
get_current_screen()
wp_enqueue_script("theme")
wp_enqueue_script("customize-loader")
require_once("./admin-header.php")
print("\n<div class="wrap">")
screen_icon()
if !is_multisite()&&current_user_can("install_themes"):
  print("<h2 class="nav-tab-wrapper">\n<a href="themes.php" class="nav-tab nav-tab-active">")
  print(esc_html(title))
  print("</a><a href="")
  print(admin_url("theme-install.php"))
  print("" class="nav-tab">")
  print(esc_html_x("Install Themes", "theme"))
  print("</a>\n")
else:
  print("<h2>")
  print(esc_html(title))
print("</h2>\n")
if !validate_current_theme()||isset(_GET["broken"]):
  print("<div id="message1" class="updated"><p>")
  _e("The active theme is broken. Reverting to the default theme.")
  print("</p></div>\n")
elif isset(_GET["activated"]):
  if isset(_GET["previewed"]):
    print("		<div id="message2" class="updated"><p>")
    printf(__("Settings saved and theme activated. <a href="%s">Visit site</a>"), home_url("/"))
    print("</p></div>\n		")
  else:
    print("<div id="message2" class="updated"><p>")
    printf(__("New theme activated. <a href="%s">Visit site</a>"), home_url("/"))
    print("</p></div>")
elif isset(_GET["deleted"]):
  print("<div id="message3" class="updated"><p>")
  _e("Theme deleted.")
  print("</p></div>\n")
ct = wp_get_theme()
screenshot = ct.get_screenshot()
class = "has-screenshot" if screenshot else ""
customize_title = sprintf(__("Customize &#8220;%s&#8221;"), ct.display("Name"))
print("<div id="current-theme" class="")
print(esc_attr(class))
print("">\n	")
if screenshot:
  print("		")
  if current_user_can("edit_theme_options"):
    print("		<a href="")
    print(wp_customize_url())
    print("" class="load-customize hide-if-no-customize" title="")
    print(esc_attr(customize_title))
    print("">\n			<img src="")
    print(esc_url(screenshot))
    print("" alt="")
    esc_attr_e("Current theme preview")
    print("" />\n		</a>\n		")
  print("		<img class="hide-if-customize" src="")
  print(esc_url(screenshot))
  print("" alt="")
  esc_attr_e("Current theme preview")
  print("" />\n	")
print("\n	<h3>")
_e("Current Theme")
print("</h3>\n	<h4>\n		")
print(ct.display("Name"))
print("	</h4>\n\n	<div>\n		<ul class="theme-info">\n			<li>")
printf(__("By %s"), ct.display("Author"))
print("</li>\n			<li>")
printf(__("Version %s"), ct.display("Version"))
print("</li>\n		</ul>\n		<p class="theme-description">")
print(ct.display("Description"))
print("</p>\n		")
if ct.parent():
  printf(" <p class="howto">"+__("This <a href="%1$s">child theme</a> requires its parent theme, %2$s.")+"</p>", __("http://codex.wordpress.org/Child_Themes"), parent())
print("		")
theme_update_available(ct)
print("	</div>\n\n	")
options = []
if is_array(submenu)&&isset(submenu["themes.php"]):
  for item in submenu["themes.php"]:
    class = ""
    if "themes.php"==item[2]||"theme-editor.php"==item[2]:
    if strcmp(self, item[2])==0&&empty(parent_file)||parent_file&&item[2]==parent_file:
      class = " class="current""
    if !empty(submenu[item[2]]):
      submenu[item[2]] = array_values(submenu[item[2]])
      menu_hook = get_plugin_page_hook(submenu[item[2]][0][2], item[2])
      if file_exists(WP_PLUGIN_DIR+"/"+submenu[item[2]][0][2]+"")||!empty(menu_hook):
        options[] = "<a href='admin.php?page="+submenu[item[2]][0][2]+"'"+class+">"+item[0]+"</a>"
      else:
        options[] = "<a href='"+submenu[item[2]][0][2]+"'"+class+">"+item[0]+"</a>"
    elif current_user_can(item[1]):
      menu_file = item[2]
      if False!==pos = strpos(menu_file, "?"):
        menu_file = substr(menu_file, 0, pos)
      if file_exists(ABSPATH+"wp-admin/"+menu_file+""):
        options[] = "<a href='"+item[2]+"'"+class+">"+item[0]+"</a>"
      else:
        options[] = "<a href='themes.php?page="+item[2]+"'"+class+">"+item[0]+"</a>"
if options||current_user_can("edit_theme_options"):
  print("	<div class="theme-options">\n		")
  if current_user_can("edit_theme_options"):
    print("		<a id="customize-current-theme-link" href="")
    print(wp_customize_url())
    print("" class="load-customize hide-if-no-customize" title="")
    print(esc_attr(customize_title))
    print("">")
    _e("Customize")
    print("</a>\n		")
  if options:
    print("		<span>")
    _e("Options:")
    print("</span>\n		<ul>\n			")
    for option in options:
      print("				<li>")
      print(option)
      print("</li>\n			")
    print("		</ul>\n		")
  print("	</div>\n	")
print("\n</div>\n\n<br class="clear" />\n")
if !current_user_can("switch_themes"):
  print("</div>")
  require("./admin-footer.php")
  exit(0)
print("\n<form class="search-form filter-form" action="" method="get">\n\n<h3 class="available-themes">")
_e("Available Themes")
print("</h3>\n\n")
if !empty(_REQUEST["s"])||!empty(_REQUEST["features"])||wp_list_table.has_items():
  print("\n<p class="search-box">\n	<label class="screen-reader-text" for="theme-search-input">")
  _e("Search Installed Themes")
  print(":</label>\n	<input type="search" id="theme-search-input" name="s" value="")
  _admin_search_query()
  print("" />\n	")
  submit_button(__("Search Installed Themes"), "button", False, False, {"id":"search-submit"})
  print("	<a id="filter-click" href="?filter=1">")
  _e("Feature Filter")
  print("</a>\n</p>\n\n<div id="filter-box" style="")
  if empty(_REQUEST["filter"]):
    print("display: none;")
  print("">\n")
  feature_list = get_theme_feature_list()
  print("	<div class="feature-filter">\n		<p class="install-help">")
  _e("Theme filters")
  print("</p>\n	")
  if !empty(_REQUEST["filter"]):
    print("		<input type="hidden" name="filter" value="1" />\n	")
  print("	")
  for features in feature_list:
    feature_name = esc_html(feature_name)
    print("\n		<div class="feature-container">\n			<div class="feature-name">")
    print(feature_name)
    print("</div>\n\n			<ol class="feature-group">\n				")
    for feature in features:
      feature_name = feature
      feature_name = esc_html(feature_name)
      feature = esc_attr(feature)
      print("				<li>\n					<input type="checkbox" name="features[]" id="feature-id-")
      print(key)
      print("" value="")
      print(key)
      print("" ")
      checked(in_array(key, wp_list_table.features))
      print("/>\n					<label for="feature-id-")
      print(key)
      print("">")
      print(feature_name)
      print("</label>\n				</li>\n				")
    print("			</ol>\n		</div>\n	")
  print("\n	<div class="feature-container">\n		")
  submit_button(__("Apply Filters"), "button-secondary submitter", False, False, {"id":"filter-submit"})
  print("		&nbsp;\n		<a id="mini-filter-click" href="")
  print(esc_url(remove_query_arg(["filter", "features", "submit"])))
  print("">")
  _e("Close filters")
  print("</a>\n	</div>\n	<br/>\n	</div>\n	<br class="clear"/>\n</div>\n\n")
print("\n<br class="clear" />\n\n")
wp_list_table.display()
print("\n</form>\n<br class="clear" />\n\n")
if !is_multisite()&&current_user_can("edit_themes")&&broken_themes = wp_get_themes({"errors":True}):
  print("\n<h3>")
  _e("Broken Themes")
  print("</h3>\n<p>")
  _e("The following themes are installed but incomplete. Themes must have a stylesheet and a template.")
  print("</p>\n\n<table id="broken-themes">\n	<tr>\n		<th>")
  _ex("Name", "theme name")
  print("</th>\n		<th>")
  _e("Description")
  print("</th>\n	</tr>\n")
  alt = ""
  for broken_theme in broken_themes:
    alt = "" if "class="alternate""==alt else "class="alternate""
    print("\n		<tr "+alt+">\n			 <td>"+broken_theme.get("Name")+"</td>\n			 <td>"+errors()+"</td>\n		</tr>")
  print("</table>\n")
print("</div>\n\n")
require("./admin-footer.php")
