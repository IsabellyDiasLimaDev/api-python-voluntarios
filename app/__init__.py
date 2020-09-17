from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

app.config.from_object('config')

db = SQLAlchemy(app)

from .controllers import volunteers_controller, socialactions_controller

api.add_resource(volunteers_controller.Voluntary, '/voluntario/<string:name>/')
api.add_resource(volunteers_controller.AllVolunteers, '/voluntarios/')
api.add_resource(socialactions_controller.SocialAction, '/acaosocial/<string:name>/')
api.add_resource(socialactions_controller.AllActions,'/acoessociais/')
