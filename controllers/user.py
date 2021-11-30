from flask import Flask, jsonify, request, json, Blueprint
from dotenv import load_dotenv

from app import db
from models.User import User

user_bp = Blueprint('user', __name__)

load_dotenv()



@user_bp.route('/users', methods=['GET'])
def index_users():
    return User.query.all()


@user_bp.route('/users', methods=['POST'])
def create_user():
    data = json.loads(request.data)
    new_user = {
        'email': data['email'],
        'password': data['password']
    }
    
    print(new_user)
    
    db.session.add(User(new_user))
    db.session.commit()
    
    return (User.query.filter_by(email=data['email']))