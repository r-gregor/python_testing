def namelist(names):

	str = ''

	if(len(names) == 0): # if no dictionary within the list
		return ''

	elif(len(names) == 1): # if only one dictionary within the list
		return names[0]['name']

	for i in range(len(names)):
		if(i == len(names)-2): # if reaches the second last dictionary
			str += names[i]['name'] + ' &amp; '
		elif(i == len(names) - 1): # if reaches the last dictionary
			str += names[i]['name']
		else:
			str += names[i]['name'] + ', '

	return str

   # After a few runs, we get the below outcomes.
print(namelist([{'name' : 'Johnny'}, {'name' : 'Bill'}, {'name' : 'Mickey'}]))
print(namelist([{'name' : 'Johnny'}, {'name' : 'Bill'}]))
print(namelist([{'name' : 'Johnny'}]))
print(namelist([]))
