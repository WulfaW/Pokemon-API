# Pokemon API
import requests
import webbrowser

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data

    else:
        print(f"Failed to retrieve data {response.status_code}")
        return None

pokemon_name = input("Enter the name of a Pokémon: ")
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")
    print(f"Base experience: {pokemon_info['base_experience']}")
    print(f"Abilities: {', '.join([ability['ability']['name'] for ability in pokemon_info['abilities']])}")
    print(f"Types: {', '.join([type['type']['name'] for type in pokemon_info['types']])}")
    print("Stats:")
    for stat in pokemon_info['stats']:
        print(f"  {stat['stat']['name']}: {stat['base_stat']}")
    sprite_url = pokemon_info['sprites']['front_default']
    print(f"Sprite URL: {sprite_url}")
    open_image = input("Open sprite image in browser? (y/n): ")
    if open_image.lower() == "y" and sprite_url:
        webbrowser.open(sprite_url)