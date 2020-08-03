from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired

from flask_security.forms import LoginForm

class ExtendedLoginForm(LoginForm):
    email = StringField('Username or Email Address', [InputRequired()])