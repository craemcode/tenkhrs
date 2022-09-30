from . import auth
from flask import render_template, request, url_for, redirect, flash
from .forms import PlugForm, RegForm
from ..models import Plug
from flask_login import login_user, logout_user, login_required
from .. import db


@auth.route('/login', methods=['POST', 'GET'])
def login():
    login_form = PlugForm()
    if login_form.validate_on_submit():
        user = Plug.query.filter_by(user_name=login_form.name.data).first()

        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, remember=False)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.products')
            return redirect(next)

        flash('invalid username or password')
    return render_template('auth/login.html', login_form=login_form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))



@auth.route('/register', methods=['POST', 'GET'])
def register():
    registration_form = RegForm()
    if registration_form.validate_on_submit():
        usrname = '@'+registration_form.username.data
        new_plug = Plug(user_name=usrname,
                        password=registration_form.password.data,
                        role_id=3)

        db.session.add(new_plug)
        try:
            db.session.commit()
            flash("User Successfully added")
            print("Success!")
            return redirect(url_for('auth.login'))
        except Exception as e:
            print(f'Error: {e}')

    return render_template('auth/register.html', registration_form=registration_form)
