from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
def initialize_db(app):
    db.init_app(app)
    return db




if __name__ == "__main__":
    pass