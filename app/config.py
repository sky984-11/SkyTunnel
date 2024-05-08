"""
@ Date: 2024-04-26 15:31:44
@ LastEditors: liupeng
@ LastEditTime: 2024-05-08 09:59:11
@ FilePath: /SkyTunnel/app/config.py
@ Desc: 
"""
import json

config_data = None
with open('../Setting.json', 'r') as f:
    config_data = json.load(f)


class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    static_folder='./static'
 
 
class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = config_data.get('sqlite_url' )
    # 这里填写自己的服务端地址
    SERVER_NAME=config_data.get('backend_ip')
    DEBUG=True

 
class DefaultConfig(BaseConfig):
    API_VERSION=config_data.get('api_version')
    