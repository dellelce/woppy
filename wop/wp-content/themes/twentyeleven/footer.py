#!/usr/bin/python
#-*- coding: utf-8 -*-
print("\n	</div><!-- #main -->\n\n	<footer id="colophon" role="contentinfo">\n\n			")
if !is_404():
  get_sidebar("footer")
print("\n			<div id="site-generator">\n				")
do_action("twentyeleven_credits")
print("				<a href="")
print(esc_url(__("http://wordpress.org/", "twentyeleven")))
print("" title="")
esc_attr_e("Semantic Personal Publishing Platform", "twentyeleven")
print("">")
printf(__("Proudly powered by %s", "twentyeleven"), "WordPress")
print("</a>\n			</div>\n	</footer><!-- #colophon -->\n</div><!-- #page -->\n\n")
wp_footer()
print("\n</body>\n</html>")
