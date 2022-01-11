import os

from dotenv import load_dotenv
load_dotenv()

from flask import Flask, g, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
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

from models.User import User
from models.Article import Article
from models.Video import Video

from views.doctor import doctor_bp
from views.user import user_bp
from views.articles import articles_bp
from views.videos import video_bp
from views.about import about_bp
from views.contact import contact_bp
from views.addiction_tool import addiction_tool_bp

@app.route("/")
def landing():
    return render_template("landing.html")

app.register_blueprint(user_bp)

doctor_bp.register_blueprint(about_bp)
doctor_bp.register_blueprint(articles_bp)
doctor_bp.register_blueprint(video_bp)
doctor_bp.register_blueprint(addiction_tool_bp)
doctor_bp.register_blueprint(contact_bp)


app.register_blueprint(doctor_bp)



