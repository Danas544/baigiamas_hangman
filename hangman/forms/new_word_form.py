# pylint: disable-all
from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField
from wtforms.validators import DataRequired, ValidationError
from hangman.hangman_db.models.word import Word
from hangman import logger


class WordForm(FlaskForm):
    name = StringField("Word name", [DataRequired()])
    activate = BooleanField("Activate this new word?")
    submit = SubmitField("Confirm")

    def __init__(self, current_theme_id, word=None):
        super(WordForm, self).__init__()
        self.current_theme_id = current_theme_id
        self.word = word

    def validate_name(self, field) -> None:
        name = field.data
        existing_word_name = Word.query.filter_by(
            name=name, theme_id=self.current_theme_id
        ).first()
        try:
            if existing_word_name.name == name and existing_word_name.id == self.word.id:
                return 
            else:
                logger.info("Such a word already exists: %s", existing_word_name.name)
                raise ValidationError("Such a word already exists")
        except:
            pass
        if existing_word_name:
            logger.info("Such a word already exists: %s", existing_word_name.name)
            raise ValidationError("Such a word already exists")
