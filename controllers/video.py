from flask import Flask, jsonify, request, json, Blueprint
from dotenv import load_dotenv

from models.Video import Video

video_bp = Blueprint('video', __name__)

load_dotenv()

@video_bp.route('/videos', methods=['GET'])
def index_videos():
    return jsonify(Video.query.all())