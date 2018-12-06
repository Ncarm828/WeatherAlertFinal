# coding=utf-8

import os
import json
import requests
import random


class TwilioClient(object):
   
    ###    A simple client for Twilio messaging  ###
    def __init__(self):
        super(TwilioClient, self).__init__()

        self.ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
        self.AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
        self.PHONE_NUM = os.environ.get("TWILIO_PHONE_NUMBER")

    def send_message(self, to, message):

        ERROR_REPORT = False

        if len(message) > 160:
            raise Exception("Message is too long ({} chars)".format(len(message)))

        if not to.startswith("+"):
            to = "+1" + str(to)

        to = to.replace(' ','')
        to = to.replace('-','')

        endpoint = "https://api.twilio.com/2010-04-01/Accounts/{acct_sid}/SMS/Messages.json".format(acct_sid=self.ACCOUNT_SID)
        data = {
            "From": self.PHONE_NUM,
            "To": to,
            "Body": message
        }

        r = requests.post(endpoint, auth=(self.ACCOUNT_SID, self.AUTH_TOKEN), data=data)
        response = json.loads(r.text)

        if r.status_code not in [200, 201]:
            raise Exception("Twilio refused the messages: %s" % response.get("message"))

        return response




    def send_confirmation_code(self, to_number):
        verification_code = self.generate_code()
        self.send_message(to_number, verification_code)
        return verification_code


    def generate_code(self):
        return str(random.randrange(100000, 999999))

