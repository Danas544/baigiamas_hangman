# pylint: disable-all
from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField
from wtforms.validators import DataRequired, ValidationError
from hangman.hangman_db.models.theme import Theme
from hangman import logger

class ThemeForm(FlaskForm):
    name = StringField("Themes name", [DataRequired()])
    activate = BooleanField("Activate this new theme?")
    submit = SubmitField("Confirm")

    def __init__(self, theme=None):
        super(ThemeForm, self).__init__()
        self.theme = theme

    def validate_name(self, field) -> None:
        name = field.data
        existing_theme_name = Theme.query.filter_by(name=name).first()
        try:
            if existing_theme_name.name == name and existing_theme_name.id == self.theme.id:
                return 
            else:
                logger.info("Such a theme already exists: %s", existing_theme_name.name)
                raise ValidationError("Such a theme already exists")
        except:
            pass
        if existing_theme_name:
            logger.info("Such a theme already exists: %s", existing_theme_name.name)
            raise ValidationError("Such a theme already exists")
