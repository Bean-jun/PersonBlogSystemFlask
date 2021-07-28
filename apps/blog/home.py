from flask.views import MethodView
from flask import render_template
from apps.models import Note, UserInfo
from apps.blog import home_blueprint


class IndexView(MethodView):
    """首页视图"""

    def get(self):
        user = UserInfo.query.filter_by(is_super=1).first()
        notes = Note.query.all()[:14]

        context = {
            'notes': notes,
            'user': user,
        }

        return render_template('index.html', **context)


# 首页视图
home_blueprint.add_url_rule('/', view_func=IndexView.as_view(name='index'))
