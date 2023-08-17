# pylint: disable-all
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField("Email", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    submit = SubmitField("Log In")
