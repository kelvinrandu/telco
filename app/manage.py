from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.resources.views import telco
from config import APP_CONFIG



app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(APP_CONFIG[config_name])

    app.register_blueprint(telco)
    

    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'



    return app

