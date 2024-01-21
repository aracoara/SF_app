

pick = {
    "quartasFinal": {"QF1": "1", "QF2": "17", "QF3": "32", "QF4": "48", "QF5": "62", "QF6": "76", "QF7": "90", "QF8": "104"},
    "semiFinal": {"SF1": "1", "SF2": "48", "SF3": "62", "SF4": "90"},
    "final": {"F1": "48", "F2": "90"},
    "campeao": "48"
}

next_round_mapping_QF_SF = {
    'QF1': 'SF1', 'QF2': 'SF1',
    'QF3': 'SF2', 'QF4': 'SF2',
    'QF5': 'SF3', 'QF6': 'SF3',
    'QF7': 'SF4', 'QF8': 'SF4'
}

# Mapeamento dos jogos de SF para F
next_round_mapping_SF_F = {
    'SF1': 'F1', 'SF2': 'F1',  # Vencedores de SF1 e SF2 vão para F1
    'SF3': 'F2', 'SF4': 'F2'  # Vencedores de SF3 e SF4 vão para F2
}


def create_qf_games( pick, next_round_mapping_QF_SF):
    # Criar dicionário para mapear ID do jogador para seus dados
    # players_dict = {player['id']: player for player in players}

    # Lista para armazenar os jogos das QFs
    qf_games = []

    # Processar cada jogo das QFs
    for game_key, player1_id in pick["quartasFinal"].items():
        # Identificar o player2_id (próximo jogador na sequência)
        game_number = int(game_key[2:])  # Extrai o número do jogo da QF (e.g., de "QF1" extrai 1)
        player2_key = f"QF{game_number + 1}" if game_number % 2 != 0 else f"QF{game_number - 1}"
        player2_id = pick["quartasFinal"][player2_key]

        # Determinar o winner_id usando o mapeamento para SF
        winner_key = next_round_mapping_QF_SF[game_key]
        winner_id = pick["semiFinal"][winner_key]

        # Criar o jogo
        game = {
            "round": "QF",
            "player1_id": player1_id,
            "player2_id": player2_id,
            "winner_id": winner_id
        }
        qf_games.append(game)

    return qf_games

qf_games = create_qf_games( pick, next_round_mapping_QF_SF)
print(qf_games)

def create_sf_games( pick, next_round_mapping_SF_F):
    # Lista para armazenar os jogos das SFs
    sf_games = []

    # Processar cada jogo das SFs
    for game_key, player1_id in pick["semiFinal"].items():
        # Identificar o player2_id (próximo jogador na sequência)
        game_number = int(game_key[2:])  # Extrai o número do jogo da SF (e.g., de "SF1" extrai 1)
        player2_key = f"SF{game_number + 1}" if game_number % 2 != 0 else f"SF{game_number - 1}"
        player2_id = pick["semiFinal"][player2_key]

        # Determinar o winner_id usando o mapeamento para F
        winner_key = next_round_mapping_SF_F[game_key]
        winner_id = pick["final"][winner_key]

        # Criar o jogo
        game = {
            "round": "SF",
            "player1_id": player1_id,
            "player2_id": player2_id,
            "winner_id": winner_id
        }
        sf_games.append(game)

    return sf_games

# Exemplo de uso
sf_games = create_sf_games( pick, next_round_mapping_SF_F)
print(sf_games)

def create_final_game( pick):
    # Lista para armazenar o jogo da Final
    final_game = []

    # Processar o jogo da Final
    for game_key, player1_id in pick["final"].items():
        # Identificar o player2_id (próximo jogador na sequência)
        game_number = int(game_key[1:])  # Extrai o número do jogo da Final (e.g., de "F1" extrai 1)
        player2_key = f"F{game_number + 1}" if game_number % 2 != 0 else f"F{game_number - 1}"
        player2_id = pick["final"][player2_key]

        # Determinar o winner_id que é o campeão
        winner_id = pick["campeao"]

        # Criar o jogo
        game = {
            "round": "F",
            "player1_id": player1_id,
            "player2_id": player2_id,
            "winner_id": winner_id
        }
        final_game.append(game)

    return final_game

final_game=create_final_game( pick)
print(final_game)


def define_champion(pick):
    # Retorna o ID do campeão
    return pick["campeao"]

champ=define_champion(pick)
print(champ)

