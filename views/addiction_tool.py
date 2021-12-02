from flask import Flask, jsonify, request, json, Blueprint, render_template
from dotenv import load_dotenv

addiction_tool_bp = Blueprint('addiction_tool', __name__)

load_dotenv()

@addiction_tool_bp.route('/addiction_tool', methods=['GET'])
def form():
    return render_template('addiction_tool.html')