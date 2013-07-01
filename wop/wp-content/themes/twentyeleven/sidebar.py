#!/usr/bin/python
#-*- coding: utf-8 -*-
options = twentyeleven_get_theme_options()
current_layout = options["theme_layout"]
if "content"!=current_layout:
  print("		<div id="secondary" class="widget-area" role="complementary">\n			")
  if !dynamic_sidebar("sidebar-1"):
    print("\n				<aside id="archives" class="widget">\n					<h3 class="widget-title">")
    _e("Archives", "twentyeleven")
    print("</h3>\n					<ul>\n						")
    wp_get_archives({"type":"monthly"})
    print("					</ul>\n				</aside>\n\n				<aside id="meta" class="widget">\n					<h3 class="widget-title">")
    _e("Meta", "twentyeleven")
    print("</h3>\n					<ul>\n						")
    wp_register()
    print("						<li>")
    wp_loginout()
    print("</li>\n						")
    wp_meta()
    print("					</ul>\n				</aside>\n\n			")
  print("\n		</div><!-- #secondary .widget-area -->\n")
