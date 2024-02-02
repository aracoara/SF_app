import pandas as pd

###################################################################### 
###########################Input######################################
######################################################################
picks_user = [
    {"player1_id": 1, "player2_id": 8, "winner_id": 1, "round": "QF"},
    {"player1_id": 2, "player2_id": 7, "winner_id": 2, "round": "QF"},
    {"player1_id": 3, "player2_id": 6, "winner_id": 3, "round": "QF"},
    {"player1_id": 4, "player2_id": 5, "winner_id": 4, "round": "QF"},
    {"player1_id": 1, "player2_id": 4, "winner_id": 8, "round": "SF"},
    {"player1_id": 2, "player2_id": 3, "winner_id": 3, "round": "SF"},
    {"player1_id": 1, "player2_id": 3, "winner_id": 3, "round": "F"},
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
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,          
    17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 
    33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 
    49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64  
])

classificados_R3 = set([
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,          
    17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32     
])

classificados_R4 = set([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16  ])
classificados_QF = set([ 1, 2, 3, 4, 5, 6, 7, 8])
classificados_SF = set([ 1, 2, 3, 4])
classificados_F = set([ 1, 2 ])
Champion = 1

###################################################################### 
###########################Processamento##############################
######################################################################

# Função para calcular jogadores eliminados
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

picks = {}

# Processando os palpites para adicionar as rodadas aos jogadores
for pick in picks_user:
    for player_key in ["player1_id", "player2_id"]:
        player = pick[player_key]
        pick_round = pick["round"]

        # Adicionando o jogador e a rodada ao dicionário picks
        if player not in picks:
            picks[player] = set()
        picks[player].add(pick_round)

# Identificando o campeão
campeao = next((pick["winner_id"] for pick in picks_user if pick["round"] == "F"), None)

# Adicionando o campeão ao dicionário picks (se aplicável)
if campeao:
    if campeao not in picks:
        picks[campeao] = set()
    picks[campeao].add("Champion")

# Convertendo o dicionário 'picks' para um DataFrame
df_picks = pd.DataFrame([(jogador, rodada) for jogador, rodadas in picks.items() for rodada in rodadas], columns=['Jogador', 'Rodada'])
# Mapeamento para a ordenação das rodadas
ordem_rodadas = {"QF": 1, "SF": 2, "F": 3, "Champion": 4}
# Aplicando a ordenação personalizada
df_picks['OrdemRodada'] = df_picks['Rodada'].map(ordem_rodadas)
df_picks.sort_values(by=['Jogador', 'OrdemRodada'], inplace=True)
# Removendo a coluna auxiliar 'OrdemRodada'
df_picks.drop('OrdemRodada', axis=1, inplace=True)
# Imprimindo o DataFrame para verificação
print("Print do DataFrame df_picks ordenado:")
print(df_picks)

# Inicializando dicionário de picks válidos
picks_valid = {}

# Processamento dos palpites para determinar picks_valid
for pick in picks_user:
    for player_key in ["player1_id", "player2_id"]:
        player = pick[player_key]
        pick_round = pick["round"]

        # Verificando se o jogador está classificado para a rodada do palpite
        if (pick_round == "QF" and player in classificados_QF) or \
           (pick_round == "SF" and player in classificados_SF) or \
           (pick_round == "F" and player in classificados_F):
            if player not in picks_valid:
                picks_valid[player] = set()
            picks_valid[player].add(pick_round)

# Verificando o pick de campeão nos palpites do usuário
campeao_user_pick = next((pick["winner_id"] for pick in picks_user if pick["round"] == "F"), None)

# Adicionando o campeão (se escolhido nos palpites do usuário)
if campeao_user_pick and campeao_user_pick == Champion:
    if Champion not in picks_valid:
        picks_valid[Champion] = set()
    picks_valid[Champion].add("Champion")

# Convertendo 'picks_valid' para DataFrame
df_picks_valid = pd.DataFrame([(jogador, rodada) for jogador, rodadas in picks_valid.items() for rodada in rodadas], columns=['Jogador', 'Rodada'])
df_picks_valid.sort_values(by=['Jogador', 'Rodada'], inplace=True)

# Convertendo 'picks_valid' para DataFrame
df_picks_valid = pd.DataFrame([(jogador, rodada) for jogador, rodadas in picks_valid.items() for rodada in rodadas], columns=['Jogador', 'Rodada'])
df_picks_valid['OrdemRodada'] = df_picks_valid['Rodada'].map(ordem_rodadas)
df_picks_valid.sort_values(by=['Jogador', 'OrdemRodada'], inplace=True)
# Removendo a coluna auxiliar 'OrdemRodada'
df_picks_valid.drop('OrdemRodada', axis=1, inplace=True)
print("Print dos picks válidos:")
print(df_picks_valid)

# Calculando a diferença para 'df_eliminated_before_pick'
df_eliminated_before_pick = pd.concat([df_picks, df_picks_valid]).drop_duplicates(keep=False)
df_eliminated_before_pick.sort_values(by='Jogador', inplace=True)
print("Print dos eliminados antes do pick:")
print(df_eliminated_before_pick)

###################################################################### 
###########################Calculo da Pontuação#######################
######################################################################

# Pesos de pontuação para cada rodada e campeão
pesos = {"QF": 1, "SF": 2, "F": 3, "Champion": 4}

# Calcular pontos ganhos total
pontos_ganhos_total = df_picks_valid['Rodada'].apply(lambda rodada: pesos[rodada]).sum()
print("Print dos pontos ganhos total:", pontos_ganhos_total)

# Calcular pontos perdidos total
pontos_perdidos_total = df_eliminated_before_pick['Rodada'].map(lambda rodada: pesos.get(rodada, 0)).sum()
pontos_possiveis_total = 26 - pontos_perdidos_total
print("Print dos pontos possíveis total:", pontos_possiveis_total)

# Cálculo de Jogadores Eliminados:
# O código começa definindo uma função 'calcular_eliminados' que calcula a diferença
# entre dois conjuntos de jogadores - os classificados em uma rodada anterior e os
# classificados em uma rodada atual. Isso é usado para determinar quais jogadores
# foram eliminados em cada transição de rodada.
# Se houver um campeão declarado, este é removido do conjunto de eliminados, pois
# ele é o vencedor final.
# A função é então utilizada para calcular os jogadores eliminados em cada etapa do
# torneio, desde as rodadas iniciais até a final.

# Processamento dos Palpites dos Usuários:
# O código processa uma lista de palpites (picks_user), onde cada palpite inclui
# informações sobre jogadores e a rodada para a qual o palpite foi feito.
# Para cada palpite, o código adiciona o jogador e a rodada correspondente a um
# dicionário (picks), onde cada chave é um jogador e cada valor é um conjunto de
# rodadas nas quais o jogador foi escolhido.

# Identificação do Campeão:
# O código identifica o campeão (o vencedor da rodada final) e adiciona uma marcação
# especial "Champion" ao dicionário picks para este jogador.

# Criação de DataFrame de Palpites:
# Os dados no dicionário picks são convertidos em um DataFrame (df_picks) para
# facilitar a análise e visualização. Este DataFrame é então ordenado primeiro por
# jogador e depois por rodada, com uma ordenação personalizada para as rodadas.

# Validação dos Palpites:
# Um novo dicionário (picks_valid) é criado para armazenar os palpites válidos.
# O código verifica cada palpite em relação aos conjuntos de jogadores classificados
# para cada rodada. Se um jogador foi escolhido para uma rodada para a qual ele está
# efetivamente classificado, o palpite é considerado válido e adicionado ao dicionário
# picks_valid.

# Verificação do Pick do Campeão:
# O código verifica se o campeão escolhido nos palpites dos usuários coincide com o
# campeão real. Se coincidir, a marcação "Champion" é adicionada a picks_valid para
# este jogador.

# Criação de DataFrame de Palpites Válidos:
# Semelhante ao df_picks, um DataFrame (df_picks_valid) é criado para os palpites
# válidos e ordenado de forma semelhante.

# Comparação dos Palpites e Identificação dos Eliminados Antes do Pick:
# Finalmente, o código compara os DataFrames de palpites e palpites válidos para
# identificar as escolhas onde os jogadores foram eliminados antes da rodada para a
# qual foram escolhidos. Isso é feito subtraindo os palpites válidos do conjunto total
# de palpites.



