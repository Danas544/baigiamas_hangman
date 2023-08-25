# pylint: disable-all
from flask import render_template, redirect, url_for, flash
from flask_login import current_user
from hangman import db, bcrypt, app
from hangman.forms.register_form import RegisterForm
from hangman.hangman_db.models.user import User
from hangman import logger
from typing import Union
from hangman.email_send.send_email import send_email_confirmation

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
        send_email_confirmation(user)
        logger.info("You have successfully registered! Please confirm your email")
        flash("You have successfully registered! Please confirm your email", "success")
        return redirect(url_for("index"))
    return render_template("register.html", title="Register", form=form)
