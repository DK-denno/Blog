from . import auth
from .. import db
from flask import render_template,redirect,url_for
from .forms import Signup, Login
from ..models import User
from flask_login import login_user,current_user


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    register = Signup()
    if register.validate_on_submit():
        user = User.query.filter_by(user_name=register.Username.data).first()
        users = User(user_name=register.Username.data,
                     email=register.Email.data, password=register.Password.data)

        db.session.add(users)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('auth/signup.html', signup=register)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    log_in = Login()
    if log_in.validate_on_submit():
        user = User.query.filter_by(user_name=log_in.Username.data).first()
        if user is not None and user.verify_password(log_in.Password.data):
            login_user(user)
            return redirect(url_for('main.index'))

        flash('Invalid username or Password')

    return render_template('auth/login.html', login=log_in)
