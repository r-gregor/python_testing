#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json

import urllib3

# http = urllib3.PoolManager() PROXY !!! --> instead of PollManager
#											ProxyManager

http = urllib3.ProxyManager("http://172.17.3.64:80/")

heroes = http.request('GET', 'https://api.opendota.com/api/heroes')


# print(heroes) --> only shows object data

# shows a list
# print(heroes.data)

# shows a dict!
heroes_dict = json.loads(heroes.data.decode('UTF-8'))

for hero in heroes_dict:
	print(hero)

for item in heroes_dict:
	print(item['localized_name'])
# # --------------------------------------------------------------------
# excersize
# https://github.com/toddmotto/public-apis
# https://dog.ceo/dog-api
dogs = http.request('GET', 'https://dog.ceo/api/breeds/list/all')
# print(dogs.data)

dogs_dict = json.loads(dogs.data.decode('UTF-8'))
print(dogs_dict)

# not working: structure of dict ...
for dog in dogs_dict:
	print(dog['message']['spaniel'])
