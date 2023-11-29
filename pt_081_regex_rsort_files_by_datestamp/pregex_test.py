import re
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir(".") if isfile(f)]
# print(onlyfiles)

flist = []

def get_expr(fname):
	M = re.search("([0-9]{8})", fname)
	if M:
		expr = (M.group(1), fname)
		flist.append(expr)
	else:
		pass

for fname in onlyfiles:
	get_expr(fname)	

flist.sort(reverse=True)

for fname2 in flist:
	print(f"{fname2[0]:<10}{fname2[1]}")
