
# tennis_app/__init__.py
from flask import Flask
import logging
from tennis_app.extensions import db, migrate, login_manager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
import os
from flask_cors import CORS   

# Configuração do logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
## Definindo o aplicativo
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

CORS(app, supports_credentials=True, origins="*")
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,X-Requested-With')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
    response.headers.add('Access-Control-Expose-Headers', 'Content-Type,Authorization,X-Requested-With,Access-Control-Allow-Origin')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sf_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bcrypt = Bcrypt(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')
mail = Mail(app)

db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    from tennis_app.models.models import User
    return User.query.get(int(user_id))

from tennis_app import routes


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager
# from tennis_app.models.models import User  # Ajuste o caminho conforme a organização do seu projeto

# # definição do banco de dados  
# db = SQLAlchemy()
# # fale mais sobre o que é o migrate
# #  As migrações são uma maneira de fazer alterações ou atualizações no banco de dados, como adicionar uma nova tabela ou uma nova coluna a uma tabela existente.
# migrate = Migrate()

# # criação do aplicativo
# app = Flask(__name__)
# # configuração do banco de dados
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sf_app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # inicialização do banco de dados e das migrações
# db.init_app(app)
# migrate.init_app(app, db)

# # Inicialização do Flask-Login
# login_manager = LoginManager()
# login_manager.init_app(app)

# # Configuração do user_loader
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# # importação das rotas e dos modelos
# print("Importando rotas...")
# from tennis_app import routes
# print("Importando modelos...")
# from tennis_app.models import models


# print(type(app.config['SECRET_KEY']))
# print(app.config['SECRET_KEY'])

# CORS(app)
# CORS(app, supports_credentials=True, resources={
#     r"/api/*": {
#         "origins": "http://localhost:3000",
#         "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
#         "allow_headers": ["Content-Type", "Authorization", "X-Requested-With"],
#         "expose_headers": ["Content-Type", "Authorization", "X-Requested-With", "Access-Control-Allow-Origin"],
#     }
# })

