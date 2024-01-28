# models.py
from enum import Enum
# Importar explicitamente o objeto db do módulo tennis_app
from tennis_app import db

# Definir o modelo Player
class Player(db.Model):
    # Cada atributo da classe será uma coluna na tabela do banco de dados
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(3))  # Código do país ISO Alpha-3
    seed = db.Column(db.Integer)    # seed do jogador
    qf_number = db.Column(db.Integer, nullable=True)  # Novo campo adicionado

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "seed": self.seed,
            'qf_number': self.qf_number
        }

    def __repr__(self):
        # Método de representação do objeto para facilitar a depuração e o log
        return f'<Player {self.name}, Country: {self.country}, seed: {self.seed},QF_number: {self.qf_number}>'
    
class RoundType(Enum):
    QF = 'QF'
    SF = 'SF'
    F = 'F'

    def __str__(self):
        return self.value


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.Enum(RoundType), nullable=False)
    player1_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    player2_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    winner_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=True)

    # Relacionamentos com Player (assumindo que a classe Player já está definida)
    player1 = db.relationship('Player', foreign_keys=[player1_id], backref='games_as_player1')
    player2 = db.relationship('Player', foreign_keys=[player2_id], backref='games_as_player2')
    winner = db.relationship('Player', foreign_keys=[winner_id], backref='won_games')

    def __repr__(self):
        round_name = self.round.name if isinstance(self.round, Enum) else self.round
        return f'<Game {self.id} - Round: {round_name}, Player 1: {self.player1_id}, Player 2: {self.player2_id}, Winner: {self.winner_id}>' 

class Pick(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    winner_id = db.Column(db.Integer, db.ForeignKey('player.id'))  # Alterado de pick_result para winner_id
    player1_id = db.Column(db.Integer)  # ID do primeiro jogador
    player2_id = db.Column(db.Integer)  # ID do segundo jogador
    round = db.Column(db.Enum(RoundType))  # Supondo que RoundType seja um Enum válido

    # Relacionamento com Game
    game = db.relationship('Game', foreign_keys=[game_id], backref='picks')

    def __repr__(self):
        return f"<Pick - User: {self.user_id}, Game: {self.game_id}, Round: {self.round.name}, Player 1: {self.player1_id}, Player 2: {self.player2_id}, Winner: {self.winner_id}>"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    picks = db.relationship('Pick', backref='user', lazy='dynamic')  # Certifique-se de que o nome da classe está correto

    def __repr__(self):
        return f'<User {self.username}>'

## Para atualizar o banco de dados, execute os seguintes comandos no terminal:
# $env:FLASK_APP = "D:\TENIS\SF_app\tennis_app"
# flask --app tennis_app db init  
# flask db migrate -m "Descrever migração"
# flask db upgrade