#!/usr/bin/python
#-*- coding: utf-8 -*-
print("	<form method="get" id="searchform" action="")
print(esc_url(home_url("/")))
print("">\n		<label for="s" class="assistive-text">")
_e("Search", "twentyeleven")
print("</label>\n		<input type="text" class="field" name="s" id="s" placeholder="")
esc_attr_e("Search", "twentyeleven")
print("" />\n		<input type="submit" class="submit" name="submit" id="searchsubmit" value="")
esc_attr_e("Search", "twentyeleven")
print("" />\n	</form>\n")
