from flask import Flask, jsonify, request, json, Blueprint, render_template
from dotenv import load_dotenv 


from models.Video import Video

video_bp = Blueprint('video', __name__, url_prefix='/<dr_name>/videos')

load_dotenv()

@video_bp.route('/', methods=['GET'])
def index_videos(dr_name):
    return render_template('videos/index.html', dr_name=dr_name)
    
@video_bp.route('/<id>', methods=['GET', 'POST', 'DELETE'])
def show_video():
    if request.method == 'GET':
        return render_template('videos/show.html')
    
    elif request.method == 'POST':
        pass

    elif request.method == 'DELETE':
        pass