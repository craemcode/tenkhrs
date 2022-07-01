from enum import unique

from datetime import datetime


db = SQLAlchemy()

class Plug(db.Model):
    __tablename__ = 'plugs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(69), unique=True)
    password = db.Column(db.String(32))
    rating = db.Column(db.Integer)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    products = db.relationship('Products', backref='plug')

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
