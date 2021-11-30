from app import db
from models.Mixins import Id_and_Timestamp, User_Foreign_Key


class Video(db.Model, Id_and_Timestamp, User_Foreign_Key):
    
    link = db.Column(db.String(128), nullable=False)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=True) 
    
    # img = db.Column(db.String(128), nullable=True)
    
    def __init__(self, init_dict:dict):
        self.link = init_dict.link
        self.title = init_dict.title
        self.description = init_dict.description
    
    def __repr__(self):
        return f''
    