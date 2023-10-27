from twilio.rest import Client
from config import account_sid,auth_token


client = Client(account_sid,auth_token)
client.messages.create(
    to="+50688473578",
    from_="+16562184241",
    body="Good night Mate"
)