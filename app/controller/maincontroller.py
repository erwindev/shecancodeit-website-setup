from flask import Blueprint, render_template, redirect, request, url_for, flash, session
from datetime import datetime
from app.dao.userdao import UserDao
from app.dao.hobbydao import HobbyDao
from app.model.usermodel import User
from app.model.hobbymodel import Hobby
from app.controller.forms import RegistrationForm, HobbyForm

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
        user = UserDao.save_user(user)
        flash('Congratulations, you are now a registered user!')
        session['user_id'] = user.id
        return redirect(url_for('sccit_app.thankyou'))
    return render_template('register.html', title='Register', form=form)

@sccit_app.route('/hobby', methods=['GET', 'POST'])
def hobby():
    form = HobbyForm()
    if form.validate_on_submit():
        hobby = Hobby()
        hobby.name = form.name.data
        hobby.user_id = session['user_id']
        HobbyDao.save_hobby(hobby)
        return redirect(url_for('sccit_app.userdetail', userid=session['user_id']))
    return render_template('hobby.html', title='Hobby', form=form)    


@sccit_app.route('/userdetail/<int:userid>', methods=['GET', 'POST'])
def userdetail(userid):
    user = UserDao.get_by_id(userid)
    session['user_id'] = user.id
    hobbies = HobbyDao.get_hobby_by_userid(user.id)
    return render_template('user_detail.html', title='User Detail', currentuser=user, hobbies=hobbies)        


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