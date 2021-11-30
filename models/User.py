from app import db
from models.Mixins import Id_and_Timestamp


class User(db.Model, Id_and_Timestamp):
    
    email = db.Column(db.String(64), unique = True, nullable = False)
    password = db.Column(db.String(64), nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=True)
    
    name = db.Column(db.String(64))
    bio = db.Column(db.Text)
    img = db.Column(db.String(128))
    
    articles = db.relationship('Article', backref='user')
    videos = db.relationship('Video', backref='user')
    
    def __init__(self, init_dict:dict):
        self.email = init_dict['email']
        self.password = init_dict['password']
    
    def __repr__(self):
        return {self.id, self.email}
