# ONE BRAND – Installation Guide

This guide explains how to install the **ONE BRAND** app and apply the default branding images for the **Entry Portal** DocType.

---

## 1. Install the App

From your bench directory, install the app on your site:

```
bench --site yoursite install-app one_brand
```

Replace **`yoursite`** with your actual site name.

Example:

```
bench --site site1.local install-app one_brand
```

---

## 2. Apply Default Branding Configuration

After installing the app, run the setup function to populate the **Entry Portal** Single DocType with the default images.

```
bench --site yoursite execute one_brand.install.setup_entry_portal
```


These images are located in:

```
apps/one_brand/one_brand/public/images/
```

---

## 3. Build Assets

Since the app contains static assets (images), rebuild the frontend assets:

```
bench build
```



---

## 4. Restart Bench

Restart bench to apply all changes:

```
bench restart
```

---

## 5. Verify Installation

Open your site in the browser and verify that the branding images load correctly.

Example test URL:

```
http://localhost:8000/assets/one_brand/images/image.png
```

If the image loads, the installation is successful.

---

## Notes

* The **Entry Portal** DocType is a **Single DocType** used for managing branding settings.
* Default images are bundled with the app and served via the **Frappe assets system**.
* If you change images inside the `public/images` folder later, you must run:

```
bench build
bench restart
```

---
