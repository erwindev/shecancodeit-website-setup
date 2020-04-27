import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from app.config import Config
from app.config import config_by_name

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()

def create_app(config_name):

    APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMPLATE_PATH = os.path.join(APP_PATH, 'app/templates')

    app = Flask(__name__, template_folder=TEMPLATE_PATH)

    bootstrap.init_app(app)

    app.config.from_object(config_by_name[config_name])

    from app.model.usermodel import User

    db.init_app(app)
    migrate.init_app(app, db)

    from app.controller.maincontroller import sccit_app
    app.register_blueprint(sccit_app)

    return app
