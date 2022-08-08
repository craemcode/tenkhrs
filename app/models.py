from enum import unique
import imp
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


db = SQLAlchemy()

class Plug(db.Model, UserMixin):
    #class variables. they need to be secret,,thus needs methods
    __tablename__ = 'plugs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(69), unique=True)
    password_hash = db.Column(db.String(128))
    rating = db.Column(db.Integer)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    products = db.relationship('Products', backref='plug')

    #getter. however, you cant read the fucking password mate!
    @property
    def password(self):
        raise AttributeError("Password nOT Readable")
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password): 
        return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        return Plug.query.get(int(user_id))
    


    def __repr__(self):
        return f'{ self.name} Rating:{ self.rating}'

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    desc = db.Column(db.Text(140))
    category = db.Column(db.String)
    pic = db.Column(db.String)
    units = db.Column(db.Integer)
    price = db.Column(db.Integer)
    
    plug_id = db.Column(db.String, db.ForeignKey('plugs.name'))

    def __repr__(self) -> str:
        return f'Product: {self.name}, {self.units }, by {self.plug_id}'
