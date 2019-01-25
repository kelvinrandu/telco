import re
import datetime
from flask_restful import Resource,reqparse,Api
from flask import Flask,jsonify,request, make_response,Blueprint,redirect
# from application.v1.resources.models import Product,Sale,User,Category 

telco = Blueprint('api', __name__)

app = Flask(__name__)
api = Api(telco)

class Home(Resource):
    def get(self):
            return {'message': 'installed correctly'}, 200

api.add_resource(Home, '/')