from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # pip install flask-sqlalchemy
from flask_login import LoginManager  # pip install flask-login
from .settings import PASSWORDHARDCODE, PATHTODB

# to run: $env:FLASK_APP="main.py"

db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = PASSWORDHARDCODE
    app.config['SQLALCHEMY_DATABASE_URI'] = PATHTODB

    db.init_app(app)

    from .auth import auth
    app.register_blueprint(auth)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
