from flask_mail import Message
from flask import url_for
from hangman import mail
from hangman.email_send.gmail_send import get_access_token
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_reset_email(user) -> None:
    try:
        token = user.get_reset_token()
        msg = Message('Password update request',
                    sender='hangman@hangman.lt',
                    recipients=[user.email])
        msg.body = f'''Click the link to reset your password:
        {url_for('reset_token', token=token, _external=True)}
        If you did not make this request, do nothing and the password will not be changed.
        '''
        mail.send(msg)
    except:
        creds = get_access_token()
        service = build('gmail', 'v1', credentials=creds)
        message = MIMEMultipart('alternative')
        html_content = f'''
        <html>
        <head></head>
        <body>
            <p>Hello,</p>
            <p>We received a request to reset your password. Click the link below to proceed.</p>
            <p>If you didn't request this, you can safely ignore this email.</p>
            <p><a href="{url_for('reset_token', token=token, _external=True)}">Click here to reset your password</a></p>
            <p>Best regards,<br>The Hangman Team</p>
        </body>
        </html>
        '''

        # Attach the HTML content to the message
        message.attach(MIMEText(html_content, 'html'))
        message['to'] = user.email
        message['subject'] = 'Password update request'
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
        message = service.users().messages().send(userId='me', body={'raw': raw_message}).execute()

def send_email_confirmation(user) -> None:
    try:
        token = user.get_reset_token(expires_sec=None)
        subject = 'Confirm Your Email'
        message = f'Thank you for registering. Please confirm your email by clicking the link: {url_for("confirm_email", token=token, _external=True)}'
        msg = Message(sender='hangman@hangman.lt', subject=subject, recipients=[user.email], body=message)
        mail.send(msg)
    except:
        creds = get_access_token()
        service = build('gmail', 'v1', credentials=creds)
        message = MIMEMultipart('alternative')
        subject = 'Confirm Your Email'
        html_content = f'''
        <html>
        <head></head>
        <body>
            <p>Dear User,</p>
            <p>Thank you for registering with Hangman! We're excited to have you on board.</p>
            <p>To complete your registration and ensure the security of your account, please confirm your email address by clicking the link below:</p>
            <p><a href="{url_for('confirm_email', token=token, _external=True)}">Click here to confirm your email</a></p>
            <p>If you did not create an account with Hangman, you can ignore this email.</p>
            <p>Best regards,<br>The Hangman Team</p>
        </body>
        </html>
        '''

        # Attach the HTML content to the message
        message.attach(MIMEText(html_content, 'html'))
        message['to'] = user.email
        message['subject'] = subject
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
        message = service.users().messages().send(userId='me', body={'raw': raw_message}).execute()

