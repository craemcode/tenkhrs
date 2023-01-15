from . import auth
from flask import render_template, request, url_for, redirect, flash
from .forms import LoginForm, RegForm
from ..models import User
from flask_login import login_user, logout_user, login_required
from .. import db


@auth.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(user_name=login_form.name.data).first()

        if user.permission == 1 and user is not None and user.verify_password(login_form.password.data):
            login_user(user, remember=False)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.products')
            return redirect(next)

        elif user.permission == 25 and user is not None and user.verify_password(login_form.password.data):
            login_user(user, remember=False)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.add_product')
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
        if registration_form.permission.data == "Buyer":
            permission = 1
            new_user = User(user_name=usrname,
                            password=registration_form.password.data,
                            permission=permission)
        elif registration_form.permission.data == "Seller":
            permission = 25
            new_user = User(user_name=usrname,
                            password=registration_form.password.data,
                            permission=permission)


        db.session.add(new_user)
        try:
            db.session.commit()
            flash("User Successfully added")
            print("Success!")
            return redirect(url_for('auth.login'))
        except Exception as e:
            print(f'Error: {e}')

    return render_template('auth/register.html', registration_form=registration_form)
