import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['ACf60fdda2798df69bd8ec1b8e3b0a46d3']
auth_token = os.environ['ef4170827ed8057bc8b618bee1c3e23a]
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+12626003393',
         to='+15183389075'
     )

print(message.sid)