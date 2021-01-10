from app import db

import logging

logging.basicConfig()
logging.getLogger('sqlalchemy').setLevel(logging.DEBUG)


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    q_txt = db.Column(db.String(500))
    q_deleted = db.Column(db.BOOLEAN, default=False)
    q_aspect_id = db.Column(db.Integer)
    q_type_id = db.Column(db.Integer, default=1)

    def __init__(self, q_txt, q_aspect_id, q_type_id):
        self.q_txt = q_txt
#        self.q_deleted = q_deleted
        self.q_aspect_id = q_aspect_id
        self.q_type_id = q_type_id


def create_question(q_txt, q_aspect_id, q_type_id):
    question = Question(q_txt, q_aspect_id, q_type_id)
    db.session.add(question)
    db.session.commit()

    return question


if __name__ == "__main__":
    # Run this file directly to create the database tables.
    print("Creating database tables...")
    db.create_all()
    print("Done!")
