from flask import render_template, request, url_for, Blueprint
from .models import *

app = Blueprint('question_type', __name__, url_prefix='/')


@app.route('/')
@app.route('/qtypelist')
def index():
    q_types = Question_type.query.all()
    return render_template('index.html', q_types=q_types)


@app.route('/typeadd', methods=['GET', 'POST'])
def typeadd():
    if request.method == 'GET':
        return render_template('typeadd.html')

    q_type_name = request.form.get('name_field')
    q_type_desc = request.form.get('type_field')

    q_type = create_question_type(q_type_name, q_type_desc)
    return render_template('typeadd.html', q_type=q_type)
