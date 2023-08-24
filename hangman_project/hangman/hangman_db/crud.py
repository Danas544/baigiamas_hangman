from hangman.hangman_db.models.stats import Stats
from sqlalchemy.orm import Session
from hangman import db
from hangman.hangman_db.models.user import User

def insert_stats(current_user: User, type: str, score: int) -> None:
    stats = Stats(type=type, score=score, user_id=current_user.id, user=current_user)
    db.session.add(stats)
    db.session.commit()

def get_user_stats(current_user: User) -> list[Stats]:
    return Stats.query.filter_by(user_id=current_user.id).all()

def get_all_stats() -> list[Stats]:
    return Stats.query.all()
