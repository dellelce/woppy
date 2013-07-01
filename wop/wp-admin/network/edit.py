#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if !is_multisite():
  wp_die(__("Multisite support is not enabled."))
if empty(_GET["action"]):
  wp_redirect(network_admin_url())
  exit(0)
do_action("wpmuadminedit", "")
do_action("network_admin_edit_"+_GET["action"])
wp_redirect(network_admin_url())
exit(0)
