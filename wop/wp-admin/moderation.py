#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("../wp-load.php")
wp_redirect(admin_url("edit-comments.php?comment_status=moderated"))
exit(0)
