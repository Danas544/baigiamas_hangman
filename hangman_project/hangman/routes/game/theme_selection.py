from flask import render_template
from flask_login import login_required, logout_user
from hangman import db, app
from hangman.game_logic.hangman_game import HangmanGame


@app.route("/theme-selection", methods=["GET", "POST"])
@login_required
def theme_selection() -> str:
    available_themes = HangmanGame.get_available_themes(db.session)
    return render_template("theme_selection.html", themes=available_themes)
