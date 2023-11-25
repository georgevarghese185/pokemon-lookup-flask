import requests

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
        "generation": species["generation"]["name"].replace("-", " ").title(),
        "capture_rate": f'{species["capture_rate"]}%',
        "names": {
            "english": getSpeciesName(species, "en"),
            "japanese": getSpeciesName(species, "ja-Hrkt")
        }
    }

def getSpeciesName(species, language):
    return next((name["name"] for name in species["names"] if name["language"]["name"] == language), None)

print(findPokemon("ditto"))
