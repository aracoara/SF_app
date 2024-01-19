# Description: This script is used to populate the database with test data for testing purposes.

from tennis_app import create_app, db
from tennis_app.models.models import Player

app = create_app()
with app.app_context():
    # Limpar dados existentes
    db.drop_all()
    db.create_all()

    # Players data

    players_info = [
        {"name": "Novak Djokovic", "country": "SRB", "ranking": 1},
        {"name": "Stefanos Tsitsipas", "country": "GRE", "ranking": 7},
        {"name": "Jannik Sinner", "country": "ITA", "ranking": 4},
        {"name": "Andrey Rublev", "country": "RUS", "ranking": 5},
        {"name": "Holger Rune", "country": "DEN", "ranking": 8},
        {"name": "Daniil Medvedev", "country": "RUS", "ranking": 3},
        {"name": "Alexander Zverev", "country": "GER", "ranking": 6},
        {"name": "Carlos Alcaraz", "country": "ESP", "ranking": 2}
    ]

    # Criar instâncias de Player
    for player_data in players_info:
        player = Player(**player_data)
        db.session.add(player)

    # Commit único para todas as adições
    try:
        db.session.commit()
    except Exception as e:
        print(f"Erro ao adicionar jogadores: {e}")
        db.session.rollback()