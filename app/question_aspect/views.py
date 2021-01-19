from flask import render_template, request, Blueprint
from .models import *

mod = Blueprint('question_aspect', __name__, url_prefix='/')


@mod.route('/qaspectadd', methods=['GET', 'POST'])
def typeadd():
    if request.method == 'GET':
        q_aspect = QuestionAspect.query.all()
        return render_template('question_aspect/question_aspect.html', q_aspect=q_aspect)

    q_aspect_name = request.form.get('q_aspect_name')
    q_aspect = create_question_aspect(q_aspect_name)
    q_aspect = QuestionAspect.query.all()
    return render_template('question_aspect/question_aspect.html', q_aspect=q_aspect)
