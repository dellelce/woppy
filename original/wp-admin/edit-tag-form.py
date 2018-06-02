#!/usr/bin/python
#-*- coding: utf-8 -*-
if !defined("ABSPATH"):
  die("-1")
if empty(tag_ID):
  print("	<div id="message" class="updated"><p><strong>")
  _e("You did not select an item for editing.")
  print("</strong></p></div>\n")
  return 
if "category"==taxonomy:
  do_action("edit_category_form_pre", tag)
elif "link_category"==taxonomy:
  do_action("edit_link_category_form_pre", tag)
else:
  do_action("edit_tag_form_pre", tag)
do_action(taxonomy+"_pre_edit_form", tag, taxonomy)
print("\n<div class="wrap">\n")
screen_icon()
print("<h2>")
print(tax.labels.edit_item)
print("</h2>\n<div id="ajax-response"></div>\n<form name="edittag" id="edittag" method="post" action="edit-tags.php" class="validate">\n<input type="hidden" name="action" value="editedtag" />\n<input type="hidden" name="tag_ID" value="")
print(esc_attr(tag.term_id))
print("" />\n<input type="hidden" name="taxonomy" value="")
print(esc_attr(taxonomy))
print("" />\n")
wp_original_referer_field(True, "previous")
wp_nonce_field("update-tag_"+tag_ID)
print("	<table class="form-table">\n		<tr class="form-field form-required">\n			<th scope="row" valign="top"><label for="name">")
_ex("Name", "Taxonomy Name")
print("</label></th>\n			<td><input name="name" id="name" type="text" value="")
if isset(tag.name):
  print(esc_attr(tag.name))
print("" size="40" aria-required="true" />\n			<p class="description">")
_e("The name is how it appears on your site.")
print("</p></td>\n		</tr>\n")
if !global_terms_enabled():
  print("		<tr class="form-field">\n			<th scope="row" valign="top"><label for="slug">")
  _ex("Slug", "Taxonomy Slug")
  print("</label></th>\n			<td><input name="slug" id="slug" type="text" value="")
  if isset(tag.slug):
    print(esc_attr(apply_filters("editable_slug", tag.slug)))
  print("" size="40" />\n			<p class="description">")
  _e("The &#8220;slug&#8221; is the URL-friendly version of the name. It is usually all lowercase and contains only letters, numbers, and hyphens.")
  print("</p></td>\n		</tr>\n")
if is_taxonomy_hierarchical(taxonomy):
  print("		<tr class="form-field">\n			<th scope="row" valign="top"><label for="parent">")
  _ex("Parent", "Taxonomy Parent")
  print("</label></th>\n			<td>\n				")
  wp_dropdown_categories({"hide_empty":0, "hide_if_empty":False, "name":"parent", "orderby":"name", "taxonomy":taxonomy, "selected":tag.parent, "exclude_tree":tag.term_id, "hierarchical":True, "show_option_none":__("None")})
  print("				")
  if "category"==taxonomy:
    print("				<p class="description">")
    _e("Categories, unlike tags, can have a hierarchy. You might have a Jazz category, and under that have children categories for Bebop and Big Band. Totally optional.")
    print("</p>\n				")
  print("			</td>\n		</tr>\n")
print("\n		<tr class="form-field">\n			<th scope="row" valign="top"><label for="description">")
_ex("Description", "Taxonomy Description")
print("</label></th>\n			<td><textarea name="description" id="description" rows="5" cols="50" class="large-text">")
print(tag.description)
print("</textarea><br />\n			<span class="description">")
_e("The description is not prominent by default; however, some themes may show it.")
print("</span></td>\n		</tr>\n		")
if "category"==taxonomy:
  do_action("edit_category_form_fields", tag)
elif "link_category"==taxonomy:
  do_action("edit_link_category_form_fields", tag)
else:
  do_action("edit_tag_form_fields", tag)
do_action(taxonomy+"_edit_form_fields", tag, taxonomy)
print("	</table>\n")
if "category"==taxonomy:
  do_action("edit_category_form", tag)
elif "link_category"==taxonomy:
  do_action("edit_link_category_form", tag)
else:
  do_action("edit_tag_form", tag)
do_action(taxonomy+"_edit_form", tag, taxonomy)
submit_button(__("Update"))
print("</form>\n</div>\n<script type="text/javascript">\ntry{document.forms.edittag.name.focus();}catch(e){}\n</script>\n")
