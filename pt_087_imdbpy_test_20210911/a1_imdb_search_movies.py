import imdb
import os
import sys
from subprocess import call

def clean_scr():
#	  # check and make call for specific operating system
#	  # _ = call('clear' if os.name =='posix' else 'cls')
	if os.name == 'posix':
		os.system('clear')
	else:
		os.system('cls')

imdbObj = imdb.IMDb()
my_movie_name = ""

movies_found = {}

if not len(sys.argv ) > 1:
	clean_scr()
	print("You must supply a part of movie name (imdb)!\n")
	sys.exit(1)
else:
	my_movie_name = sys.argv[1]

ML = imdbObj.search_movie(my_movie_name)


""" print(ML[1].keys())
keys = ['title', 'kind', 'year', 'cover url', 'canonical title', 'long imdb title', 'long imdb canonical title', 'smart canonical title', 'smart long imdb canonical title', 'full-size cover url']
for key in keys:
	print(key + ": " + str(ML[1].get(key))) """

""" if len(ML) > 0:
	for MV in ML:
		print(f"id: {MV['id']}, {MV.get('long imdb title')}") """

if len(ML) > 0:
	for i in range(len(ML)):
		id = ML[i].movieID
		title = ML[i].get('long imdb title')
		movies_found[id] = title
		# print(f"{i:<4}{id}: {title}")
else:
	clean_scr()
	print(f"No movie \"{my_movie_name}\" found!")

for id,title in movies_found.items():
	print(f"{id:<12}{title}")

