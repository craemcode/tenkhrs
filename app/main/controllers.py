"""these are the functions that handle things in the app"""
# by importing the blueprint, it means these functions will only be associated with the blueprint...

from . import main
from .. import db
from flask import render_template, url_for, flash, redirect, request
from .forms import ProductForm
from ..models import Plug, Product
from flask_login import login_required, current_user


@main.route('/', methods=['GET'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('.products'))
    return render_template('main/index.html')


@main.route('/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    prod_form = ProductForm()
    if prod_form.validate_on_submit():
        product = Product(name=prod_form.name.data,
                          desc=prod_form.desc.data,
                          category=prod_form.category.data,
                          pic="string",
                          price=prod_form.price.data,
                          units=prod_form.units.data,
                          plug_name=current_user.user_name)
        db.session.add(product)
        try:
            db.session.commit()
            flash("added to db")
            return redirect(url_for('.products'))
        except Exception as e:
            print(f'Error: {e}')

    return render_template('main/addprod.html', prod_form=prod_form)


@main.route('/products', methods=['GET'])
@login_required
def products():
    products = Product.query.all()


    return render_template('main/products.html', products=products)

