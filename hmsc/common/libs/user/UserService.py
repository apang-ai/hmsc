import hashlib, base64
# from random import Random


# 获取由16位随机大小写字母、数字组成的new_salt值 获取new_salt值
# def create_salt(length=16):
#     new_salt = ''
#     chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
#     len_chars = len(chars) - 1
#     random = Random()
#     for i in range(length):
#         # 每次从chars中随机取一位
#         new_salt += chars[random.randint(0, len_chars)]
#
#     return new_salt

class UserService():

    @staticmethod
    # 结合salt 和 md5 生成新的密码
    def generatePwd(pwd, salt):

        m = hashlib.md5()
        str = '%s-%s'%(base64.encodebytes(pwd.encode('utf-8')), salt)
        m.update(str.encode('utf-8'))

        return m.hexdigest()

    # 对cookie中存储的信息进行加密
    @staticmethod
    def generateAuthCode(user_info=None):

        m = hashlib.md5()
        str = '%s-%s-%s-%s'%(user_info.uid, user_info.login_name, user_info.login_pwd, user_info.login_salt)
        m.update(str.encode('utf-8'))
        return m.hexdigest()

    # 创建新的加密密码
    @staticmethod
    def generateCreatePwd(new_pwd, user_obj):
        md5_obj = hashlib.md5()
        str = '%s-%s'%(base64.encodebytes(new_pwd.encode('utf-8')), user_obj.login_salt)
        md5_obj.update(str.encode('utf-8'))

        return md5_obj.hexdigest()
