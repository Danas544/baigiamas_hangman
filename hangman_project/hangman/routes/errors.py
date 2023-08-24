from flask import render_template
from hangman import app


@app.errorhandler(404)
def page_not_found(error) -> str:
    return render_template("404.html"), 404
