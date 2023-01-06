from flask import Blueprint, render_template
from flask_login import login_required, current_user  # protect the view
from typing import Tuple
from .settings import STATUS_200_SUCCESS


main = Blueprint("main", __name__)


@main.route('/')
def index() -> Tuple[str, int]:
    return render_template("index.html"), STATUS_200_SUCCESS


@main.route('/profile')
@login_required
def profile() -> Tuple[str, int]:
    name = current_user.username
    return render_template("profile.html", name=name), STATUS_200_SUCCESS
