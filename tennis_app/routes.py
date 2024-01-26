# routes.py

from flask import jsonify, render_template, request
from tennis_app import app, db
from tennis_app.models.models import Player, Game, User , Pick
# import logging
from .utils.utils import create_qf_games, create_sf_games, create_final_game_and_champion   

print("Definindo rotas...")

# Rota para obter todos os jogadores
@app.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    # Retorna a lista de jogadores em formato JSON
    return jsonify([player.to_dict() for player in players])

# Rota para submeter palpites
@app.route('/submit_picks', methods=['POST'])
def submit_picks():
    data = request.get_json()
    # print("Dados recebidos:", data)  # Imprime os dados recebidos no terminal

    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    username = data['username']

    try:
        user = User.query.filter_by(username=username).first()
        print("Usuário encontrado:", user)

        if user is None:
            user = User(username=username)
            db.session.add(user)
            # Não faça commit aqui. Faremos isso mais tarde para garantir atomicidade.
            
        # Limpa todos os jogos existentes no banco de dados
        Game.query.delete()

        all_games_data = create_qf_games(data) + create_sf_games(data) + create_final_game_and_champion(data)
        # print(all_games)

        # Adiciona os jogos ao banco de dados
        for game_data in all_games_data:
            game = Game(
                round=game_data['round'].value,  # Converte Enum para string
                player1_id=int(game_data['player1_id']),  # Garante que são inteiros
                player2_id=int(game_data['player2_id']),
                winner_id=int(game_data['winner_id']) if game_data['winner_id'] is not None else None
            )
            db.session.add(game)
        # db.session.commit()  # Salva as mudanças no banco de dados
        # print("Jogos salvos com sucesso.")

        # Associa ou atualiza os palpites dos jogos ao usuário
        db.session.flush()  # Flush as sessões para obter os IDs dos jogos
        for game_data, game in zip(all_games_data, Game.query.all()):
            pick = Pick.query.filter_by(user_id=user.id, game_id=game.id).first()
            if pick is None:
                pick = Pick(
                    user_id=user.id, 
                    game_id=game.id, 
                    pick_result=game.winner_id,  # assumindo que esta é a previsão do usuário
                    player1_id=game.player1_id,  # assumindo que estas informações estão disponíveis no objeto game
                    player2_id=game.player2_id,
                    round=game.round  # Supondo que você quer armazenar a rodada aqui
                )
                db
                db.session.add(pick)
            else:
                pick.pick_result = game.winner_id
                pick.player1_id = game.player1_id
                pick.player2_id = game.player2_id        

        db.session.commit()  # Agora, fazemos commit de todas as mudanças de uma vez

        return jsonify({'message': 'Picks submitted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        print("Erro ao salvar jogos:", e)
        return jsonify({'error': str(e)}), 500

# Rota principal que renderiza a página inicial
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
