# pylint: disable-all
from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField
from wtforms.validators import DataRequired, ValidationError
from hangman.hangman_db.models.word import Word


class WordForm(FlaskForm):
    name = StringField("Word name", [DataRequired()])
    activate = BooleanField("Activate this new word?")
    submit = SubmitField("Confirm")

    def __init__(self, current_theme_id, *args, **kwargs):
        super(WordForm, self).__init__(*args, **kwargs)
        self.current_theme_id = current_theme_id

    def validate_name(self, field):
        name = field.data
        word_name = Word.query.filter_by(
            name=name, theme_id=self.current_theme_id
        ).first()
        try:
            if word_name.name == name:
                return None
        except:
            pass
        if word_name:
            raise ValidationError("Such a word already exists")
