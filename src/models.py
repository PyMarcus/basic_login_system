from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(50))
    email: str = db.Column(db.String(100), unique=True)
    password: str = db.Column(db.String(500))

    def __repr__(self) -> str:
        return f'<User {self.username}>'
