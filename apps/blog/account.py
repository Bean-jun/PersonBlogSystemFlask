from flask import request, redirect, url_for, session, flash
from flask import render_template
from flask.views import MethodView
from apps.models import UserInfo
from flask import current_app
from apps import db


class LoginView(MethodView):
    """用户登录"""
    def get(self):
        return render_template("login.html")

    def post(self):
        _ = request.form
        email = _.get('email')
        pwd = _.get('pwd')

        if not all([email, pwd]):
            flash("请输入完整的账号及密码")
            return redirect(url_for("blog.login"))

        user = UserInfo.query.filter_by(email=email).first()
        if not user:
            flash("用户不存在")
            return redirect(url_for("blog.login"))

        flag = user.check_password(pwd)
        if not flag:
            flash("账号密码无效")
            return redirect(url_for("blog.login"))

        session['id'] = user.id
        return redirect(url_for("blog.index"))


class RegisterView(MethodView):
    """用户注册"""
    def get(self):
        return render_template("register.html")

    def post(self):
        _ = request.form
        username = _.get('username')
        email = _.get('email')
        pwd = _.get('pwd')
        confirm_pwd = _.get('confirm_pwd')

        if not all([username, email, pwd, confirm_pwd]):
            flash("请输入完整的账号及密码")
            return redirect(url_for("blog.register"))

        if pwd != confirm_pwd:
            flash("请确保密码一致")
            return redirect(url_for("blog.register"))

        user = UserInfo.query.filter_by(email=email).first()
        if user:
            flash("此账号已经注册")
            return redirect(url_for("blog.register"))

        user = UserInfo(username=username,
                        email=email)

        if email in  current_app.config['SUPER_USER']:
            user.is_super = True
        else:
            user.is_super = False

        user.password = pwd
        db.session.add(user)
        db.session.commit()

        session['id'] = user.id
        return redirect(url_for("blog.index"))


class LogoutView(MethodView):
    """用户退出"""
    def get(self):
        session.clear()
        return redirect(url_for('blog.index'))