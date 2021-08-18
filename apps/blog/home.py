from flask.views import MethodView
from flask import render_template, request
from apps.models import Note, UserInfo, UserComment, Category


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


class ProfileView(MethodView):
    """个人视图"""

    def get(self):
        comment = UserComment.query.filter_by(user=request.user).all()
        category = Category.query.filter_by(user=request.user).all()
        context = {
            "comment": comment,
            'category': category
        }
        return render_template("profile.html", **context)
