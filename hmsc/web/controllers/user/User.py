from flask import Blueprint, request, jsonify, make_response, redirect, g

from application import app, db
from common.models.user import User
from common.libs.user.UserService import UserService
from common.libs.UrlManager import UrlManager
from common.libs.Helper import ops_render

import json

router_user = Blueprint('user_page', __name__)


@router_user.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if g.current_user:
            return redirect(UrlManager.buildUrl("/"))
        return ops_render("user/login.html")

    # POST请求
    resp = {
        'code': 200,
        'msg': '登录成功',
        'data': {}
    }
    req = request.values

    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的用户名"
        return jsonify(resp)
    if login_pwd is None or len(login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的密码"
        return jsonify(resp)
    # 从数据库中取出user
    user_info = User.query.filter_by(login_name=login_name).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = "用户不存在"
        return jsonify(resp)
    # 判断密码
    if user_info.login_pwd != UserService.generatePwd(login_pwd, user_info.login_salt):
        resp['code'] = -1
        resp['msg'] = "密码输入错误"
        return jsonify(resp)

    # 判断用户状态
    if user_info.status != 1:
        resp['code'] = -1
        resp['msg'] = "用户已经被禁用，请联系管理员处理"
        return jsonify(resp)

    response = make_response(json.dumps({'code': 200, 'msg': '登录成功~~~'}))
    # Cookie中存入的信息是user_info.uid,user_info
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], "%s@%s" % (UserService.generateAuthCode(user_info), user_info.uid), 60 * 60 * 24 * 15)
    return response


@router_user.route("/logout")
def logout():
    return "登出"


@router_user.route("/edit", methods=['GET', 'POST'])
def edit():
    return ops_render("user/edit.html")


@router_user.route("/reset-pwd", methods=['GET', 'POST'])
def resetPwd():

    # GET请求
    if request.method == 'GET':
        return ops_render("user/reset_pwd.html")

    # POST请求
    resp = {
        'code': 200,
        'msg': '修改密码成功',
        'data': {}
    }

    req = request.values
    # print('打印', req)
    old_pwd = req['old_pwd']if 'old_pwd' in req else ''
    new_pwd = req['new_pwd']if 'new_pwd' in req else ''
    # print('旧密码',old_pwd)
    # print('新密码',new_pwd)

    # 判断原密码和新密码是否输入
    if old_pwd is None or len(old_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入原密码！"
        return jsonify(resp)
    if new_pwd is None or len(new_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入新密码！'
        return jsonify(resp)

    # 判断旧密码是与当前用户的密码一致
    user_old = g.current_user.login_pwd
    print('老旧密码', user_old)
    user_pwd = UserService.generatePwd(old_pwd, g.current_user.login_salt)
    print('原密码', user_pwd)
    # 判断密码
    if g.current_user.login_pwd != UserService.generatePwd(old_pwd, g.current_user.login_salt):
        resp['code'] = -1
        resp['msg'] = "原密码输入错误！无法修改"
        return jsonify(resp)

    # 判断新密码是与当前用户的密码一致
    if UserService.generateCreatePwd(new_pwd, g.current_user) == UserService.generatePwd(old_pwd, g.current_user.login_salt):
        resp['code'] = -1
        resp['msg'] = '修改后的密码与原密码相同无需修改 ^！^'

    g.current_user.login_pwd = UserService.generateCreatePwd(new_pwd, g.current_user)
    db.session.add(g.current_user)
    db.session.commit()

    response = make_response(json.dumps({'code': 200, 'msg': '密码修改成功！~~~'}))
    # 修改完密码之后 删除原来的Cookie值  返回登录页面用户重新登录
    # response.set_cookie(app.config['AUTH_COOKIE_NAME'],"%s@%s" % (UserService.generateAuthCode(g.current_user), g.current_user.uid), 60 * 60 * 24 * 15)
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
    return response