from flask import Flask, jsonify, request
from config import Config
from messenger import send_messenger_reply
from parser import parse_order_message
from steadfast import create_steadfast_order

app = Flask(__name__)

@app.route("/webhook", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == Config.FB_VERIFY_TOKEN:
        return challenge, 200
    return "Verification failed", 403

@app.route("/webhook", methods=["POST"])
def handle_webhook():
    body = request.get_json()
    if body and body.get("object") == "page":
        for entry in body.get("entry", []):
            for event in entry.get("messaging", []):
                sender_id = event["sender"]["id"]
                if "message" in event and "text" in event["message"]:
                    msg_text = event["message"]["text"]
                    order = parse_order_message(msg_text)

                    if order["name"] and order["phone"] and order["address"]:
                        res = create_steadfast_order(
                            order["name"],
                            order["phone"],
                            order["address"],
                            order["amount"],
                        )
                        if res.get("status") == 200:
                            consignment = res.get("consignment", {})
                            tracking = consignment.get("tracking_code", "N/A")
                            reply = f"✅ আপনার অর্ডারটি বুকিং হয়েছে!\nTracking Code: {tracking}"
                        else:
                            reply = "⚠️ কুরিয়ার বুকিংয়ে সমস্যা হয়েছে। অনুগ্রহ করে অপেক্ষা করুন।"
                        send_messenger_reply(sender_id, reply)
        return jsonify({"status": "ok"}), 200
    return "Not Found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=Config.PORT)
