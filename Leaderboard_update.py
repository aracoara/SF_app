from tennis_app.utils.utils import (process_results_data, picks_por_usuario, calcular_eliminados, picks_valid, 
                                    calcular_pontos_possiveis, calcular_pontos_ganhos, get_picks, get_user_data)
from tennis_app.models.models import Pontuacoes
from tennis_app import app, db
import pandas as pd
import numpy as np

# Crie uma instância do aplicativo Flask se ainda não tiver uma
app.app_context()

##########################################################################################
#########################ATUALIZAR OS RESULTADOS DA RODADA################################
##########################################################################################


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
# print("Classificados da QF:")
# print(classificados_QF)
classificados_SF = process_results_data(file_path_SF)
# print("Classificados da SF:")
# print(classificados_SF)
classificados_F = process_results_data(file_path_F)
# print("Classificados da F:")
# print(classificados_F)
Champion = process_results_data(file_path_Champion)
# print("Champion:")
# print(Champion)

# # # Atualizar os resultados conforme o torneio avança
atualizacoes = [
                ("R1", classificados_R1), 
                ("R2", classificados_R2), 
                # ("R3", classificados_R3), 
                # ("R4", classificados_R4), 
                # ("QF", classificados_QF), 
                # ("SF", classificados_SF), 
                # ("F", classificados_F),
                # ("Champion", Champion)
                ]
# print("Print das atualizações:")
# print(atualizacoes)

##########################################################################################

##########################################################################################
#########################PROCESSAR OS RESULTADOS DA RODADA################################
##########################################################################################

# Uso da função para processamento interno
picks_user = get_picks()
# print("Print dos Picks dos usuários:")
# print(picks_user)

# # DataFrame com os picks dos usuários
picks_user_df = picks_por_usuario(picks_user)
# print("Print do DF dos picks por usuário:")
# print(picks_user_df)
picks_user_df.to_csv('df_picks_user.csv', sep=';', encoding='utf-8', index=False)

# # Chamar a função com os palpites dos usuários e os dados dos classificados
df_eliminados = calcular_eliminados(picks_user_df, atualizacoes)
# print("Print dos jogadores eliminados:")
# print(df_eliminados)
df_eliminados.to_csv('df_eliminados.csv', sep=';', encoding='utf-8', index=False)

# # Chamada da função para determinar os picks válidos dos usuários
df_valid_picks = picks_valid(picks_user_df, df_eliminados, atualizacoes)
df_valid_picks.to_csv('df_picks_valid.csv', sep=';', encoding='utf-8', index=False)
# # Exibir o DataFrame dos palpites válidos
# print("DataFrame dos Palpites Válidos:")
# print(df_valid_picks)

# ##########################################################################################

# ##########################################################################################
# #########################CALCULAR OS PONTOS DA RODADA#####################################
# ##########################################################################################

# Definindo os pesos para cada rodada
pesos = {"QF": 1, "SF": 2, "F": 3, "Champion": 4}

# Obtendo dados dos usuários
user_data_df = get_user_data()

# Calculando os pontos possíveis por usuário
pontos_possiveis_df = calcular_pontos_possiveis(df_valid_picks, pesos)
# Realizando merge com dados dos usuários
pontos_possiveis_username_df = pd.merge(pontos_possiveis_df, user_data_df, left_on='User_ID', right_on='user_id', how='inner')
# Renomeando colunas
pontos_possiveis_username_df.rename(columns={'username': 'Participante', 'Pontos_Possiveis': 'Pontos Possíveis'}, inplace=True)
# Ordenando por "Pontos Possíveis" em ordem decrescente
pontos_possiveis_username_df.sort_values(by='Pontos Possíveis', ascending=False, inplace=True)
# Adicionando coluna de ranking baseada na ordem decrescente dos pontos possíveis
pontos_possiveis_username_df['Ranking PP'] = pontos_possiveis_username_df['Pontos Possíveis'].rank(ascending=False, method='min')
# Selecionando as colunas desejadas
pontos_possiveis_final_df = pontos_possiveis_username_df[['Ranking PP', 'Participante', 'Pontos Possíveis']].copy()
# Pega a última rodada
ultima_rodada = atualizacoes[-1][0]  # Obtém a última rodada, assumindo que 'atualizacoes' esteja ordenado
# Adiciona uma coluna 'Rodada' com a última rodada para todas as linhas
pontos_possiveis_final_df.loc[:, 'Rodada'] = ultima_rodada
# print("Ranking de Pontos Possíveis por Usuário:")
# print(pontos_possiveis_final_df)


# Calculando os pontos ganhos por usuário
df_pontos_ganhos = calcular_pontos_ganhos(df_valid_picks, atualizacoes, pesos)
# 1. Merge com user_data_df para adicionar os nomes dos usuários
df_pontos_ganhos_com_nomes = pd.merge(df_pontos_ganhos, user_data_df, left_on='User_ID', right_on='user_id', how='inner')
# Renomear colunas para manter consistência e facilitar a leitura
df_pontos_ganhos_com_nomes.rename(columns={'username': 'Participante', 'Pontos_Ganhos': 'Pontos Ganhos'}, inplace=True)
# 2. Adicionar a coluna "Rodada" com a última rodada
# ultima_rodada = atualizacoes[-1][0]
# df_pontos_ganhos_com_nomes['Rodada'] = ultima_rodada
# 3. Adicionar a coluna "Ranking PG"
df_pontos_ganhos_com_nomes['Ranking PG'] = df_pontos_ganhos_com_nomes['Pontos Ganhos'].rank(ascending=False, method='min')
# Ordenar o DataFrame por "Pontos Ganhos" em ordem decrescente
df_pontos_ganhos_com_nomes.sort_values(by='Pontos Ganhos', ascending=False, inplace=True)
# Resetar o índice para refletir a nova ordenação
df_pontos_ganhos_com_nomes.reset_index(drop=True, inplace=True)
# Selecionar e reordenar as colunas para o formato final desejado
df_pontos_ganhos_final = df_pontos_ganhos_com_nomes[['Ranking PG', 'Participante', 'Pontos Ganhos']].copy()
# print("Ranking de Pontos Ganhos por Usuário:")
# print(df_pontos_ganhos_final)

## DataFrame Final
# Exemplo de DataFrame vazio para simular df_pontos_ganhos_final vazio
# df_pontos_ganhos_final = pd.DataFrame()

if df_pontos_ganhos_final.empty:
    # Se df_pontos_ganhos_final for vazio, criar colunas 'Ranking PG' e 'Pontos Ganhos' com valores nulos
    pontos_possiveis_final_df['Ranking PG'] = np.nan
    pontos_possiveis_final_df['Pontos Ganhos'] = np.nan
    df_pontuacao_final = pontos_possiveis_final_df
else:
    # Se df_pontos_ganhos_final não estiver vazio, realizar o merge e preencher NaN para 'Pontos Ganhos' após o merge, se necessário
    df_pontuacao_final = pd.merge(pontos_possiveis_final_df, df_pontos_ganhos_final, on='Participante', how='left')
    df_pontuacao_final['Pontos Ganhos'] = df_pontuacao_final['Pontos Ganhos'].fillna(0)
    df_pontuacao_final['Ranking PG'] = df_pontuacao_final['Ranking PG'].fillna(np.nan)

# Ordenar o DataFrame final por 'Pontos Possíveis' em ordem decrescente
df_pontuacao_final.sort_values(by='Pontos Possíveis', ascending=False, inplace=True)    
# Resetar o índice do DataFrame final para refletir a nova ordenação
df_pontuacao_final.reset_index(drop=True, inplace=True)
# Agora, vamos adicionar os novos dados
df_pontuacao_final = df_pontuacao_final[['Ranking PP', 'Ranking PG', 'Participante', 'Pontos Possíveis', 'Pontos Ganhos', 'Rodada']]
df_pontuacao_final.to_csv('df_pontuacao_final.csv', sep=';', encoding='utf-8', index=False)
print("DataFrame Final Após Merge:")
print(df_pontuacao_final)
## Reordenando as colunas conforme solicitado

## Primeiro, vamos deletar os dados de pontuação existentes
# with app.app_context():
#     try:
#         # Isso irá deletar todos os registros da tabela Pontuacoes
#         db.session.query(Pontuacoes).delete()
#         db.session.commit()
#     except Exception as e:
#         print(f"Ocorreu um erro ao limpar os dados de pontuação: {e}")
#         db.session.rollback()

with app.app_context():
    for index, row in df_pontuacao_final.iterrows():
        pontuacao_db = Pontuacoes(
            ranking_pp=row['Ranking PP'],
            ranking_pg=row['Ranking PG'],
            username=row['Participante'],  # Usando 'Participante' para preencher o campo 'username'
            pontos_possiveis=row['Pontos Possíveis'],
            pontos_ganhos=row['Pontos Ganhos'],
            rodada=row['Rodada']
        )
        db.session.add(pontuacao_db)

    try:
        db.session.commit()
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar o banco de dados: {e}")
        db.session.rollback()


# ##########################################################################################