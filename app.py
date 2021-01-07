from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up the SQLAlchemy Database to be a local file 'desserts.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questioner.db'
db = SQLAlchemy(app)
extend_existing = True

if __name__ == "__main__":
    from question_type.views import *

    app.run(debug=True)
