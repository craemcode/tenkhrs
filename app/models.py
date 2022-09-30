
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from app import db


class Role(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    users = db.relationship('Plug', backref='role', lazy=True)


class Plug(UserMixin, db.Model):
    # class variables. they need to be secret,,thus needs methods
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(69), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    rating = db.Column(db.Integer)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    products = db.relationship('Product', backref='plug')

    # getter. however, you cant read the fucking password mate!
    @property
    def password(self):
        raise AttributeError("Password nOT Readable")
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

    def verify_password(self, password): 
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'{ self.name} Rating:{ self.rating}'


@login_manager.user_loader
def load_user(user_id):

    return Plug.query.get(int(user_id))


class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    desc = db.Column(db.Text(140))
    category = db.Column(db.String)
    pic = db.Column(db.String)
    units = db.Column(db.Integer)
    price = db.Column(db.Integer)

    plug_name = db.Column(db.Integer, db.ForeignKey('plug.user_name'), nullable=False)

    #plug = db.relationship("Plug", backref='product')

    def __repr__(self) -> str:
        return f'Product: {self.name}, {self.units }, by {self.plug_id}'
