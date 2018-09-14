from flask import Flask
from config import config_options


def create_app(config_name):
    app = Flask(__name__)


    app.config.from_object(config_options[config_name])


    #importing and initialsing the auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')
    #importing and initialising he main blueprint   
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint,url_prefix='/main')

    return app