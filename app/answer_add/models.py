from app import db

import logging

logging.basicConfig()
logging.getLogger('sqlalchemy').setLevel(logging.DEBUG)


class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True)
    a_txt = db.Column(db.Integer)
    a_deleted = db.Column(db.BOOLEAN, default=False)
    q_id = db.Column(db.Integer)

    def __init__(self, answer_txt, question_id):
        self.a_txt = answer_txt
        self.q_id = question_id


def create_answer(a_txt, q_id):
    answer = Answer(a_txt, q_id)
    db.session.add(answer)
    db.session.commit()

    return answer
