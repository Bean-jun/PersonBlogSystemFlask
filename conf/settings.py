"""
项目配置文件
"""
try:
    from blog_secret_key import *
except Exception as e:
    pass


class Config(object):
    '''基本配置'''
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'abc'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 管理员
    SUPER_USER = ADMIN_ACCOUNT  # ADMIN_ACCOUNT = ["xxx@gmail.com"]
    # 白名单-所有用户可以访问
    WHITE_LIST = ["", "login", "register", "detail", "api"]
    # 头像目录
    UPLOAD_FOLDER = "apps/blog/static/asset"
    # 默认注册默认头像
    USER_LOGO = "asset/685b7e29-7daa-44de-a5f4-a1f39d1f969f.png"

    # top_image目录
    TOP_IMAGE_UPLOAD_FOLDER = "apps/blog/static/asset/top_image"


class DevelopConfig(Config):
    '''开发环境'''
    TESTING = False


class ProductConfig(Config):
    '''生产环境'''
    DEBUG = False
    TESTING = False


class TestConfig(Config):
    '''测试环境'''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


# 配置图
ConfigMap = {
    'develop': DevelopConfig,
    'product': ProductConfig,
    'test': TestConfig,
}