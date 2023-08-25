# pylint: disable-all
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email
from hangman.hangman_db.models.user import User




class ForgotPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Confirm')

    def validate_email(self, email) -> None:
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account registered with this email. Sign up.')
        

class NewPasswordForm(FlaskForm):
    new_password = PasswordField("New password", [DataRequired()])
    new_approved_password = PasswordField(
        "Repeat a new password", [EqualTo("new_password", "The password must match.")]
    )
    submit = SubmitField("Confirm")