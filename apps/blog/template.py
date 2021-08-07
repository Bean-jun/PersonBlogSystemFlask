from apps.blog import home_blueprint
from apps.models import Category


@home_blueprint.app_template_global("category_navigate")
def category_navigate():
    category_obj = Category.query.all()
    return category_obj
