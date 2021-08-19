import os
import uuid
from flask import request, redirect, url_for, session, flash
from flask import render_template, jsonify
from flask.views import MethodView
from apps.models import UserInfo, Category
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

        # 用户默认头像
        user.image = current_app.config.get("USER_LOGO", None)

        if email in current_app.config['SUPER_USER']:
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


class ModifyLogo(MethodView):
    """修改用户头像"""

    def post(self):
        f = request.files.get("image")
        # 处理文件夹
        _ = current_app.config.get("UPLOAD_FOLDER", None)
        if not _:
            raise Exception("请设置UPLOAD_FOLDER")
        FILE_NAME = str(uuid.uuid4()) + ".png"
        FILE_NAME_FULL = str(_) + "/" + FILE_NAME

        # 数据库保存路径
        SAVE_PATH = str(_).rsplit('/')[-1] + "/" + FILE_NAME

        # 文件保存路径
        FULL_PATH = os.path.join(os.getcwd(), FILE_NAME_FULL)

        # 保存文件
        f.save(FULL_PATH)

        # 处理用户数据库
        user = UserInfo.query.filter_by(id=request.user.id).first()
        if not user:
            return redirect(url_for('blog.login'))

        user.image = SAVE_PATH
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('blog.profile'))


class ModifyPassWdView(MethodView):
    """修改密码视图"""

    def post(self):
        r = request.form
        print(r)
        old_pwd = r.get("old_pwd", None)
        pwd = r.get("pwd", None)
        if not all([old_pwd, pwd]):
            return jsonify({"msg": False})

        user = UserInfo.query.filter_by(id=request.user.id).first()
        if not user:
            return jsonify({"msg": False})

        if not user.check_password(old_pwd):
            return jsonify({"msg": False, "content": "初始密码错误~"})
        else:
            user.password = pwd

        db.session.add(user)
        db.session.commit()

        session.clear()

        return jsonify({"msg": True, "content": "修改密码成功~"})


class AddCategory(MethodView):
    """添加博客分类"""
    def post(self):
        r = request.form.get("category", None)
        if not r:
            return jsonify({"msg": False})

        category = Category(user=request.user,
                            name=r)

        db.session.add(category)
        db.session.commit()

        return jsonify({"msg": True, "content": "添加成功~"})