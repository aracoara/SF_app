
from tennis_app.models.models import Game
import enum

class RoundType(enum.Enum):
    QF = 'QF'
    SF = 'SF'
    F = 'F'


data = {
    "quartasFinal": {"QF1": "1", "QF2": "17", "QF3": "32", "QF4": "48", "QF5": "62", "QF6": "76", "QF7": "90", "QF8": "104"},
    "semiFinal": {"SF1": "1", "SF2": "48", "SF3": "62", "SF4": "90"},
    "final": {"F1": "48", "F2": "90"},
    "campeao": "48"
}

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
qf_games = create_qf_games(data)
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
sf_games = create_sf_games(data)
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

# Exemplo de uso
final_game = create_final_game_and_champion(data)
# print(final_game)

picks_games= qf_games + sf_games + final_game
# print(picks_games)

# Criação de instâncias da classe Game
game_objects = []
for game_data in picks_games:
    game = Game(
        round=game_data['round'],
        player1_id=game_data['player1_id'],
        player2_id=game_data['player2_id'],
        winner_id=game_data['winner_id']
    )
    game_objects.append(game)

print(game_objects) 



# def get_champion(data):
#     # Acessa diretamente a chave "campeao" no dicionário
#     champion_id = data.get("campeao", None)

#     # Retorna o ID do campeão
#     return champion_id

# # Exemplo de uso
# champion_id = get_champion(data)
# print(f"ID do Campeão: {champion_id}")


