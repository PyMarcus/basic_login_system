from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy  # pip install flask-sqlalchemy
from flask_login import LoginManager  # pip install flask-login
from .settings import PASSWORDHARDCODE, PATHTODB, STATUS_404_NOT_FOUND

# to run: $env:FLASK_APP="main.py"

db = SQLAlchemy()


def page_not_found(e):
    return render_template('error404.html'), STATUS_404_NOT_FOUND


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = PASSWORDHARDCODE
    app.config['SQLALCHEMY_DATABASE_URI'] = PATHTODB

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # when start, calls the blueprint
    login_manager.init_app(app)

    # session. Flask login creates a cookie thats is a session of user
    from .models import User  # models use db,so heres must import

    @login_manager.user_loader
    def load_user(user_id: int) -> User:
        return User.query.get(int(user_id))  # recover user by id from cookie

    app.register_error_handler(STATUS_404_NOT_FOUND, page_not_found)

    from .auth import auth
    app.register_blueprint(auth)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
