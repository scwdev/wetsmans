from flask import Flask, jsonify, request, json, Blueprint, render_template
import feedparser

from dotenv import load_dotenv 

from models.Video import Video

video_bp = Blueprint('videos', __name__, url_prefix='/videos')

load_dotenv()

@video_bp.route('/', methods=['GET'])
def index(dr_name:str):
    video_feed = []
    # if dr_name == 'Howard':
    video_feed = feedparser.parse('https://www.youtube.com/feeds/videos.xml?channel_id=UCT0_JeyTysWfMp25xcJthMg')
        
    return render_template('videos/index.html', feed=video_feed)
    
    
    
    
    
    
@video_bp.route('/<id>', methods=['GET', 'POST', 'DELETE'])
def show_video():
    if request.method == 'GET':
        return render_template('videos/show.html')
    
    elif request.method == 'POST':
        pass

    elif request.method == 'DELETE':
        pass