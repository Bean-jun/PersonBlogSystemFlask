from flask import Blueprint

# 创建蓝图
home_blueprint = Blueprint('blog', __name__)

# 导入视图函数
from . import home
