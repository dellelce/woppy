#!/usr/bin/python
#-*- coding: utf-8 -*-
if !is_active_sidebar("sidebar-2")&&!is_active_sidebar("sidebar-3"):
  return 
print("<div id="secondary" class="widget-area" role="complementary">\n	")
if is_active_sidebar("sidebar-2"):
  print("	<div class="first front-widgets">\n		")
  dynamic_sidebar("sidebar-2")
  print("	</div><!-- .first -->\n	")
print("\n	")
if is_active_sidebar("sidebar-3"):
  print("	<div class="second front-widgets">\n		")
  dynamic_sidebar("sidebar-3")
  print("	</div><!-- .second -->\n	")
print("</div><!-- #secondary -->")
