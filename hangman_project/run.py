# pylint: disable-all
from hangman import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5002, debug=True)
else:
    gunicorn_app = app