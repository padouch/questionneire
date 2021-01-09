from flask import render_template, request, url_for, Blueprint
from .models import *

mod = Blueprint('question_add', __name__, url_prefix='/questionadd')


@mod.route('/questionadd')
def questionadd():
    if request.method == 'GET':
        q_questions = Question.query.all()
        return render_template('question_add/addquestion.html', q_questions=q_questions)

    q_txt = request.form.get('q_txt_lb')
    q_aspect_id = request.form.get('q_asc_id')
    q_type_id = request.form.get('q_type_id')

    q_cr_question = create_question(q_txt, q_aspect_id, q_type_id)
    return render_template('question_add/addquestion.html', q_add=q_cr_question)
