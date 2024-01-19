
# test_models.py
# import sys
# sys.path.append('D:\\TENIS\\SF_app\\tennis_app')

import pytest
from flask_testing import TestCase
from tennis_app import app, db  # Importe app aqui, não create_app
from tennis_app.models.models import Player, Game, RoundType

class TestGameModel(TestCase):
    
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # Usar banco de dados em memória para testes
    TESTING = True

    def create_app(self):
        # Configurações do app para testes
        app.config['SQLALCHEMY_DATABASE_URI'] = self.SQLALCHEMY_DATABASE_URI
        app.config['TESTING'] = self.TESTING
        return app

    def setUp(self):
        db.create_all()
        # Adicionar alguns jogadores de teste
        player1 = Player(name="Player 1", country="C1", ranking=1)
        player2 = Player(name="Player 2", country="C2", ranking=2)
        db.session.add(player1)
        db.session.add(player2)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_game_creation(self):
        # Criação de um jogo deve funcionar
        player1 = Player.query.first()
        player2 = Player.query.get(2)
        game = Game(round=RoundType.QF, player1_id=player1.id, player2_id=player2.id)
        db.session.add(game)
        db.session.commit()

        self.assertEqual(Game.query.count(), 1)
        self.assertEqual(game.player1.name, "Player 1")
        self.assertEqual(game.player2.name, "Player 2")

    def test_game_relationships(self):
        # Testar se as relações entre Game e Player estão funcionando
        player1 = Player.query.first()
        player2 = Player.query.get(2)
        game = Game(round=RoundType.QF, player1_id=player1.id, player2_id=player2.id)
        db.session.add(game)
        db.session.commit()

        self.assertEqual(game.player1.id, player1.id)
        self.assertEqual(game.player2.id, player2.id)

# Adicionar mais testes conforme necessário

# Para executar os testes com pytest
if __name__ == '__main__':
    pytest.main()
    
## Comando para executar os testes
# pytest games_players_test.py
