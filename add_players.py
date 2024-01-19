# add_players.py

from tennis_app import app, db
from tennis_app.models.models import Player

# app = create_app()
app.app_context().push()

# Lista de jogadores a serem adicionados
new_players_info = [
    {"name": "Q", "country": None, "ranking": None, "pick_number": 1},
    {"name": "Alexei Popyrin", "country": "AUS", "ranking": None, "pick_number": 1},
    {"name": "Marc Polmans", "country": "AUS", "ranking": "WC", "pick_number": 1},
    {"name": "Yannick Hanfmann", "country": "GER", "ranking": None, "pick_number": 1},
    {"name": "Gael Monfils", "country": "FRA", "ranking": None, "pick_number": 1},
    {"name": "Andy Murray", "country": "GBR", "ranking": None, "pick_number": 1},
    {"name": "Tomas Martin Etcheverry", "country": "ARG", "ranking": "30", "pick_number": 1},
    {"name": "Adrian Mannarino", "country": "FRA", "ranking": "20", "pick_number": 1},
    {"name": "Stan Wawrinka", "country": "SUI", "ranking": None, "pick_number": 1},
    {"name": "Alexander Shevchenko", "country": "RUS", "ranking": None, "pick_number": 1},
    {"name": "Jaume Munar", "country": "ESP", "ranking": None, "pick_number": 1},
    {"name": "Christopher O'Connell", "country": "AUS", "ranking": None, "pick_number": 1},
    {"name": "Cristian Garin", "country": "CHI", "ranking": None, "pick_number": 1},
    {"name": "Roberto Bautista Agut", "country": "ESP", "ranking": None, "pick_number": 1},
    {"name": "Ben Shelton", "country": "USA", "ranking": "16", "pick_number": 1}
]



# Adicionando novos jogadores ao banco de dados
for player_data in new_players_info:
    player = Player(
        name=player_data['name'],
        country=player_data.get('country'),
        ranking=player_data.get('ranking'),
        pick_number=player_data.get('pick_number')  # Aqui incluímos o pick_number
    )
    db.session.add(player)
try:
    db.session.commit()
except Exception as e:
    print(f"Erro ao adicionar jogadores: {e}")
    db.session.rollback()
