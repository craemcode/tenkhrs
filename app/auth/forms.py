# from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import Plug


class PlugForm(FlaskForm):
    name = StringField("Username", validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(5,20),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or '
               'underscores')])

    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_user_name(self, field):
        if Plug.query.filter_by(user_name=field.data).first():
            raise ValidationError('Username already in use.')

    