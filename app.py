import requests
from flask import Flask, render_template

app = Flask(__name__)

# Get Rick and Morty Characters
data = requests.get('https://rickandmortyapi.com/api/character')
data = data.json()['results']

# Show Rick and Morty Characters in homepage
@app.route('/')
def index():
    return render_template('index.html', data=data)

# Show characters by ID
@app.route('/character/<int:id>')
def character(id=None):
    return render_template('character.html', character=data[id-1])

if __name__ == "__main__":
    app.run( debug=True)