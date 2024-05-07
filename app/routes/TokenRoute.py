"""
@ Date: 2024-04-29 16:08:39
@ LastEditors: error: git config user.name & please set dead value or install git
@ LastEditTime: 2024-04-30 15:36:52
@ FilePath: /SkyTunnel/app/routes/TokenRoute.py
@ Desc: 
"""
from public.user.auth import *
from flask import request, jsonify,send_file
from db import User,db
from run import app

def get_token():
    """
    生成授权凭证
    ---
    tags:
      - token
    parameters:
      - in: body
        name: body
        required: true
        schema:
          properties:
            username:
              type: string
              description: 用户名
              required: true
            password:
              type: string
              description: 用户密码
              required: true
            exp:
              type: number
              description: 过期时间
    responses:
      200:
        description: 成功
      400:
        description: 用户名和密码不能为空
      404:
        description: 用户不存在
      405:
        description: 密码错误
    """
    json_data = request.get_json()
    username = json_data.get('username')
    password = json_data.get('password')
    exp = json_data.get('exp')
    
    if not username or not password:
        return jsonify({'msg': '用户名和密码不能为空', 'code': 400}), 400
    with app.app_context():
      user = User.query.filter_by(username=username).first()
      if not user:
        return jsonify({"code": 404, "msg": "用户不存在"}), 404
      if not user.verify_password(password):
        return jsonify({"code": 405, "msg": "密码错误"}), 405

      encoded_jwt = generate_token(username, password, exp) if exp else generate_token(username, password)
      return jsonify({'msg': {'token':encoded_jwt},'code':200})