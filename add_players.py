# add_players.py

from tennis_app import create_app, db
from tennis_app.models.models import Player

app = create_app()
app.app_context().push()

# Lista de jogadores a serem adicionados
new_players_info = [
    {"name": "Q", "country": None, "ranking": None},
    {"name": "Alexei Popyrin", "country": "AUS", "ranking": None},
    {"name": "Marc Polmans", "country": "AUS", "ranking": "WC"},
    {"name": "Yannick Hanfmann", "country": "GER", "ranking": None},
    {"name": "Gael Monfils", "country": "FRA", "ranking": None},
    {"name": "Andy Murray", "country": "GBR", "ranking": None},
    {"name": "Tomas Martin Etcheverry", "country": "ARG", "ranking": "30"},
    {"name": "Adrian Mannarino", "country": "FRA", "ranking": "20"},
    {"name": "Stan Wawrinka", "country": "SUI", "ranking": None},
    {"name": "Alexander Shevchenko", "country": "RUS", "ranking": None},
    {"name": "Jaume Munar", "country": "ESP", "ranking": None},
    {"name": "Christopher O'Connell", "country": "AUS", "ranking": None},
    {"name": "Cristian Garin", "country": "CHI", "ranking": None},
    {"name": "Roberto Bautista Agut", "country": "ESP", "ranking": None},
    {"name": "Ben Shelton", "country": "USA", "ranking": "16"}
]


# Adicionando novos jogadores ao banco de dados
for player_data in new_players_info:
    player = Player(name=player_data['name'],
                    country=player_data.get('country'),
                    ranking=player_data.get('ranking'))
    db.session.add(player)

try:
    db.session.commit()
except Exception as e:
    print(f"Erro ao adicionar jogadores: {e}")
    db.session.rollback()
