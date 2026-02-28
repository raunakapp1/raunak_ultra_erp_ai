from sender import send_whatsapp

def send_invoice(num,amount,bill):
    send_whatsapp(num,f"🧾 Bill {bill} | ₹{amount}")