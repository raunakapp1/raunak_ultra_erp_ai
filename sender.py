from twilio.rest import Client

ACCOUNT_SID="YOUR_SID"
AUTH_TOKEN="YOUR_TOKEN"

client=Client(ACCOUNT_SID,AUTH_TOKEN)

def send_whatsapp(num,msg):
    client.messages.create(
        from_="whatsapp:+14155238886",
        to=f"whatsapp:{num}",
        body=msg
    )