# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "l3harris"
app_title = "L3Harris"
app_publisher = "Rahi Systems Pvt Ltd"
app_description = "L3Harris ISP Ecommerce Website"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "vigneshwaran.a@rahisystems.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/l3harris/css/l3harris.css"
# app_include_js = "/assets/l3harris/js/l3harris.js"

# include js, css files in header of web template
web_include_css = [
    
    #"assets/l3harris/css/bootstrap.min.css",
    "assets/l3harris/css/responsive.css",
    "/assets/l3harris/vendors/scroll/jquery.mCustomScrollbar.min.css",
    "/assets/l3harris/vendors/bootstrap-selector/css/bootstrap-select.min.css",
    "/assets/l3harris/vendors/themify-icon/themify-icons.css",
    "/assets/l3harris/vendors/flaticon/flaticon.css",
    "/assets/l3harris/vendors/animation/animate.css",
    "/assets/l3harris/vendors/owl-carousel/assets/owl.carousel.min.css",
    "/assets/l3harris/vendors/magnify-pop/magnific-popup.css",
    "/assets/l3harris/vendors/nice-select/nice-select.css",
    "/assets/l3harris/vendors/elagent/style.css",
    "assets/l3harris/css/style.css",
    "assets/l3harris/css/l3harris.css"
]
web_include_js = [
    "/assets/l3harris/vendors/wow/wow.min.js",
    "/assets/l3harris/vendors/sckroller/jquery.parallax-scroll.js",
    "/assets/l3harris/vendors/owl-carousel/owl.carousel.min.js",
    "/assets/l3harris/vendors/imagesloaded/imagesloaded.pkgd.min.js",
    "/assets/l3harris/vendors/isotope/isotope-min.js",
    "/assets/l3harris/vendors/magnify-pop/jquery.magnific-popup.min.js",
    "/assets/l3harris/vendors/bootstrap-selector/js/bootstrap-select.min.js",
    "/assets/l3harris/vendors/nice-select/jquery.nice-select.min.js",
    "/assets/l3harris/vendors/scroll/jquery.mCustomScrollbar.concat.min.js",
    #"/assets/l3harris/js/jquery-3.2.1.min.js",
    "/assets/l3harris/js/propper.js",
    #"/assets/l3harris/js/bootstrap.min.js",
    "/assets/l3harris/js/main.js",
    "/assets/l3harris/js/plugins.js",
    "/assets/l3harris/js/jquery.validate.min.js",
    "/assets/l3harris/js/jquery.form.js"
    
]

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "homepage"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "l3harris.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "l3harris.install.before_install"
# after_install = "l3harris.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "l3harris.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"l3harris.tasks.all"
# 	],
# 	"daily": [
# 		"l3harris.tasks.daily"
# 	],
# 	"hourly": [
# 		"l3harris.tasks.hourly"
# 	],
# 	"weekly": [
# 		"l3harris.tasks.weekly"
# 	]
# 	"monthly": [
# 		"l3harris.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "l3harris.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "l3harris.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "l3harris.task.get_dashboard_data"
# }

