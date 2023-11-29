import json

'''
Serialization: dump of dict to external JSON file, and load the data from external JSON file to dict object.

'''

D = {}
D['ime'] = 'Gregor'
D['priimek'] = 'Redelonghi'
D['naslov'] = ['Valvasorjeva ulica', 5]
D['kraj'] = ['Ljubljana', 1000]
D['e-posta'] = ['gredelonghi@gmail.com', 'rgregor.rgr@gmail.com', 'gregorr@email.si', 'gredelonghi@yahoo.com']
D['leto-rojstva'] = 1968

# dump the contents of dict into JSON
with open('JAZ.json', mode='w', encoding='utf-8') as f:
	json.dump(D, f, indent=4)

# read JSON into dict object
with open('JAZ.json', mode='r', encoding='utf-8') as f:
	entry = json.load(f)

# printout contents of a dict -- if value is a list --> print elements in a single line
# separated by commas

def printout(entry):
	for k, v in entry.items():
		print("{0:<15}".format(k.capitalize() + ": "), end="")
		# print(k, end=": ")
		if isinstance(v, list):
			L = [] # empty list
			for e in v:
				L.append(str(e))
			vls = ", ".join(L)
			print(vls)	
			del L # flush from memmory
			del vls # flush from memmory
		else:
			print(v)
	print()

printout(entry)
