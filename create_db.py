

# Este script cria o banco de dados e as tabelas necessárias para o aplicativo
from tennis_app import db
from tennis_app.models.models import Player  # Importe todos os modelos necessários

# Cria as tabelas no banco de dados
db.create_all()

# Aqui você também pode adicionar comandos para preencher o banco de dados com dados iniciais se necessário
