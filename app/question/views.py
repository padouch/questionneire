from flask import render_template, request, url_for



@app.route('/questionadd', methods=['GET', 'POST'])
def questionadd():
    if request.method == 'GET':
        return render_template("addquestion.html")

    q_txt = request.form.get()
    q_cr_question = create_question(q_txt, q_asc_id, q_type_id)
    return render_template('addquestion.html', q_add=q_cr_question)


with app.test_request_context():
    print(url_for('index'))
    print(url_for('typeadd'))
