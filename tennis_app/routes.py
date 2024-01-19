# routes.py

from flask import jsonify, render_template
from tennis_app import app, db
from tennis_app.models.models import Player


print("Definindo rotas...")

# Rota para obter todos os jogadores
@app.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    return jsonify([player.to_dict() for player in players])

# Rota para obter jogadores por qf_number
@app.route('/players/qf/<int:qf_number>', methods=['GET'])
def get_players_by_qf(qf_number):
    # Filtrar jogadores com base no qf_number
    players = Player.query.filter_by(qf_number=qf_number).all()
    return jsonify([player.to_dict() for player in players])

print("Rotas definidas com sucesso.")

@app.route('/')
def index():
    return render_template('index.html')