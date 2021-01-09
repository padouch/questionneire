from flask import render_template, request, Blueprint
from .models import *

mod = Blueprint('question_type', __name__, url_prefix='/')


@mod.route('/')
@mod.route('/qtypelist')
def index():
    q_types = Question_type.query.all()
    return render_template('home/index.html', q_types=q_types)


@mod.route('/typeadd', methods=['GET', 'POST'])
def typeadd():
    if request.method == 'GET':
        q_types = Question_type.query.all()
        return render_template('question_type/typeadd.html', q_types=q_types)

    q_type_name = request.form.get('name_field')
    q_type_desc = request.form.get('type_field')

    q_types = create_question_type(q_type_name, q_type_desc)
    return render_template('question_type/typeadd.html', q_types=q_types)
