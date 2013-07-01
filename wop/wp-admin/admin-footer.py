#!/usr/bin/python
#-*- coding: utf-8 -*-
if !defined("ABSPATH"):
  die("-1")
print("\n<div class="clear"></div></div><!-- wpbody-content -->\n<div class="clear"></div></div><!-- wpbody -->\n<div class="clear"></div></div><!-- wpcontent -->\n\n<div id="wpfooter">\n")
do_action("in_admin_footer")
print("<p id="footer-left" class="alignleft">")
print(apply_filters("admin_footer_text", "<span id="footer-thankyou">"+__("Thank you for creating with <a href="http://wordpress.org/">WordPress</a>.")+"</span>"))
print("</p>\n<p id="footer-upgrade" class="alignright">")
print(apply_filters("update_footer", ""))
print("</p>\n<div class="clear"></div>\n</div>\n")
do_action("admin_footer", "")
do_action("admin_print_footer_scripts")
do_action("admin_footer-"+GLOBALS["hook_suffix"])
if function_exists("get_site_option"):
  if False===get_site_option("can_compress_scripts"):
    compression_test()
print("\n<div class="clear"></div></div><!-- wpwrap -->\n<script type="text/javascript">if(typeof wpOnload=='function')wpOnload();</script>\n</body>\n</html>\n")
