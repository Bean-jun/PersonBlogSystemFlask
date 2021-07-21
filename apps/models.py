from apps import db
from werkzeug.security import generate_password_hash, check_password_hash


class UserInfo(db.Model):
    """用户表"""
    __tablename__ = "userinfo"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(32), unique=True, nullable=False)
    pwd = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return self.username
