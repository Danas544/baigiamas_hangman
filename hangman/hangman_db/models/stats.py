# pylint: disable-all
from hangman import db
from flask_login import UserMixin
from sqlalchemy import DateTime
from datetime import datetime

class Stats(db.Model, UserMixin):
    __tablename__ = "stats"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column("type", db.String(4), nullable=False)
    score = db.Column("score", db.Integer)
    date = db.Column("date", DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", lazy=True)



