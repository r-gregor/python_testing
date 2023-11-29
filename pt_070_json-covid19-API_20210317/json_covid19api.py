#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
import os, sys

# test (json) API URL
summary = "https://api.covid19api.com/summary"

response = requests.get(summary).text
# response = requests.get(summary).json()

# load jason into dictionary
response_info = json.loads(response)

# Countires list into my dict
countries_L2= {}
for country_info in response_info['Countries']:
	countries_L2[country_info['Country']] = [country_info["NewConfirmed"], country_info['TotalConfirmed']]


def headerPrint():
	print("{:<40}{:<16}{:<7}".format("Country", "New confirmed", "Total"))
	print("-"*63)

def checkIfKey(partName):
	state = False
	for k,v in countries_L2.items():
		if partName.upper() in k.upper():
			state = True
			return state
	return state


def choicePrint(partName):
	if checkIfKey(partName):
		headerPrint()
		for k,v in countries_L2.items():
			if partName.upper() in k.upper():
				print("{:<40}{:<16}{:<7}".format(k, v[0], v[1]))
	else:
		print("{} not in database!".format(partName))


if len(sys.argv) != 2:
	print("No countryname as parameter suplied!")
	sys.exit(1)
elif sys.argv[1] =="0":
	list = []
	print("Countries with 0 new comfirmed cases:", end=" ")
	for k,v in countries_L2.items():
		if v[0] == 0:
			list.append(k)
			# print("{:<40}{:<16}{:<7}".format(k, v[0], v[1]))
	print(",".join(list))

elif sys.argv[1] == "1":
	headerPrint()
	for k,v in countries_L2.items():
		if int(v[0]) > 0:
			print("{:<40}{:<16}{:<7}".format(k, v[0], v[1]))

else:
	partName = sys.argv[1]
	choicePrint(partName)

