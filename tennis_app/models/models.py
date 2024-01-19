# models.py

# Importar explicitamente o objeto db do módulo tennis_app
from tennis_app import db

# Definir o modelo Player
class Player(db.Model):
    # Cada atributo da classe será uma coluna na tabela do banco de dados
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(3))  # Código do país ISO Alpha-3
    ranking = db.Column(db.Integer)    # Ranking do jogador

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "ranking": self.ranking
        }

    def __repr__(self):
        # Método de representação do objeto para facilitar a depuração e o log
        return f'<Player {self.name}, Country: {self.country}, Ranking: {self.ranking}>'
