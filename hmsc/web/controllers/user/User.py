import json

from flask import Blueprint, render_template, request, jsonify, make_response
from common.models.user import User
from common.libs.user.UserService import UserService


route_user = Blueprint('user_page', __name__)


@route_user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':

        return render_template('user/login.html')

    resp = {
        'code': 200,
        'msg': '登陆成功 @!@ ',
        'data':{}
    }
    req = request.values
    login_name = req['login_name']if 'login_name' in req else ''
    login_pwd = req['login_pwd']if 'login_pwd' in req else ''

    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名'
        return jsonify(resp)
    if login_pwd is None or len(login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的密码'
        return jsonify(resp)
    user_info = User.query.filter_by(login_name=login_name).first()
    print(user_info)
    if not user_info:
        resp['code'] = -1
        resp['msg'] = '用户不存在'
        return jsonify(resp)
    # 判断密码
    if user_info.login_pwd != UserService.generatePwd(login_pwd, user_info.login_salt):
        resp['code'] = -1
        resp['msg'] = '密码输入错误'
        return jsonify(resp)

    # 判断用户状态
    if user_info.status != 1:
        resp['code'] = -1
        resp['msg'] = '用户已经被禁用，请与管理员联系'
        return jsonify(resp)

    # 加入cookie 状态
    response = make_response(json.dumps({'code': 200, "msg": '登陆成功~~~'}))
    # Cookie 中存入的信息是 user_info.login_name, user_info.uid
    response.set_cookie('hmsc_1901C', '%s@%s'%(UserService.generateAuthCode(user_info), user_info.uid), 60*60*25*15)

    return response




@route_user.route('/edit')
def edit():

    return '编辑'


@route_user.route('/logout')
def logout():

    return '登出'

@route_user.route('/reset-pwd')
def resetpwd():

    return '重置密码'
