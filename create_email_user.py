from tennis_app import app
from tennis_app.extensions import db
from tennis_app.models.models import User

# Adicionar email ao usuário com ID 1
# Lista de usuários e e-mails para atualizar
users_emails = {
    1: 'smashpicksteste01@gmail.com',
    6: 'smashpicksteste02@gmail.com',
    25: 'guilherme.solino@gmail.com',
    26: 'solino.bcb@gmail.com',
    30: 'solino.solino@gmail.com'
}

# Atualizar o banco de dados com os novos e-mails
with app.app_context():
    try:
        # Iterar sobre os pares de id de usuário e e-mail
        for user_id, email in users_emails.items():
            # Buscar usuário por ID utilizando a sessão
            user = db.session.get(User, user_id)
            if user:
                user.email = email  # Definir o novo email do usuário
            else:
                print(f"Usuário com ID {user_id} não encontrado.")

        db.session.commit()  # Confirmar todas as mudanças no banco de dados
        print("Todos os e-mails foram atualizados com sucesso.")
    except Exception as e:
        print("Ocorreu um erro ao atualizar os e-mails:", e)
        db.session.rollback()  # Reverter a sessão em caso de erro
    finally:
        db.session.close()  # Fechar a sessão para liberar recursos

