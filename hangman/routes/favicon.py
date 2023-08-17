# pylint: disable-all
from flask import send_from_directory
import os

from hangman import app


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"), "favicon/favicon.ico"
    )
