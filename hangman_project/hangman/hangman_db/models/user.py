# pylint: disable-all
from hangman import db, app
from flask_login import UserMixin

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column("username", db.String(50), nullable=False)
    email: str = db.Column("email", db.String(120), unique=True, nullable=False)
    photo: str = db.Column(db.String(20), nullable=False, default="default.jpg")
    password: str = db.Column("password", db.String(60), nullable=False)
    email_confirm: bool = db.Column(db.Boolean, default=False)
    admin: bool = db.Column(db.Boolean, default=False)


    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
    
