import requests

API_URL = "https://api.whatsapp.com/send"

def send_invoice(phone, amount):
    message = f"""
🙏 Thank you for visiting!

Your bill: ₹{amount}

Next visit: Flat 10% OFF 🎉
    """

    payload = {
        "phone": phone,
        "text": message
    }

    requests.post(API_URL, json=payload)
