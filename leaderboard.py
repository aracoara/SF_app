
# import sys
# sys.path.append("..")  # Adiciona o diretório pai ao sys.path
from tennis_app.models.models import Player, Game, Pick, User
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from tennis_app import app, db  # Substitua pelo nome da sua aplicação Flask
import pandas as pd

def process_results_data(file_path_r2):
    # Lendo e processando o arquivo CSV
    df = pd.read_csv(file_path_r2, encoding='ISO-8859-1', header=None, names=['qf_number','result'])
    # como pegar o campo abaixo e transformar em inteiro?
    df['qf_number'] = pd.to_numeric(df['qf_number'], errors='coerce')
    df['name'] = df['result'].str.extract(r'^(.*?)\s+\(')
    df['country'] = df['result'].str.extract(r'\((.*?)\)')
    df['ranking'] = df['result'].str.extract(r'\[(\d+)\]')

    with app.app_context():
        # Criar um dicionário para mapear nomes de jogadores para seus IDs
        player_id_map = {player.name: player.id for player in Player.query.all()}

        # Mapear os IDs dos jogadores no DataFrame
        df['player_id'] = df['name'].map(player_id_map)

    return df[['qf_number', 'name', 'country', 'ranking', 'player_id']]

# Caminho para o arquivo CSV com os resultados
file_path_r2 = 'D:/TENIS/SF_app/tennis_app/assets/r2-ao24.csv'

# Processando os resultados e mapeando os IDs dos jogadores
results_r2_df = process_results_data(file_path_r2)
# print(results_r2_df)


def get_all_picks():
    with app.app_context():
        picks = Pick.query.all()
        picks_df = pd.DataFrame([{
            "id": pick.id,
            "user_id": pick.user_id,
            "game_id": pick.game_id,
            # Inclua outros campos conforme necessário
        } for pick in picks])
        return picks_df
        
picks=get_all_picks()
# print(picks)

# Função para calcular a perda de pontos para todos os usuarios
def calculate_points_loss_for_all_users(r2_results_df):
    # Criar um dicionário para armazenar a perda de pontos de cada usuário
    users_points_loss = {}
    with app.app_context():
        # Obter todos os IDs de usuários únicos de picks
        user_ids = set([pick.user_id for pick in Pick.query.all()])

        for user_id in user_ids:
            lost_points = 0
            user_picks = Pick.query.filter_by(user_id=user_id).all()
            print(user_picks)

            for pick in user_picks:
                # Verifique se o jogador escolhido não está na lista de classificados da R2
                if pick.round == 'QF' and pick.player1_id not in r2_results_df['name'].values:
                    lost_points += 1  # Ajuste a lógica de pontuação conforme necessário
                # Adicione lógica similar para SF e F, se necessário

            # Armazenar a perda de pontos para o usuário atual
            users_points_loss[user_id] = lost_points

        return users_points_loss

# Exemplo de uso
# file_path = 'path_to_r2_results.csv'  # Substitua pelo caminho correto do arquivo
r2_results_df = process_results_data(file_path_r2)
points_loss_per_user = calculate_points_loss_for_all_users(r2_results_df)
print(points_loss_per_user)




# def get_all_users():
#     with app.app_context():
#         users=User.query.all()
#         users_df=pd.DataFrame([{
#             "id":user.id,
#             "username":user.username,
#             # "picks":user.picks,
#             # Inclua outros campos conforme necessário
#         } for user in users])  
#         return users_df
# users=get_all_users()
# print(users)



# # Funções de consulta simples
# def get_all_players_df():
#     with app.app_context():
#         players = Player.query.all()
#         # Convertendo a lista de objetos Player em um DataFrame
#         players_df = pd.DataFrame([player.to_dict() for player in players])
#         return players_df

# players=get_all_players_df()
# # print(players)