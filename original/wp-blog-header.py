#!/usr/bin/python
#-*- coding: utf-8 -*-
if !isset(wp_did_header):
  wp_did_header = True
  require_once(dirname("wop/wp-blog-header.php")+"/wp-load.php")
  wp()
  require_once(ABSPATH+WPINC+"/template-loader.php")
