from flask import Flask
from config import Config
from app.resources.views import telco
from config import APP_CONFIG



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(APP_CONFIG[config_name])

    app.register_blueprint(telco)


    return app

