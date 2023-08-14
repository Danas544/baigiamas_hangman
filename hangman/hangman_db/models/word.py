from hangman import db
from flask_login import UserMixin


class Word(db.Model, UserMixin):
    __tablename__ = "word"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("name", db.String(20), nullable=False)
    activate = db.Column("activate", db.Boolean, default=1)
    theme_id = db.Column(db.Integer, db.ForeignKey("theme.id"))
    theme = db.relationship("Theme")
