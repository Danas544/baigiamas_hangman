from hangman.hangman_db.models.stats import Stats
from sqlalchemy.orm import Session
from hangman import db


def insert_stats(current_user, type, score):
    stats = Stats(type=type, score=score, user_id=current_user.id, user=current_user)
    db.session.add(stats)
    db.session.commit()


def get_user_stats(current_user):
    return Stats.query.filter_by(user_id=current_user.id).all()


def get_all_stats():
    return Stats.query.all()
