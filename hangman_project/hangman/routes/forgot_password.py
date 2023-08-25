# pylint: disable-all
from flask import render_template, redirect, url_for, flash
from flask_login import current_user
from hangman.forms.forgot_password_form import (ForgotPasswordForm,NewPasswordForm)
from hangman.hangman_db.models.user import User
from hangman import db, bcrypt, app
from hangman.email_send.send_email import send_reset_email
from typing import List, Union

@app.route("/reset_password", methods=["GET", "POST"])
def reset_request() -> Union[str, redirect]:
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash(
            "Email sent to you email with password reset instructions.",
            "info",
        )
        return redirect(url_for("login"))
    return render_template("reset_request.html", title="Reset Password", form=form)


@app.route("/reset_password/<string:token>", methods=["GET", "POST"])
def reset_token(token:str) -> Union[str, redirect]:
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    user = User.verify_reset_token(token)
    if user is None:
        flash("The request is invalid or expired", "warning")
        return redirect(url_for("reset_request"))
    form = NewPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.new_password.data).decode(
            "utf-8"
        )
        user.password = hashed_password
        db.session.commit()
        flash("Your password has been updated! You can connect", "success")
        return redirect(url_for("login"))
    return render_template("reset_token.html", title="Reset Password", form=form)
