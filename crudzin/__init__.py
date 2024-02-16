from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crudzin.db'

    config_db(app)

    Migrate(app, app.db)

    return app