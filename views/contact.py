from flask import Blueprint, render_template
from dotenv import load_dotenv

contact_bp = Blueprint('contact', __name__)

load_dotenv()

@contact_bp.route('/contact', methods=['GET'])
def form(dr_name:str):
    return render_template('contact.html')