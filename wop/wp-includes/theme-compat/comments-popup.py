#!/usr/bin/python
#-*- coding: utf-8 -*-
_deprecated_file(sprintf(__("Theme without %1$s"), basename("wop/wp-includes/theme-compat/comments-popup.php")), "3.0", , sprintf(__("Please include a %1$s template in your theme."), basename("wop/wp-includes/theme-compat/comments-popup.php")))
print("<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n     <title>")
printf(__("%1$s - Comments on %2$s"), get_option("blogname"), the_title("", "", False))
print("</title>\n\n	<meta http-equiv="Content-Type" content="")
bloginfo("html_type")
print("; charset=")
print(get_option("blog_charset"))
print("" />\n	<style type="text/css" media="screen">\n		@import url( ")
bloginfo("stylesheet_url")
print(" );\n		body { margin: 3px; }\n	</style>\n\n</head>\n<body id="commentspopup">\n\n<h1 id="header"><a href="" title="")
print(get_option("blogname"))
print("">")
print(get_option("blogname"))
print("</a></h1>\n\n")
add_filter("comment_text", "popuplinks")
if have_posts():
  while :
    the_post()
    print("<h2 id="comments">")
    _e("Comments")
    print("</h2>\n\n<p><a href="")
    print(esc_url(get_post_comments_feed_link(post.ID)))
    print("">")
    _e("<abbr title="Really Simple Syndication">RSS</abbr> feed for comments on this post.")
    print("</a></p>\n\n")
    if pings_open():
      print("<p>")
      printf(__("The <abbr title="Universal Resource Locator">URL</abbr> to TrackBack this entry is: <em>%s</em>"), get_trackback_url())
      print("</p>\n")
    print("\n")
    commenter = wp_get_current_commenter()
    extract(commenter)
    comments = get_approved_comments(id)
    post = get_post(id)
    if post_password_required(post):
      print(get_the_password_form())
    else:
      print("\n")
      if comments:
        print("<ol id="commentlist">\n")
        for comment in comments:
          print("	<li id="comment-")
          comment_ID()
          print("">\n	")
          comment_text()
          print("	<p><cite>")
          comment_type()
          print(" ")
          printf(__("by %1$s &#8212; %2$s @ <a href="#comment-%3$s">%4$s</a>"), get_comment_author_link(), get_comment_date(), get_comment_ID(), get_comment_time())
          print("</cite></p>\n	</li>\n\n")
        print("\n</ol>\n")
      else:
        print("\n	<p>")
        _e("No comments yet.")
        print("</p>\n")
      print("\n")
      if comments_open():
        print("<h2>")
        _e("Leave a comment")
        print("</h2>\n<p>")
        printf(__("Line and paragraph breaks automatic, e-mail address never displayed, <acronym title="Hypertext Markup Language">HTML</acronym> allowed: <code>%s</code>"), allowed_tags())
        print("</p>\n\n<form action="")
        print(get_option("siteurl"))
        print("/wp-comments-post.php" method="post" id="commentform">\n")
        if user_ID:
          print("	<p>")
          printf(__("Logged in as <a href="%1$s">%2$s</a>. <a href="%3$s" title="Log out of this account">Log out &raquo;</a>"), get_edit_user_link(), user_identity, wp_logout_url(get_permalink()))
          print("</p>\n")
        else:
          print("	<p>\n	  <input type="text" name="author" id="author" class="textarea" value="")
          print(esc_attr(comment_author))
          print("" size="28" tabindex="1" />\n	   <label for="author">")
          _e("Name")
          print("</label>\n	</p>\n\n	<p>\n	  <input type="text" name="email" id="email" value="")
          print(esc_attr(comment_author_email))
          print("" size="28" tabindex="2" />\n	   <label for="email">")
          _e("E-mail")
          print("</label>\n	</p>\n\n	<p>\n	  <input type="text" name="url" id="url" value="")
          print(esc_attr(comment_author_url))
          print("" size="28" tabindex="3" />\n	   <label for="url">")
          _e("<abbr title="Universal Resource Locator">URL</abbr>")
          print("</label>\n	</p>\n")
        print("\n	<p>\n	  <label for="comment">")
        _e("Your Comment")
        print("</label>\n	<br />\n	  <textarea name="comment" id="comment" cols="70" rows="4" tabindex="4"></textarea>\n	</p>\n\n	<p>\n	  <input type="hidden" name="comment_post_ID" value="")
        print(id)
        print("" />\n	  <input type="hidden" name="redirect_to" value="")
        print(esc_attr(_SERVER["REQUEST_URI"]))
        print("" />\n	  <input name="submit" type="submit" tabindex="5" value="")
        esc_attr_e("Say It!")
        print("" />\n	</p>\n	")
        do_action("comment_form", post.ID)
        print("</form>\n")
      else:
        print("\n<p>")
        _e("Sorry, the comment form is closed at this time.")
        print("</p>\n")
    print("\n<div><strong><a href="javascript:window.close()">")
    _e("Close this window.")
    print("</a></strong></div>\n\n")
else:
  print("<p>")
  _e("Sorry, no posts matched your criteria.")
  print("</p>\n")
print("<!-- // this is just the end of the motor - don't touch that line either :) -->\n")
print("\n<p class="credit">")
timer_stop(1)
print(" <cite>")
printf(__("Powered by <a href="%s" title="Powered by WordPress, state-of-the-art semantic personal publishing platform"><strong>WordPress</strong></a>"), "http://wordpress.org/")
print("</cite></p>\n")
print("\n<script type="text/javascript">\n<!--\ndocument.onkeypress = function esc(e) {\n	if(typeof(e) == "undefined") { e=event; }\n	if (e.keyCode == 27) { self.close(); }\n}\n// -->\n</script>\n</body>\n</html>\n")
