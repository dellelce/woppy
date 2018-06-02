#!/usr/bin/python
#-*- coding: utf-8 -*-
define("IFRAME_REQUEST", True)
require_once("./admin.php")
if !current_user_can("edit_theme_options"):
  wp_die(__("Cheatin&#8217; uh?"))
wp_reset_vars(["url", "return"])
url = urldecode(url)
url = wp_validate_redirect(url, home_url("/"))
if return:
  return = wp_validate_redirect(urldecode(return))
if !return:
  return = url
wp_scriptswp_customizeregistered = wp_scripts.registered
wp_scripts = WP_Scripts()
wp_scripts.registered = registered
add_action("customize_controls_print_scripts", "print_head_scripts", 20)
add_action("customize_controls_print_footer_scripts", "_wp_footer_scripts")
add_action("customize_controls_print_styles", "print_admin_styles", 20)
do_action("customize_controls_init")
wp_enqueue_script("customize-controls")
wp_enqueue_style("customize-controls")
do_action("customize_controls_enqueue_scripts")
header("Content-Type: "+get_option("html_type")+"; charset="+get_option("blog_charset"))
wp_user_settings()
_wp_admin_html_begin()
body_class = "wp-core-ui"
if wp_is_mobile():
  body_class+=" mobile"
  print("<meta name="viewport" id="viewport-meta" content="width=device-width, initial-scale=0.8, minimum-scale=0.5, maximum-scale=1.2">")
is_ios = wp_is_mobile()&&preg_match("/iPad|iPod|iPhone/", _SERVER["HTTP_USER_AGENT"])
if is_ios:
  body_class+=" ios"
if is_rtl():
  body_class+=" rtl"
body_class+=" locale-"+sanitize_html_class(strtolower(str_replace("_", "-", get_locale())))
admin_title = sprintf(__("%1$s &#8212; WordPress"), strip_tags(sprintf(__("Customize %s"), theme())))
print("<title>")
print(admin_title)
print("</title>")
do_action("customize_controls_print_styles")
do_action("customize_controls_print_scripts")
print("</head>\n<body class="")
print(esc_attr(body_class))
print("">\n<div class="wp-full-overlay expanded">\n	<form id="customize-controls" class="wrap wp-full-overlay-sidebar">\n\n		<div id="customize-header-actions" class="wp-full-overlay-header">\n			")
save_text = __("Save &amp; Publish") if wp_customize.is_theme_active() else __("Save &amp; Activate")
submit_button(save_text, "primary save", "save", False)
print("			<span class="spinner"></span>\n			<a class="back button" href="")
print(esc_url(return if return else admin_url("themes.php")))
print("">\n				")
_e("Cancel")
print("			</a>\n		</div>\n\n		")
screenshot = theme()
cannot_expand = !screenshot||theme()
print("\n		<div class="wp-full-overlay-sidebar-content" tabindex="-1">\n			<div id="customize-info" class="customize-section")
if cannot_expand:
  print(" cannot-expand")
print("">\n				<div class="customize-section-title" aria-label="")
esc_attr_e("Theme Customizer Options")
print("" tabindex="0">\n					<span class="preview-notice">")
print(sprintf(__("You are previewing %s"), "<strong class="theme-name">"+theme()+"</strong>"))
print("</span>\n				</div>\n				")
if !cannot_expand:
  print("				<div class="customize-section-content">\n					")
  if screenshot:
    print("						<img class="theme-screenshot" src="")
    print(esc_url(screenshot))
    print("" />\n					")
  print("\n					")
  if theme():
    print("						<div class="theme-description">")
    print(theme())
    print("</div>\n					")
  print("				</div>\n				")
print("			</div>\n\n			<div id="customize-theme-controls"><ul>\n				")
for section in wp_customize:
  section.maybe_render()
print("			</ul></div>\n		</div>\n\n		<div id="customize-footer-actions" class="wp-full-overlay-footer">\n			<a href="#" class="collapse-sidebar button-secondary" title="")
esc_attr_e("Collapse Sidebar")
print("">\n				<span class="collapse-sidebar-arrow"></span>\n				<span class="collapse-sidebar-label">")
_e("Collapse")
print("</span>\n			</a>\n		</div>\n	</form>\n	<div id="customize-preview" class="wp-full-overlay-main"></div>\n	")
do_action("customize_controls_print_footer_scripts")
allowed_urls = [home_url("/")]
admin_origin = parse_url(admin_url())
home_origin = parse_url(home_url())
cross_domain = strtolower(admin_origin["host"])!=strtolower(home_origin["host"])
if is_ssl()&&!cross_domain:
  allowed_urls[] = home_url("/", "https")
allowed_urls = array_unique(apply_filters("customize_allowed_urls", allowed_urls))
fallback_url = add_query_arg({"preview":1, "template":wp_customize.get_template(), "stylesheet":wp_customize.get_stylesheet(), "preview_iframe":True, "TB_iframe":"true"}, home_url("/"))
login_url = add_query_arg({"interim-login":1, "customize-login":1}, wp_login_url())
settings = {"theme":{"stylesheet":wp_customize.get_stylesheet(), "active":wp_customize.is_theme_active()}, "url":{"preview":esc_url(url if url else home_url("/")), "parent":esc_url(admin_url()), "activated":admin_url("themes.php?activated=true&previewed"), "ajax":esc_url(admin_url("admin-ajax.php", "relative")), "allowed":array_map("esc_url", allowed_urls), "isCrossDomain":cross_domain, "fallback":fallback_url, "home":esc_url(home_url("/")), "login":login_url}, "browser":{"mobile":wp_is_mobile(), "ios":is_ios}, "settings":[], "controls":[], "nonce":{"save":wp_create_nonce("save-customize_"+wp_customize.get_stylesheet()), "preview":wp_create_nonce("preview-customize_"+wp_customize.get_stylesheet())}}
for setting in wp_customize:
  settings["settings"][id] = {"value":setting.js_value(), "transport":setting.transport}
for control in wp_customize:
  control.to_json()
  settings["controls"][id] = control.json
print("	<script type="text/javascript">\n		var _wpCustomizeSettings = ")
print(json_encode(settings))
print(";\n	</script>\n</div>\n</body>\n</html>\n")
