
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# definição do banco de dados  
db = SQLAlchemy()
# fale mais sobre o que é o migrate
#  As migrações são uma maneira de fazer alterações ou atualizações no banco de dados, como adicionar uma nova tabela ou uma nova coluna a uma tabela existente.
migrate = Migrate()

# criação do aplicativo
app = Flask(__name__)
# configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sf_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# inicialização do banco de dados e das migrações
db.init_app(app)
migrate.init_app(app, db)

# importação das rotas e dos modelos
print("Importando rotas...")
from tennis_app import routes
print("Importando modelos...")
from tennis_app.models import models



