from flask import Flask, jsonify, request, json, Blueprint, render_template
from dotenv import load_dotenv

import feedparser

articles_bp = Blueprint('articles', __name__, url_prefix='/articles')

load_dotenv()

@articles_bp.route('/', methods=['GET'])
def index(dr_name:str):
    article_feed = feedparser.parse('https://medium.com/feed/@addictiondocMD')
    return render_template('articles.html')