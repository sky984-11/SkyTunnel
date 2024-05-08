"""
@ Date: 2024-04-26 15:31:44
@ LastEditors: liupeng
@ LastEditTime: 2024-05-08 08:59:13
@ FilePath: /SkyTunnel/app/config.py
@ Desc: 
"""

class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    static_folder='./static'
 
 
class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite://///home/ubuntu/SkyTunnel/app/SkyTunnel.db' 
    # 这里填写自己的服务端地址
    SERVER_NAME="127.0.0.1:5001"
    DEBUG=True

 
class DefaultConfig(BaseConfig):
    API_VERSION = 'v1'
    