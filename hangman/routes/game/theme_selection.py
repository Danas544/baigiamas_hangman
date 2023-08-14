
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required, logout_user
from hangman import bcrypt
from hangman.forms.profile_form import ProfileForm
from hangman.forms.change_password_form import ChangePasswordForm
from hangman.photo.save_photo import save_photo
from hangman import db, app
from hangman.hangman_db.models.user import User
from hangman.game_logic.hangman_game import HangmanGame

@app.route("/theme-selection", methods=["GET", "POST"])
@login_required
def theme_selection():
    available_themes = HangmanGame.get_available_themes(db.session)
    return render_template("theme_selection.html", themes=available_themes)