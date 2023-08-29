from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from dotenv import load_dotenv
import os
from sqlalchemy_utils import database_exists, create_database


db = SQLAlchemy()


def initialize_db(app: Flask) -> SQLAlchemy:
    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        create_database(app.config['SQLALCHEMY_DATABASE_URI'])
        

    db.init_app(app)
    return db


if __name__ == "__main__":
    pass


def get_db_uri() -> str:
    load_dotenv("db.env")
    db_user = os.environ.get("POSTGRES_USER")
    db_password = os.environ.get("POSTGRES_PASSWORD")
    db_name = os.environ.get("POSTGRES_DB")
    port = os.environ.get("PORT")
    server = os.environ.get("POSTGRES_SERVER")
    db_uri = f"postgresql+psycopg2://{db_user}:{db_password}@{server}:{port}/{db_name}"
    return db_uri
