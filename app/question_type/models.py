from app import db

import logging

logging.basicConfig()
logging.getLogger('sqlalchemy').setLevel(logging.DEBUG)


class Question_type(db.Model):
    __tablename__ = 'question_type'
    id = db.Column(db.Integer, primary_key=True)
    q_type_name = db.Column(db.String(100))
    q_type_desc = db.Column(db.String(250))

    def __init__(self, name, desc):
        self.q_type_name = name
        self.q_type_desc = desc


def create_question_type(new_q_type, new_q_type_desc):
    question_type = Question_type(new_q_type, new_q_type_desc)
    db.session.add(question_type, new_q_type_desc)
    db.session.commit()

    return question_type


if __name__ == "__main__":
    # Run this file directly to create the database tables.
    print("Creating database tables...")
    db.create_all()
    print("Done!")
