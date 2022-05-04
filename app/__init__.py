from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from .request import configure_request
from .main import main as main_blueprint

bootstrap = Bootstrap()

def create_app(config_name):

    # Initializing application
    app = Flask(__name__,instance_relative_config=True)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
 
    # Initializing Flask Extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    configure_request(app)

    return app






from app.main import views
from app.main import error


