# pylint: disable-all
import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
from flask_mail import Mail
import logging
import logging.config
from hangman.hangman_db.create_db import get_db_uri


logging.config.fileConfig("logging_config.ini", disable_existing_loggers=False)

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SECRET_KEY"] = "4654f5dfadsrfasdr54e6rae"
app.config["SQLALCHEMY_DATABASE_URI"] = get_db_uri()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
MAX_IMAGE_SIZE = 20 * 1024 * 1024
app.config['MAX_CONTENT_LENGTH'] = MAX_IMAGE_SIZE
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True


admin = Admin(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "User needs to be logged in to view this page"
login_manager.login_message_category = "info"
logger = logging.getLogger(__name__)

from hangman.hangman_db.create_db import initialize_db

db = initialize_db(app)


from hangman.hangman_db.models.user import User


@login_manager.user_loader
def load_user(user_id: str) -> User:
    return User.query.get(int(user_id))


import hangman.routes.index_default
import hangman.routes.register
import hangman.routes.login
import hangman.routes.signout
import hangman.routes.user_profile
import hangman.routes.game.game_mode
import hangman.routes.game.theme_selection
import hangman.routes.game.single_player_game
import hangman.routes.game.two_player_game
import hangman.routes.themes
import hangman.routes.words
import hangman.routes.user_stats
import hangman.routes.all_user_stats
import hangman.routes.errors
import hangman.routes.favicon
import hangman.routes.forgot_password
import hangman.routes.email_confirm


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
