import imdb
import os
import sys
from subprocess import call

def clean_scr():
#     # check and make call for specific operating system
#     _ = call('clear' if os.name =='posix' else 'cls')
	if os.name == 'posix':
		os.system('cear')
	else:
		os.system('cls')

imdbObj = imdb.IMDb()
movie_id = ""

# movie_id = '0082198' # from a1_imdb_search_movies.py
if not len(sys.argv ) > 1:
    # clean_scr()
    print("You must supply a movie ID (imdb)!\n")
    sys.exit(1)
else:
    movie_id = sys.argv[1]

MV = imdbObj.get_movie(movie_id)

# print(MV.keys())

""" def print_names(my_list):
    if not len(my_list) < 1:
        for name in my_list:
            print(f'{name.get("name")}') """

def print_names(my_list):
    if not len(my_list) < 1:
        print(", ".join([name.get("name") for name in my_list]))

def movie_info():
    mv_title = MV.get('long imdb title')
    mv_cast = MV.get('cast')
    mv_plot = MV.get('plot')
    print(f"Title: {mv_title}")
    # print(f'\nCast:\n{mv_cast[0].get("name")}')
    print(f'\nCast:')
    print_names(mv_cast)
    print(f'\nPlot:\n{mv_plot}')

if __name__ == "__main__":
    # clean_scr()
    print("Printing movie info ...")
    movie_info()

