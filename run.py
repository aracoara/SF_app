
# Import app from tennis_app package
# from tennis_app import create_app
# app = create_app()

from tennis_app import app

print("Inicializando o aplicativo tennis_app...")
app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)

# venv\Scripts\activate # Ativar ambiente virtual

# # comandos para subir alterações no git
# git status
# git add .
# git commit -m "Descrever o que foi feito"
# git branch
# git checkout -b feature/html
# git push

## comando para definir a variável de ambiente FLASK_APP para indicar ao Flask qual é o arquivo de entrada da sua aplicação
# $env:FLASK_APP = "D:\TENIS\SF_app\tennis_app"
# flask db migrate -m "Add qf_number to Player"
# flask db upgrade
    