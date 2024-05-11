"""
@ Date: 2024-04-26 17:36:23
@ LastEditors: sky
@ LastEditTime: 2024-05-11 17:18:02
@ FilePath: /SkyTunnel/app/routes/luckyRoute.py
@ Desc: 
"""

from flask import request, jsonify
from run import app
from db import Tunner, db,User

from datetime import datetime

from public.user.auth import *



def sync_webhook():
    """
    通过lucky webhook同步数据
    ---
    tags:
      - lucky
    parameters:
      - in: header
        name: Authorization
        type: string
        required: true
        description: 授权凭证
      - in: body
        name: body
        required: true
        schema:
          properties:
            ip:
              type: string
              description: 公网ip
              required: true
            port:
              type: number
              description: 公网端口
              required: true
            rulename:
              type: string
              description: 服务名称
              required: true
            otime:
              type: string
              description: 触发webhook时间
    responses:
      200:
        description: 成功
      400:
        description: JSON数据格式错误,格式实例:{"msg":{"port":"#{port}", "ip":"#{ip}","rulename":"#{ruleName}","otime":"#{time}"}}
      401:
        description: token未授权或过期
      404:
        description: 授权用户用户不存在
      405:
        description: ip,port,rulename参数信息缺失
    """
    json_data = request.get_json()
    token = request.headers.get('Authorization')
    # print(json_data,token)
    # Content-Type: application/json
    # Authorization:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MzYwNjY4NDEuNDIzNzYxLCJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJhZG1pbiJ9.8nX9PaFZguUddH-StMEbpQYOeSW1PVE3jUhVvmNM_gc
    # {"msg":{"port":"#{port}", "ip":"#{ip}","rulename":"#{ruleName}","otime":"#{time}"}}
    if not json_data or 'msg' not in json_data:
        return jsonify({'msg': 'JSON数据格式错误,格式见错误代码','code':400}), 400

    if not token:
        return jsonify({'msg': 'token未授权或过期','code':401}),401

    token_dict = decode_token(token)

    if 'error' in token_dict:
        return jsonify({'msg': 'token未授权或过期','code':401}),401

    username = token_dict['username']
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({"code": 404, "msg": "授权用户用户不存在"}), 404

        user_id = user.user_id
        ip = json_data.get('msg').get('ip')
        port = json_data.get('msg').get('port')
        rulename = json_data.get('msg').get('rulename')
        otime = json_data.get('msg').get('otime')
        source = 'lucky'

        if not ip or not port or not rulename:
            return jsonify({'msg': 'ip,port,rulename参数信息缺失','code':405}),405

        
        tunner = Tunner.query.filter_by(name=rulename).first()

        if tunner:
            tunner.ip = ip
            tunner.port = port
            if otime:
                tunner.otime = datetime.strptime(otime , '%Y-%m-%d %H:%M:%S')
        else:
            tunner = Tunner(ip=ip, source=source, port=port, name=rulename, otime=datetime.strptime(otime , '%Y-%m-%d %H:%M:%S'),user_id=user_id) if otime else Tunner(ip=ip, source=source, port=port, name=rulename,user_id=user_id)
            db.session.add(tunner)
        db.session.commit()
        return jsonify({'msg': '成功', 'code': 200}), 200


def stunrule_list():
    """
    获取穿透规则列表
    ---
    tags:
      - lucky
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
        user_id = user.user_id
        stunrules = db.session.query(Tunner).filter_by(user_id=user_id).all()
        stunrule_list = [stunrule.to_dict() for stunrule in stunrules]
        return jsonify({"code": 200, "msg": stunrule_list})

def delete_stunrule(stun_id):
    """
    删除stun规则
    ---
    tags:
      - lucky
    parameters:
      - name: stun_id
        in: path
        type: string
        required: true
        description: 要删除的stun规则ID
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
        description: 规则不存在
      405:
        description: 授权用户不存在
      411:
        description: 要删除的数据不属于该授权凭证
      500:
        description: 服务端错误
    """

    token = request.headers.get('Authorization')

    if not token:
        return jsonify({'msg': 'token未授权或过期','code':401}),401

    data = decode_token(token)
    if 'error' in data:
        return jsonify({'msg': 'token未授权或过期','code':401}),401
        
    with app.app_context():
        try:
            tunner = Tunner.query.filter_by(id=stun_id).first()
            if not tunner:
                return jsonify({"code": 404, "msg": "规则不存在"}), 404

            username = data['username']
            user = User.query.filter_by(username=username).first()
            if not user:
                return jsonify({"code": 405, "msg": "授权用户不存在"}), 405

            user_id = user.user_id
            if user_id != tunner.user_id:
              return jsonify({"code": 411, "msg": "要删除的数据不属于该授权凭证"}), 411
            db.session.delete(tunner)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({"code": 500, "msg": str(e)}), 500

        return jsonify({"code": 200, "msg": f"规则删除成功"})

def edit_stunrule():
    """
    修改stun规则
    ---
    tags:
      - lucky
    parameters:
      - in: header
        name: Authorization
        type: string
        required: true
        description: 授权凭证
      - in: body
        name: body
        required: true
        schema:
          properties:
            domain:
              type: string
              description: 域名
              required: true
            suffix:
              type: string
              description: 访问地址后缀
              required: true
            id:
              type: number
              description: stun规则id
              required: true
    responses:
      200:
        description: 成功
      401:
        description: token未授权或过期
      404:
        description: 规则不存在
      405:
        description: 授权用户不存在
      411:
        description: 要修改的数据不属于该授权凭证
      500:
        description: 服务端错误
    """

    json_data = request.get_json()
    token = request.headers.get('Authorization')

    if not json_data:
        return jsonify({'msg': 'JSON数据格式错误','code':400}), 400
        
    if not token:
        return jsonify({'msg': 'token未授权或过期','code':401}),401

    data = decode_token(token)
    if 'error' in data:
        return jsonify({'msg': 'token未授权或过期','code':401}),401
        
    with app.app_context():
        try:
            username = data['username']
            user = User.query.filter_by(username=username).first()
            if not user:
                return jsonify({"code": 405, "msg": "授权用户不存在"}), 405
            user_id = user.user_id


            suffix = json_data.get('suffix')
            domain = json_data.get('domain')
            https = json_data.get('https')
            stun_id = json_data.get('id')
            tunner = Tunner.query.filter_by(id=stun_id).first()

            if user_id != tunner.user_id:
              return jsonify({"code": 411, "msg": "要修改的数据不属于该授权凭证"}), 411
              
            tunner.suffix = suffix
            tunner.domain = domain
            tunner.https = https
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({"code": 500, "msg": str(e)}), 500

        return jsonify({"code": 200, "msg": '修改成功'})