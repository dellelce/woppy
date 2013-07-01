#!/usr/bin/python
#-*- coding: utf-8 -*-
define("WP_NETWORK_ADMIN", True)
require_once(dirname(dirname("wop/wp-admin/network/admin.php"))+"/admin.php")
if !is_multisite():
  wp_die(__("Multisite support is not enabled."))
redirect_network_admin_request = current_blog.domain!=current_site.domain||current_blog.path!=current_site.path
redirect_network_admin_request = apply_filters("redirect_network_admin_request", redirect_network_admin_request)
if redirect_network_admin_request:
  wp_redirect(network_admin_url())
  exit(0)
unset(redirect_network_admin_request)
