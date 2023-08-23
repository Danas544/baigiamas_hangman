# pylint: disable-all
from flask import render_template, redirect, url_for, flash
from flask_login import current_user
from hangman import db, bcrypt, app
from hangman.forms.register_form import RegisterForm
from hangman.hangman_db.models.user import User
from hangman import logger
from typing import Union


@app.route("/register", methods=["GET", "POST"])
def register() -> Union[str, redirect]:
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegisterForm()
    if form.validate_on_submit():
        crypted_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=crypted_password,
        )
        db.session.add(user)
        db.session.commit()
        logger.info("You have successfully registered! You can login")
        flash("You have successfully registered! You can login", "success")
        return redirect(url_for("index"))
    return render_template("register.html", title="Register", form=form)
