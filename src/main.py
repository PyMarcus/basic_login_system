from flask import Blueprint, render_template
from typing import Tuple
from .settings import STATUS_200_SUCCESS


main = Blueprint("main", __name__)


@main.route('/')
def index() -> Tuple[str, int]:
    return render_template("index.html"), STATUS_200_SUCCESS


@main.route('/profile')
def profile() -> Tuple[str, int]:
    return render_template("profile.html"), STATUS_200_SUCCESS

