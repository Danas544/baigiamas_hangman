# pylint: disable-all
from flask import redirect, url_for
from flask_login import (current_user, login_required,)
from flask_admin.contrib.sqla import ModelView
from hangman import admin, db, app
from hangman.hangman_db.models.user import User
# from appsas.models.irasas import Irasas


class ManoModelView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.admin is True:
            adminas = True
            return (
                current_user.is_authenticated
                and current_user.admin
                and adminas
            )
        else:
            adminas = False
            return adminas


# admin.add_view(ManoModelView(Irasas, db.session))
admin.add_view(ManoModelView(User, db.session))

