import flask
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name) :
    url= f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    #print(response)
    
    if response.status_code == 200:
        print("Data Retrieved")
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Request Failed")
    
pokemon_name = "charizard"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info :
    print(f"{pokemon_info["name"]}")
    print(f"{pokemon_info["abilities"]}")
    print(f"{pokemon_info["types"]}")