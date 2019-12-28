import os
import requests
import random

# For User Interface
print("Pokemon World")
print("@@@@@@@@@@@@@")
pokemon = input("Enter the Pokemon : ")

# Getting response from Pokemontcg API
url = "https://api.pokemontcg.io/v1/cards?name=" + pokemon
response = requests.get(url)

# Validating Response from API
if response:
	cards = response.json()["cards"]
	# Generating Random Card
	rand = random.randrange(0, len(cards), 1)
	image = cards[rand]["imageUrlHiRes"]
	# Displaying PokeCard generated.
	img_response = requests.get(image)
	with open("pokemon.png",'wb') as f:
		f.write(img_response.content) 
	os.system("shotwell pokemon.png")
	os.remove("pokemon.png")
else:
	print("Please Enter a valid Pokemon name")