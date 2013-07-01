#!/usr/bin/python
#-*- coding: utf-8 -*-
define("ABSPATH", dirname("wop/wp-load.php")+"/")
error_reporting(E_CORE_ERROR|E_CORE_WARNING|E_COMPILE_ERROR|E_ERROR|E_WARNING|E_PARSE|E_USER_ERROR|E_USER_WARNING|E_RECOVERABLE_ERROR)
if file_exists(ABSPATH+"wp-config.php"):
  require_once(ABSPATH+"wp-config.php")
elif file_exists(dirname(ABSPATH)+"/wp-config.php")&&!file_exists(dirname(ABSPATH)+"/wp-settings.php"):
  require_once(dirname(ABSPATH)+"/wp-config.php")
elif strpos(_SERVER["PHP_SELF"], "wp-admin")!==False:
  path = "setup-config.php"
else:
  path = "wp-admin/setup-config.php"
