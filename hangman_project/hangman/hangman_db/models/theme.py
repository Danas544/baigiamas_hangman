# pylint: disable-all
from hangman import db
from flask_login import UserMixin


class Theme(db.Model, UserMixin):
    __tablename__ = "theme"
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column("name", db.String(20), unique=True, nullable=False)
    activate: bool = db.Column("activate", db.Boolean, default=True)
