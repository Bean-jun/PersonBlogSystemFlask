"""
项目配置文件
"""


class Config(object):
    '''基本配置'''
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'abc'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


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