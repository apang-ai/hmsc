# -*- coding: utf-8 -*-
from application import app
from flask import request, g, redirect

from common.models.user import (User)
from common.libs.user.UserService import (UserService)
from common.libs.UrlManager import (UrlManager)
import re

'''
判断用户是否已经登录
'''
def check_login():
    print('检查登陆')
    cookies = request.cookies.get(app.config['AUTH_COOKIE_NAME'])
    print('整体cookie', cookies)
    # auth_cookie = cookies[app.config['AUTH_COOKIE_NAME']] if app.config['AUTH_COOKIE_NAME'] in cookies else None
    # print('产生的cookie',auth_cookie)
    if cookies is None:
        return False

    auth_info = cookies.split("@")
    if len(auth_info) != 2:
        return False

    try:
        user_info = User.query.filter_by(uid=auth_info[1]).first()
    except Exception:
        return False

    if user_info is None:
        return False

    if auth_info[0] != UserService.generateAuthCode(user_info):
        return False

    if user_info.status != 1:
        return False
    print('最后',user_info)
    return user_info


@app.before_request
def before_request():
    print('开始')
    ignore_urls = app.config['IGNORE_URLS']
    ignore_check_login_urls = app.config['IGNORE_CHECK_LOGIN_URLS']
    path = request.path

    # 如果是静态文件就不要查询用户信息了
    pattern = re.compile('%s' % "|".join(ignore_check_login_urls))
    if pattern.match(path):
        return

    if '/api' in path:
        return

    user_info = check_login()
    print('名字',user_info)
    g.current_user = None
    if user_info:

        print('g', g.current_user)
        g.current_user = user_info

        print(g.current_user)

    pattern = re.compile('%s' % "|".join(ignore_urls))
    if pattern.match(path):
        return

    if not user_info:
        return redirect(UrlManager.buildUrl("/user/login"))

    return


