from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from conf.settings import ConfigMap


# 创建数据库db
db = SQLAlchemy()


def create_app(config):
    '''
    工厂模式创建app

    @config: 'develop': 开发环境, 'product': 生产环境, 'test': 测试环境
    '''

    app = Flask(__name__)

    # 加载配置文件
    app.config.from_object(ConfigMap[config])

    # 初始化db
    db.init_app(app=app)

    return app