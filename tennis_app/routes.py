# routes.py

from flask import jsonify, render_template, request
from tennis_app import app, db
from tennis_app.models.models import Player, Game
# import logging
from .utils.utils import create_qf_games, create_sf_games, create_final_game_and_champion   


print("Definindo rotas...")

# Rota para obter todos os jogadores
@app.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    return jsonify([player.to_dict() for player in players])

@app.route('/submit_picks', methods=['POST'])
def submit_picks():
    data = request.get_json()
    # print("Dados recebidos:", data)

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    try:
        # Limpar todos os jogos existentes no banco de dados
        Game.query.delete()
        # Processamento dos dados para criar os jogos
        qf_games = create_qf_games(data)
        sf_games = create_sf_games(data)
        final_games = create_final_game_and_champion(data)

        all_games = qf_games + sf_games + final_games
        # print(all_games)

        # Adicionar os jogos ao banco de dados
        for game_data in all_games:
            game = Game(
                round=game_data['round'].value,  # Converter Enum para string
                player1_id=int(game_data['player1_id']),  # Garantir que são inteiros
                player2_id=int(game_data['player2_id']),
                winner_id=int(game_data['winner_id']) if game_data['winner_id'] is not None else None
            )
            db.session.add(game)
            print("Jogo a ser adicionado:", game)

        db.session.commit()
        print("Jogos salvos com sucesso.")
        return jsonify({'message': 'Picks submitted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        print("Erro ao salvar jogos:", e)
        return jsonify({'error': str(e)}), 500



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

