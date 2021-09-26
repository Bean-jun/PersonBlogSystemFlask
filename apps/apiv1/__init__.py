from flask import Blueprint
from flask_restful import Api

api_blueprint = Blueprint('api', __name__)

from .resource import account

api = Api()
api.init_app(api_blueprint)


api.add_resource(account.RegisterView, "/register", endpoint="register")
