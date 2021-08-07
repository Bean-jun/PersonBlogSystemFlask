from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from conf.settings import ConfigMap
from middleware.auth import auth

# 创建数据库db
db = SQLAlchemy()


def create_app(config):
    '''
    工厂模式创建app

    @config: 'develop': 开发环境, 'product': 生产环境, 'test': 测试环境
    '''

    app = Flask(__name__, static_folder='blog/static', template_folder='blog/templates')

    # 加载配置文件
    app.config.from_object(ConfigMap[config])

    # 初始化db
    db.init_app(app=app)

    # 创建请求中间件
    app.before_request(auth)


    # 导入blog蓝图
    from apps.blog import home_blueprint  # fix: 修复循导入问题
    app.register_blueprint(home_blueprint, url_prefix="")

    return app
