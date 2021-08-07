from flask import Blueprint

# 创建蓝图
home_blueprint = Blueprint('blog', __name__)

# 导入视图函数
from . import home, template

# 首页视图
home_blueprint.add_url_rule('/', view_func=home.IndexView.as_view(name='index'))
home_blueprint.add_url_rule('/detail/<int:id>/', view_func=home.DetailView.as_view(name='detail'))
