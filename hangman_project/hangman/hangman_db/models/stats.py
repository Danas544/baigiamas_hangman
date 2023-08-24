# pylint: disable-all
from hangman import db
from flask_login import UserMixin
from sqlalchemy import DateTime
from datetime import datetime
from typing import Literal
from hangman.hangman_db.models.user import User
Type = Literal["win", "lose"]

class Stats(db.Model, UserMixin):
    __tablename__ = "stats"
    id: int = db.Column(db.Integer, primary_key=True)
    type: Type = db.Column("type", db.String(4), nullable=False)
    score: int = db.Column("score", db.Integer)
    date: DateTime = db.Column("date", DateTime, default=datetime.now())
    user_id: int = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", lazy=True)