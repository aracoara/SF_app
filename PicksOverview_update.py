from tennis_app import app, db
from tennis_app.models.models import User, Player
import pandas as pd
from tennis_app.utils.utils import process_results_data, map_ids_to_names, get_classified_players, process_results_data_position



##########################################################################################
#########################ATUALIZAR OS RESULTADOS DA RODADA################################
##########################################################################################

file_paths = {
    'QF': 'tennis_app/assets/QF-ao24_v2.csv',
    'SF': 'tennis_app/assets/SF-ao24_v2.csv',
    'F': 'tennis_app/assets/F-ao24_v2.csv',
    'Champion': 'tennis_app/assets/Champion-ao24_v2.csv'
}

# Processa os dados para cada fase
# Assegurando que process_results_data_position retorna DataFrames
df_classified_players_QF = process_results_data_position(file_paths['QF'])
df_classified_players_SF = process_results_data_position(file_paths['SF'])
df_classified_players_F = process_results_data_position(file_paths['F'])
df_classified_players_Champion = process_results_data_position(file_paths['Champion'])

# Concatenar os DataFrames
frames = [df_classified_players_QF, df_classified_players_SF, df_classified_players_F, df_classified_players_Champion]
df_concatenated = pd.concat(frames)
# print(df_concatenated)

with app.app_context():
    player_ids = df_concatenated['player_id'].dropna().unique().astype(int).tolist()
    player_names_dict = {}
        
    for player_id in player_ids:
        # Busca cada jogador individualmente
        player = db.session.query(Player).filter(Player.id == player_id).first()
        if player:
            player_names_dict[player_id] = player.name
    
    # Mapeia os player_id para nomes usando o dicionário criado
    df_concatenated['Jogadores'] = df_concatenated['player_id'].map(player_names_dict)

# Preparando o DataFrame para retorno JSON
df_classified_players = df_concatenated[['Position', 'Jogadores']].rename(columns={'Position': 'Posição'})
# print(df_classified_players)


# # Caminho relativo para o arquivo CSV com os resultados
# file_path_R1 = 'tennis_app/assets/R1-ao24.csv'
# file_path_R2 = 'tennis_app/assets/R2-ao24.csv'
# file_path_R3 = 'tennis_app/assets/R3-ao24.csv'
# file_path_R4 = 'tennis_app/assets/R4-ao24.csv'
# file_path_QF = 'tennis_app/assets/QF-ao24.csv'
# file_path_QF_v2 = 'tennis_app/assets/QF-ao24_v2.csv'
# file_path_SF = 'tennis_app/assets/SF-ao24.csv'
# file_path_F = 'tennis_app/assets/F-ao24.csv'
# file_path_Champion = 'tennis_app/assets/Champion-ao24.csv'

# # Processando os resultados e mapeando os IDs dos jogadores
# classificados_R1 = process_results_data(file_path_R1)
# # print("Classificados da R1:")
# # print(classificados_R1)
# classificados_R2 = process_results_data(file_path_R2)
# # print("Classificados da R2:")
# # print(classificados_R2)
# classificados_R3 = process_results_data(file_path_R3)
# # print("Classificados da R3:")
# # print(classificados_R3)
# classificados_R4 = process_results_data(file_path_R4)
# # print("Classificados da R4:")
# # print(classificados_R4)
# classificados_QF = process_results_data(file_path_QF)
# # print("Classificados da QF:")
# # print(classificados_QF)
# classificados_SF = process_results_data(file_path_SF)
# # print("Classificados da SF:")
# # print(classificados_SF)
# classificados_F = process_results_data(file_path_F)
# # print("Classificados da F:")
# # print(classificados_F)
# Champion = process_results_data(file_path_Champion)
# # print("Champion:")
# # print(Champion)

# def process_results_data_position(file_path):
#     # Lendo o arquivo CSV
#     df = pd.read_csv(file_path, encoding='ISO-8859-1', skiprows=1, names=['Position', 'Player'])

#     with app.app_context():
#         # Criar um dicionário para mapear nomes de jogadores para seus IDs
#         player_id_map = {player.name: player.id for player in Player.query.all()}

#         # Assegura que a coluna 'Player' é tratada como string
#         df['Player'] = df['Player'].astype(str)

#         # Extrair o nome do jogador da coluna 'Player' e mapear para player_id
#         # O uso de [0] após o .extract() seleciona a primeira coluna do resultado, que contém os nomes extraídos
#         df['player_id'] = df['Player'].str.extract(r'^(.*?)\s+\(')[0].map(player_id_map)

#         # Removendo linhas com valores NaN em 'player_id'
#         df.dropna(subset=['player_id'], inplace=True)

#         # Convertendo 'player_id' para int, tratando erros
#         df['player_id'] = pd.to_numeric(df['player_id'], downcast='integer', errors='coerce')

#     # Retorna o DataFrame ajustado
#     return df[['Position', 'player_id']]


# # Exemplo de uso:
# file_path_QF = 'tennis_app/assets/QF-ao24_v2.csv'
# df_classified_players_QF = process_results_data_position(file_path_QF)
# # print(df_classified_players_QF)
# file_path_SF = 'tennis_app/assets/SF-ao24_v2.csv'
# df_classified_players_SF = process_results_data_position(file_path_SF)
# # print(df_classified_players_SF)
# file_path_F = 'tennis_app/assets/F-ao24_v2.csv'
# df_classified_players_F = process_results_data_position(file_path_F)
# # print(df_classified_players_F)
# file_path_Champion = 'tennis_app/assets/Champion-ao24_v2.csv'
# df_classified_players_Champion = process_results_data_position(file_path_Champion)
# # print(df_classified_players_Champion)

# # Concatenar os DataFrames
# frames = [df_classified_players_QF, df_classified_players_SF, df_classified_players_F, df_classified_players_Champion]
# df_concatenated = pd.concat(frames)

# # Garantir que 'player_id' esteja no tipo correto
# df_concatenated['player_id'] = df_concatenated['player_id'].astype(int)

# with app.app_context():
#     # Buscar nomes dos jogadores baseando-se nos player_id
#     player_names = db.session.query(Player.id, Player.name).filter(Player.id.in_(df_concatenated['player_id'].tolist())).all()
#     player_names_dict = {id: name for id, name in player_names}

#     # Mapear player_id para nomes de jogadores
#     df_concatenated['Jogadores'] = df_concatenated['player_id'].map(player_names_dict)

# # Selecionar e renomear colunas para o DataFrame final
# df_classified_players = df_concatenated[['Position', 'Jogadores']].rename(columns={'Position': 'Posição'})

# # Exemplo de como o DataFrame final pode ser exibido
# print(df_classified_players)