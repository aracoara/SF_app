import sys
import os
sys.path.insert(0, os.path.abspath('D:\\TENIS\\SF_app'))

import unittest
# from flask_sqlalchemy import SQLAlchemy
from tennis_app import app, db
from tennis_app.models.models import Player, Game, RoundType
import logging
# from tennis_app.routes import process_round  # Importe a função process_round

class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()  # Use a instância existente do SQLAlchemy
        self.add_test_players()

    def tearDown(self):
        db.session.remove()  # Use a instância existente do SQLAlchemy
        db.drop_all()  # Use a instância existente do SQLAlchemy
        self.app_context.pop()

    def add_test_players(self):
        players = [
            Player(id=1, name="Player 1", country="Country A", ranking=1),
            Player(id=2, name="Player 2", country="Country B", ranking=2),
            Player(id=3, name="Player 3", country="Country C", ranking=3),
            Player(id=4, name="Player 4", country="Country D", ranking=4),
            Player(id=5, name="Player 5", country="Country E", ranking=5),
            Player(id=6, name="Player 6", country="Country F", ranking=6),
            Player(id=7, name="Player 7", country="Country G", ranking=7),
            Player(id=8, name="Player 8", country="Country H", ranking=8)
        ]
        for player in players:
            existing_player = Player.query.filter_by(id=player.id).first()
            if not existing_player:
                db.session.add(player)
                logging.info(f'Player {player.id} created successfully')
            else:
                logging.info(f'Player {player.id} already exists')
        db.session.commit()


    def test_game_creation(self):
        # Dados fictícios de entrada
        input_data = {
            "quartasFinal": {"QF1": "1", "QF2": "2", "QF3": "3", "QF4": "4", "QF5": "5", "QF6": "6", "QF7": "7", "QF8": "8"},
            "semiFinal": {"SF1": "1", "SF2": "3", "SF3": "5", "SF4": "6"},
            "final": {"F1": "1", "F2": "5"},
            "campeao": "1"
        }

        next_round_mapping_QF_SF = {
            'QF1': 'SF1', 'QF2': 'SF1',  # Vencedores de QF1 e QF2 vão para SF1
            'QF3': 'SF2', 'QF4': 'SF2',  # Vencedores de QF3 e QF4 vão para SF2
            'QF5': 'SF3', 'QF6': 'SF3',  # Vencedores de QF5 e QF6 vão para SF3
            'QF7': 'SF4', 'QF8': 'SF4'   # Vencedores de QF7 e QF8 vão para SF4
        }

        # Mapeamento dos jogos de SF para F
        next_round_mapping_SF_F = {
            'SF1': 'F1', 'SF2': 'F1',  # Vencedores de SF1 e SF2 vão para F1
            'SF3': 'F2', 'SF4': 'SF2'  # Vencedores de SF3 e SF4 vão para F2

        }

        next_round_mapping_F = {
            'F1': 'Final', 'F2': 'Final'  # Vencedores de F1 e F2 vão para a Final
        }

        def process_round(round_data, next_round_mapping, round_type):
            processed_games = []

            # Processa os jogos de cada rodada
            for game_key, player1_id in round_data.items():
                # Determina o jogo correspondente na próxima rodada para encontrar o vencedor
                next_round_game_key = next_round_mapping.get(game_key)
                winner_id = None
                if next_round_game_key:
                    winner_id = round_data.get(next_round_game_key)

                # Identifica o player2_id com base no mapeamento (ex: QF1 e QF2 são ambos mapeados para SF1)
                player2_key = [key for key, value in next_round_mapping.items() if value == next_round_game_key and key != game_key]
                player2_id = round_data.get(player2_key[0]) if player2_key else None

                # Cria o jogo
                game = Game(
                    round=round_type,
                    player1_id=player1_id,
                    player2_id=player2_id,
                    winner_id=winner_id
                )
                processed_games.append(game)

            return processed_games
        
        # Processamento dos jogos
        qf_games = process_round(input_data["quartasFinal"], next_round_mapping_QF_SF, RoundType.QF)

        sf_games = process_round(input_data["semiFinal"], next_round_mapping_SF_F, RoundType.SF)

        f_games = process_round(input_data["final"], next_round_mapping_F, RoundType.F)

        # Adicione os jogos processados ao banco de dados para teste
        for game in qf_games + sf_games + f_games:
            db.session.add(game)
        db.session.commit()

        # Verificações
        self.assertEqual(Game.query.filter_by(round=RoundType.QF).count(), 4)
        self.assertEqual(Game.query.filter_by(round=RoundType.SF).count(), 2)
        self.assertEqual(Game.query.filter_by(round=RoundType.F).count(), 1)
        self.assertEqual(Game.query.filter_by(round=RoundType.F).first().winner_id, 1)


if __name__ == '__main__':
    unittest.main()

        # def process_game(round_data, round_type, next_round_data, next_round_mapping):
        #     games = []
        #     for game_key, winner_id in round_data.items():
        #         # Identifica os IDs dos jogadores
        #         player1_id = game_key
        #         player2_id = next_round_mapping.get(game_key)  # Use o método get para evitar KeyError

        #         # Verifica se player2_id não é None
        #         if player2_id is None:
        #             raise ValueError(f"Não foi possível encontrar o mapeamento para {game_key} em next_round_mapping")

        #         # Cria o jogo
        #         game = Game(round=round_type, player1_id=player1_id, player2_id=player2_id, winner_id=winner_id)
        #         games.append(game)

        #         # Atualiza o próximo jogo com o vencedor
        #         next_game_key = next_round_mapping[game_key]
        #         next_round_data[next_game_key] = winner_id

        #     return games