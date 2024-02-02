
from tennis_app.utils.utils import (process_results_data, get_all_picks, picks_por_usuario, calcular_eliminados, 
                                    picks_valid, calcular_pontos_possiveis, calcular_pontos_ganhos, get_picks)
from tennis_app.models.models import Player, Pick
from tennis_app import app
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.orm import joinedload  # Para carregamento otimizado das relações

# Crie uma instância do aplicativo Flask se ainda não tiver uma
app.app_context()

# Uso da função para processamento interno
picks_user = get_picks()
# print("Print dos jogadores:")
# print(picks_user)

# Caminho relativo para o arquivo CSV com os resultados
file_path_R1 = 'tennis_app/assets/R1-ao24.csv'
file_path_R2 = 'tennis_app/assets/R2-ao24.csv'
file_path_R3 = 'tennis_app/assets/R3-ao24.csv'
file_path_R4 = 'tennis_app/assets/R4-ao24.csv'
file_path_QF = 'tennis_app/assets/QF-ao24.csv'
file_path_SF = 'tennis_app/assets/SF-ao24.csv'
file_path_F = 'tennis_app/assets/F-ao24.csv'
file_path_Champion = 'tennis_app/assets/Champion-ao24.csv'

# Processando os resultados e mapeando os IDs dos jogadores
classificados_R1 = process_results_data(file_path_R1)
# print("Classificados da R1:")
# print(classificados_R1)
classificados_R2 = process_results_data(file_path_R2)
# print("Classificados da R2:")
# print(classificados_R2)
classificados_R3 = process_results_data(file_path_R3)
# print("Classificados da R3:")
# print(classificados_R3)
classificados_R4 = process_results_data(file_path_R4)
# print("Classificados da R4:")
# print(classificados_R4)
classificados_QF = process_results_data(file_path_QF)
print("Classificados da QF:")
print(classificados_QF)
classificados_SF = process_results_data(file_path_SF)
print("Classificados da SF:")
print(classificados_SF)
classificados_F = process_results_data(file_path_F)
print("Classificados da F:")
print(classificados_F)
Champion = process_results_data(file_path_Champion)
print("Champion:")
print(Champion)

# # # Atualizar os resultados conforme o torneio avança
atualizacoes = [
                ("R1", classificados_R1), 
                ("R2", classificados_R2), 
                ("R3", classificados_R3), 
                ("R4", classificados_R4), 
                ("QF", classificados_QF), 
                ("SF", classificados_SF), 
                ("F", classificados_F),
                ("Champion", Champion)
                ]
# print("Print das atualizações:")
# print(atualizacoes)

# # DataFrame com os picks dos usuários
picks_user_df = picks_por_usuario(picks_user)
print("Print dos picks por usuário:")
print(picks_user_df)

# # Chamar a função com os palpites dos usuários e os dados dos classificados
df_eliminados = calcular_eliminados(picks_user_df, atualizacoes)
print("Print dos jogadores eliminados:")
print(df_eliminados)

# # Chamada da função para determinar os picks válidos dos usuários
# # Chamada da função para determinar os picks válidos dos usuários
df_valid_picks = picks_valid(picks_user_df, df_eliminados)
# # Exibir o DataFrame dos palpites válidos
print("DataFrame dos Palpites Válidos:")
print(df_valid_picks)


# Definindo os pesos para cada rodada
pesos = {"QF": 1, "SF": 2, "F": 3, "Champion": 4}

# Calculando os pontos possíveis por usuário
pontos_possiveis_por_usuario = calcular_pontos_possiveis(df_valid_picks, pesos)
pontos_possiveis_por_usuario = pontos_possiveis_por_usuario.sort_values(ascending=False)
print("Pontos possíveis por usuário:")
print(pontos_possiveis_por_usuario)

# Calculando os pontos ganhos por usuário
df_pontos_ganhos = calcular_pontos_ganhos(df_valid_picks, atualizacoes, pesos)
df_pontos_ganhos = df_pontos_ganhos.sort_values(by='Pontos_Ganhos', ascending=False)
print("Pontos ganhos por usuário:")
print(df_pontos_ganhos)
