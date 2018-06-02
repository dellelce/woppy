#!/usr/bin/python
#-*- coding: utf-8 -*-
define("DB_NAME", "database_name_here")
define("DB_USER", "username_here")
define("DB_PASSWORD", "password_here")
define("DB_HOST", "localhost")
define("DB_CHARSET", "utf8")
define("DB_COLLATE", "")
define("AUTH_KEY", "put your unique phrase here")
define("SECURE_AUTH_KEY", "put your unique phrase here")
define("LOGGED_IN_KEY", "put your unique phrase here")
define("NONCE_KEY", "put your unique phrase here")
define("AUTH_SALT", "put your unique phrase here")
define("SECURE_AUTH_SALT", "put your unique phrase here")
define("LOGGED_IN_SALT", "put your unique phrase here")
define("NONCE_SALT", "put your unique phrase here")
table_prefix = "wp_"
define("WPLANG", "")
define("WP_DEBUG", False)
if !defined("ABSPATH"):
  define("ABSPATH", dirname("wop/wp-config-sample.php")+"/")
require_once(ABSPATH+"wp-settings.php")
