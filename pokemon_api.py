import requests
import re

def findPokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code == 404:
        return { "error": "Could not find a Pokémon with that name" }

    if response.status_code != 200:
        return { "error": response.text() }

    pokemon = response.json()

    return {
        "height": pokemon["height"],
        "sprite": pokemon["sprites"]["front_default"],
        "species": getPokemonSpecies(pokemon)
    }


def getPokemonSpecies(pokemon):
    url = pokemon["species"]["url"]
    species = requests.get(url).json()

    return {
        "generation": capitalize_generation(species["generation"]["name"].replace("-", " ")),
        "capture_rate": f'{round(species["capture_rate"] / 255 * 100, 2)}%',
        "names": {
            "english": getSpeciesName(species, "en"),
            "japanese": getSpeciesName(species, "ja-Hrkt")
        }
    }

def getSpeciesName(species, language):
    return next((name["name"] for name in species["names"] if name["language"]["name"] == language), None)

def capitalize_generation(s):
    def capitalize_roman(match):
        return match.group(0).upper()

    s = s.capitalize()
    s = re.sub(r'\b[ivxlcdm]+\b', capitalize_roman, s)

    return s

if __name__ == "__main__":
    print(findPokemon("ditto"))
