from app import db

import logging

logging.basicConfig()
logging.getLogger('sqlalchemy').setLevel(logging.DEBUG)


class QuestionAspect(db.Model):
    __tablename__ = 'question_aspect'
    id = db.Column(db.Integer, primary_key=True)
    q_aspect = db.Column(db.String(100))

    def __init__(self, q_aspect_name):
        self.q_aspect = q_aspect_name


def create_question_aspect(new_q_aspect):
    question_aspect = QuestionAspect(new_q_aspect)
    db.session.add(question_aspect)
    db.session.commit()

    return question_aspect


if __name__ == "__main__":
    # Run this file directly to create the database tables.
    print("Creating database tables...")
    db.create_all()
    print("Done!")
