import sys
import os
sys.path.insert(0, os.path.abspath('D:\\TENIS\\SF_app'))

import unittest
from unittest.mock import patch
from flask import jsonify
from tennis_app import app, db
from tennis_app.models.models import db, Game, RoundType, Player

# Classe de teste para testar a lógica de processamento de jogos
class GameRouteTestCase(unittest.TestCase):
    # Configuração do ambiente de teste
    def setUp(self):
        self.app = app('testing')
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
    # Limpeza do ambiente de teste
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_tournament_route(self):
        # Dados fictícios do torneio
        torneio_data = {
            "quartasFinal": {"QF1": "1", "QF2": "17", "QF3": "32", "QF4": "48", "QF5": "62", "QF6": "76", "QF7": "90", "QF8": "104"},
            "semiFinal": {"SF1": "1", "SF2": "48", "SF3": "62", "SF4": "90"},
            "final": {"F1": "48", "F2": "90"},
            "campeao": "48"
        }

        # Envia uma solicitação POST para a rota do torneio com os dados do torneio
        response = self.client.post('/tournament', json=torneio_data)

        # Verifica se a resposta tem status 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verifica se os jogos das Quartas de Final foram criados corretamente no banco de dados
        qf_games = Game.query.filter_by(round=RoundType.QF).all()
        self.assertEqual(len(qf_games), 4)

        # Verifica se os jogos das Semifinais foram criados corretamente no banco de dados
        sf_games = Game.query.filter_by(round=RoundType.SF).all()
        self.assertEqual(len(sf_games), 2)

        # Verifica se o jogo da Final foi criado corretamente no banco de dados
        f_game = Game.query.filter_by(round=RoundType.F).first()
        self.assertIsNotNone(f_game)
        self.assertEqual(f_game.player1_id, 48)
        self.assertEqual(f_game.player2_id, 90)

        # Verifica se o campeão foi definido corretamente
        self.assertEqual(f_game.winner_id, 48)

if __name__ == '__main__':
    unittest.main()
