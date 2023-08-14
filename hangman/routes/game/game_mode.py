from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required, logout_user
from hangman import bcrypt
from hangman.forms.profile_form import ProfileForm
from hangman.forms.change_password_form import ChangePasswordForm
from hangman.photo.save_photo import save_photo
from hangman import db, app
from hangman.hangman_db.models.user import User


@app.route("/game-mode-selection", methods=["POST", "GET"])
@login_required
def game_mode_selection():
    if request.method == "POST":
        return render_template("game_mode_selection.html")

    return redirect(url_for("index"))
