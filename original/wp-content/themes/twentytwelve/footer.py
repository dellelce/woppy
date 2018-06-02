#!/usr/bin/python
#-*- coding: utf-8 -*-
print("	</div><!-- #main .wrapper -->\n	<footer id="colophon" role="contentinfo">\n		<div class="site-info">\n			")
do_action("twentytwelve_credits")
print("			<a href="")
print(esc_url(__("http://wordpress.org/", "twentytwelve")))
print("" title="")
esc_attr_e("Semantic Personal Publishing Platform", "twentytwelve")
print("">")
printf(__("Proudly powered by %s", "twentytwelve"), "WordPress")
print("</a>\n		</div><!-- .site-info -->\n	</footer><!-- #colophon -->\n</div><!-- #page -->\n\n")
wp_footer()
print("</body>\n</html>")
