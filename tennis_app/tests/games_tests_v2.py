
pick = {
    "quartasFinal": {"QF1": "1", "QF2": "17", "QF3": "32", "QF4": "48", "QF5": "62", "QF6": "76", "QF7": "90", "QF8": "104"},
    "semiFinal": {"SF1": "1", "SF2": "48", "SF3": "62", "SF4": "90"},
    "final": {"F1": "48", "F2": "90"},
    "campeao": "48"
}

def create_games(pick, next_round_mapping, round_type):
    games = []

    for game_key, player1_id in pick[round_type].items():
        game_number = int(game_key[2:]) if round_type != "final" else int(game_key[1:])
        player2_key = f"{game_key[:2]}{game_number + 1}" if game_number % 2 == 0 else f"{game_key[:2]}{game_number - 1}"
        player2_id = pick[round_type].get(player2_key, None)

        next_round_key = next_round_mapping.get(game_key)
        if next_round_key:
            next_round_type = "final" if next_round_key.startswith("F") else "semiFinal"
            winner_id = pick[next_round_type].get(next_round_key, None)
        else:
            winner_id = None

        game = {
            "round": round_type.upper(),
            "player1_id": player1_id,
            "player2_id": player2_id,
            "winner_id": winner_id
        }
        games.append(game)

    return games

# Mapeamentos
next_round_mapping_QF_SF = {'QF1': 'SF1', 'QF2': 'SF1', 'QF3': 'SF2', 'QF4': 'SF2', 'QF5': 'SF3', 'QF6': 'SF3', 'QF7': 'SF4', 'QF8': 'SF4'}
next_round_mapping_SF_F = {'SF1': 'F1', 'SF2': 'F1', 'SF3': 'F2', 'SF4': 'F2'}

# Função para criar todos os jogos com base nos dados da pick
def create_all_games(pick, next_round_mapping_QF_SF, next_round_mapping_SF_F):
    qf_games = create_games(pick, next_round_mapping_QF_SF, "quartasFinal")
    sf_games = create_games(pick, next_round_mapping_SF_F, "semiFinal")
    final_game = create_games(pick, {}, "final")  # Não há mapeamento adicional para a final

    # Combina todas as listas de jogos
    all_games = qf_games + sf_games + final_game
    return all_games

# Exemplo de uso
all_games = create_all_games(pick, next_round_mapping_QF_SF, next_round_mapping_SF_F)
print(all_games)

# Campeão
champion = pick["campeao"]


