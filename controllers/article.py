from flask import Flask, jsonify, request, json, Blueprint
from dotenv import load_dotenv

from models.Article import Article

article_bp = Blueprint('article', __name__)

load_dotenv()

@article_bp.route('/articles', methods=['GET'])
def index_articles():
    return jsonify(Article.query.all())