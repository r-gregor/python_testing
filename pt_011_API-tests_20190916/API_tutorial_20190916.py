#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# freom: https://www.dataquest.io/blog/python-api-tutorial/

import requests
response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)

print(response.json())

import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())


#LJUBLJANA GEO info:
# https://www.latlong.net/place/ljubljana-slovenia-9549.html
# 
# Ljubljana, Slovenia Geographic Information
# Country       Slovenia
# Latitude      46.056946
# Longitude     14.505751
# DMS Lat       46° 3' 25.0056'' N
# DMS Long      14° 30' 20.7036'' E
# UTM Easting   461,768.45
# UTM Northing  5,100,493.35
# Category      Cities
# Country Code  SI
# Zoom Level    10


# ISS pass time endpoint:
# http://open-notify.org/Open-Notify-API/ISS-Pass-Times/


# acceptable range:
# Latitude      The latitude of the place to predict passes     lat -80..80     degrees
# Longitude     The longitude of the place to predict passes    lon -180..180   degrees

# location in degrees only:
# Latitude: 46° 3' 25.0056" = 46° + 3'/60 + 25.0056"/3600 = 46.05695°
# Longitude: 14° 30' 20.7036" = 14° + 30'/60 + 20.7036"/3600 = 14.50575°

parameters = {
    "lat": 46.06,
    "lon": 14.51
}

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
jprint(response.json())

# extract just the risetime durations into a list
pass_times = response.json()['response']
jprint(pass_times)

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)

# convert risetimes to date format:
from datetime import datetime

times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)

# List od public APIs:
# https://github.com/public-apis/public-apis
