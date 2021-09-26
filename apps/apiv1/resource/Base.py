from flask_restful import Resource
from flask import request
from apps.apiv1.common.response import response

class BaseView(Resource):

    def get(self):
        return response(400, f"{request.method}请求方式异常")

    def post(self):
        return response(400, f"{request.method}请求方式异常")

    def delete(self):
        return response(400, f"{request.method}请求方式异常")

    def put(self):
        return response(400, f"{request.method}请求方式异常")
