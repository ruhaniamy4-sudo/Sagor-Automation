import time
import requests
from config import Config

def create_steadfast_order(name, phone, address, amount, invoice=None):
    if not invoice:
        invoice = f"INV-{int(time.time())}"

    url = f"{Config.STEADFAST_BASE_URL}/create_order"
    headers = {
        "Api-Key": Config.STEADFAST_API_KEY,
        "Secret-Key": Config.STEADFAST_SECRET_KEY,
        "Content-Type": "application/json",
    }
    payload = {
        "invoice": invoice,
        "recipient_name": name,
        "recipient_phone": phone,
        "recipient_address": address,
        "cod_amount": amount,
    }

    response = requests.post(url, json=payload, headers=headers, timeout=10)
    return response.json()
