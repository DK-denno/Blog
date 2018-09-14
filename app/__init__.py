from flask import Flask


def create_app(config_name):
    app = Flask(__name__)



    #importing and initialsing the auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    #importing and initialising he main blueprint   
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app