
from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField
from wtforms.validators import DataRequired,  EqualTo





class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Current password', [DataRequired()])
    new_password = PasswordField('New password', [DataRequired()])
    new_approved_password = PasswordField("Repeat a new password", [EqualTo('new_password', "The password must match.")])
    submit = SubmitField('Confirm')

