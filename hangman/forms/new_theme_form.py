# pylint: disable-all
from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField
from wtforms.validators import DataRequired, ValidationError
from hangman.hangman_db.models.theme import Theme


class ThemeForm(FlaskForm):
    name = StringField("Themes name", [DataRequired()])
    activate = BooleanField("Activate this new theme?")
    submit = SubmitField("Confirm")

    def validate_name(self, field):
        name = field.data
        theme_name = Theme.query.filter_by(name=name).first()
        try:
            if theme_name.name == name:
                return None
        except:
            pass
        if theme_name:
            raise ValidationError("Such a theme already exists")
