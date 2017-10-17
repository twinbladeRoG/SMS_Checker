# -*- coding: utf-8 -*-

"""
Profanity check enabled SMS check using Twilio
----------------------------------------------

To run this program type following commands in your console:-

> python send_sms.py <your message>

Example:-

> python send_sms.py "Hello World"

"""

# %%
import sys
import requests
from twilio.rest import Client
from credentials import account_sid, auth_token, my_twilio_no, my_cell_no


# %%
def send_msg(msg):
    """ Sends the SMS using Twilio Clent """
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=my_cell_no,
        from_=my_twilio_no,
        body=msg)
    print("Message ID:", message.sid)


# %%
def request(word):
    """ Sends and Checks for profanity """
    payload = {'q': word}
    r = requests.get('http://www.wdylike.appspot.com/', params=payload)
    if "true" in r.text:
        print("\nAlert! Profanity in the message.\n")
    elif "false" in r.text:
        print("\nNo Profanity detected.\nSending message to", my_cell_no, "\n")
        send_msg(word)
    else:
        print("\nFailed to detect\n")


# %%
def send_request(s):
    """ Checks for empty request """
    if s:
        request(s)
    else:
        print("Empty")


# %%
def get_arg():
    """ Gets the command line arguments """
    n = len(sys.argv)  # stores the number of arguments
    if n == 2:
        send_request(sys.argv[1])
    else:
        print("No or more arguments passed")


# %%
get_arg()
# %%
