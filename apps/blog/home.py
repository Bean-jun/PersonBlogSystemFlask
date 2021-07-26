from flask.views import MethodView
from flask import render_template

from apps.blog import home_blueprint


class IndexView(MethodView):
    """首页视图"""

    def get(self):
        return render_template('index.html')


# 首页视图
home_blueprint.add_url_rule('/', view_func=IndexView.as_view(name='index'))
