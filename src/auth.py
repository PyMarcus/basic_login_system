from flask import Blueprint, render_template, redirect, url_for, Response, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .settings import STATUS_200_SUCCESS, STATUS_302_REDIRECT
from typing import Tuple
from .models import User, db


auth = Blueprint("auth", __name__)


@auth.route('/login')
def login() -> Tuple[str, int]:
    return render_template("login.html"), STATUS_200_SUCCESS


@auth.route('/login', methods=['POST'])
def login_post() -> Tuple[str or Response, int]:
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()
    print(username)
    print(password)
    print(user.username, check_password_hash(user.password, password))
    if not user or not check_password_hash(user.password, password):
        flash("Account not registered.Please, register")
        return redirect(url_for('auth.signup')), STATUS_302_REDIRECT

    # creates a cookie (save data from user at pc or browser) and session (activity time to enter or exit from session)
    login_user(user)

    return redirect(url_for('main.profile')), STATUS_302_REDIRECT


@auth.route('/signup')
def signup() -> Tuple[str, int]:
    return render_template("signup.html"), STATUS_200_SUCCESS


@auth.route('/signup', methods=['POST'])
def signup_post() -> Tuple[str or Response, int]:
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()   # check if user already exists

    if user:
        flash("This account already exists.")
        return redirect(url_for('auth.login')), STATUS_302_REDIRECT

    # create a new user instance and update database
    new_user = User(username=username,
                     email=email,
                     password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login')), STATUS_302_REDIRECT


@auth.route('/logout')
@login_required
def logout() -> Tuple[Response, int]:
    logout_user()
    return redirect(url_for('main.index')), STATUS_302_REDIRECT
