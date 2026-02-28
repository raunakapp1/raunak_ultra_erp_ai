from sender import send_whatsapp

def send_campaign(numbers,offer):
    for n in numbers:
        send_whatsapp(n,f"🔥 Offer: {offer}")