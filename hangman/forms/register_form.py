# pylint: disable-all
from flask_wtf import FlaskForm
from wtforms import SubmitField,  StringField, PasswordField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from hangman.hangman_db.models.user import User





class RegisterForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    email = StringField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    approved_password = PasswordField("Repeat password", [EqualTo('password', "Passwords must match.")])
    submit = SubmitField('Confirm')


    def validate_email(self, new_email):
        user = User.query.filter_by(email=new_email.data).first()
        if user:
            raise ValidationError(
                "This email address is already registered"
            )
