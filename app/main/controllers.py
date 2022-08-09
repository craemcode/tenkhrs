"""these are the functions that handle things in the app"""
#by importing the blueprint, it means these functions will only be associated with the blueprint...

from . import main
from .. import db
from flask import render_template, url_for
from .forms import ProductForm
from ..models import Plug, Product


@main.route('/', methods=['GET','POST'])
def index():

    
    
    
    return render_template('main/index.html')


@main.route('/add_product', methods=['GET','POST'])
def add_product():
    prod_form = ProductForm()


    return render_template('main/addprod.html', prod_form=prod_form)