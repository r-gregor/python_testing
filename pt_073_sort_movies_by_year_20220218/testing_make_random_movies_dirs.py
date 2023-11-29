import random

year = random.randint(1970, 2022)

alphabet = ["a","b","c","č","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","š","t","u","v","z",
"ž","A","B","C","Č","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","Š","T","U","V","Z"]

word = ""
wordlen = random.randint(5,15)


for i in range(wordlen):
	char = random.randint(0, len(alphabet) - 1)
	word += alphabet[char]

print(f"Movie {word} ({year})")

# bash command to create 100 dumy movie dirs:
#	for N in $(seq 1 100); do mkdir -p "$(p3 testing_make_random_movies_dirs.py)"; done
