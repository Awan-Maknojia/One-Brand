import frappe
def setup_entry_portal():
    entry_portal = frappe.get_single("Entry Portal")
    entry_portal.logo = "/assets/one_brand/images/cubezixone.png"
    entry_portal.ios_logo = "/assets/one_brand/images/appstore.png"
    entry_portal.android_logo = "/assets/one_brand/images/playstore.png"
    entry_portal.save()
    website_settings = frappe.get_doc("Website Settings")
    website_settings.brand_image = "/assets/one_brand/images/cubezixone.png"
    website_settings.banner_image = "/assets/one_brand/images/cubezixone.png"
    website_settings.splash_image = "/assets/one_brand/images/cubezixone.png"
    website_settings.favicon = "/assets/one_brand/images/cubezixone.png"
    website_settings.app_logo = "/assets/one_brand/images/cubezixone.png"
    website_settings.save()
