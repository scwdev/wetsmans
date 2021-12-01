import os

from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager, login_manager

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

app.register_blueprint(user_bp)
app.register_blueprint(article_bp)
app.register_blueprint(video_bp)

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/<dr_name>")
def menu(dr_name:str):
    dr = {}
    if dr_name == "Howard":
        
        dr = {
            "name": "Howard",
            "img": "https://merriam-webster.com/assets/mw/images/article/art-wap-landing-mp-lg/alt-5ae892611bf1a-5168-1472832016f2509f3889266323039a33@1x.jpg",
            "links": [
                {
                    "href": "www.xkcd.com",
                    "text": "some text"
                },
                {
                    "href": "www.xkcd.com",
                    "text": "some text"
                },
                {
                    "href": "www.xkcd.com",
                    "text": "some text"
                }
            ]
        }
    return render_template("menu.html", dr=dr)