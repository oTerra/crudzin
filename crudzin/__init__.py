from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serealizer import configure as config_ma

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crudzin.db'

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    from .books import bp_books
    app.register_blueprint(bp_books, url_prefix='/books')

    return app