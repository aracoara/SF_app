# routes.py

from flask import jsonify, render_template, request, abort
from tennis_app import app, db
from tennis_app.models.models import Player, Game, RoundType
import logging

print("Definindo rotas...")

# Rota para obter todos os jogadores
@app.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    return jsonify([player.to_dict() for player in players])




@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# Mapeamento dos jogos de QF para SF
# next_round_mapping_QF_SF = {
#     'QF1': 'SF1', 'QF2': 'SF1',  # Vencedores de QF1 e QF2 vão para SF1
#     'QF3': 'SF2', 'QF4': 'SF2',  # Vencedores de QF3 e QF4 vão para SF2
#     'QF5': 'SF3', 'QF6': 'SF3',  # Vencedores de QF5 e QF6 vão para SF3
#     'QF7': 'SF4', 'QF8': 'SF4'   # Vencedores de QF7 e QF8 vão para SF4
# }

# # Mapeamento dos jogos de SF para F
# next_round_mapping_SF_F = {
#     'SF1': 'F1', 'SF2': 'F1',  # Vencedores de SF1 e SF2 vão para F1
#     'SF3': 'F2', 'SF4': 'SF2'  # Vencedores de SF3 e SF4 vão para F2

# }

# def process_round(round_data, next_round_mapping, round_type):
#     processed_games = []

#     # Processa os jogos de cada rodada
#     for game_key, player1_id in round_data.items():
#         # Determina o jogo correspondente na próxima rodada para encontrar o vencedor
#         next_round_game_key = next_round_mapping.get(game_key)
#         winner_id = None
#         if next_round_game_key:
#             winner_id = round_data.get(next_round_game_key)

#         # Identifica o player2_id com base no mapeamento (ex: QF1 e QF2 são ambos mapeados para SF1)
#         player2_key = [key for key, value in next_round_mapping.items() if value == next_round_game_key and key != game_key]
#         player2_id = round_data.get(player2_key[0]) if player2_key else None

#         # Cria o jogo
#         game = Game(
#             round=round_type,
#             player1_id=player1_id,
#             player2_id=player2_id,
#             winner_id=winner_id
#         )
#         processed_games.append(game)

#     return processed_games


# @app.route('/submit_picks', methods=['POST'])
# def submit_picks():
#     # Recebe os dados do JSON enviado pelo cliente
#     data = request.get_json()

#     # Verifica se os dados estão presentes
#     if not data:
#         return jsonify({'error': 'No data provided'}), 400

#     try:
#         # Processa as Quartas de Final
#         qf_games = process_round(data.get('quartasFinal', {}), RoundType.QF, next_round_mapping_QF_SF)
#         # Adiciona os jogos das Quartas de Final ao banco de dados
#         for game in qf_games:
#             db.session.add(game)

#         # Processa as Semifinais
#         sf_games = process_round(data.get('semiFinal', {}), RoundType.SF, next_round_mapping_SF_F)
#         # Adiciona os jogos das Semifinais ao banco de dados
#         for game in sf_games:
#             db.session.add(game)

#         # Processa a Final
#         f_games = process_round(data.get('final', {}), RoundType.F, {'F1': data.get('campeao'), 'F2': data.get('campeao')})
#         # Adiciona os jogos da Final ao banco de dados
#         for game in f_games:
#             db.session.add(game)

#         # Confirma as mudanças no banco de dados
#         db.session.commit()

#         return jsonify({'message': 'Picks submitted successfully'}), 200

#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 500



# def set_champion(champion_id):
#     if champion_id:
#         champion = Player.query.get(int(champion_id))
#         if champion:
#             # Faça algo com o campeão (por exemplo, atualizar um registro ou enviar notificação)
#             print(f'O campeão é: {champion.name}')