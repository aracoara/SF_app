
# Import app from tennis_app package
from tennis_app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

# venv\Scripts\activate # Ativar ambiente virtual
    