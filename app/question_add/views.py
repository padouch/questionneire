from flask import render_template, request, url_for, Blueprint
from .models import *
from app.question_type.models import *
from app.question_aspect.models import *

mod = Blueprint('question_add', __name__, url_prefix='/')
print('view q_add')


@mod.route('/questionadd', methods=['GET', 'POST'])
def questionadd():
    if request.method == 'GET':
        q_questions = Question.query.all()
        q_types = Question_type.query.all()
        q_aspect = QuestionAspect.query.all()
        return render_template('question_add/addquestion.html', q_questions=q_questions, q_types=q_types,
                               q_aspect=q_aspect)

    q_txt = request.form.get('q_txt')
    q_asc_id = request.form.get('q_asc_id')
    q_type_id = request.form.get('q_type_id')

    q_cr_question = create_question(q_txt, q_asc_id, q_type_id)

    q_questions = Question.query.all()
    q_types = Question_type.query.all()
    q_aspect = QuestionAspect.query.all()
    return render_template('question_add/addquestion.html', q_questions=q_questions, q_types=q_types,
                           q_aspect=q_aspect)
