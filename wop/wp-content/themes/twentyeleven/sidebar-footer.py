#!/usr/bin/python
#-*- coding: utf-8 -*-
print("\n")
if !is_active_sidebar("sidebar-3")&&!is_active_sidebar("sidebar-4")&&!is_active_sidebar("sidebar-5"):
  return 
print("<div id="supplementary" ")
twentyeleven_footer_sidebar_class()
print(">\n	")
if is_active_sidebar("sidebar-3"):
  print("	<div id="first" class="widget-area" role="complementary">\n		")
  dynamic_sidebar("sidebar-3")
  print("	</div><!-- #first .widget-area -->\n	")
print("\n	")
if is_active_sidebar("sidebar-4"):
  print("	<div id="second" class="widget-area" role="complementary">\n		")
  dynamic_sidebar("sidebar-4")
  print("	</div><!-- #second .widget-area -->\n	")
print("\n	")
if is_active_sidebar("sidebar-5"):
  print("	<div id="third" class="widget-area" role="complementary">\n		")
  dynamic_sidebar("sidebar-5")
  print("	</div><!-- #third .widget-area -->\n	")
print("</div><!-- #supplementary -->")
