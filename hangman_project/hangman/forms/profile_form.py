# pylint: disable-all
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.file import FileField, FileAllowed
from hangman.hangman_db.models.user import User
from hangman import logger

class ProfileForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    email = StringField("Email", [DataRequired()])
    photo = FileField(
        "Updated profile picture", validators=[FileAllowed(["jpg", "png"])]
    )
    submit = SubmitField("Confirm")

    def __init__(self, current_user):
        super(ProfileForm, self).__init__()
        self.current_user = current_user

    def validate_email(self, new_email)-> None:
        if len(new_email.data) > 120:
            logger.info("Email too long")
            raise ValidationError("Email too long")
        if new_email.data != self.current_user.email:
            user = User.query.filter_by(email=new_email.data).first()
            if user:
                logger.info("This email address is already registered: %s", user.email)
                raise ValidationError("This email address is already registered")
        else:
            return 
        
    def validate_username(self, username)-> None:
        if len(username.data) > 20:
            logger.info("Name too long")
            raise ValidationError("Name too long")
        else:
            return 
