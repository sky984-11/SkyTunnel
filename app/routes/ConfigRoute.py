"""
@ Date: 2024-04-26 15:31:44
@ LastEditors: error: git config user.name & please set dead value or install git
@ LastEditTime: 2024-05-06 10:57:40
@ FilePath: /SkyTunnel/app/routes/ConfigRoute.py
@ Desc: 
"""
from flask import request, jsonify
from run import app
from config import ProductionConfig
from db import  db,User

import json,os

from public.user.auth import *



def get_server():
    """
    获取服务器信息
    ---
    tags:
      - config
    parameters:
      - in: header
        name: Authorization
        type: string
        required: true
        description: 授权凭证
    responses:
      200:
        description: 成功
      401:
        description: token未授权或过期
      404:
        description: 授权用户用户不存在
    """

    token = request.headers.get('Authorization')

    if not token:
        return jsonify({'msg': 'token未授权或过期','code':401}),401

    data = decode_token(token)
    if 'error' in data:
        return jsonify({'msg': 'token未授权或过期','code':401}),401


    username = data['username']
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({"code": 404, "msg": "授权用户用户不存在"}), 404

    ip = ProductionConfig.SERVER_NAME.split(':')[0]
    port = int(ProductionConfig.SERVER_NAME.split(':')[1])
    return jsonify({'msg': {'ip':ip,'port':port},'code':200})