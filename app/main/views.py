from . import main
from .. import db
from flask import render_template
from .forms import PlugForm, ProductForm


@main.route('/')
def index():
    plug_form = PlugForm()

    
    
    
    return render_template('domanip.html', plug_form=plug_form)


@main.route('/add_product', methods=['GET','POST'])
def add_product():
    prod_form = ProductForm()


    return render_template('addprod.html', prod_form=prod_form)