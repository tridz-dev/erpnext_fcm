import frappe
import requests
import json
from frappe import enqueue
import re

def user_id(doc):
    user_email = doc.for_user
    user_device_id = frappe.get_all("User Device", filters= {"user": user_email}, fields=["device_id"])
    return user_device_id

@frappe.whitelist()
def send_notification(doc):
    device_ids = user_id(doc)

    for device_id in device_ids:
        enqueue(process_notification, queue="default", now=False,\
                         device_id=device_id, notification=doc)

def convert_message(message):
    CLEANR = re.compile('<.*?>')
    cleanmessage = re.sub(CLEANR, "",message)
    # cleantitle = re.sub(CLEANR, "",title)
    return cleanmessage

def process_notification(device_id, notification):
    message = notification.email_content
    title = notification.subject
    if message:
        message = convert_message(message)
    if title:
        title = convert_message(title)

    url = "https://fcm.googleapis.com/fcm/send"
    body = {
        "to": device_id.device_id,
        "notification": {
            "body": message,
            "title": title
        },
        "data": {
            "doctype": notification.document_type,
            "docname": notification.document_name
        }
    }

    server_key = frappe.db.get_single_value('FCM Notification Settings', 'server_key')
    req = requests.post(url=url, data=json.dumps(body), headers={"Authorization": server_key, \
                                                                "Content-Type": "application/json", \
                                                                "Accept": "application/json"})
