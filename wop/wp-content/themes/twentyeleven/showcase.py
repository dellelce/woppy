#!/usr/bin/python
#-*- coding: utf-8 -*-
wp_enqueue_script("twentyeleven-showcase", get_template_directory_uri()+"/js/showcase.js", ["jquery"], "2011-04-28")
get_header()
print("\n		<div id="primary" class="showcase">\n			<div id="content" role="main">\n\n				")
while ""!=get_the_content():
  the_post()
  print("\n				")
  if ""!=get_the_content():
    get_template_part("content", "intro")
  print("\n				")
print("\n				")
sticky = get_option("sticky_posts")
if !empty(sticky):
  featured_args = {"post__in":sticky, "post_status":"publish", "posts_per_page":10, "no_found_rows":True}
  featured = WP_Query(featured_args)
  if featured.have_posts():
    counter_slider = 0
    if function_exists("get_custom_header"):
      header_image_width = get_theme_support("custom-header", "width")
    else:
      header_image_width = HEADER_IMAGE_WIDTH
    print("\n				<div class="featured-posts">\n					<h1 class="showcase-heading">")
    _e("Featured Post", "twentyeleven")
    print("</h1>\n\n				")
    while image[1]>=header_image_width:
      featured.the_post()
      counter_slider+=1
      feature_class = "feature-text"
      if has_post_thumbnail():
        feature_class = "feature-image small"
        image = wp_get_attachment_image_src(get_post_thumbnail_id(post.ID), [header_image_width, header_image_width])
        if image[1]>=header_image_width:
          feature_class = "feature-image large"
      print("\n					<section class="featured-post ")
      print(feature_class)
      print("" id="featured-post-")
      print(counter_slider)
      print("">\n\n						")
      if has_post_thumbnail():
        if image[1]>=header_image_width:
          thumbnail_size = "large-feature"
        else:
          thumbnail_size = "small-feature"
        print("								<a href="")
        the_permalink()
        print("" title="")
        print(esc_attr(sprintf(__("Permalink to %s", "twentyeleven"), the_title_attribute("echo=0"))))
        print("" rel="bookmark">")
        the_post_thumbnail(thumbnail_size)
        print("</a>\n								")
      print("						")
      get_template_part("content", "featured")
      print("					</section>\n				")
    print("\n				")
    if featured.post_count>1:
      print("				<nav class="feature-slider">\n					<ul>\n					")
      counter_slider = 0
      rewind_posts()
      while 1==counter_slider:
        featured.the_post()
        counter_slider+=1
        if 1==counter_slider:
          class = "class="active""
        else:
          class = ""
        print("						<li><a href="#featured-post-")
        print(counter_slider)
        print("" title="")
        print(esc_attr(sprintf(__("Featuring: %s", "twentyeleven"), the_title_attribute("echo=0"))))
        print("" ")
        print(class)
        print("></a></li>\n					")
      print("					</ul>\n				</nav>\n				")
    print("\n				</div><!-- .featured-posts -->\n				")
  print("\n				")
print("\n\n				<section class="recent-posts">\n					<h1 class="showcase-heading">")
_e("Recent Posts", "twentyeleven")
print("</h1>\n\n					")
recent_args = {"order":"DESC", "post__not_in":get_option("sticky_posts"), "tax_query":[{"taxonomy":"post_format", "terms":["post-format-aside", "post-format-link", "post-format-quote", "post-format-status"], "field":"slug", "operator":"NOT IN"}], "no_found_rows":True}
recent = WP_Query(recent_args)
if recent.have_posts():
  recent.the_post()
  moremore = 0
  get_template_part("content", get_post_format())
  print("<ol class="other-recent-posts">")
while "<span class="leave-reply">"+__("Leave a reply", "twentyeleven")+"</span>":
  recent.the_post()
  print("\n						<li class="entry-title">\n							<a href="")
  the_permalink()
  print("" title="")
  print(esc_attr(sprintf(__("Permalink to %s", "twentyeleven"), the_title_attribute("echo=0"))))
  print("" rel="bookmark">")
  the_title()
  print("</a>\n							<span class="comments-link">\n								")
  comments_popup_link("<span class="leave-reply">"+__("Leave a reply", "twentyeleven")+"</span>", __("<b>1</b> Reply", "twentyeleven"), __("<b>%</b> Replies", "twentyeleven"))
  print("							</span>\n						</li>\n\n					")
if recent.post_count>0:
  print("</ol>")
print("				</section><!-- .recent-posts -->\n\n				<div class="widget-area" role="complementary">\n					")
if !dynamic_sidebar("sidebar-2"):
  print("\n						")
  the_widget("Twenty_Eleven_Ephemera_Widget", "", {"before_title":"<h3 class="widget-title">", "after_title":"</h3>"})
  print("\n					")
print("\n				</div><!-- .widget-area -->\n\n			</div><!-- #content -->\n		</div><!-- #primary -->\n\n")
get_footer()
