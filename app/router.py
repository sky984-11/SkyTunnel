"""
@ Date: 2024-04-26 15:31:44
@ LastEditors: sky
@ LastEditTime: 2024-05-08 10:11:21
@ FilePath: /SkyTunnel/app/router.py
@ Desc: 
"""


from flask_cors import CORS
from flask import Blueprint

from routes.UserRoute import *
from routes.ConfigRoute import *
from routes.luckyRoute import *
from routes.TokenRoute import *

from config import DefaultConfig


# 创建蓝图
b1 = Blueprint('b1', __name__)
# 解决跨域问题
CORS(b1)


##################################### token start #####################################
# 获取server url地址
b1.route(f'/api/{DefaultConfig.API_VERSION}/token/get', methods=['POST'])(get_token)

#####################################  token end  #####################################

##################################### config start #####################################
# 获取server url地址
b1.route(f'/api/{DefaultConfig.API_VERSION}/config/server/get', methods=['POST'])(get_server)

#####################################  config end  #####################################

##################################### User start #####################################
# 新用户注册
b1.route(f'/api/{DefaultConfig.API_VERSION}/user/register', methods=['POST'])(register)
# 用户登录
b1.route(f'/api/{DefaultConfig.API_VERSION}/user/login', methods=['POST'])(login)
# 用户密码修改
b1.route(f'/api/{DefaultConfig.API_VERSION}/user/password/change', methods=['POST'])(change_password)
# 用户注销
b1.route(f'/api/{DefaultConfig.API_VERSION}/user/del/<int:user_id>', methods=['DELETE'])(delete_user)
# 用户退出
b1.route(f'/api/{DefaultConfig.API_VERSION}/user/logout', methods=['GET'])(logout)
# 用户随机头像
b1.route(f'/api/{DefaultConfig.API_VERSION}/user/image/random', methods=['GET'])(range_user_image)
# 查询某个用户信息
b1.route(f'/api/{DefaultConfig.API_VERSION}/user/info', methods=['POST'])(select_user_info)

# 用户头像上传
# b1.route(f'/api/{DefaultConfig.API_VERSION}/user/image/upload', methods=['POST'])(upload_image)
#####################################  User end  #####################################

##################################### lucky start #####################################

# lucky webhook数据同步
b1.route(f'/api/{DefaultConfig.API_VERSION}/lucky/webhook/sync', methods=['POST'])(sync_webhook)

# lucky stunrule列表
b1.route(f'/api/{DefaultConfig.API_VERSION}/lucky/stunrule/list', methods=['GET'])(stunrule_list)

# lucky 规则删除
b1.route(f'/api/{DefaultConfig.API_VERSION}/lucky/del/<int:stun_id>', methods=['DELETE'])(delete_stunrule)

# lucky 规则修改
b1.route(f'/api/{DefaultConfig.API_VERSION}/lucky/edit', methods=['POST'])(edit_stunrule)
#####################################  lucky end  #####################################



