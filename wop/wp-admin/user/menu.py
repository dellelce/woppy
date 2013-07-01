#!/usr/bin/python
#-*- coding: utf-8 -*-
menu[2] = [__("Dashboard"), "exist", "index.php", "", "menu-top menu-top-first menu-icon-dashboard", "menu-dashboard", "div"]
menu[4] = ["", "exist", "separator1", "", "wp-menu-separator"]
menu[70] = [__("Profile"), "exist", "profile.php", "", "menu-top menu-icon-users", "menu-users", "div"]
menu[99] = ["", "exist", "separator-last", "", "wp-menu-separator-last"]
_wp_real_parent_file["users.php"] = "profile.php"
compat = []
submenu = []
require_once(ABSPATH+"wp-admin/includes/menu.php")
