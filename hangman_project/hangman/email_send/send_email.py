from flask_mail import Message
from flask import url_for
from hangman import mail

def send_reset_email(user) -> None:
    token = user.get_reset_token()
    msg = Message('Password update request',
                  sender='hangman@hangman.lt',
                  recipients=[user.email])
    msg.body = f'''Click the link to reset your password:
    {url_for('reset_token', token=token, _external=True)}
    If you did not make this request, do nothing and the password will not be changed.
    '''
    mail.send(msg)

def send_email_confirmation(user) -> None:
    token = user.get_reset_token(expires_sec=None)
    subject = 'Confirm Your Email'
    message = f'Thank you for registering. Please confirm your email by clicking the link: {url_for("confirm_email", token=token, _external=True)}'
    msg = Message(sender='hangman@hangman.lt', subject=subject, recipients=[user.email], body=message)
    mail.send(msg)
