import os
from flask import request, json, Blueprint, flash, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv

from pprint import pprint

from app import db, login_manager
from models.User import User

user_bp = Blueprint('user', __name__)

load_dotenv()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('users/login.html')
    else:
        login_data = request.form
        user = User.query.filter_by(email = login_data['email']).first()
        login_error = None
        
        if user == None:
            print('incorrect email')
            login_error = "incorrect email"
            
        elif not check_password_hash(user.password, login_data['password']):
            print('incorrect pw')
            login_error = "incorrect password"
        
        if login_error is None:
            print('success')
            login_user(user)
            flash('Login successful')
            return redirect(url_for('landing'))
        else:
            return render_template('users/login.html', error=login_error)



@user_bp.route('/update', methods=['GET', 'POST'])
@login_required
def update():
    if request.method == 'GET':
        return render_template('users/update.html')
    else:
        user = User.query.get(current_user.id)
        update_data = request.form
        request_error = None
        
        user.name = update_data['name']
        user.img = update_data['img']
        
        db.session.commit()
        
        return redirect(url_for('landing'))
        




@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('users/register.html')
    else:
        register_data = request.form
        
        register_error = None
        
        if User.query.filter_by(email=register_data['email']).first() != None:
            register_error = "user email already exists"
            print('email exists')
        
        pw_hash = generate_password_hash(register_data['password'])
        is_admin = False
        if register_data['key'] == os.environ.get('ADMIN_KEY'):
            is_admin = True
        
        user = User(email=register_data['email'], password=pw_hash, admin=is_admin)
        
        print(user)
        
        if register_error is None:
            print('error is none')
            db.session.add(user)
            db.session.commit()
            
            login_user(user)
            flash('Registration successful')
            
            return redirect(url_for('landing'))
        
        else:
            return render_template('users/register.html', error=register_error)


@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('landing')





#########################

@user_bp.route('/users', methods=['GET'])
def index_users():
    return f"{User.query.all()}"




@user_bp.route('/users', methods=['POST'])
def create_user():
    data = json.loads(request.data)
    new_user = {
        'email': data['email'],
        'password': data['password']
    }

    db.session.add(User(new_user))
    db.session.commit()
    
    return (User.query.filter_by(email=data['email']))