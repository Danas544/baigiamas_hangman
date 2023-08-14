# pylint: disable-all
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.file import FileField, FileAllowed
from hangman.hangman_db.models.user import User


class ProfileForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    email = StringField("Email", [DataRequired()])
    photo = FileField(
        "Updated profile picture", validators=[FileAllowed(["jpg", "png"])]
    )
    submit = SubmitField("Confirm")

    def __init__(self, current_user, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.current_user = current_user


    def validate_email(self, new_email):
        if new_email.data != self.current_user.email:
            user = User.query.filter_by(email=new_email.data).first()
            if user:
                raise ValidationError(
                "This email address is already registered"
                )
        else:
            return None
