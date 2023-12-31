# pylint: disable-all

from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from hangman import admin, db
from hangman.hangman_db.models.user import User
from hangman.hangman_db.models.theme import Theme
from hangman.hangman_db.models.word import Word
from hangman.hangman_db.models.stats import Stats



class ManoModelView(ModelView):
    def is_accessible(self) -> bool:
        if current_user.is_authenticated and current_user.admin is True:
            return current_user.is_authenticated and current_user.admin



admin.add_view(ManoModelView(User, db.session))
admin.add_view(ManoModelView(Theme, db.session))
admin.add_view(ManoModelView(Word, db.session))
admin.add_view(ManoModelView(Stats, db.session))
