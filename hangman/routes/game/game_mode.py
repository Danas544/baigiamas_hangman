from flask import render_template, redirect, url_for, request
from flask_login import login_required
from hangman import app
from typing import Union


@app.route("/game-mode-selection/<int:theme_id>", methods=["POST", "GET"])
@login_required
def game_mode_selection(theme_id: int) -> Union[str, redirect]:
    if request.method == "POST":
        return render_template("game_mode_selection.html", theme_id=theme_id)

    return redirect(url_for("index"))
