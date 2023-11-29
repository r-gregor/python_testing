import imdb
ia = imdb.Cinemagoer()
movies = ia.search_movie('conan')
movies_nmr = len(movies)
print(f"Number of 'conan' media found: {movies_nmr}")

# TEST
# print(movies)
# print(movies[0].keys())
# print(movies[0].get('title'))

count = 0
for mv in movies:
	count += 1
	print(f"{count:>2} |", end = "")
	print(f"{mv.movieID:>12} | ", end="")
	print(f"{mv.get('long imdb title')}")

print("------------------------------------------------")

selected = 1
selected_mv = ia.get_movie(movies[selected - 1].movieID)
print(f"Displaying entry {selected}: ", end="")
print(f"{selected_mv.get('long imdb title')}")
print(f"Plot:")
print(f"{selected_mv.get('plot')}")

