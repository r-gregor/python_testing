#!/usr/bin/env python3
# coding: utf-8

import json
import requests
import datetime

danes = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

apiurl = "https://api.sunrise-sunset.org/json"

"""
# test print
parameters = {
    "lat": 46.06,
    "lng": 14.51
}

# response = requests.get(apiurl, params=parameters)
# print(response.status_code)
"""

def vzhod_zahod(*datum):
    # danes = datetime.datetime.now().strftime("%Y-%m-%d")

    for dt in datum:
        parameters = {
        "lat": 46.06,
        "lng": 14.51,
        "date": dt
        }
        
        response = requests.get(apiurl, params=parameters)
        data = response.json()['results']

        vzhod = data['sunrise']
        zahod = data['sunset']
        dolzina = data['day_length']

        print("Datum: {}\n==========================".format(dt))
        print("Sončni vzhod: {}".format(vzhod))
        print("Sončni zahod: {}".format(zahod))
        print("Dolžina dneva: {}".format(dolzina))
        print("")



vzhod_zahod("1968-02-22", "2022-02-22", "1970-01-19")
