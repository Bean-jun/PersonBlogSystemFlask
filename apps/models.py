from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from apps import db


class UserInfo(db.Model):
    """用户表"""
    __tablename__ = "userinfo"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(32), unique=True, nullable=False)
    _password = db.Column(db.String(32), nullable=False)
    is_super = db.Column(db.BOOLEAN, default=False)  # 是否为管理员
    image = db.Column(db.String(256))  # 用户头像
    bucket = db.Column(db.String(128))
    region = db.Column(db.String(32))
    create_datetime = db.Column(db.DATETIME, default=datetime.now)

    category = db.relationship('Category', backref="user")  # 用户的文章分类
    note = db.relationship('Note', backref="user")  # 用户的文章
    usercomment = db.relationship('UserComment', backref="user")  # 用户的评论
    userinfoweibo = db.relationship('UserInfoWeiBo', backref="user")  # 用户的评论

    def __repr__(self):
        return self.username

    @property
    def password(self):
        raise AttributeError("密码不可读")

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def check_password(self, pwd):
        return check_password_hash(self._password, pwd)


class UserInfoWeiBo(db.Model):
    """微博用户"""
    __tablename__ = "userinfoweibo"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("userinfo.id"))
    access_token = db.Column(db.String(32), nullable=False)
    expires = db.Column(db.String(32), nullable=False)
    create_datetime = db.Column(db.DATETIME, default=datetime.now)
    modify_datetime = db.Column(db.DATETIME, nullable=False)


class Category(db.Model):
    """分类表"""
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("userinfo.id"))
    name = db.Column(db.String(32), nullable=False)
    repos_slug = db.Column(db.String(32), nullable=False)  # 语雀知识库slug
    create_datetime = db.Column(db.DATETIME, default=datetime.now)

    note = db.relationship('Note', backref="category")  # 用户的评论

    def __repr__(self):
        return self.name


class Note(db.Model):
    """用户笔记表"""
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("userinfo.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    title = db.Column(db.String(32), nullable=False)
    content = db.Column(db.TEXT, nullable=False)
    yuque = db.Column(db.String(32), default="")
    sync_status = db.Column(db.BOOLEAN, default=False)
    create_datetime = db.Column(db.DATETIME, default=datetime.now)
    modify_datetime = db.Column(db.DATETIME, nullable=False)
    top_image = db.Column(db.String(256))

    usercomment = db.relationship('UserComment', backref="note")  # 用户的评论


class UserComment(db.Model):
    """用户评论"""
    __tablename__ = "usercomment"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("userinfo.id"))
    note_id = db.Column(db.Integer, db.ForeignKey("note.id"))
    content = db.Column(db.String(32), nullable=False)
    create_datetime = db.Column(db.DATETIME, default=datetime.now)
    up = db.Column(db.Integer, default=0)
    down = db.Column(db.Integer, default=0)
    is_top = db.Column(db.BOOLEAN, default=False)


class VisitorRecord(db.Model):
    """访客记录"""
    __tablename__ = "visitorrecord"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(16))
    host = db.Column(db.String(16))
    create_datetime = db.Column(db.DATETIME, default=datetime.now)


class CityWeather(db.Model):
    """天气内容"""
    __tablename__ = "cityweather"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(32))  # 地名
    city_num = db.Column(db.String(32))  # 地名编号
    temperature = db.Column(db.String(32))  # 温度
    humidity = db.Column(db.String(32))  # 湿度
    wind = db.Column(db.String(32))  # 风向风力
    aqi = db.Column(db.String(32))  # 空气指数
    create_datetime = db.Column(db.DATETIME, default=datetime.now)


class Machine(db.Model):
    """机器状态信息"""
    __tablename__ = "machine"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    platform = db.Column(db.String(128))
    version = db.Column(db.String(128))
    comment = db.Column(db.String(256))  # 备注
    create_datetime = db.Column(db.DATETIME, default=datetime.now)
