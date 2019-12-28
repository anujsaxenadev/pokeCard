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
else:
	print("Please Enter a valid Pokemon name")