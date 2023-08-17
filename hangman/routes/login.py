# pylint: disable-all
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user
from hangman import bcrypt
from hangman.forms.login_form import LoginForm
from hangman.hangman_db.models.user import User
from hangman import app


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("index"))
        else:
            flash("Login failed. Check email email and password", "danger")
    return render_template("login.html", title="Log In", form=form)
