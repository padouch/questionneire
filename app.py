import os
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from app import create_app, db

if os.path.exists('.env'):
    print('Importing environment from .env file')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

if os.environ.get('FLATCOKE') == 'production':
    app = DispatcherMiddleware(create_app(os.environ.get("FLATCOKE")), {
        '/api': create_app('api')
    })
else:
    app = create_app(os.environ.get("FLATCOKE") or 'development')

app.config['DEBUG'] = True
questionnaire = Manager(app)



if __name__ == "__main__":
    questionnaire.run()
