from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    extend_existing = True
    app = Flask(__name__)
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:cokolisehodi@localhost/postgres"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    from app.question_type.views import app as q_type_module

    app.register_blueprint(q_type_module)

    with app.app_context():
        db.create_all()

    return app
