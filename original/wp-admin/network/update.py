#!/usr/bin/python
#-*- coding: utf-8 -*-
if isset(_GET["action"])&&in_array(_GET["action"], ["update-selected", "activate-plugin", "update-selected-themes"]):
  define("IFRAME_REQUEST", True)
require_once("./admin.php")
if !is_multisite():
  wp_die(__("Multisite support is not enabled."))
require("../update.php")
