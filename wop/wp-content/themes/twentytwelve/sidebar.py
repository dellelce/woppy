#!/usr/bin/python
#-*- coding: utf-8 -*-
print("\n	")
if is_active_sidebar("sidebar-1"):
  print("		<div id="secondary" class="widget-area" role="complementary">\n			")
  dynamic_sidebar("sidebar-1")
  print("		</div><!-- #secondary -->\n	")
