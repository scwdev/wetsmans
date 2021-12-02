from flask import Flask, jsonify, request, json, Blueprint, render_template, g
from dotenv import load_dotenv

about_bp = Blueprint('about', __name__)

load_dotenv()

@about_bp.route('/about', methods=['GET'])
def about(dr_name:str):
    return render_template('about.html')