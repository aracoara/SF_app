import pandas as pd
# from tennis_app.utils.utils import  picks_por_usuario, calcular_eliminados, picks_valid, calcular_pontos_possiveis, calcular_pontos_ganhos

# Método para atualizar os resultados do torneio
# def atualizar_resultados_multiplos(atualizacoes):
#     # Inicializando o dicionário de resultados do torneio dentro da função
#     resultados_torneio = {
#         "R1": set(), "R2": set(), "R3": set(), "R4": set(),
#         "QF": set(), "SF": set(), "F": set(), "Champion": None
#     }

#     for rodada, classificados in atualizacoes:
#         # Atualizar o dicionário com base nas atualizações fornecidas
#         if rodada in resultados_torneio:
#             if rodada == "Champion":
#                 # Tratar "Champion" como um caso especial, se necessário
#                 resultados_torneio[rodada] = classificados
#             else:
#                 resultados_torneio[rodada] = set(classificados)
#         else:
#             print(f"Rodada {rodada} inválida. Verifique se a rodada está correta.")

#     # Retornando o dicionário atualizado para uso ou inspeção fora da função
#     return resultados_torneio


# Método para determinar os picks dos usuários
def picks_por_usuario(picks_user):
    picks_data = []
    for palpite in picks_user:
        user_id = palpite["user_id"]
        player1_id = palpite["player1_id"]
        player2_id = palpite["player2_id"]
        winner_id = palpite["winner_id"]
        pick_round = palpite["round"]

        picks_data.append((user_id, player1_id, pick_round))
        picks_data.append((user_id, player2_id, pick_round))

        if pick_round == "F":
            picks_data.append((user_id, winner_id, "Champion"))

    df_picks_por_usuario = pd.DataFrame(picks_data, columns=['User_ID', 'Jogador', 'Rodada'])
    # Mapeamento para a ordenação das rodadas
    ordem_rodadas = {"QF": 1, "SF": 2, "F": 3, "Champion": 4}
    # Aplicando a ordenação personalizada
    df_picks_por_usuario['OrdemRodada'] = df_picks_por_usuario['Rodada'].map(ordem_rodadas)
    df_picks_por_usuario.sort_values(by=['User_ID', 'Jogador', 'OrdemRodada'], inplace=True)

    # Removendo a coluna auxiliar 'OrdemRodada'
    df_picks_por_usuario.drop('OrdemRodada', axis=1, inplace=True)

    return df_picks_por_usuario


# Método para determinar os players eliminados dos picks dos usuários
def calcular_eliminados(df_picks_por_usuario, atualizacoes):
    # Criar um dicionário para os classificados de cada rodada
    classificados_dict = dict(atualizacoes)

    # Tratando 'Champion' como um caso especial
    if 'Champion' in classificados_dict:
        champion = classificados_dict['Champion']
        # Garantir que champion esteja em um conjunto para unificação da lógica
        classificados_dict['Champion'] = {champion}
    
    # Obter uma lista única de (user_id, player_id) a partir de df_picks_por_usuario
    users_picks_players = df_picks_por_usuario[['User_ID', 'Jogador']].drop_duplicates()

    # Preparar uma lista para armazenar os dados dos jogadores eliminados
    players_eliminated_data = []

    # Iterar pela lista de palpites dos usuários
    for _, row in users_picks_players.iterrows():
        user_id = row['User_ID']
        player_id = row['Jogador']

        # Verificar se o jogador foi eliminado em alguma rodada
        for i in range(len(atualizacoes) - 1):
            rodada_atual = atualizacoes[i][0]
            rodada_seguinte = atualizacoes[i + 1][0]

            classificados_atual = classificados_dict[rodada_atual]
            classificados_seguinte = classificados_dict.get(rodada_seguinte, set())

            if player_id in classificados_atual and player_id not in classificados_seguinte:
                # Para a rodada 'Champion', a eliminação é marcada na rodada anterior
                rodada_eliminacao = 'Champion' if rodada_seguinte == 'Champion' else rodada_atual
                players_eliminated_data.append((user_id, rodada_eliminacao, player_id))

    # Converter a lista para um DataFrame
    df_players_eliminated = pd.DataFrame(players_eliminated_data, columns=['User_ID', 'Rodada_Eliminacao', 'Jogador'])

    # Ordenar o DataFrame
    ordem_rodadas = {"R1": 1, "R2": 2, "R3": 3, "QF": 4, "SF": 5, "F": 6, "Champion": 7}
    df_players_eliminated['OrdemRodada'] = df_players_eliminated['Rodada_Eliminacao'].map(ordem_rodadas)
    df_players_eliminated.sort_values(by=['User_ID', 'OrdemRodada', 'Jogador'], inplace=True)

    # Remover a coluna auxiliar 'OrdemRodada'
    df_players_eliminated.drop('OrdemRodada', axis=1, inplace=True)

    return df_players_eliminated


# Método para determinar os picks válidos dos usuários
def picks_valid(picks_user_df, df_eliminados):
    # Obter os IDs dos jogadores eliminados
    jogadores_eliminados = set(df_eliminados['Jogador'])

    # Filtrar os palpites válidos
    df_picks_valid = picks_user_df[~picks_user_df['Jogador'].isin(jogadores_eliminados)]

    return df_picks_valid

def calcular_pontos_possiveis(df_picks_valid, pesos):
    """
    Calcula os pontos possíveis para cada usuário com base nos palpites válidos.

    Parâmetros:
    - df_valid_picks (DataFrame): DataFrame contendo os palpites válidos.
    - pesos (dict): Dicionário com os pesos atribuídos para cada rodada.

    Retorna:
    - pontos_possiveis_por_usuario (Series): Pontos possíveis para cada usuário.
    """
    pontos_possiveis_por_usuario = df_picks_valid.groupby('User_ID')['Rodada'].apply(
        lambda rodadas: sum(pesos[rodada] for rodada in rodadas)
    )
    
    return pontos_possiveis_por_usuario

def calcular_pontos_ganhos(df_picks_valid, atualizacoes, pesos):
    """
    Calcula os pontos ganhos para cada usuário com base nos palpites válidos e nas atualizações fornecidas.

    Parâmetros:
    - df_picks_valid (DataFrame): DataFrame contendo os palpites válidos.
    - atualizacoes (list): Lista de tuplas com a rodada e os classificados/set do campeão.
    - pesos (dict): Dicionário com os pesos atribuídos para cada rodada.

    Retorna:
    - df_pontos_ganhos (DataFrame): DataFrame contendo os pontos ganhos por cada usuário.
    """
    # Convertendo o dicionário de atualizações para facilitar a verificação de classificados
    classificados_por_rodada = {rodada: (classificados if isinstance(classificados, set) else {classificados})
                                for rodada, classificados in atualizacoes}

    # Inicializando um dicionário para armazenar os pontos ganhos por usuário
    pontos_ganhos_por_usuario = {}

    # Iterando sobre cada palpite válido
    for _, row in df_picks_valid.iterrows():
        user_id = row['User_ID']
        jogador = row['Jogador']
        rodada = row['Rodada']

        # Verificar se a rodada é uma das que contam pontos e se o jogador estava entre os classificados
        if rodada in pesos and jogador in classificados_por_rodada.get(rodada, set()):
            # Adicionando os pontos ao usuário
            pontos_ganhos_por_usuario[user_id] = pontos_ganhos_por_usuario.get(user_id, 0) + pesos[rodada]

    # Convertendo os pontos ganhos para um DataFrame para facilitar a visualização
    df_pontos_ganhos = pd.DataFrame([(user_id, pontos) for user_id, pontos in pontos_ganhos_por_usuario.items()], 
                                    columns=['User_ID', 'Pontos_Ganhos'])

    return df_pontos_ganhos


###########################################################################################

# Exemplo de uso
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
    1, 65, 3, 66, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,          
    17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 
    33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 
    49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64  
])

classificados_R3 = set([
    1, 33, 3, 34, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,          
    17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32     
])

classificados_R4 = set([ 1, 18, 3, 19, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16  ])
classificados_QF = set([ 1, 10, 3, 11, 5, 6, 7, 8])
classificados_SF = set([ 1, 5, 3, 6])
classificados_F = set([ 1, 3 ])
Champion = 1

# # Atualizar os resultados conforme o torneio avança
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
print("Print das atualizações:")
print(atualizacoes)

# DataFrame com os picks dos usuários
picks_user_df = picks_por_usuario(picks_user)
print("Print dos picks por usuário:")
print(picks_user_df)

# Chamar a função com os palpites dos usuários e os dados dos classificados
df_eliminados = calcular_eliminados(picks_user_df, atualizacoes)
print("Print dos jogadores eliminados:")
print(df_eliminados)

# Chamada da função para determinar os picks válidos dos usuários
# Chamada da função para determinar os picks válidos dos usuários
df_valid_picks = picks_valid(picks_user_df, df_eliminados)

# Exibir o DataFrame dos palpites válidos
print("DataFrame dos Palpites Válidos:")
print(df_valid_picks)


# Definindo os pesos para cada rodada
pesos = {"QF": 1, "SF": 2, "F": 3, "Champion": 4}

# Calculando os pontos possíveis por usuário
pontos_possiveis_por_usuario = calcular_pontos_possiveis(df_valid_picks, pesos)
print("Pontos possíveis por usuário:")
print(pontos_possiveis_por_usuario)

# Calculando os pontos ganhos por usuário
df_pontos_ganhos = calcular_pontos_ganhos(df_valid_picks, atualizacoes, pesos)
print(df_pontos_ganhos)