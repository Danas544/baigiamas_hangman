# pylint: disable-all
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user
from hangman import bcrypt
from hangman.forms.login_form import LoginForm
from hangman.hangman_db.models.user import User
from hangman import app
from hangman import logger
from typing import Union


@app.route("/login", methods=["GET", "POST"])
def login() -> Union[str, redirect]:
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            logger.info(f"Login success: {user.username}")
            flash(f"Login success: {user.username}", "success")
            return redirect(url_for("index"))
        else:
            logger.warning("Login failed. Check email email and password")
            flash("Login failed. Check email email and password", "danger")
    return render_template("login.html", title="Log In", form=form)
