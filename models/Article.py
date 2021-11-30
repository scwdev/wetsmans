from app import db

from models.Mixins import Id_and_Timestamp, User_Foreign_Key


class Article(db.Model, Id_and_Timestamp, User_Foreign_Key):
    
    img = db.Column(db.String(128))
    title = db.Column(db.String(64), nullable=False)
    subtitle = db.Column(db.String(64), nullable=True)
    description = db.Column(db.Text, nullable=True) 
    body = db.Column(db.Text, nullable=False)
    
    # references = db.relationship('ArticleRef', backref='article')
    
    def __init__(self, init_dict:dict):
        pass
    
    def __repr__(self):
        return f''
    
    
# class ArticleRef(db.Model, Id_and_Timestamp):
    
#     title = db.Column(db.String(64), nullable=False)
#     link = db.Column(db.String(128), nullable=True)
    
#     article = db.Column(db.Integer, db.ForeignKey('article.id'))
    
#     def __init__(self, init_dict:dict):
#         pass
