# Description: This script is used to populate the database with test data for testing purposes.

from tennis_app import app, db
from tennis_app.models.models import Player


# adicionar jogadores ao banco de dados
app.app_context().push()
with app.app_context():
    # Limpar dados existentes
    db.drop_all()
    db.create_all()

    # Players data

    players_info = [
        {"name": "Novak Djokovic", "country": "SRB", "seed": 1, "qf_number": 1},
        {"name": "Dino PRIZMIC", "country": "CRO", "seed": None, "qf_number": 1},
        {"name": "Alexei Popyrin", "country": "AUS", "seed": None, "qf_number": 1},
        {"name": "Marc Polmans", "country": "AUS", "seed": "WC", "qf_number": 1},
        {"name": "Yannick Hanfmann", "country": "GER", "seed": None, "qf_number": 1},
        {"name": "Gael Monfils", "country": "FRA", "seed": None, "qf_number": 1},
        {"name": "Andy Murray", "country": "GBR", "seed": None, "qf_number": 1},
        {"name": "Tomas Martin Etcheverry", "country": "ARG", "seed": "30", "qf_number": 1},
        {"name": "Adrian Mannarino", "country": "FRA", "seed": "20", "qf_number": 1},
        {"name": "Stan Wawrinka", "country": "SUI", "seed": None, "qf_number": 1},
        {"name": "Alexander Shevchenko", "country": "RUS", "seed": None, "qf_number": 1},
        {"name": "Jaume Munar", "country": "ESP", "seed": None, "qf_number": 1},
        {"name": "Christopher O'Connell", "country": "AUS", "seed": None, "qf_number": 1},
        {"name": "Cristian Garin", "country": "CHI", "seed": None, "qf_number": 1},
        {"name": "Roberto Bautista Agut", "country": "ESP", "seed": None, "qf_number": 1},
        {"name": "Ben Shelton", "country": "USA", "seed": "16", "qf_number": 1},

        {"name": "Taylor Fritz", "country": "USA", "seed": 12, "qf_number": 2},
        {"name": "Facundo Diaz Acosta", "country": "ARG", "seed": None, "qf_number": 2},
        {"name": "Roberto Carballes Baena", "country": "ESP", "seed": None, "qf_number": 2},
        {"name": "Borna Gojo", "country": "CRO", "seed": None, "qf_number": 2},
        {"name": "Fabian Marozsan", "country": "HUN", "seed": None, "qf_number": 2},
        {"name": "Marin Cilic", "country": "CRO", "seed": None, "qf_number": 2},
        {"name": "Francisco Cerundolo", "country": "ARG", "seed": 22, "qf_number": 2},
        {"name": "Lorenzo Musetti", "country": "ITA", "seed": 25, "qf_number": 2},
        {"name": "Lucca Van Assche", "country": "FRA", "seed": None, "qf_number": 2},
        {"name": "James Duckworth", "country": "AUS", "seed": "WC", "qf_number": 2},
        {"name": "Luca Van Assche", "country": "FRA", "seed": None, "qf_number": 2},
        {"name": "Aleksandar Vukic", "country": "AUS", "seed": None, "qf_number": 2},
        {"name": "Jordan Thompson", "country": "AUS", "seed": None, "qf_number": 2},
        {"name": "Matteo Berrettini", "country": "ITA", "seed": None, "qf_number": 2},
        {"name": "Stefanos Tsitsipas", "country": "GRE", "seed": 7, "qf_number": 2},

        {"name": "Jannik Sinner", "country": "ITA", "seed": 4, "qf_number": 3},
        {"name": "Botic van de Zandschulp", "country": "NED", "seed": None, "qf_number": 3},
        {"name": "Pedro Cachin", "country": "ARG", "seed": None, "qf_number": 3},
        {"name": "Jesper DE JONG", "country": "NED", "seed": None, "qf_number": 3},
        {"name": "Daniel Elahi Galan", "country": "COL", "seed": None, "qf_number": 3},
        {"name": "Jason Kubler", "country": "AUS", "seed": "WC", "qf_number": 3},
        {"name": "J.J. Wolf", "country": "USA", "seed": None, "qf_number": 3},
        {"name": "Sebastian Baez", "country": "ARG", "seed": 26, "qf_number": 3},
        {"name": "Frances Tiafoe", "country": "USA", "seed": 17, "qf_number": 3},
        {"name": "Borna Coric", "country": "CRO", "seed": None, "qf_number": 3},
        {"name": "Tomas Machac", "country": "CZE", "seed": None, "qf_number": 3},
        {"name": "Aleksandar KOVACEVIC", "country": "USA", "seed": None, "qf_number": 3},
        {"name": "Alejandro Tabilo", "country": "CHI", "seed": None, "qf_number": 3},
        {"name": "Flavio COBOLLI", "country": "ITA", "seed": None, "qf_number": 3},
        {"name": "Daniel Altmaier", "country": "GER", "seed": None, "qf_number": 3},
        {"name": "Karen Khachanov", "country": "RUS", "seed": 15, "qf_number": 3},

        {"name": "Alex de Minaur", "country": "AUS", "seed": 10, "qf_number": 4},
        {"name": "Milos Raonic", "country": "CAN", "seed": None, "qf_number": 4},
        {"name": "Matteo Arnaldi", "country": "ITA", "seed": None, "qf_number": 4},
        {"name": "Adam Walton", "country": "AUS", "seed": "WC", "qf_number": 4},
        {"name": "Pavel Kotov", "country": "RUS", "seed": None, "qf_number": 4},
        {"name": "Arthur Rinderknech", "country": "FRA", "seed": None, "qf_number": 4},
        {"name": "Flavio COBOLLI,", "country": "ITA", "seed": None, "qf_number": 4},
        {"name": "Nicolas Jarry", "country": "CHI", "seed": 18, "qf_number": 4},
        {"name": "Sebastian Korda", "country": "USA", "seed": 29, "qf_number": 4},
        {"name": "HALYS, Quentin", "country": "FRA", "seed": None, "qf_number": 4},
        {"name": "Vit KOPRIVA", "country": "CZE", "seed": None, "qf_number": 4},
        {"name": "HARRIS, Lloyd", "country": "RSA", "seed": None, "qf_number": 4},
        {"name": "Christopher Eubanks", "country": "USA", "seed": None, "qf_number": 4},
        {"name": "Taro Daniel", "country": "JPN", "seed": None, "qf_number": 4},
        {"name": "Thiago Seyboth Wild", "country": "BRA", "seed": None, "qf_number": 4},
        {"name": "Andrey Rublev", "country": "RUS", "seed": 5, "qf_number": 4},

        {"name": "Holger Rune", "country": "DEN", "seed": 8, "qf_number": 5},
        {"name": "Yoshihito Nishioka", "country": "JPN", "seed": None, "qf_number": 5},
        {"name": "Laslo Djere", "country": "SRB", "seed": None, "qf_number": 5},
        {"name": "Arthur Cazaux", "country": "FRA", "seed": "WC", "qf_number": 5},
        {"name": "Arthur Fils", "country": "FRA", "seed": None, "qf_number": 5},
        {"name": "Jiri Vesely", "country": "CZE", "seed": None, "qf_number": 5},
        {"name": "Roman Safiullin", "country": "RUS", "seed": None, "qf_number": 5},
        {"name": "Tallon Griekspoor", "country": "NED", "seed": 28, "qf_number": 5},
        {"name": "Ugo Humbert", "country": "FRA", "seed": 21, "qf_number": 5},
        {"name": "GOFFIN, David", "country": "BEL", "seed": None, "qf_number": 5},
        {"name": "Zhizhen Zhang", "country": "CHN", "seed": None, "qf_number": 5},
        {"name": "Federico Coria", "country": "ARG", "seed": None, "qf_number": 5},
        {"name": "Denis Shapovalov", "country": "CAN", "seed": None, "qf_number": 5},
        {"name": "Hubert Hurkacz", "country": "POL", "seed": 9, "qf_number": 5},

        {"name": "Grigor Dimitrov", "country": "BUL", "seed": 13, "qf_number": 6},
        {"name": "Marton Fucsovics", "country": "HUN", "seed": None, "qf_number": 6},
        {"name": "Sebastian Ofner", "country": "AUT", "seed": None, "qf_number": 6},
        {"name": "Thanasi Kokkinakis", "country": "AUS", "seed": None, "qf_number": 6},
        {"name": "Maximilian Marterer", "country": "GER", "seed": None, "qf_number": 6},
        {"name": "Nuno Borges", "country": "POR", "seed": None, "qf_number": 6},
        {"name": "Constant Lestienne", "country": "FRA", "seed": None, "qf_number": 6},
        {"name": "Alejandro Davidovich Fokina", "country": "ESP", "seed": 23, "qf_number": 6},
        {"name": "Felix Auger-Aliassime", "country": "CAN", "seed": 27, "qf_number": 6},
        {"name": "Dominic Thiem", "country": "AUT", "seed": None, "qf_number": 6},
        {"name": "Alexandre Muller", "country": "FRA", "seed": None, "qf_number": 6},
        {"name": "Q", "country": None, "seed": None, "qf_number": 6},
        {"name": "Emil Ruusuvuori", "country": "FIN", "seed": None, "qf_number": 6},
        {"name": "Daniil Medvedev", "country": "RUS", "seed": 3, "qf_number": 6},

        {"name": "Alexander Zverev", "country": "GER", "seed": 6, "qf_number": 7},
        {"name": "Dominik Koepfer", "country": "GER", "seed": None, "qf_number": 7},
        {"name": "Soonwoo Kwon", "country": "KOR", "seed": None, "qf_number": 7},
        {"name": "James McCabe", "country": "AUS", "seed": "WC", "qf_number": 7},
        {"name": "Alex Michelsen", "country": "USA", "seed": None, "qf_number": 7},
        {"name": "Bernabe Zapata Miralles", "country": "ESP", "seed": None, "qf_number": 7},
        {"name": "Jiri Lehecka", "country": "CZE", "seed": 32, "qf_number": 7},
        {"name": "Cameron Norrie", "country": "GBR", "seed": 19, "qf_number": 7},
        {"name": "Juan Pablo Varillas", "country": "PER", "seed": None, "qf_number": 7},
        {"name": "Dusan Lajovic", "country": "SRB", "seed": None, "qf_number": 7},
        {"name": "ZEPPIERI, Giulio", "country": "ITA", "seed": None, "qf_number": 7},
        {"name": "Max Purcell", "country": "AUS", "seed": None, "qf_number": 7},
        {"name": "Albert Ramos-Vinolas", "country": "ESP", "seed": None, "qf_number": 7},
        {"name": "Casper Ruud", "country": "NOR", "seed": 11, "qf_number": 7},

        {"name": "Tommy Paul", "country": "USA", "seed": 14, "qf_number": 8},
        {"name": "Gregoire Barrere", "country": "FRA", "seed": None, "qf_number": 8},
        {"name": "Marcos Giron", "country": "USA", "seed": None, "qf_number": 8},
        {"name": "Jack Draper", "country": "GBR", "seed": None, "qf_number": 8},
        {"name": "Miomir Kecmanovic", "country": "SRB", "seed": None, "qf_number": 8},
        {"name": "Yosuke Watanuki", "country": "JPN", "seed": None, "qf_number": 8},
        {"name": "Rinky Hijikata", "country": "AUS", "seed": None, "qf_number": 8},
        {"name": "Jan-Lennard Struff", "country": "GER", "seed": 24, "qf_number": 8},
        {"name": "Alexander Bublik", "country": "KAZ", "seed": 31, "qf_number": 8},
        {"name": "NAGAL, Sumit", "country": "IND", "seed": None, "qf_number": 8},
        {"name": "Mackenzie McDonald", "country": "USA", "seed": None, "qf_number": 8},
        {"name": "Juncheng Shang", "country": "CHN", "seed": "WC", "qf_number": 8},
        {"name": "Daniel Evans", "country": "GBR", "seed": None, "qf_number": 8},
        {"name": "Lorenzo Sonego", "country": "ITA", "seed": None, "qf_number": 8},
        {"name": "Richard Gasquet", "country": "FRA", "seed": None, "qf_number": 8},
        {"name": "Carlos Alcaraz", "country": "ESP", "seed": 2, "qf_number": 8}

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