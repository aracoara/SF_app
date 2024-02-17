# routes.py
#  
from flask import jsonify, render_template, request, json, url_for, Flask, redirect,  flash, Blueprint
from flask_mail import Message, Mail
from flask_login import login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
from werkzeug.security import check_password_hash
from tennis_app.forms import LoginForm  # Ajuste o caminho conforme sua estrutura
from tennis_app import app, mail
from werkzeug.security import generate_password_hash
from tennis_app.extensions import db
from tennis_app.models.models import Player, Game, User , Pick, Pontuacoes
from .utils.utils import (create_qf_games, create_sf_games, create_final_game_and_champion, get_and_process_picks, 
                          process_results_data_position, get_classified_players, process_results_data)
import logging
logging.basicConfig(level=logging.DEBUG)
import pandas as pd
from flask_mail import Message
import bcrypt

# Configuração do Serializer para gerar o token
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
logging.basicConfig(level=logging.INFO)

print("Definindo rotas...")
# Rota para obter todos os jogadores
@app.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    return jsonify([player.to_dict() for player in players])

# Rota para enviar os picks de um participante
@app.route('/submit_picks', methods=['POST'])
def submit_picks():
    data = request.get_json()
    print("Dados recebidos:", data)

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    user_id = data.get('user_id')

    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # Limpa todos os jogos existentes no banco de dados
    Game.query.delete()

    # Cria os jogos para as quartas de final, semifinais e final
    qf_games = create_qf_games(data)
    sf_games = create_sf_games(data)
    final_games = create_final_game_and_champion(data)

    all_games = qf_games + sf_games + final_games
    # print(all_games)        

    # Adiciona os jogos ao banco de dados
    for game_data in all_games:
        game = Game(
            round=game_data['round'].value,  # Agora 'round' já é uma string
            player1_id=int(game_data['player1_id']),
            player2_id=int(game_data['player2_id']),
            winner_id=int(game_data['winner_id']) if game_data['winner_id'] is not None else None
        )
        db.session.add(game)

    db.session.flush()
    for game_data, game in zip(all_games, Game.query.all()):
        pick = Pick.query.filter_by(user_id=user.id, game_id=game.id).first()
        if pick is None:
            pick = Pick(
                user_id=user.id, 
                game_id=game.id, 
                winner_id=game.winner_id,  # assumindo que esta é a previsão do usuário
                player1_id=game.player1_id,  # assumindo que estas informações estão disponíveis no objeto game
                player2_id=game.player2_id,
                round=game.round  # Supondo que você quer armazenar a rodada aqui
            )
            db
            db.session.add(pick)
        else:
            pick.winner_id  = game.winner_id
            pick.player1_id = game.player1_id
            pick.player2_id = game.player2_id        

    db.session.commit()  # Agora, fazemos commit de todas as mudanças de uma vez

    return jsonify({'message': 'Picks submitted successfully'}), 200

    # except Exception as e:
    #     db.session.rollback()
    #     print("Erro ao salvar jogos:", e)
    #     return jsonify({'error': str(e)}), 500

# Rota para obter as pontuações por rodada    
@app.route('/pontuacoes/rodada/<rodada>', methods=['GET'])
def get_pontuacoes_por_rodada(rodada):
    print("Rota chamada: /pontuacoes/rodada/<rodada>")
    pontuacoes = Pontuacoes.query.filter_by(rodada=rodada).all()
    if pontuacoes:
        return jsonify([pontuacao.to_dict() for pontuacao in pontuacoes]), 200
    return jsonify({'message': 'Nenhuma pontuação encontrada para esta rodada'}), 404

# Método auxiliar para converter o objeto Pontuacoes em dicionário
def to_dict(self):
    return {
        'id': self.id,
        'ranking_pp': self.ranking_pp,
        'ranking_pg': self.ranking_pg,
        'username': self.username,
        'pontos_possiveis': self.pontos_possiveis,
        'pontos_ganhos': self.pontos_ganhos,
        'rodada': self.rodada,
        'data_atualizacao': self.data_atualizacao.isoformat()
    }

# Adicionando o método to_dict à classe Pontuacoes
Pontuacoes.to_dict = to_dict

# Rota para obter os Picks de todos os usuários
@app.route('/api/PicksOverview', methods=['GET'])
def picks_overview():
    # Chama a função para obter o DataFrame com os picks processados
    df_picks = get_and_process_picks()
    # Converte o DataFrame para JSON
    picks_json = df_picks.to_json(orient='records')
    # Converte a string JSON para um objeto Python
    picks_data = json.loads(picks_json)

    # Retorna a resposta JSON
    return jsonify(picks_data)

# Rota para obter os jogadores classificados
@app.route('/api/classified-players', methods=['GET'])
def classified_players():
    # Corrigindo a definição do dicionário file_paths
    file_paths = {
        'QF': 'tennis_app/assets/QF-ao24_v2.csv',
        'SF': 'tennis_app/assets/SF-ao24_v2.csv',
        'F': 'tennis_app/assets/F-ao24_v2.csv',
        'Champion': 'tennis_app/assets/Champion-ao24_v2.csv'
    }

    # Processa os dados para cada fase
    # Assegurando que process_results_data_position retorna DataFrames
    df_classified_players_QF = process_results_data_position(file_paths['QF'])
    df_classified_players_SF = process_results_data_position(file_paths['SF'])
    df_classified_players_F = process_results_data_position(file_paths['F'])
    df_classified_players_Champion = process_results_data_position(file_paths['Champion'])

    # Concatenar os DataFrames
    frames = [df_classified_players_QF, df_classified_players_SF, df_classified_players_F, df_classified_players_Champion]
    df_concatenated = pd.concat(frames)

    with app.app_context():
        player_ids = df_concatenated['player_id'].dropna().unique().astype(int).tolist()
        player_names_dict = {}
            
        for player_id in player_ids:
            # Busca cada jogador individualmente
            player = db.session.query(Player).filter(Player.id == player_id).first()
            if player:
                player_names_dict[player_id] = player.name
        
        # Mapeia os player_id para nomes usando o dicionário criado
        df_concatenated['Jogadores'] = df_concatenated['player_id'].map(player_names_dict)

    # Preparando o DataFrame para retorno JSON
    df_classified_players = df_concatenated[['Position', 'Jogadores']].rename(columns={'Position': 'Posição'})
    output_dict = pd.Series(df_classified_players.Jogadores.values,index=df_classified_players.Posição).to_dict()

    # Retorna os dados como JSON
    return jsonify(output_dict)

# Rota para o login
@app.route('/api/login', methods=['POST'])
def login():
    # Receber dados da solicitação
    email = request.json.get('email')
    password = request.json.get('password')

    # Encontrar usuário pelo email
    user = User.query.filter_by(email=email).first()

    # Verificar se o usuário existe e se a senha está correta
    if user and check_password_hash(user.password_hash, password):
        login_user(user)
        # Incluir o 'id' e 'username' no objeto JSON de resposta
        return jsonify({
            'login': True, 
            'redirect': url_for('index'), 
            'username': user.username,
            'user_id': user.id  # Inclui o ID do usuário na resposta
        }), 200
    else:
        # Resposta para falha no login
        return jsonify({
            'login': False, 
            'message': 'Login Unsuccessful. Please check email and password'
        }), 401
# Certifique-se de remover render_template e não usar o Flask-WTF form se você estiver usando JSON para autenticação.

# Rota para realizar o logout
@app.route('/api/logout', methods=['POST'])
def logout():
    logout_user()
    # Retorna uma resposta JSON indicando sucesso no logout
    return jsonify({'success': True, 'message': 'Logged out successfully'}), 200
 

# Rota para solicitar redefinição de senha
# @app.route('/api/reset_password', methods=['POST'])
# # Supondo que esta seja sua função de redefinição de senha no Flask
# def reset_password():
#     email = request.json.get('email')
#     user = User.query.filter_by(email=email).first()
#     if not user:
#         return jsonify({'message': 'E-mail not found.'}), 404

#     token = s.dumps(email, salt='email-reset')
#     reset_url = f'http://localhost:3000/reset_password/{token}'  # URL do frontend React

#     msg = Message('Redefinição de Senha',
#                   sender=app.config['MAIL_DEFAULT_SENDER'],
#                   recipients=[email])
#     msg.body = f'Por favor, clique no link para redefinir sua senha: {reset_url}'
#     mail.send(msg)
#     return jsonify({'message': 'E-mail de redefinição de senha enviado com sucesso.'}), 200
@app.route('/api/reset_password', methods=['POST'])
def reset_password():
    email = request.json.get('email')
    user = User.query.filter_by(email=email).first()
    if not user:
        app.logger.info(f'Reset password attempt for non-existent email: {email}')
        # It's a good practice not to reveal whether an email exists in the system
        return jsonify({'message': 'If your email is registered, you will receive a password reset link.'}), 200

    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    token = serializer.dumps(email, salt='email-reset-salt')
    reset_url = f'http://localhost:3000/reset_password/{token}'

    # Assuming you have a function to send emails
    send_reset_email(email, reset_url)
    app.logger.info(f'Password reset email sent to: {email}')
    return jsonify({'message': 'If your email is registered, you will receive a password reset link.'}), 200

def send_reset_email(email, url):
    msg = Message('Redefinição de Senha',
                  sender=app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[email])
    msg.body = f'Por favor, clique no link para redefinir sua senha: {url}'
    mail.send(msg)

# Rota para redefinir a senha
@app.route('/api/reset_password/<token>', methods=['POST'])
def reset_password_token(token):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(token, salt='email-reset-salt', max_age=3600)
    except (SignatureExpired, BadSignature) as e:
        app.logger.error(f'Invalid or expired token: {str(e)}')
        return jsonify({'message': 'Invalid or expired token.'}), 401

    user = User.query.filter_by(email=email).first()
    if not user:
        app.logger.error(f'Token decoding succeeded but no user found for email: {email}')
        return jsonify({'message': 'Invalid token.'}), 401

    data = request.get_json()
    new_password = data.get('password')
    if not new_password or len(new_password) < 6:
        return jsonify({'message': 'Password must be at least 6 characters long.'}), 400

    user.password_hash = generate_password_hash(new_password)
    db.session.commit()
    app.logger.info(f'Password reset successful for user: {email}')
    return jsonify({'message': 'Your password has been updated! You are now able to log in'}), 200


## Rota para registrar um novo usuário
@app.route('/api/signup', methods=['POST'])
def signup():
    # 1. Receber dados da solicitação
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # 2. Validação dos dados (exemplo simplificado)
    if not username or not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400

    # 3. Verificar existência do usuário ou e-mail
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({'error': 'Username or email already in use'}), 409

    # 4. Hashing da senha
    password_hash = generate_password_hash(password)

    # 5. Criação do novo usuário
    new_user = User(username=username, email=email, password_hash=password_hash)

    # 6. Salvar usuário no banco de dados
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Could not register user'}), 500

# Rota principal que renderiza a página inicial
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
