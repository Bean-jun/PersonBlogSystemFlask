from flask import request
from apps.blog import home_blueprint
from apps.models import Category


@home_blueprint.app_template_global("category_navigate")
def category_navigate():
    """导航栏"""
    category_obj = Category.query.all()
    return category_obj


@home_blueprint.app_template_global("userinfo_navigate")
def userinfo_navigate():
    """导航栏"""
    return request.user