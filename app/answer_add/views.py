from flask import render_template, request, url_for, Blueprint
from .models import *
from app.question_add.models import *

mod = Blueprint('answer_add', __name__, url_prefix='/')
print('view answer_add')


@mod.route('/answeradd', methods=['GET', 'POST'])
def answeradd():
    qr_id = request.args.get('question_id')

    if request.method == 'GET':
        ar = Answer.query.filter_by(q_id=qr_id)
        qr = Question.query.filter_by(id=qr_id)
        return render_template('answer_add/answeradd.html', answers=ar, quest_id=qr_id, que=qr)

    a_text = request.form.get('a_txt')
    q_id = request.form.get('q_id')

    a_add = create_answer(a_text, q_id)
    ar = Answer.query.filter_by(q_id=q_id)
    #   question = db.engine.execute("select q_txt from question where id = 1")
    qr = Question.query.filter_by(id=q_id)
    return render_template('answer_add/answeradd.html', answers=ar, quest_id=q_id, que=qr)


@mod.route('/answertmpl', methods=['POST'])
def answertmpl():
    qr_id = request.form.get('q_id')
    a_tmpl = request.form.get('tmp_txt')
    if a_tmpl == "scale1-5-aggree":
        print("scale1-5-aggree")
        a_add = create_answer("Strongly Disagree", qr_id)
        a_add = create_answer("Disagree", qr_id)
        a_add = create_answer("Undecided", qr_id)
        a_add = create_answer("Agree", qr_id)
        a_add = create_answer("Strongly Agree", qr_id)
    elif a_tmpl == "scale1-5-improve":
        print("scale1-5-improve")
        a_add = create_answer("Needs Improvement", qr_id)
        a_add = create_answer("Advanced", qr_id)
        a_add = create_answer("Leader", qr_id)
        a_add = create_answer("Master", qr_id)
        a_add = create_answer("Expert and excelling", qr_id)
    elif a_tmpl == "boolean-tmpl":
        print("boolean-tmpl")
        a_add = create_answer("Yes", qr_id)
        a_add = create_answer("No", qr_id)
    else:
        print("wrong param")

    ar = Answer.query.filter_by(q_id=qr_id)
    #        question = db.engine.execute ("select q_txt from question where id = 1")
    qr = Question.query.filter_by(id=qr_id)
    return render_template('answer_add/answeradd.html', answers=ar, quest_id=qr_id, que=qr)
