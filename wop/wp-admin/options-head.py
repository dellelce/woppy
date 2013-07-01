#!/usr/bin/python
#-*- coding: utf-8 -*-
wp_reset_vars(["action", "standalone", "option_group_id"])
if isset(_GET["updated"])&&isset(_GET["page"]):
  add_settings_error("general", "settings_updated", __("Settings saved."), "updated")
settings_errors()
