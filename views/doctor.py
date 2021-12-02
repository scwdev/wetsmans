from flask import Flask, jsonify, request, json, Blueprint, render_template, g, url_for
from dotenv import load_dotenv

from models.User import User

doctor_bp = Blueprint('doctor', __name__, url_prefix='/<dr_name>')

load_dotenv()


@doctor_bp.url_value_preprocessor
def nav_links(endpoints, values):
    dr_name = values['dr_name']
    g.nav_links=[
        {
            'href': url_for('landing'),
            'text': 'Landing'
        },
        {
            'href': url_for('doctor.about.about', dr_name=dr_name),
            'text': 'About Me'
        },
        {
            'href': url_for('doctor.videos.index', dr_name=dr_name),
            'text': 'Videos'
        },
        {
            'href': url_for('doctor.articles.index', dr_name=dr_name),
            'text': 'Articles'
        },
        {
            'href': url_for('doctor.addiction_tool.form', dr_name=dr_name),
            'text': 'Addiction Tool'
        },
        {
            'href': url_for('doctor.contact.form', dr_name=dr_name),
            'text': 'Contact'
        }
        ]

@doctor_bp.route("/")
def menu(dr_name:str):
    links = []
    if dr_name == "Howard":
        dr = User.query.filter_by(email="howard@tocdr.com").first()
        links = g.nav_links
    
    return render_template("menu.html", links=links, dr=dr)
