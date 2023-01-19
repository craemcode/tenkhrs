
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from app import db


class Permission:

    BUYER = 1
    SELL = 25
    ADMIN = 625


class Role(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    permission = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy=True)

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permission is None:
            self.permission = 0



    def add_permission(self, perm):
        if not self.has_permsion(perm):
            self.permission *= perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permission /= perm

    def reset_permission(self):
        self.permission = 0

    def has_permission(self, perm):
        return self.permission & perm == perm


class User(UserMixin, db.Model):
    # class variables. they need to be secret,,thus needs methods
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(69), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    rating = db.Column(db.Integer, default=0)
    permission = db.Column(db.Integer, db.ForeignKey('role.permission'), nullable=False)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    products = db.relationship('Product', backref='user')

    # getter. however, you cant read the fucking password mate!
    @property
    def password(self):
        raise AttributeError("Password nOT Readable")
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

    def verify_password(self, password): 
        return check_password_hash(self.password_hash, password)

    def can(self, perm):
        return self.permission == perm


    def __repr__(self):
        return f'{ self.name} Rating:{ self.rating}'


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    desc = db.Column(db.Text(140))
    category = db.Column(db.String)
    pic = db.Column(db.String)
    units = db.Column(db.Integer)
    price = db.Column(db.Integer)

    plug_name = db.Column(db.Integer, db.ForeignKey('user.user_name'), nullable=False)

    # plug = db.relationship("Plug", backref='product')

    def __repr__(self) -> str:
        return f'Product: {self.name}, {self.units }, by {self.plug_name}'
