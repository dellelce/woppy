#!/usr/bin/python
#-*- coding: utf-8 -*-
if isset(_GET["tab"])&&"theme-information"==_GET["tab"]:
  define("IFRAME_REQUEST", True)
require_once("./admin.php")
if !is_multisite():
  wp_die(__("Multisite support is not enabled."))
require("../theme-install.php")
