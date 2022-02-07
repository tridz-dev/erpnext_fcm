# FCM Notification for ERPNext
Send notifications created in Frappe or ERPNext as push notication via Firebase Cloud Message(FCM)

### Steps to use the app:

1. Install the app into your site. [(Refer)](https://frappeframework.com/docs/v13/user/en/bench/frappe-commands#app-installation)

2. Create a new Server Script with values given below<br />
  i. Script Type: **DocType Event**<br />
  ii. Reference Document Type: **Notification Log**<br />
  iii. DocType Event: **Before Insert**<br />
  iv. Script: `frappe.call("fcm_notification.send_notification.send_notification", doc=doc)`<br />
To learn more about server scripts [see this link.](https://frappeframework.com/docs/v13/user/en/desk/scripting/server-script) 

2. Add your server key in FCM Notification Settings.

3. Optionally create a notification in Frappe/ERPNext. [(Refer)](https://docs.erpnext.com/docs/v12/user/manual/en/setting-up/notifications)

4. Run an event that triggers any notification. The notifcation will be send the respetive user via FCM if they have subscribed to it.


## Supporting Organization

The development of this app was commissioned by [Searchosis marketing Pvt Ltd](searchosis.com)

<img src="https://user-images.githubusercontent.com/246454/152739360-185e022a-3474-4d4a-9c89-5922bad401c0.png" width="120">
