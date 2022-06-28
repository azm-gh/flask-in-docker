from flask import Blueprint, request
from flask_restx import Resource, Api

from src import db
from src.api.models import User

# Linking a Flask-RESTX API to the Flask Blueprint and then defined the route handler.
# Check RestX namespace https://flask-restx.readthedocs.io/en/stable/api.html#flask_restx.Namespace

users_blueprint =  Blueprint('users', __name__)
api = Api(users_blueprint)

class UsersList(Resource):
    def post(self):
        post_data = request.get_json()
        username = post_data.get('username')
        email = post_data.get('email')

        db.session.add(User(username=username, email=email))
        db.session.commit()

        response_object={
            'message':f'{email} was added!'
        }
        return response_object, 201

api.add_resource(UsersList, '/users')

