# routes.py

from flask import jsonify, render_template
from tennis_app import app, db
from tennis_app.models.models import Player


print("Definindo rotas...")

@app.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    return jsonify([player.to_dict() for player in players])

print("Rotas definidas com sucesso.")

@app.route('/')
def index():
    return render_template('index.html')