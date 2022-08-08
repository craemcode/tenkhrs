from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired



class PlugForm(FlaskForm):
    name = StringField("Your Username")
    password = PasswordField('password')
    submit = SubmitField('Login',validators=[DataRequired()])

    