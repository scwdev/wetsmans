from flask import Blueprint, render_template
from dotenv import load_dotenv

from pprint import pprint 
import feedparser

articles_bp = Blueprint('articles', __name__, url_prefix='/articles')

load_dotenv()

@articles_bp.route('/', methods=['GET'])
def index(dr_name:str):
    article_feed = feedparser.parse('https://medium.com/feed/@addictiondocMD')
    # print(article_feed.feed.title)
    # ['bozo', 'entries', 'feed', 'headers', 'href', 'status', 'encoding', 'version', 'namespaces']
    return render_template('articles.html', feed=article_feed)