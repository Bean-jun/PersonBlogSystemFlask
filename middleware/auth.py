"""
请求中间件
"""
from flask import request, session, current_app, redirect, url_for
from apps.models import UserInfo


def auth():
    """
    中间件

    用户授权中间件
    普通访客只能查看白名单页面

    注册访客查看特定页面

    管理员查看全部页面
    """
    id = session.get('id', None)
    user = UserInfo.query.filter_by(id=id).first()
    if not user:
        WHITE_LIST = current_app.config.get("WHITE_LIST", None)

        try:
            PATH = request.path.split("/")[1]
        except Exception as e:
            print(e.args)
            return redirect(url_for("blog.index"))

        if PATH not in WHITE_LIST:
            return redirect(url_for("blog.login"))

        request.user = None
    else:
        request.user = user


def custom_after_request(environ):
    """
    处理跨域问题
    """
    environ.headers['Access-Control-Allow-Origin'] = '*'
    environ.headers['Access-Control-Allow-Method'] = '*'
    environ.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return environ
