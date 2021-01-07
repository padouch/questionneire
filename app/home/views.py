from flask import render_template, url_for

from question_type.models import Question_type
from app import app

@app.route('/')
def index():

    q_type = Question_type.query.all()

    return render_template('question_type/index.html', q_type=q_type)


with app.test_request_context():
    print(url_for('index'))

