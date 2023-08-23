# pylint: disable-all
from flask import redirect, url_for
from flask_login import logout_user
from hangman import app


@app.route("/signout")
def signout() -> redirect:
    logout_user()
    return redirect(url_for("index"))
