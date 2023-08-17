from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required, logout_user
from hangman import bcrypt
from hangman.forms.profile_form import ProfileForm
from hangman.forms.change_password_form import ChangePasswordForm
from hangman.photo.save_photo import save_photo
from hangman import db, app
from hangman.hangman_db.models.user import User


@app.route("/two-player-game/<theme_id>", methods=["GET", "POST"])
@login_required
def two_player_game(theme_id):
    if request.method == "POST":
        # Handle two-player game logic
        # ...
        pass
    return render_template("two_player_game.html")
