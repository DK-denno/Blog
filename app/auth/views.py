from . import auth
from .. import db
from flask import render_template
from .forms import Signup, Login
from ..models import User


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    register = Signup()
    if register.validate_on_submit():
        user = User.query.filter_by(user_name=register.Username.data).first()
        users = User(user_name=register.Username.data,
                     email=register.Email.data, password=register.Password.data)

        db.session.add(users)
        db.session.commit()

        mail_message("Welcome to pitches", "email/welcome_user",
                     users.email, user=user)

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
