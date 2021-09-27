import datetime
from functools import wraps
import jwt

from flask_restful import Resource
from flask import request, current_app
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

    def token_encode(self, **kwargs):
        if not "exp" in kwargs:
            exp = current_app.config.get("TOKEN_EXP")
            kwargs["exp"] = datetime.datetime.utcnow() + datetime.timedelta(seconds=exp)
        encode = jwt.encode(kwargs, current_app.config.get("SECRET_KEY"), algorithm="HS256")
        return encode

    @staticmethod
    def _token_decode(token):
        try:
            msg_dict = jwt.decode(token, current_app.config.get("SECRET_KEY"), algorithms="HS256",
                                  options= {'verify_exp':True})
        except jwt.exceptions.ExpiredSignatureError:
            return False, response(400, "认证已过期")
        except jwt.exceptions.InvalidSignatureError:
            return False, response(400, "签名异常")
        except:
            return False, response(400, "请重新登录获取token")
        else:
            return True, response(200, "登录成功", msg_dict)

    @staticmethod
    def auth(f):

        @wraps(f)
        def inner(*args, **kwargs):
            flag, msg = BaseView._token_decode(request.headers.get("Authorization"))
            if not flag:
                return msg
            return f(*args, **kwargs)

        return inner
