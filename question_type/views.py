from flask import render_template, request, url_for

from question_type.models import Question_type, create_question_type
from question.models import Question, create_question
from app import app

@app.route('/')
def index():

    q_type = Question_type.query.all()

    return render_template('question_type/index.html', q_type=q_type)


@app.route('/typeadd', methods=['GET', 'POST'])
def typeadd():

    if request.method == 'GET':
        return render_template('question_type/typeadd.html')

    q_type_name = request.form.get('name_field')
    q_type_desc = request.form.get('type_field')

    q_type = create_question_type(q_type_name, q_type_desc)
    return render_template('question_type/typeadd.html', q_type=q_type)

@app.route('/questionadd', methods=['GET','POST'])
def questionadd():
    if request.method == 'GET':
        return render_template("question_add/addquestion.html")

    q_txt = request.form.get()
    q_cr_question = create_question(q_txt,q_asc_id,q_type_id)
    return render_template('question_add/addquestion.html', q_add=q_cr_question)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('typeadd'))
    print(url_for('questionadd'))
