# pylint: disable-all
from flask import render_template
from hangman import db, app
from hangman.hangman_db.models.user import User
from hangman.admin_model.admino import ManoModelView


@app.route("/")
def index():
    adminas = ManoModelView(User, db.session)
    adminas = adminas.is_accessible()
    return render_template("index.html", adminas=adminas)
