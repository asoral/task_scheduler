from . import __version__ as app_version

app_name = "task_scheduler"
app_title = "Task Scheduler"
app_publisher = "k"
app_description = "kk"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "k"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/task_scheduler/css/task_scheduler.css"
# app_include_js = "/assets/task_scheduler/js/task_scheduler.js"

# include js, css files in header of web template
# web_include_css = "/assets/task_scheduler/css/task_scheduler.css"
# web_include_js = "/assets/task_scheduler/js/task_scheduler.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "task_scheduler/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Project" : "public/custom_project.js",
			"Task" : "public/js/custom_task.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "task_scheduler.install.before_install"
# after_install = "task_scheduler.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "task_scheduler.uninstall.before_uninstall"
# after_uninstall = "task_scheduler.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "task_scheduler.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#  	"Project": {
# 		"refresh": "task_scheduler.task_scheduler.custom_pjoject.task",
# # 		"on_cancel": "method",
# # 		"on_trash": "method"
# 	}
#  }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"task_scheduler.tasks.all"
# 	],
# 	"daily": [
# 		"task_scheduler.tasks.daily"
# 	],
# 	"hourly": [
# 		"task_scheduler.tasks.hourly"
# 	],
# 	"weekly": [
# 		"task_scheduler.tasks.weekly"
# 	]
# 	"monthly": [
# 		"task_scheduler.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "task_scheduler.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "task_scheduler.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "task_scheduler.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"task_scheduler.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
