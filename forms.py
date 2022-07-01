from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, IntegerField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired

class PlugForm(FlaskForm):
    name = StringField("Your Username")
    password = PasswordField('password')
    submit = SubmitField(validators=[DataRequired()])

class ProductForm(FlaskForm):
     name = StringField("Product Name")
     desc = TextAreaField("Description")
     category = SelectField("Category",choices=['Choose 1','Smokables','Edibles','Oils'])
     pic = FileField("Picture")
     price = IntegerField("Units")
     units = IntegerField("Price per Unit")
     submit = SubmitField("Add Product",validators=[DataRequired()])
