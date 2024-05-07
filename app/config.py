"""
@ Date: 2024-04-26 15:31:44
@ LastEditors: error: git config user.name & please set dead value or install git
@ LastEditTime: 2024-04-30 10:59:58
@ FilePath: /SkyTunnel/app/config.py
@ Desc: 
"""

class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    static_folder='./static'
 
 
class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite://///home/ubuntu/SkyTunnel/app/SkyTunnel.db' 
    SERVER_NAME="113.31.114.236:5001"
    DEBUG=True

 
class DefaultConfig(BaseConfig):
    API_VERSION = 'v1'
    