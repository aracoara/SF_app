from tennis_app import app
from tennis_app.models.models import Pick, Player, RoundType
import pandas as pd
from sqlalchemy.orm import joinedload  # Para carregamento otimizado das relações


# Função para criar jogos de QF
def create_qf_games(data):
    qf_games = []
    # Mapeamento dos jogos de QF para SF
    next_round_mapping_QF_SF = {
        'QF1': 'SF1', 'QF2': 'SF1',
        'QF3': 'SF2', 'QF4': 'SF2',
        'QF5': 'SF3', 'QF6': 'SF3',
        'QF7': 'SF4', 'QF8': 'SF4'
    }

    # As chaves QF são sempre em pares, então iterar de dois em dois
    sorted_qf_keys = sorted(data["quartasFinal"].keys())
    for i in range(0, len(sorted_qf_keys), 2):
        qf_key1 = sorted_qf_keys[i]
        qf_key2 = sorted_qf_keys[i + 1]

        player1_id = data["quartasFinal"][qf_key1]
        player2_id = data["quartasFinal"][qf_key2]
        winner_id = data["semiFinal"][next_round_mapping_QF_SF[qf_key1]]

        # Aqui fazemos a conversão da string 'QF' para o enum RoundType.QF
        round_enum = RoundType.QF

        qf_games.append({
            "round": round_enum,
            "player1_id": player1_id,
            "player2_id": player2_id,
            "winner_id": winner_id
        })

    return qf_games

# Exemplo de uso
# qf_games = create_qf_games(data)
# print(qf_games)

# Função para criar jogos de SF
def create_sf_games(data):
    sf_games = []
    # Mapeamento dos jogos de SF para F
    next_round_mapping_SF_F = {
        'SF1': 'F1', 'SF2': 'F1',
        'SF3': 'F2', 'SF4': 'F2'
    }

    # As chaves SF também são sempre em pares, então iterar de dois em dois
    sorted_sf_keys = sorted(data["semiFinal"].keys())
    for i in range(0, len(sorted_sf_keys), 2):
        sf_key1 = sorted_sf_keys[i]
        sf_key2 = sorted_sf_keys[i + 1]

        player1_id = data["semiFinal"][sf_key1]
        player2_id = data["semiFinal"][sf_key2]
        winner_id = data["final"][next_round_mapping_SF_F[sf_key1]]

        # Aqui fazemos a conversão da string 'QF' para o enum RoundType.QF
        round_enum = RoundType.SF

        sf_games.append({
            "round": round_enum,
            "player1_id": player1_id,
            "player2_id": player2_id,
            "winner_id": winner_id
        })

    return sf_games

# Exemplo de uso
# sf_games = create_sf_games(data)
# print(sf_games)

# Função para criar o jogo final e identificar o campeão
def create_final_game_and_champion(data):
    final_games = []

    # Identificar os jogadores da final e o campeão
    player1_key = 'F1'
    player2_key = 'F2'
    player1_id = data["final"][player1_key]
    player2_id = data["final"][player2_key]
    champion_id = data["campeao"]

    round_enum = RoundType.F

    # Criar o jogo final
    final_game = {
        "round": round_enum,
        "player1_id": player1_id,
        "player2_id": player2_id,
        "winner_id": champion_id  # O campeão é o vencedor do jogo final
    }
    final_games.append(final_game)

    return final_games

# Função para processar o arquivo de resultados
def process_results_data(file_path):
    # Lendo e processando o arquivo CSV
    df = pd.read_csv(file_path, encoding='ISO-8859-1', header=None, names=['result'])
    # # como pegar o campo abaixo e transformar em inteiro?
    # # df['qf_number'] = pd.to_numeric(df['qf_number'], errors='coerce')
    # df['name'] = df['result'].str.extract(r'^(.*?)\s+\(')
    # df['country'] = df['result'].str.extract(r'\((.*?)\)')
    # df['ranking'] = df['result'].str.extract(r'\[(\d+)\]')

    with app.app_context():
        # Criar um dicionário para mapear nomes de jogadores para seus IDs
        player_id_map = {player.name: player.id for player in Player.query.all()}

        # Extrair o nome do jogador do campo 'result' e mapear para player_id
        df['name'] = df['result'].str.extract(r'^(.*?)\s+\(')
        df['player_id'] = df['name'].map(player_id_map)

        # Removendo linhas com valores NaN em 'player_id'
        df = df.dropna(subset=['player_id'])

        # Convertendo 'player_id' para int, tratando erros
        df['player_id'] = pd.to_numeric(df['player_id'], downcast='integer', errors='coerce').dropna()

    # Convertendo a coluna 'player_id' para um set e descartando NaN
    player_ids = set(df['player_id'].dropna())

    return player_ids

# Função para obter todos os picks
def get_all_picks():
    with app.app_context():
        picks = Pick.query.all()
        picks_df = pd.DataFrame([{
            "id": pick.id,
            "user_id": pick.user_id,
            "game_id": pick.game_id,
            "player1_id": pick.player1_id,
            "player2_id": pick.player2_id,
            "round": pick.round,
            "winner_id": pick.winner_id
            # Inclua outros campos conforme necessário
        } for pick in picks])
        return picks_df


# Método para atualizar os resultados do torneio
def atualizar_resultados_multiplos(atualizacoes):
    # Inicializando o dicionário de resultados do torneio dentro da função
    resultados_torneio = {
        "R1": set(), "R2": set(), "R3": set(), "R4": set(),
        "QF": set(), "SF": set(), "F": set(), "Champion": None
    }

    for rodada, classificados in atualizacoes:
        # Atualizar o dicionário com base nas atualizações fornecidas
        if rodada in resultados_torneio:
            if rodada == "Champion":
                # Tratar "Champion" como um caso especial, se necessário
                resultados_torneio[rodada] = classificados
            else:
                resultados_torneio[rodada] = set(classificados)
        else:
            print(f"Rodada {rodada} inválida. Verifique se a rodada está correta.")

    # Retornando o dicionário atualizado para uso ou inspeção fora da função
    return resultados_torneio


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
    # if 'Champion' in classificados_dict:
    #     champion = classificados_dict['Champion']
    #     # Garantir que champion esteja em um conjunto para unificação da lógica
    #     classificados_dict['Champion'] = {champion}
    
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

# Método para obter todos os picks
def get_picks():
    with app.app_context():
        # Buscando todos os picks e pré-carregando as relações necessárias para evitar N+1 queries
        picks = Pick.query.options(joinedload(Pick.game)).all()
        
        # Formatando os resultados em uma lista de dicionários
        picks_user = [
            {
                "user_id": pick.user_id,
                "player1_id": pick.player1_id,
                "player2_id": pick.player2_id,
                "winner_id": pick.winner_id,
                "round": str(pick.round)
            }
            for pick in picks
        ]
        
        return picks_user
    
# Método para obter todos os IDs dos jogadores
def get_player_ids():
    with app.app_context():
        # Dentro deste bloco, você está no contexto da aplicação
        # Agora você pode realizar consultas ao banco de dados
        player_ids = [player.id for player in Player.query.with_entities(Player.id).all()]

        return player_ids