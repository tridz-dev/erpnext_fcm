## Fcm Notification

Sends Frappe notifications to devices via Firebase Cloud Message

### Steps:

1. Install the app into your site
2. Create a new Server Script with values given below<br />
  i. Script Type: **DocType Event**<br />
  ii. Reference Document Type: **Notification Log**<br />
  iii. DocType Event: **Before Insert**<br />
  iv. Script: `frappe.call("fcm_notification.send_notification.send_notification", doc=doc)`<br />

2. Add your server key in FCM Notification Settings.

3. Create any notification.

4. Run an event that triggers the notification created above.
