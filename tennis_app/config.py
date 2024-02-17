class TestConfig:
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 8025
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = 'noreply@example.com'
    MAIL_SUPPRESS_SEND = True  # Importante para testes: impede o envio de e-mails reais
    TESTING = True
    SECRET_KEY = 'your_secret_key'
