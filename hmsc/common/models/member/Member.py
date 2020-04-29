# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
from application import db



class Member(db.Model):
    __tablename__ = 'member'

    id = db.Column(db.Integer, primary_key=True, info='用户id')
    nickname = db.Column(db.String(100), nullable=False, info='会员昵称')
    mobile = db.Column(db.String(20), nullable=False, info='会员手机号码')
    sex = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1：男  2：女 0 ：没有填写')
    avatar = db.Column(db.String(64), nullable=False, info='会员头像')
    salt = db.Column(db.String(32), nullable=False, info='登录密码的随机秘钥')
    reg_ip = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='注册ip')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1:有效 2：无效')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最后一次更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
