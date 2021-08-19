import os
import uuid
from datetime import datetime
from flask.views import MethodView
from flask import render_template, request, redirect, url_for, flash, current_app
from apps.models import Note, UserInfo, UserComment, Category
from apps import db


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


class EditView(MethodView):
    """编辑视图"""

    def get(self):

        editor_category_list_id = request.args.get('editor_category_list')
        notes = None

        try:
            category_id = int(editor_category_list_id)
            notes = Note.query.filter_by(category_id=category_id).all()
        except Exception as e:
            pass

        category = Category.query.filter_by(user=request.user).all()

        category_list = []
        for item in category:
            count = Note.query.filter_by(category_id=item.id).count()
            # 处理当前分类数量
            setattr(item, 'count', count)
            category_list.append(item)

        context = {
            "notes": notes,
            'category_list': category_list,
            'category': category
        }
        return render_template("editor.html", **context)

    def post(self):
        r = request.form
        title = r.get('title')
        content = r.get('content')
        category = r.get('category')
        if not all([title, content, category]):
            flash("信息不全")
            return redirect(url_for("blog.edit"))

        f = request.files.get("top_image")

        # 处理文件夹
        _ = current_app.config.get("TOP_IMAGE_UPLOAD_FOLDER", None)
        if not _:
            raise Exception("请设置TOP_IMAGE_UPLOAD_FOLDER")

        FILE_NAME = str(uuid.uuid4()) + ".png"
        FILE_NAME_FULL = str(_) + "/" + FILE_NAME

        # 数据库保存路径
        SAVE_PATH = str(_).rsplit('static')[-1] + "/" + FILE_NAME

        # 文件保存路径
        FULL_PATH = os.path.join(os.getcwd(), FILE_NAME_FULL)

        # 保存文件
        f.save(FULL_PATH)

        # 处理数据库
        _note = Note(user=request.user,
                     category_id=category,
                     title=title,
                     content=content,
                     modify_datetime=datetime.now(),
                     top_image=SAVE_PATH)

        db.session.add(_note)
        db.session.commit()

        return redirect(url_for("blog.edit", editor_category_list=category))


class DeleteNoteView(MethodView):
    """删除博客文章"""

    def get(self, id):
        note = Note.query.filter_by(id=id).first()
        db.session.delete(note)
        db.session.commit()

        return redirect(url_for('blog.edit'))


class NoteListView(MethodView):
    """博客分类列表"""

    def get(self, id):
        notes = Note.query.filter_by(category_id=id).all()
        return render_template("category_list.html", notes=notes)
