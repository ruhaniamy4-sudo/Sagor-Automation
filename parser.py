import re

def parse_order_message(text):
    """মেসেজ থেকে নাম, ফোন নম্বর, ঠিকানা এবং দাম আলাদা করে।"""
    data = {"name": None, "phone": None, "address": None, "amount": 0}

    phone_match = re.search(r"(?:\+?88)?(01[3-9]\d{8})", text)
    if phone_match:
        data["phone"] = phone_match.group(1)

    name_match = re.search(
        r"(?:নাম|Name)\s*[:\-]\s*(.+)", text, re.IGNORECASE
    )
    address_match = re.search(
        r"(?:ঠিকানা|Address)\s*[:\-]\s*(.+)", text, re.IGNORECASE
    )
    amount_match = re.search(
        r"(?:দাম|টাকা|মুল্য|COD|Amount|Price)\s*[:\-]?\s*(\d+)",
        text,
        re.IGNORECASE,
    )

    if name_match:
        data["name"] = name_match.group(1).strip()
    if address_match:
        data["address"] = address_match.group(1).strip()
    if amount_match:
        data["amount"] = int(amount_match.group(1))

    return data
