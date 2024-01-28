from tennis_app.models.models import RoundType
# import enum


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


# # Função auxiliar para mapear strings para enumerações
# def map_round_type(round_str):
#     if round_str == 'QF':
#         return RoundType.QF
#     elif round_str == 'SF':
#         return RoundType.SF
#     elif round_str == 'F':
#         return RoundType.F
#     else:
#         raise ValueError("Rodada não reconhecida")

# def create_games(data, round_str):
#     """
#     Cria jogos para uma rodada específica (QF, SF, F).
#     :param data: Dados dos jogos.
#     :param round_str: A rodada como string (QF, SF, F).
#     """
#     games = []
#     next_round_mapping = {
#         RoundType.QF: {RoundType.QF1: RoundType.SF, RoundType.QF2: RoundType.SF, RoundType.QF3: RoundType.SF, RoundType.QF4: RoundType.SF},
#         RoundType.SF: {RoundType.SF1: RoundType.F, RoundType.SF2: RoundType.F}
#     }


#     # Use a função auxiliar para mapear a string da rodada para a enumeração
#     round_enum = map_round_type(round_str)

#     round_keys = sorted(data[round_str].keys())

#     for i in range(0, len(round_keys), 2):
#         key1 = round_keys[i]
#         key2 = round_keys[i + 1]

#         player1_id = data[round_str][key1]
#         player2_id = data[round_str][key2]
#         winner_id = None

#         if round_enum != RoundType.F:
#             winner_id = data[next_round_mapping[round_str][key1]]

#         games.append({
#             "round": round_enum,
#             "player1_id": player1_id,
#             "player2_id": player2_id,
#             "winner_id": winner_id
#         })

#     return games



# def create_final_game_and_champion(data):
#     """
#     Função para criar o jogo final e identificar o campeão.
#     :param data: Dicionário com dados dos jogos.
#     :return: Jogo final com o campeão.
#     """
#     player1_key = 'F1'
#     player2_key = 'F2'
#     player1_id = data["final"][player1_key]
#     player2_id = data["final"][player2_key]
#     champion_id = data["campeao"]

#     final_game = {
#         "round": RoundType.F,
#         "player1_id": player1_id,
#         "player2_id": player2_id,
#         "winner_id": champion_id
#     }

#     return [final_game]

# Exemplo de uso
# data = {...}  # Dados do torneio
# qf_games = create_games(data, RoundType.QF)
# sf_games = create_games(data, RoundType.SF)
# final_game = create_final_game_and_champion(data)


