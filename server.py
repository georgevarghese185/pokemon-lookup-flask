from flask import Flask, render_template, jsonify, request
from pokemon_api import findPokemon

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon', methods=['GET'])
def get_pokemon():
    pokemon_name = request.args.get('name')

    if pokemon_name:
        pokemon_data = findPokemon(pokemon_name)

        return jsonify(pokemon_data)
    else:
        return jsonify({'error': 'Please provide a Pokémon name in the query parameter'}), 400

if __name__ == "__main__":
    app.run(debug=True)
