from hangman import db
from flask_login import UserMixin


class Word(db.Model, UserMixin):
    __tablename__ = "word"
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column("name", db.String(20), nullable=False)
    activate: bool = db.Column("activate", db.Boolean, default=True)
    theme_id: int = db.Column(db.Integer, db.ForeignKey("theme.id"))
    theme = db.relationship("Theme")
