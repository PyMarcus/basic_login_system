from flask import Blueprint, render_template, redirect, url_for, Response
from .settings import STATUS_200_SUCCESS, STATUS_302_REDIRECT, STATUS_201_UPDATE
from typing import Tuple

auth = Blueprint("auth", __name__)


@auth.route('/login')
def login() -> Tuple[str, int]:
    return render_template("login.html"), STATUS_200_SUCCESS


"""@auth.route('/login', methods=['POST'])
def login() -> Tuple[str, int]:
    ..."""


@auth.route('/signup')
def signup() -> Tuple[str, int]:
    return render_template("signup.html"), STATUS_200_SUCCESS


"""@auth.route('/login', methods=['POST'])
def signup() -> Tuple[str, int]:
    ..."""


@auth.route('/logout')
def logout() -> Tuple[Response, int]:
    return redirect(url_for('main.index')), STATUS_302_REDIRECT
