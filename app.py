from flask import Flask, render_template, jsonify, request, Response
from pokemon_api import findPokemon
import os

template_dir = os.path.abspath('./docs')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon', methods=['GET'])
def get_pokemon():
    pokemon_name = request.args.get('name')

    if pokemon_name:
        pokemon_data = findPokemon(pokemon_name)
        resp = jsonify(pokemon_data)
        resp.headers["Access-Control-Allow-Origin"] = "https://georgevarghese185.github.io"
        return resp
    else:
        return jsonify({'error': 'Please provide a Pokémon name in the query parameter'}), 400
