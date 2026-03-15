import frappe

def get_context(context):
    enabled = frappe.db.get_single_value("Entry Portal", "enable_page")

    if not enabled:
        frappe.local.flags.redirect_location = "/login"
        raise frappe.Redirect
