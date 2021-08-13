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


class DetailView(MethodView):
    """详细视图"""

    def get(self, id):
        note = Note.query.filter_by(id=id).first()

        return render_template("detail.html", note=note)
