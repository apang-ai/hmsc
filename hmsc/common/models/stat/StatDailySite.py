# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Float, Integer
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
from application import db



class StatDailySite(db.Model):
    __tablename__ = 'stat_daily_site'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, index=True, info='日期')
    total_pay_money = db.Column(db.Float(10), nullable=False, info='当日收入总数')
    total_member_count = db.Column(db.Integer, nullable=False, info='会员总数')
    total_new_member_count = db.Column(db.Integer, nullable=False, info='当日新增会员数')
    total_order_count = db.Column(db.Integer, nullable=False, info='当日订单总数')
    total_shared_count = db.Column(db.Integer, nullable=False, info='分享总数')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最近更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='插入时间')
