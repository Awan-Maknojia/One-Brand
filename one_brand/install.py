import frappe
def setup_entry_portal():
    doc = frappe.get_single("Entry Portal")
    doc.logo = "/assets/one_brand/images/cubezixone.png"
    doc.ios_logo = "/assets/one_brand/images/appstore.png"
    doc.android_logo = "/assets/one_brand/images/playstore.png"
    doc.save(ignore_permissions=True)