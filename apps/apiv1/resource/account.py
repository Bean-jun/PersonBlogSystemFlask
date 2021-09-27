import json
from json import JSONDecodeError

from flask import request, current_app
from sqlalchemy import or_

from apps import db
from apps.apiv1.common.response import response
from apps.apiv1.resource.Base import BaseView
from apps.models import UserInfo


class RegisterView(BaseView):

    def post(self):
        try:
            _ = json.loads(request.get_data())
            username = _.get('username')
            email = _.get('email')
            pwd = _.get('pwd')
            confirm_pwd = _.get('confirm_pwd')
        except JSONDecodeError:
            return response(400, "数据格式异常")

        if not all([username, email, pwd, confirm_pwd]):
            return response(400, "请输入完整的账号及密码")

        if pwd != confirm_pwd:
            return response(400, "请确保密码一致")

        user = UserInfo.query.filter_by(email=email).first()
        if user:
            return response(400, "此账号已经注册")

        user = UserInfo(username=username, email=email)

        if email in current_app.config['SUPER_USER']:
            user.is_super = True
        else:
            user.is_super = False

        user.password = pwd
        db.session.add(user)
        db.session.commit()

        return response(200, "注册成功", {"username": user.username, "token": self.token_encode(
            username=user.username,
            email=user.email
        )})


class LoginView(BaseView):

    def post(self):
        try:
            _ = json.loads(request.get_data())
            username = _.get('username')
            pwd = _.get('pwd')
        except JSONDecodeError:
            return response(400, "数据格式异常")

        if not all([username, pwd]):
            return response(400, "账号信息不完整")

        user = UserInfo.query.filter(or_(UserInfo.username==username, UserInfo.email==username)).first()
        if not user:
            return response(400, "账号不存在")

        if not user.check_password(pwd):
            return response(400, "账号密码有误")

        return response(200, "登录成功", {"username": user.username, "token": self.token_encode(
            username=user.username,
            email=user.email
        )})
