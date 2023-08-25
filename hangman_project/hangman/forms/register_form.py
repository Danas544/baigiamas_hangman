# pylint: disable-all
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from hangman.hangman_db.models.user import User
from hangman import logger
import re
from hangman.check_password.password_strength import PasswordStrength

class RegisterForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    email = StringField("Email", [DataRequired()])
    password = PasswordField("Password", [DataRequired(), PasswordStrength()])
    approved_password = PasswordField(
        "Repeat password", [EqualTo("password", "Passwords must match.")]
    )
    submit = SubmitField("Confirm")

    def validate_email(self, new_email) -> None:
        user = User.query.filter_by(email=new_email.data).first()
        if user:
            if user.email_confirm is False:
                logger.info("This email address is already registered, please confirm email: %s", user.email)
                raise ValidationError("This email address is already registered, please confirm email")
            logger.info("This email address is already registered: %s", user.email)
            raise ValidationError("This email address is already registered")

