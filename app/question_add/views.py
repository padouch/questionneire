from flask import render_template, request, url_for, Blueprint
from .models import *
from app.question_type.models import *
from app.question_aspect.models import *

mod = Blueprint('question_add', __name__, url_prefix='/')
print('view q_add')


@mod.route('/questionadd', methods=['GET', 'POST'])
def questionadd():
    if request.method == 'GET':
        qr = db.engine.execute(
            "select qu.id as q_id, qu.q_txt as q_txt, qu.q_deleted as q_deleted, qa.q_aspect as q_aspect, qt.q_type_name as q_type from question qu inner join question_type qt on qu.q_type_id = qt.id inner join question_aspect qa on qu.q_aspect_id = qa.id")
        q_questions = Question.query.all()
        q_types = QuestionType.query.all()
        q_aspect = QuestionAspect.query.all()
        return render_template('question_add/addquestion.html', q_questions=q_questions, q_types=q_types,
                               q_aspect=q_aspect, qrList=qr)

    q_txt = request.form.get('q_txt')
    q_asc_id = request.form.get('q_asc_id')
    q_type_id = request.form.get('q_type_id')

    q_cr_question = create_question(q_txt, q_asc_id, q_type_id)
    qr = db.engine.execute(
        "select qu.id as q_id, qu.q_txt as q_txt, qu.q_deleted as q_deleted, qa.q_aspect as q_aspect, qt.q_type_name as q_type from question qu inner join question_type qt on qu.q_type_id = qt.id inner join question_aspect qa on qu.q_aspect_id = qa.id")

    q_questions = Question.query.all()
    q_types = QuestionType.query.all()
    q_aspect = QuestionAspect.query.all()
    return render_template('question_add/addquestion.html', q_questions=q_questions, q_types=q_types,
                           q_aspect=q_aspect, qrList=qr)
