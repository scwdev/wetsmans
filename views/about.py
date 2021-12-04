from flask import Blueprint, g, render_template, url_for, redirect
from dotenv import load_dotenv

about_bp = Blueprint('about', __name__)

load_dotenv()

howard_bio = [
    "Transitioning to full-time work in data science. As both a psychiatrist and business executive my life-long focus has been on helping people and organizations bring about change. Stories are so important in facilitating change that I wrote a book about them, and at the heart of every story is data. My career in Data Science began when I designed a novel portal/EHR/dashboard for addiction treatment that created an improved environment of care. I’m excited to be retraining in the technical aspects Data Science to add writing as well as designing for change and continuous improvement. (Python, Pandas, Matplotlib, SQL, bash, Linux, Excel)",
    "Author of \"Questions and Answers on Addiction,\" \"Healing Stories,\" \"Addiction Medicine: The Townsend Way,\" and \"A Beginner's Second Text of Psychotherapy.\"",
    "Currently YouTube serial on ending addiction as a problem in America. https://youtu.be/K4jkgpvQwN4",
    "Always open to opportunities to help others solve conflicts and problems at any scale."
    ]

@about_bp.route('/about', methods=['GET'])
def about(dr_name:str):
    if g.dr_name == 'Howard':
        return render_template('about.html', bio=howard_bio)
    
    return redirect(url_for('landing'))