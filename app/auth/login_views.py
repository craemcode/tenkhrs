from . import auth
from flask import render_template, request, url_for
from .forms import PlugForm
from ..models import Plug
from flask_login import login_user

@auth.route('/login', methods=['GET,POST'])
def login():
    login_form = PlugForm()
    if login_form.validate_on_submit():
        user = Plug.query.filter_by(name=login_form.name.data)

        if user and user.verify_password(login_form.password.data):
            login_user(user, remember=True)   

    return render_template('auth/login.html', login_form=login_form)
