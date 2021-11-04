import requests
from twilio.rest import Client
import time

ACCOUNT_SID = "ACf66ecabe3a907d6c1ac8a0f0cd9ea8b7"
AUTH_TOKEN = "f14ffeb42d0ee8e89e7fe9d2e893ae11"

ISS_API_ENDPOINT = 'http://api.open-notify.org/iss-now.json'
MY_LATITUDE = 51.497799
MY_LONGITUDE = -0.179220


def iss_overhead(latitude, longitude):
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    iss_latitude = response.json()['iss_position']['latitude']
    iss_longitude = response.json()['iss_position']['longitude']
    if MY_LATITUDE - 5 < float(iss_latitude) < MY_LATITUDE + 5:
        if MY_LATITUDE - 5 < float(iss_longitude) < MY_LATITUDE + 5:
            return True


def send_twilio_message(phone_number):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        body="Hello Charlie Lindsay. Based on your current coordinates, if you go outside (and it is dark), you should be able to see the ISS!! Hurry! Don't miss it! 🛰️",
        from_='+14174572296',
        to=phone_number
    )


for i in range(100):
    if iss_overhead(latitude=MY_LATITUDE, longitude=MY_LONGITUDE):
        send_twilio_message(phone_number='+447414803838')
    time.sleep(5 * 60)

