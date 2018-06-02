#!/usr/bin/python
#-*- coding: utf-8 -*-
define("WP_USER_ADMIN", True)
require_once(dirname(dirname("wop/wp-admin/user/admin.php"))+"/admin.php")
if !is_multisite():
  wp_redirect(admin_url())
  exit(0)
redirect_user_admin_request = current_blog.domain!=current_site.domain||current_blog.path!=current_site.path
redirect_user_admin_request = apply_filters("redirect_user_admin_request", redirect_user_admin_request)
if redirect_user_admin_request:
  wp_redirect(user_admin_url())
  exit(0)
unset(redirect_user_admin_request)
