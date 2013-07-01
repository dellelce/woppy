#!/usr/bin/python
#-*- coding: utf-8 -*-
_deprecated_file(sprintf(__("Theme without %1$s"), basename("wop/wp-includes/theme-compat/footer.php")), "3.0", , sprintf(__("Please include a %1$s template in your theme."), basename("wop/wp-includes/theme-compat/footer.php")))
print("\n<hr />\n<div id="footer" role="contentinfo">\n<!-- If you'd like to support WordPress, having the "powered by" link somewhere on your blog is the best way; it's our only promotion or advertising. -->\n	<p>\n		")
printf(__("%1$s is proudly powered by %2$s"), get_bloginfo("name"), "<a href="http://wordpress.org/">WordPress</a>")
print("		<br />")
printf(__("%1$s and %2$s."), "<a href=""+get_bloginfo("rss2_url")+"">"+__("Entries (RSS)")+"</a>", "<a href=""+get_bloginfo("comments_rss2_url")+"">"+__("Comments (RSS)")+"</a>")
print("		<!-- ")
printf(__("%d queries. %s seconds."), get_num_queries(), timer_stop(0, 3))
print(" -->\n	</p>\n</div>\n</div>\n\n<!-- Gorgeous design by Michael Heilemann - http://binarybonsai.com/kubrick/ -->\n")
print("\n		")
wp_footer()
print("</body>\n</html>\n")
