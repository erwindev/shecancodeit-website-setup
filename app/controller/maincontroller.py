from flask import Blueprint, render_template, redirect, request, url_for, flash
from datetime import datetime
from app.dao.userdao import UserDao
from app.model.usermodel import User
from app.controller.forms import RegistrationForm

sccit_app = Blueprint('sccit_app', __name__)


@sccit_app.route('/')
def index():
    return render_template('index.html', title='Home')


@sccit_app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        user.email = form.email.data
        user.firstname = form.firstname.data
        user.lastname = form.lastname.data
        user.street = form.street.data
        user.city = form.city.data
        user.state = form.state.data
        user.zipcode = form.zipcode.data
        UserDao.save_user(user)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('sccit_app.thankyou'))
    return render_template('register.html', title='Register', form=form)


@sccit_app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html',
                           title='Thank You!')


@sccit_app.route('/dashboard')
def dashboard():
    all_users = UserDao.get_all()
    return render_template('dashboard.html',
                           all_users = all_users,
                           title='All Users!')                           