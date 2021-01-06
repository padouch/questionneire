from app import db

class Question(db.model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    deleted = db.Column(db.BOOLEAN,default=False)
    question_txt = db.Column(db.String(500))
    aspect_id = db.Column(db.Integer)

def create_question(new_question_txt, new_aspect_id):
    question = Question(new_question_txt,new_aspect_id)
    db.session.add(question)
    db.session.commit()

