
from flask import Blueprint, flash, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/sign-in', methods = ['GET', 'POST'])
def signIn():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.browse'))
            else:
                flash("Incorrect Password, try again", category='error')
        else:
            flash('Email does not exist, try again', category='error')
    return render_template("signIn.html", user=current_user)

@auth.route('/registration', methods=['GET', 'POST'])
def registration():
    return render_template("registration.html")

@auth.route('/regform', methods=['GET', 'POST'])
def regForm():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Looks Like That Account already Exists', category='error')
        elif len(email)< 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(password) < 2:
            flash("Password must be greater than 3 characters", category="error")
        else:
            #add user to database
            new_user = User(email=email, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category="success")
            #login_user(user, remember="True")
            return redirect(url_for('views.browse'))
    return render_template("regForm.html")