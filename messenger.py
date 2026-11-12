import requests
from config import Config

def send_messenger_reply(recipient_id, message_text):
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={Config.FB_PAGE_ACCESS_TOKEN}"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text},
    }
    response = requests.post(url, json=payload, timeout=10)
    return response.json()
