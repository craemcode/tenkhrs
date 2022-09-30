from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, IntegerField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired



class ProductForm(FlaskForm):
     name = StringField("Product Name")
     desc = TextAreaField("Description")
     category = SelectField("Category",choices=['Choose 1','Smokables','Edibles','Oils'])
     pic = StringField("Picture")
     price = IntegerField("Price per Unit")
     units = IntegerField("Units")
     submit = SubmitField("Add Product")
