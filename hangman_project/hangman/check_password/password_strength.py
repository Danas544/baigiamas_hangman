from wtforms.validators import ValidationError
import re

class PasswordStrength(object):
    def __init__(self, min_length=8, require_lowercase=True, require_uppercase=True, require_digits=True, require_special=False):
        self.min_length = min_length
        self.require_lowercase = require_lowercase
        self.require_uppercase = require_uppercase
        self.require_digits = require_digits
        self.require_special = require_special

    def __call__(self, form, field):
        password = field.data
        if len(password) < self.min_length:
            raise ValidationError(f"Password must be at least {self.min_length} characters long.")

        if self.require_lowercase and not any(c.islower() for c in password):
            raise ValidationError("Password must contain at least one lowercase letter.")

        if self.require_uppercase and not any(c.isupper() for c in password):
            raise ValidationError("Password must contain at least one uppercase letter.")

        if self.require_digits and not any(c.isdigit() for c in password):
            raise ValidationError("Password must contain at least one digit.")

        if self.require_special and not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValidationError("Password must contain at least one special character.")