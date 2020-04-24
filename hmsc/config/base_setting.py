SERVER_PORT = 9000
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Myp199706@127.0.0.1/hmsc_db?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False  # 关闭了对模型的监控

# Cookie
AUTH_COOKIE_NAME = 'hmsc'

# 设置拦截器规则
IGNORE_URLS = [
    '^/user/login'
]

IGNORE_CHECK_LOGIN_URLS = [
    '^/static'
    '^/favicon.ico'
]