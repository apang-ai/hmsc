# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
from application import db



class User(db.Model):
    __tablename__ = 'user'

    uid = db.Column(db.Integer, primary_key=True, info='用户id')
    nickname = db.Column(db.String(100), nullable=False, info='用户昵称')
    mobile = db.Column(db.String(20), nullable=False, info='手机号码')
    email = db.Column(db.String(100), nullable=False, info='用户邮箱')
    sex = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1：男  2：女 0 ：没有填写')
    avatar = db.Column(db.String(64), nullable=False, info='头像')
    login_name = db.Column(db.String(20), nullable=False, unique=True, info='登录用户名')
    login_pwd = db.Column(db.String(32), nullable=False, info='登录密码')
    login_salt = db.Column(db.String(32), nullable=False, info='登录密码的随机秘钥')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1:有效 2：无效')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最后一次更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
