from flask import Blueprint, render_template
from dotenv import load_dotenv

from pprint import pprint 
import feedparser

articles_bp = Blueprint('articles', __name__, url_prefix='/articles')

load_dotenv()

@articles_bp.route('/', methods=['GET'])
def index(dr_name:str):
    article_feed = feedparser.parse('https://medium.com/feed/@addictiondocMD')
    pprint(article_feed.entries[0])
    
    return render_template('articles.html', feed=article_feed)