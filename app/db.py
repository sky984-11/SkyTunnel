"""
@ Date: 2024-04-26 16:54:11
@ LastEditors: sky
@ LastEditTime: 2024-05-08 10:11:16
@ FilePath: /SkyTunnel/app/db.py
@ Desc: 
"""


from run import app
import datetime
from sqlalchemy.orm import relationship, backref
from flask_sqlalchemy import SQLAlchemy

from passlib.apps import custom_app_context as pwd_context

# 加载数据库
db = SQLAlchemy(app)

class User(db.Model):
    """
        用户表
        user_id:主键，自动递增的整数。
        username:登陆账户，可以为手机号或者邮箱
        password:md5密码加密字符串
        nickname:用户昵称，可为空。
        avatar:用户头像的文件名称。可为空。
        qq:用户的QQ号码,可为空。
        role:用户角色，默认用户。(admin,user)。
        ctime:记录时间，采用 TIMESTAMP 类型，采用当前时间。
        utime:最后一次更新的时间，不可为空。
        token:授权凭证,可为空。
        oauth_secret:OAuth 客户端密钥,可为空。
        oauth_id:OAuth 客户端id,可为空。
    """
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    # nullable是否为空，unique唯一约束
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=True, unique=True)
    password = db.Column(db.String(150), nullable=True)
    nickname = db.Column(db.String(50), nullable=True)
    avatar = db.Column(db.String(50), nullable=True)
    qq = db.Column(db.String(100), nullable=True)
    role = db.Column(db.String(250), default='user')
    ctime = db.Column(db.DateTime, default=datetime.datetime.now)
    utime = db.Column(db.DateTime, nullable=False)
    token = db.Column(db.String(255), nullable=True)
    oauth_secret = db.Column(db.String(255), nullable=True)
    oauth_id = db.Column(db.String(255), nullable=True)

    records = relationship('Tunner', backref='tunner',cascade='all,delete-orphan')

    def hash_password(self, password):  # 给密码加密方法
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):  # 验证密码方法
        return pwd_context.verify(password, self.password)
    
class Tunner(db.Model):
    """
        穿透信息表
        ip:动态公网ip
        port:动态公网端口
        ctime:数据创建时间
        otime:触发webhook时间
        name:项目名称
        souce:数据来源
        suffix:访问地址后缀
        domain:域名
    """
    __tablename__ = 'tunner'
    __table_args__ = {'extend_existing': True}
    # nullable是否为空，unique唯一约束
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(20), nullable=False)
    source = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    suffix = db.Column(db.String(255), nullable=True)
    domain = db.Column(db.String(255), nullable=True)
    ctime = db.Column(db.DateTime, default=datetime.datetime.now)
    otime = db.Column(db.DateTime, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.user_id', ondelete='CASCADE'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "ip": self.ip,
            "port": self.port,
            "name": self.name,
            "source": self.source,
            "ctime": self.ctime.strftime("%Y年%m月%d日 %H:%M:%S"),
            "otime": self.otime.strftime("%Y年%m月%d日 %H:%M:%S"),
            "suffix":self.suffix,
            "source":self.source,
            "domain":self.domain
        }




with app.app_context():
    db.create_all()
# 删除表
# db.drop_all()
