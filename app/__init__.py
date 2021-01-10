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
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    print('init app')
    from app.question_add.views import mod as q_add_v
    from app.question_type.views import mod as q_type_v
    from app.question_aspect.views import mod as q_aspect_v
    app.register_blueprint(q_add_v)
    app.register_blueprint(q_type_v)
    app.register_blueprint(q_aspect_v)

    return app
