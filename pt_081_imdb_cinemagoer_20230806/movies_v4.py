# v4
import imdb
ia = imdb.Cinemagoer()

movie_name = input("Enter movie name: ")
movies = ia.search_movie(movie_name)
movies_nmr = len(movies)
print(f"Number of '{movie_name}' media found: {movies_nmr}")

# TEST
# print(movies)
# print(movies[0].keys())
# print(movies[0].get('title'))

while True:
	count = 0
	for mv in movies:
		count += 1
		print(f"{count:>2} |", end = "")
		print(f"{mv.movieID:>12} | ", end="")
		print(f"{mv.get('long imdb title')}")

	print("-" * 110)

	print(f"Select movie: [1 .. {movies_nmr}]:  ", end="")
	selected = int(input())
	selected_mv = ia.get_movie(movies[selected - 1].movieID)
	print(f"Displaying entry {selected}: ", end="")
	print(f"{selected_mv.get('long imdb title')}")
	print(f"Plot:")
	print(f"{selected_mv.get('plot')}")
	leave = input("q - Quit, or keep going - any key: ")
	if leave == "q" or leave == "Q":
		break

