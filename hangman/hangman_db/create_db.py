from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()


def initialize_db(app: Flask) -> SQLAlchemy:
    db.init_app(app)
    return db


if __name__ == "__main__":
    pass
