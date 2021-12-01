import os

from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, url_for, g, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager, login_manager, current_user

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = os.environ.get('SECRET_KEY')

login_manager = LoginManager()
login_manager.init_app(app)

CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

## TODO Remove before deploy

from controllers.user import user_bp
from controllers.article import article_bp
from controllers.video import video_bp

from models.User import User

app.register_blueprint(user_bp)

app.register_blueprint(article_bp)
app.register_blueprint(video_bp)

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/<dr_name>")
def menu(dr_name:str):
    
    dr = {}
    links = []
    
    if dr_name == "Howard":
        dr = User.query.filter_by(email="howard@tocdr.com").first()
        links = [
            {
                "href": "/bio",
                "text": "About Me"
            },
            {
                "href": url_for('video.index_videos', dr_name=dr_name, videos=dr['videos']),
                "text": "Videos"
            },
            {
                "href": "",
                "text": "Articles"
            },
            {
                "href": "/gene_tool",
                "text": "Addiction Tool"
            }
        ]
    
    return render_template("menu.html", dr=dr, links=links)