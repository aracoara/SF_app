import pandas as pd

###################################################################### 
###########################Input######################################
######################################################################
picks_user = [
    {"user_id": 1, "player1_id": 1, "player2_id": 8, "winner_id": 1, "round": "QF"},
    {"user_id": 1, "player1_id": 2, "player2_id": 7, "winner_id": 2, "round": "QF"},
    {"user_id": 1, "player1_id": 3, "player2_id": 6, "winner_id": 3, "round": "QF"},
    {"user_id": 1, "player1_id": 4, "player2_id": 5, "winner_id": 4, "round": "QF"},
    {"user_id": 1, "player1_id": 1, "player2_id": 4, "winner_id": 1, "round": "SF"},
    {"user_id": 1, "player1_id": 2, "player2_id": 3, "winner_id": 2, "round": "SF"},
    {"user_id": 1, "player1_id": 1, "player2_id": 2, "winner_id": 1, "round": "F"},
    {"user_id": 2, "player1_id": 1, "player2_id": 8, "winner_id": 1, "round": "QF"},
    {"user_id": 2, "player1_id": 2, "player2_id": 7, "winner_id": 2, "round": "QF"},
    {"user_id": 2, "player1_id": 3, "player2_id": 6, "winner_id": 3, "round": "QF"},
    {"user_id": 2, "player1_id": 4, "player2_id": 5, "winner_id": 4, "round": "QF"},
    {"user_id": 2, "player1_id": 1, "player2_id": 4, "winner_id": 1, "round": "SF"},
    {"user_id": 2, "player1_id": 2, "player2_id": 3, "winner_id": 2, "round": "SF"},
    {"user_id": 2, "player1_id": 1, "player2_id": 2, "winner_id": 2, "round": "F"},	
]


classificados_R1 = set([
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,          
    17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 
    33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 
    49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
    65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96,
    97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112,
    113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128 
])

classificados_R2 = set([
    1, 65, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,          
    17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 
    33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 
    49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64  
])

classificados_R3 = set([
    1, 33, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,          
    17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32     
])

classificados_R4 = set([ 1, 17, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16  ])
classificados_QF = set([ 1, 9, 3, 4, 5, 6, 7, 8])
classificados_SF = set([ 1, 5, 3, 4])
classificados_F = set([ 1, 3 ])
Champion = 1

###################################################################### 
###########################Processamento##############################
######################################################################

#### Processamento para definir eliminados e mapeamento de rodadas ###
def calcular_eliminados(classificados_anterior, classificados_atual, champion=None):
    eliminados = classificados_anterior - classificados_atual
    if champion:
        eliminados -= set([champion])
    return eliminados

# Calculando conjuntos de jogadores eliminados
eliminados_R1 = calcular_eliminados(classificados_R1, classificados_R2)
eliminados_R2 = calcular_eliminados(classificados_R2, classificados_R3)
eliminados_R3 = calcular_eliminados(classificados_R3, classificados_R4)
eliminados_QF = calcular_eliminados(classificados_QF, classificados_SF)
eliminados_SF = calcular_eliminados(classificados_SF, classificados_F)
eliminados_F = calcular_eliminados(classificados_F, set(), Champion)
# print("Eliminados na F:", eliminados_F)

# Mapeamento das rodadas e seus respectivos conjuntos de eliminados
rodadas = {
    "R1": eliminados_R1, "R2": eliminados_R2, "R3": eliminados_R3,
    "QF": eliminados_QF, "SF": eliminados_SF, "F": eliminados_F
}
ordem_rodadas = ["R1", "R2", "R3", "QF", "SF", "F"]

######################################################################


####################### picks por usuario ############################
# Inicializar um dicionário vazio para armazenar os palpites de todos os usuários
picks_por_usuario = {}

# Supondo que picks_user seja uma lista de dicionários contendo os palpites dos usuários
for palpite in picks_user:
    user_id = palpite["user_id"]
    player1_id = palpite["player1_id"]
    player2_id = palpite["player2_id"]
    winner_id = palpite["winner_id"]
    pick_round = palpite["round"]

    # Inicializar o dicionário de palpites do usuário se ainda não existir
    if user_id not in picks_por_usuario:
        picks_por_usuario[user_id] = {"picks": [], "campeao": None}

    # Adicionar os palpites do jogador 1 e 2 à lista de palpites do usuário
    picks_por_usuario[user_id]["picks"].append((player1_id, pick_round))
    picks_por_usuario[user_id]["picks"].append((player2_id, pick_round))

    # Se a rodada for a final, determinar o campeão com base no winner_id
    if pick_round == "F":
        picks_por_usuario[user_id]["campeao"] = winner_id
        # Adicionar o campeão como um palpite válido
        picks_por_usuario[user_id]["picks"].append((winner_id, "Champion"))


# Convertendo o dicionário 'picks_por_usuario' para um DataFrame
# Incluindo 'user_id' junto com 'jogador' e 'rodada'
df_picks_por_usuario = pd.DataFrame([(user_id, jogador, rodada) 
                                     for user_id, dados_usuario in picks_por_usuario.items() 
                                     for jogador, rodada in dados_usuario["picks"]], 
                                    columns=['User_ID', 'Jogador', 'Rodada'])

# Mapeamento para a ordenação das rodadas
ordem_rodadas = {"QF": 1, "SF": 2, "F": 3, "Champion": 4}

# Aplicando a ordenação personalizada
df_picks_por_usuario['OrdemRodada'] = df_picks_por_usuario['Rodada'].map(ordem_rodadas)
df_picks_por_usuario.sort_values(by=['User_ID', 'Jogador', 'OrdemRodada'], inplace=True)

# Removendo a coluna auxiliar 'OrdemRodada'
df_picks_por_usuario.drop('OrdemRodada', axis=1, inplace=True)

# Imprimindo o DataFrame para verificação
print("Print do DataFrame df_picks_por_usuario ordenado:")
print(df_picks_por_usuario)
######################################################################

########################## picks validos por usuario #################

# Inicializando dicionário para armazenar os palpites válidos de cada usuário
# Ajustando a lógica para garantir que a marcação "Champion" seja correta

picks_valid = {}
for user_id, dados_usuario in picks_por_usuario.items():
    palpites_validos_usuario = []

    for jogador, rodada in dados_usuario["picks"]:
        # Verificar se o palpite é válido e se a marcação "Champion" é correta
        if (rodada == "QF" and jogador in classificados_QF) or \
           (rodada == "SF" and jogador in classificados_SF) or \
           (rodada == "F" and jogador in classificados_F) or \
           (rodada == "Champion" and jogador == Champion):
            palpites_validos_usuario.append((jogador, rodada))

    picks_valid[user_id] = palpites_validos_usuario

# Convertendo picks_valid para um DataFrame
df_picks_valid = pd.DataFrame([(user_id, jogador, rodada) 
                               for user_id, palpites in picks_valid.items() 
                               for jogador, rodada in palpites], 
                              columns=['User_ID', 'Jogador', 'Rodada'])

# Aplicando a ordenação personalizada
df_picks_valid['OrdemRodada'] = df_picks_valid['Rodada'].map(ordem_rodadas)
df_picks_valid.sort_values(by=['User_ID', 'Jogador', 'OrdemRodada'], inplace=True)

# Removendo a coluna auxiliar 'OrdemRodada'
df_picks_valid.drop('OrdemRodada', axis=1, inplace=True)

# Imprimindo DataFrame para verificação
print("Print do DataFrame df_picks_valid:")
print(df_picks_valid)

######################################################################

###################picks eliminados ##################################
df_picks_total = df_picks_por_usuario.copy()
df_picks_total['Tipo'] = 'Total'

df_picks_validos = df_picks_valid.copy()
df_picks_validos['Tipo'] = 'Valido'

# Combinando os dois DataFrames
df_combinado = pd.concat([df_picks_total, df_picks_validos])

# Identificando os palpites eliminados antes do pick
df_eliminated_before_pick = df_combinado.drop_duplicates(subset=['User_ID', 'Jogador', 'Rodada'], keep=False)

# Filtrando apenas os palpites que não são válidos
df_eliminated_before_pick = df_eliminated_before_pick[df_eliminated_before_pick['Tipo'] == 'Total']

# Removendo a coluna 'Tipo'
df_eliminated_before_pick.drop('Tipo', axis=1, inplace=True)

# Ordenando o DataFrame
df_eliminated_before_pick.sort_values(by=['User_ID', 'Jogador'], inplace=True)

# Imprimindo DataFrame para verificação
print("Print dos eliminados antes do pick:")
print(df_eliminated_before_pick)

######################################################################

###################################################################### 
###########################Calculo da Pontuação#######################
######################################################################

# Pesos de pontuação para cada rodada e campeão
pesos = {"QF": 1, "SF": 2, "F": 3, "Champion": 4}

# Total de pontos possíveis em todas as rodadas
# 8 jogos na QF, 4 na SF, 2 na F, e 1 campeão
total_pontos_possiveis = 8 * pesos["QF"] + 4 * pesos["SF"] + 2 * pesos["F"] + 1 * pesos["Champion"]

# Calcular pontos ganhos por usuário
pontos_ganhos_por_usuario = df_picks_valid.groupby('User_ID')['Rodada'].apply(lambda rodadas: sum(pesos[rodada] for rodada in rodadas))
print("Print dos pontos ganhos por usuário:")
print(pontos_ganhos_por_usuario)

# Calcular pontos perdidos por usuário
pontos_perdidos_por_usuario = df_eliminated_before_pick.groupby('User_ID')['Rodada'].apply(lambda rodadas: sum(pesos.get(rodada, 0) for rodada in rodadas))
print("Print dos pontos perdidos por usuário:")
print(pontos_perdidos_por_usuario)

# Calcular pontos possíveis por usuário
# Subtraindo pontos perdidos do total de pontos possíveis
pontos_possiveis_por_usuario = 26 - pontos_perdidos_por_usuario
print("Print dos pontos possíveis por usuário:")
print(pontos_possiveis_por_usuario)

###################################################################### 
###########################Pseudo-codigo##############################
######################################################################

# Inicializar um dicionário vazio para armazenar os palpites de todos os usuários
# picks_por_usuario = {}

# # Iterar sobre cada palpite em picks_user
# para cada palpite em picks_user:
#     # Extrair as informações relevantes do palpite
#     user_id = palpite["user_id"]
#     player1_id = palpite["player1_id"]
#     player2_id = palpite["player2_id"]
#     winner_id = palpite["winner_id"]
#     pick_round = palpite["round"]

#     # Inicializar o dicionário de palpites do usuário se ainda não existir
#     se user_id não estiver em picks_por_usuario:
#         picks_por_usuario[user_id] = { "picks": [], "campeao": None }

#     # Adicionar os palpites do jogador 1 e 2 à lista de palpites do usuário
#     picks_por_usuario[user_id]["picks"].adicionar((player1_id, pick_round))
#     picks_por_usuario[user_id]["picks"].adicionar((player2_id, pick_round))

#     # Se a rodada for a final, determinar o campeão com base no winner_id
#     se pick_round for "F":
#         picks_por_usuario[user_id]["campeao"] = winner_id

# # Processar cada conjunto de palpites para determinar os palpites válidos
# para cada user_id, dados_usuario em picks_por_usuario.items():
#     # Inicializar uma lista para armazenar os palpites válidos do usuário
#     palpites_validos = []

#     # Iterar sobre os palpites do usuário
#     para player_id, round em dados_usuario["picks"]:
#         # Verificar se o palpite é válido com base na classificação do jogador para aquela rodada
#         se (round for "QF" e player_id em classificados_QF) ou \
#            (round for "SF" e player_id em classificados_SF) ou \
#            (round for "F" e player_id em classificados_F) ou \
#            (round for "F" e player_id for o campeão):
#             # Adicionar palpite à lista de palpites válidos
#             palpites_validos.adicionar((player_id, round))

#     # Atualizar os dados do usuário com os palpites válidos
#     picks_por_usuario[user_id]["picks_validos"] = palpites_validos

# # O dicionário picks_por_usuario agora contém os palpites e os palpites válidos de cada usuário
