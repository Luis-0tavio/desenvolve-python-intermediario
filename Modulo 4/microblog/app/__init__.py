from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# Obter o caminho absoluto do diretório do projeto
basedir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.dirname(basedir)

app = Flask(__name__)
app.config['SECRET_KEY'] = "PD12345678"
# Caminho correto para o banco em instance/
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(project_dir, 'instance', 'microblog.db')}"

db = SQLAlchemy()
db.init_app(app)

login = LoginManager(app)
login.login_view = 'login_route'
login.login_message = 'Por favor, faça login para acessar esta página.'

# Importar modelos ANTES de routes
from app.models import models
from app import routes, alquimias

# Criar tabelas com o app context
with app.app_context():
    db.create_all()

@login.user_loader
def load_user(id):
    from app.models.models import User
    try:
        return db.session.get(User, int(id))
    except:
        return None