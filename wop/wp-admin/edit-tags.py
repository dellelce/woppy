#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./admin.php")
if !taxnow:
  wp_die(__("Invalid taxonomy"))
tax = get_taxonomy(taxnow)
if !tax:
  wp_die(__("Invalid taxonomy"))
if !current_user_can(tax.cap.manage_terms):
  wp_die(__("Cheatin&#8217; uh?"))
wp_list_table = _get_list_table("WP_Terms_List_Table")
pagenum = wp_list_table.get_pagenum()
title = tax.labels.name
if "post"!=post_type:
  parent_file = "upload.php" if "attachment"==post_type else "edit.php?post_type="+post_type+""
  submenu_file = "edit-tags.php?taxonomy="+taxonomy+"&amp;post_type="+post_type+""
elif "link_category"==tax.name:
  parent_file = "link-manager.php"
  submenu_file = "edit-tags.php?taxonomy=link_category"
else:
  parent_file = "edit.php"
  submenu_file = "edit-tags.php?taxonomy="+taxonomy+""
add_screen_option("per_page", {"label":title, "default":20, "option":"edit_"+tax.name+"_per_page"})
if wp_list_table=="add-tag":
  check_admin_referer("add-tag", "_wpnonce_add-tag")
  if !current_user_can(tax.cap.edit_terms):
    wp_die(__("Cheatin&#8217; uh?"))
  ret = wp_insert_term(_POST["tag-name"], taxonomy, _POST)
  location = "edit-tags.php?taxonomy="+taxonomy
  if "post"!=post_type:
    location+="&post_type="+post_type
  if referer = wp_get_original_referer():
    if False!==strpos(referer, "edit-tags.php"):
      location = referer
  if ret&&!is_wp_error(ret):
    location = add_query_arg("message", 1, location)
  else:
    location = add_query_arg("message", 4, location)
  wp_redirect(location)
  exit(0)
elif wp_list_table=="delete":
  location = "edit-tags.php?taxonomy="+taxonomy
  if "post"!=post_type:
    location+="&post_type="+post_type
  if referer = wp_get_referer():
    if False!==strpos(referer, "edit-tags.php"):
      location = referer
  if !isset(_REQUEST["tag_ID"]):
    wp_redirect(location)
    exit(0)
  tag_ID = _REQUEST["tag_ID"]
  check_admin_referer("delete-tag_"+tag_ID)
  if !current_user_can(tax.cap.delete_terms):
    wp_die(__("Cheatin&#8217; uh?"))
  wp_delete_term(tag_ID, taxonomy)
  location = add_query_arg("message", 2, location)
  wp_redirect(location)
  exit(0)
elif wp_list_table=="bulk-delete":
  check_admin_referer("bulk-tags")
  if !current_user_can(tax.cap.delete_terms):
    wp_die(__("Cheatin&#8217; uh?"))
  tags = _REQUEST["delete_tags"]
  for tag_ID in tags:
    wp_delete_term(tag_ID, taxonomy)
  location = "edit-tags.php?taxonomy="+taxonomy
  if "post"!=post_type:
    location+="&post_type="+post_type
  if referer = wp_get_referer():
    if False!==strpos(referer, "edit-tags.php"):
      location = referer
  location = add_query_arg("message", 6, location)
  wp_redirect(location)
  exit(0)
elif wp_list_table=="edit":
  title = tax.labels.edit_item
  tag_ID = _REQUEST["tag_ID"]
  tag = get_term(tag_ID, taxonomy, OBJECT, "edit")
  if !tag:
    wp_die(__("You attempted to edit an item that doesn&#8217;t exist. Perhaps it was deleted?"))
  require_once("admin-header.php")
  include("./edit-tag-form.php")
elif wp_list_table=="editedtag":
  tag_ID = _POST["tag_ID"]
  check_admin_referer("update-tag_"+tag_ID)
  if !current_user_can(tax.cap.edit_terms):
    wp_die(__("Cheatin&#8217; uh?"))
  tag = get_term(tag_ID, taxonomy)
  if !tag:
    wp_die(__("You attempted to edit an item that doesn&#8217;t exist. Perhaps it was deleted?"))
  ret = wp_update_term(tag_ID, taxonomy, _POST)
  location = "edit-tags.php?taxonomy="+taxonomy
  if "post"!=post_type:
    location+="&post_type="+post_type
  if referer = wp_get_original_referer():
    if False!==strpos(referer, "edit-tags.php"):
      location = referer
  if ret&&!is_wp_error(ret):
    location = add_query_arg("message", 3, location)
  else:
    location = add_query_arg("message", 5, location)
  wp_redirect(location)
  exit(0)
else:
  if !empty(_REQUEST["_wp_http_referer"]):
    location = remove_query_arg(["_wp_http_referer", "_wpnonce"], stripslashes(_SERVER["REQUEST_URI"]))
    if !empty(_REQUEST["paged"]):
      location = add_query_arg("paged", _REQUEST["paged"])
    wp_redirect(location)
    exit(0)
  wp_list_table.prepare_items()
  total_pages = wp_list_table.get_pagination_arg("total_pages")
  if pagenum>total_pages&&total_pages>0:
    wp_redirect(add_query_arg("paged", total_pages))
    exit(0)
  wp_enqueue_script("admin-tags")
  if current_user_can(tax.cap.edit_terms):
    wp_enqueue_script("inline-edit-tax")
  if "category"==taxonomy||"link_category"==taxonomy||"post_tag"==taxonomy:
    help = ""
    if "category"==taxonomy:
      help = "<p>"+sprintf(__("You can use categories to define sections of your site and group related posts. The default category is &#8220;Uncategorized&#8221; until you change it in your <a href="%s">writing settings</a>."), "options-writing.php")+"</p>"
    elif "link_category"==taxonomy:
      help = "<p>"+__("You can create groups of links by using Link Categories. Link Category names must be unique and Link Categories are separate from the categories you use for posts.")+"</p>"
    else:
      help = "<p>"+__("You can assign keywords to your posts using <strong>tags</strong>. Unlike categories, tags have no hierarchy, meaning there&#8217;s no relationship from one tag to another.")+"</p>"
    if "link_category"==taxonomy:
      help+="<p>"+__("You can delete Link Categories in the Bulk Action pull-down, but that action does not delete the links within the category. Instead, it moves them to the default Link Category.")+"</p>"
    else:
      help+="<p>"+__("What&#8217;s the difference between categories and tags? Normally, tags are ad-hoc keywords that identify important information in your post (names, subjects, etc) that may or may not recur in other posts, while categories are pre-determined sections. If you think of your site like a book, the categories are like the Table of Contents and the tags are like the terms in the index.")+"</p>"
    get_current_screen()
    if "category"==taxonomy||"post_tag"==taxonomy:
      if "category"==taxonomy:
        help = "<p>"+__("When adding a new category on this screen, you&#8217;ll fill in the following fields:")+"</p>"
      else:
        help = "<p>"+__("When adding a new tag on this screen, you&#8217;ll fill in the following fields:")+"</p>"
      help+="<ul>"+"<li>"+__("<strong>Name</strong> - The name is how it appears on your site.")+"</li>"
      if !global_terms_enabled():
        help+="<li>"+__("<strong>Slug</strong> - The &#8220;slug&#8221; is the URL-friendly version of the name. It is usually all lowercase and contains only letters, numbers, and hyphens.")+"</li>"
      if "category"==taxonomy:
        help+="<li>"+__("<strong>Parent</strong> - Categories, unlike tags, can have a hierarchy. You might have a Jazz category, and under that have child categories for Bebop and Big Band. Totally optional. To create a subcategory, just choose another category from the Parent dropdown.")+"</li>"
      help+="<li>"+__("<strong>Description</strong> - The description is not prominent by default; however, some themes may display it.")+"</li>"+"</ul>"+"<p>"+__("You can change the display of this screen using the Screen Options tab to set how many items are displayed per screen and to display/hide columns in the table.")+"</p>"
      get_current_screen()
    help = "<p><strong>"+__("For more information:")+"</strong></p>"
    if "category"==taxonomy:
      help+="<p>"+__("<a href="http://codex.wordpress.org/Posts_Categories_Screen" target="_blank">Documentation on Categories</a>")+"</p>"
    elif "link_category"==taxonomy:
      help+="<p>"+__("<a href="http://codex.wordpress.org/Links_Link_Categories_Screen" target="_blank">Documentation on Link Categories</a>")+"</p>"
    else:
      help+="<p>"+__("<a href="http://codex.wordpress.org/Posts_Tags_Screen" target="_blank">Documentation on Tags</a>")+"</p>"
    help+="<p>"+__("<a href="http://wordpress.org/support/" target="_blank">Support Forums</a>")+"</p>"
    get_current_screen()
    unset(help)
  require_once("admin-header.php")
  if !current_user_can(tax.cap.edit_terms):
    wp_die(__("You are not allowed to edit this item."))
  messages[1] = __("Item added.")
  messages[2] = __("Item deleted.")
  messages[3] = __("Item updated.")
  messages[4] = __("Item not added.")
  messages[5] = __("Item not updated.")
  messages[6] = __("Items deleted.")
  print("\n<div class="wrap nosubsub">\n")
  screen_icon()
  print("<h2>")
  print(esc_html(title))
  if !empty(_REQUEST["s"]):
    printf("<span class="subtitle">"+__("Search results for &#8220;%s&#8221;")+"</span>", esc_html(stripslashes(_REQUEST["s"])))
  print("</h2>\n\n")
  if isset(_REQUEST["message"])&&msg = _REQUEST["message"]:
    print("<div id="message" class="updated"><p>")
    print(messages[msg])
    print("</p></div>\n")
    _SERVER["REQUEST_URI"] = remove_query_arg(["message"], _SERVER["REQUEST_URI"])
  print("<div id="ajax-response"></div>\n\n<form class="search-form" action="" method="get">\n<input type="hidden" name="taxonomy" value="")
  print(esc_attr(taxonomy))
  print("" />\n<input type="hidden" name="post_type" value="")
  print(esc_attr(post_type))
  print("" />\n\n")
  wp_list_table.search_box(tax.labels.search_items, "tag")
  print("\n</form>\n<br class="clear" />\n\n<div id="col-container">\n\n<div id="col-right">\n<div class="col-wrap">\n<form id="posts-filter" action="" method="post">\n<input type="hidden" name="taxonomy" value="")
  print(esc_attr(taxonomy))
  print("" />\n<input type="hidden" name="post_type" value="")
  print(esc_attr(post_type))
  print("" />\n\n")
  wp_list_table.display()
  print("\n<br class="clear" />\n</form>\n\n")
  if "category"==taxonomy:
    print("<div class="form-wrap">\n<p>")
    printf(__("<strong>Note:</strong><br />Deleting a category does not delete the posts in that category. Instead, posts that were only assigned to the deleted category are set to the category <strong>%s</strong>."), apply_filters("the_category", get_cat_name(get_option("default_category"))))
    print("</p>\n")
    if current_user_can("import"):
      print("<p>")
      printf(__("Categories can be selectively converted to tags using the <a href="%s">category to tag converter</a>."), "import.php")
      print("</p>\n")
    print("</div>\n")
  elif "post_tag"==taxonomy&&current_user_can("import"):
    print("<div class="form-wrap">\n<p>")
    printf(__("Tags can be selectively converted to categories using the <a href="%s">tag to category converter</a>."), "import.php")
    print("</p>\n</div>\n")
  do_action("after-"+taxonomy+"-table", taxonomy)
  print("\n</div>\n</div><!-- /col-right -->\n\n<div id="col-left">\n<div class="col-wrap">\n\n")
  if !is_null(tax.labels.popular_items):
    if current_user_can(tax.cap.edit_terms):
      tag_cloud = wp_tag_cloud({"taxonomy":taxonomy, "echo":False, "link":"edit"})
    else:
      tag_cloud = wp_tag_cloud({"taxonomy":taxonomy, "echo":False})
    if tag_cloud:
      print("<div class="tagcloud">\n<h3>")
      print(tax.labels.popular_items)
      print("</h3>\n")
      print(tag_cloud)
      unset(tag_cloud)
      print("</div>\n")
  if current_user_can(tax.cap.edit_terms):
    if "category"==taxonomy:
      do_action("add_category_form_pre", {"parent":0})
    elif "link_category"==taxonomy:
      do_action("add_link_category_form_pre", {"parent":0})
    else:
      do_action("add_tag_form_pre", taxonomy)
    do_action(taxonomy+"_pre_add_form", taxonomy)
    print("\n<div class="form-wrap">\n<h3>")
    print(tax.labels.add_new_item)
    print("</h3>\n<form id="addtag" method="post" action="edit-tags.php" class="validate">\n<input type="hidden" name="action" value="add-tag" />\n<input type="hidden" name="screen" value="")
    print(esc_attr(current_screen.id))
    print("" />\n<input type="hidden" name="taxonomy" value="")
    print(esc_attr(taxonomy))
    print("" />\n<input type="hidden" name="post_type" value="")
    print(esc_attr(post_type))
    print("" />\n")
    wp_nonce_field("add-tag", "_wpnonce_add-tag")
    print("\n<div class="form-field form-required">\n	<label for="tag-name">")
    _ex("Name", "Taxonomy Name")
    print("</label>\n	<input name="tag-name" id="tag-name" type="text" value="" size="40" aria-required="true" />\n	<p>")
    _e("The name is how it appears on your site.")
    print("</p>\n</div>\n")
    if !global_terms_enabled():
      print("<div class="form-field">\n	<label for="tag-slug">")
      _ex("Slug", "Taxonomy Slug")
      print("</label>\n	<input name="slug" id="tag-slug" type="text" value="" size="40" />\n	<p>")
      _e("The &#8220;slug&#8221; is the URL-friendly version of the name. It is usually all lowercase and contains only letters, numbers, and hyphens.")
      print("</p>\n</div>\n")
    print("\n")
    if is_taxonomy_hierarchical(taxonomy):
      print("<div class="form-field">\n	<label for="parent">")
      _ex("Parent", "Taxonomy Parent")
      print("</label>\n	")
      wp_dropdown_categories({"hide_empty":0, "hide_if_empty":False, "taxonomy":taxonomy, "name":"parent", "orderby":"name", "hierarchical":True, "show_option_none":__("None")})
      print("	")
      if "category"==taxonomy:
        print("\n		<p>")
        _e("Categories, unlike tags, can have a hierarchy. You might have a Jazz category, and under that have children categories for Bebop and Big Band. Totally optional.")
        print("</p>\n	")
      print("</div>\n")
    print("\n<div class="form-field">\n	<label for="tag-description">")
    _ex("Description", "Taxonomy Description")
    print("</label>\n	<textarea name="description" id="tag-description" rows="5" cols="40"></textarea>\n	<p>")
    _e("The description is not prominent by default; however, some themes may show it.")
    print("</p>\n</div>\n\n")
    if !is_taxonomy_hierarchical(taxonomy):
      do_action("add_tag_form_fields", taxonomy)
    do_action(taxonomy+"_add_form_fields", taxonomy)
    submit_button(tax.labels.add_new_item)
    if "category"==taxonomy:
      do_action("edit_category_form", {"parent":0})
    elif "link_category"==taxonomy:
      do_action("edit_link_category_form", {"parent":0})
    else:
      do_action("add_tag_form", taxonomy)
    do_action(taxonomy+"_add_form", taxonomy)
    print("</form></div>\n")
  print("\n</div>\n</div><!-- /col-left -->\n\n</div><!-- /col-container -->\n</div><!-- /wrap -->\n<script type="text/javascript">\ntry{document.forms.addtag['tag-name'].focus();}catch(e){}\n</script>\n")
  wp_list_table.inline_edit()
  print("\n")
include("./admin-footer.php")
