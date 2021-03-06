from app import db


class Question_type(db.Model):
    # See http://flask-sqlalchemy.pocoo.org/2.0/models/#simple-example
    # for details on the column types.

    # We always need an id
    id = db.Column(db.Integer, primary_key=True)
    q_type_name = db.Column (db.String(100))
    q_type_desc = db.Column (db.String(250))

    def __init__(self, name, desc):
        self.q_type_name = name
        self.q_type_desc = desc


class Question(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(400))
    question_type_id = db.Column(db.Integer)

    def __init__(self, name):
        self.name = name


def create_question_type(new_q_type, new_q_type_desc):
    # Create a dessert with the provided input.
    # At first, we will trust the user.

    # This line maps to line 16 above (the Dessert.__init__ method)
    question_type = Question_type(new_q_type, new_q_type_desc)

    # Actually add this dessert to the database
    db.session.add(question_type)

    # Save all pending changes to the database
    db.session.commit()

    return question_type


if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print("Creating database tables...")
    db.create_all()
    print("Done!")
