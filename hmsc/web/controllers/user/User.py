from flask import Blueprint, render_template

route_user = Blueprint('user_page', __name__)


@route_user.route('/login')
def login():

    return render_template('user/login.html')


@route_user.route('/edit')
def edit():

    return '编辑'


@route_user.route('/logout')
def logout():

    return '登出'

@route_user.route('/reset-pwd')
def resetpwd():

    return '重置密码'
