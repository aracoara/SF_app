# add_players.py

from tennis_app import app, db
from tennis_app.models.models import Player

# app = create_app()
app.app_context().push()

# Deletar registros existentes na tabela de jogadores
try:
    db.session.query(Player).delete()
    db.session.commit()
except Exception as e:
    print(f"Erro ao deletar registros existentes: {e}")
    db.session.rollback()

# Lista de jogadores a serem adicionados
new_players_info = [

        {"name": "Novak Djokovic", "country": "SRB", "ranking": 1, "qf_number": 1},
        {"name": "Q", "country": None, "ranking": None, "qf_number": 1},
        {"name": "Alexei Popyrin", "country": "AUS", "ranking": None, "qf_number": 1},
        {"name": "Marc Polmans", "country": "AUS", "ranking": "WC", "qf_number": 1},
        {"name": "Yannick Hanfmann", "country": "GER", "ranking": None, "qf_number": 1},
        {"name": "Gael Monfils", "country": "FRA", "ranking": None, "qf_number": 1},
        {"name": "Andy Murray", "country": "GBR", "ranking": None, "qf_number": 1},
        {"name": "Tomas Martin Etcheverry", "country": "ARG", "ranking": "30", "qf_number": 1},
        {"name": "Adrian Mannarino", "country": "FRA", "ranking": "20", "qf_number": 1},
        {"name": "Stan Wawrinka", "country": "SUI", "ranking": None, "qf_number": 1},
        {"name": "Alexander Shevchenko", "country": "RUS", "ranking": None, "qf_number": 1},
        {"name": "Jaume Munar", "country": "ESP", "ranking": None, "qf_number": 1},
        {"name": "Christopher O'Connell", "country": "AUS", "ranking": None, "qf_number": 1},
        {"name": "Cristian Garin", "country": "CHI", "ranking": None, "qf_number": 1},
        {"name": "Roberto Bautista Agut", "country": "ESP", "ranking": None, "qf_number": 1},
        {"name": "Ben Shelton", "country": "USA", "ranking": "16", "qf_number": 1},

        {"name": "Taylor Fritz", "country": "USA", "ranking": 12, "qf_number": 2},
        {"name": "Facundo Diaz Acosta", "country": "ARG", "ranking": None, "qf_number": 2},
        {"name": "Roberto Carballes Baena", "country": "ESP", "ranking": None, "qf_number": 2},
        {"name": "Borna Gojo", "country": "CRO", "ranking": None, "qf_number": 2},
        {"name": "Fabian Marozsan", "country": "HUN", "ranking": None, "qf_number": 2},
        {"name": "Marin Cilic", "country": "CRO", "ranking": None, "qf_number": 2},
        {"name": "Francisco Cerundolo", "country": "ARG", "ranking": 22, "qf_number": 2},
        {"name": "Lorenzo Musetti", "country": "ITA", "ranking": 25, "qf_number": 2},
        {"name": "Lucca Van Assche", "country": "FRA", "ranking": None, "qf_number": 2},
        {"name": "James Duckworth", "country": "AUS", "ranking": "Wildcard", "qf_number": 2},
        {"name": "Luca Van Assche", "country": "FRA", "ranking": None, "qf_number": 2},
        {"name": "Aleksandar Vukic", "country": "AUS", "ranking": None, "qf_number": 2},
        {"name": "Jordan Thompson", "country": "AUS", "ranking": None, "qf_number": 2},
        {"name": "Matteo Berrettini", "country": "ITA", "ranking": None, "qf_number": 2},
        {"name": "Stefanos Tsitsipas", "country": "GRE", "ranking": 7, "qf_number": 2},

        {"name": "Jannik Sinner", "country": "ITA", "ranking": 4, "qf_number": 3},
        {"name": "Botic van de Zandschulp", "country": "NED", "ranking": None, "qf_number": 3},
        {"name": "Pedro Cachin", "country": "ARG", "ranking": None, "qf_number": 3},
        {"name": "Q", "country": None, "ranking": None, "qf_number": 3},
        {"name": "Daniel Elahi Galan", "country": "COL", "ranking": None, "qf_number": 3},
        {"name": "Jason Kubler", "country": "AUS", "ranking": "Wildcard", "qf_number": 3},
        {"name": "J.J. Wolf", "country": "USA", "ranking": None, "qf_number": 3},
        {"name": "Sebastian Baez", "country": "ARG", "ranking": 26, "qf_number": 3},
        {"name": "Frances Tiafoe", "country": "USA", "ranking": 17, "qf_number": 3},
        {"name": "Borna Coric", "country": "CRO", "ranking": None, "qf_number": 3},
        {"name": "Tomas Machac", "country": "CZE", "ranking": None, "qf_number": 3},
        {"name": "Q", "country": None, "ranking": None, "qf_number": 3},
        {"name": "Alejandro Tabilo", "country": "CHI", "ranking": None, "qf_number": 3},
        {"name": "Q", "country": None, "ranking": None, "qf_number": 3},
        {"name": "Daniel Altmaier", "country": "GER", "ranking": None, "qf_number": 3},
        {"name": "Karen Khachanov", "country": "RUS", "ranking": 15, "qf_number": 3},

        {"name": "Alex de Minaur", "country": "AUS", "ranking": 10, "qf_number": 4},
        {"name": "Milos Raonic", "country": "CAN", "ranking": None, "qf_number": 4},
        {"name": "Matteo Arnaldi", "country": "ITA", "ranking": None, "qf_number": 4},
        {"name": "Adam Walton", "country": "AUS", "ranking": "Wildcard", "qf_number": 4},
        {"name": "Pavel Kotov", "country": "RUS", "ranking": None, "qf_number": 4},
        {"name": "Arthur Rinderknech", "country": "FRA", "ranking": None, "qf_number": 4},
        {"name": "Nicolas Jarry", "country": "CHI", "ranking": 18, "qf_number": 4},
        {"name": "Sebastian Korda", "country": "USA", "ranking": 29, "qf_number": 4},
        {"name": "Quentin Halys", "country": "FRA", "ranking": None, "qf_number": 4},
        {"name": "Q", "country": None, "ranking": None, "qf_number": 4},
        {"name": "Christopher Eubanks", "country": "USA", "ranking": None, "qf_number": 4},
        {"name": "Taro Daniel", "country": "JPN", "ranking": None, "qf_number": 4},
        {"name": "Thiago Seyboth Wild", "country": "BRA", "ranking": None, "qf_number": 4},
        {"name": "Andrey Rublev", "country": "RUS", "ranking": 5, "qf_number": 4},

        {"name": "Holger Rune", "country": "DEN", "ranking": 8, "qf_number": 5},
        {"name": "Yoshihito Nishioka", "country": "JPN", "ranking": None, "qf_number": 5},
        {"name": "Laslo Djere", "country": "SRB", "ranking": None, "qf_number": 5},
        {"name": "Arthur Cazaux", "country": "FRA", "ranking": "Wildcard", "qf_number": 5},
        {"name": "Arthur Fils", "country": "FRA", "ranking": None, "qf_number": 5},
        {"name": "Jiri Vesely", "country": "CZE", "ranking": None, "qf_number": 5},
        {"name": "Roman Safiullin", "country": "RUS", "ranking": None, "qf_number": 5},
        {"name": "Tallon Griekspoor", "country": "NED", "ranking": 28, "qf_number": 5},
        {"name": "Ugo Humbert", "country": "FRA", "ranking": 21, "qf_number": 5},
        {"name": "Q", "country": None, "ranking": None, "qf_number": 5},
        {"name": "Zhizhen Zhang", "country": "CHN", "ranking": None, "qf_number": 5},
        {"name": "Federico Coria", "country": "ARG", "ranking": None, "qf_number": 5},
        {"name": "Denis Shapovalov", "country": "CAN", "ranking": None, "qf_number": 5},
        {"name": "Hubert Hurkacz", "country": "POL", "ranking": 9, "qf_number": 5},

        {"name": "Grigor Dimitrov", "country": "BUL", "ranking": 13, "qf_number": 6},
        {"name": "Marton Fucsovics", "country": "HUN", "ranking": None, "qf_number": 6},
        {"name": "Sebastian Ofner", "country": "AUT", "ranking": None, "qf_number": 6},
        {"name": "Thanasi Kokkinakis", "country": "AUS", "ranking": None, "qf_number": 6},
        {"name": "Maximilian Marterer", "country": "GER", "ranking": None, "qf_number": 6},
        {"name": "Nuno Borges", "country": "POR", "ranking": None, "qf_number": 6},
        {"name": "Constant Lestienne", "country": "FRA", "ranking": None, "qf_number": 6},
        {"name": "Alejandro Davidovich Fokina", "country": "ESP", "ranking": 23, "qf_number": 6},
        {"name": "Felix Auger-Aliassime", "country": "CAN", "ranking": 27, "qf_number": 6},
        {"name": "Dominic Thiem", "country": "AUT", "ranking": None, "qf_number": 6},
        {"name": "Alexandre Muller", "country": "FRA", "ranking": None, "qf_number": 6},
        {"name": "Q", "country": None, "ranking": None, "qf_number": 6},
        {"name": "Emil Ruusuvuori", "country": "FIN", "ranking": None, "qf_number": 6},
        {"name": "Daniil Medvedev", "country": "RUS", "ranking": 3, "qf_number": 6},

        {"name": "Alexander Zverev", "country": "GER", "ranking": 6, "qf_number": 7},
        {"name": "Dominik Koepfer", "country": "GER", "ranking": None, "qf_number": 7},
        {"name": "Soonwoo Kwon", "country": "KOR", "ranking": None, "qf_number": 7},
        {"name": "James McCabe", "country": "AUS", "ranking": "Wildcard", "qf_number": 7},
        {"name": "Alex Michelsen", "country": "USA", "ranking": None, "qf_number": 7},
        {"name": "Bernabe Zapata Miralles", "country": "ESP", "ranking": None, "qf_number": 7},
        {"name": "Jiri Lehecka", "country": "CZE", "ranking": 32, "qf_number": 7},
        {"name": "Cameron Norrie", "country": "GBR", "ranking": 19, "qf_number": 7},
        {"name": "Juan Pablo Varillas", "country": "PER", "ranking": None, "qf_number": 7},
        {"name": "Dusan Lajovic", "country": "SRB", "ranking": None, "qf_number": 7},
        {"name": "Q", "country": None, "ranking": None, "qf_number": 7},
        {"name": "Max Purcell", "country": "AUS", "ranking": None, "qf_number": 7},
        {"name": "Albert Ramos-Vinolas", "country": "ESP", "ranking": None, "qf_number": 7},
        {"name": "Casper Ruud", "country": "NOR", "ranking": 11, "qf_number": 7},

        {"name": "Tommy Paul", "country": "USA", "ranking": 14, "qf_number": 8},
        {"name": "Gregoire Barrere", "country": "FRA", "ranking": None, "qf_number": 8},
        {"name": "Marcos Giron", "country": "USA", "ranking": None, "qf_number": 8},
        {"name": "Jack Draper", "country": "GBR", "ranking": None, "qf_number": 8},
        {"name": "Miomir Kecmanovic", "country": "SRB", "ranking": None, "qf_number": 8},
        {"name": "Yosuke Watanuki", "country": "JPN", "ranking": None, "qf_number": 8},
        {"name": "Rinky Hijikata", "country": "AUS", "ranking": None, "qf_number": 8},
        {"name": "Jan-Lennard Struff", "country": "GER", "ranking": 24, "qf_number": 8},
        {"name": "Alexander Bublik", "country": "KAZ", "ranking": 31, "qf_number": 8},
        {"name": "Q", "country": None, "ranking": None, "qf_number": 8},
        {"name": "Mackenzie McDonald", "country": "USA", "ranking": None, "qf_number": 8},
        {"name": "Juncheng Shang", "country": "CHN", "ranking": "Wildcard", "qf_number": 8},
        {"name": "Daniel Evans", "country": "GBR", "ranking": None, "qf_number": 8},
        {"name": "Lorenzo Sonego", "country": "ITA", "ranking": None, "qf_number": 8},
        {"name": "Richard Gasquet", "country": "FRA", "ranking": None, "qf_number": 8},
        {"name": "Carlos Alcaraz", "country": "ESP", "ranking": 2, "qf_number": 8}
        
        ]


# Adicionando novos jogadores ao banco de dados
for player_data in new_players_info:
    player = Player(
        name=player_data['name'],
        country=player_data.get('country'),
        ranking=player_data.get('ranking'),
        qf_number=player_data.get('qf_number')  # Usando qf_number aqui
    )
    db.session.add(player)
try:
    db.session.commit()
except Exception as e:
    print(f"Erro ao adicionar jogadores: {e}")
    db.session.rollback()
