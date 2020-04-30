# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
from application import db



class Goods(db.Model):
    __tablename__ = 'goods'

    id = db.Column(db.Integer, primary_key=True)
    cat_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='分类id')
    name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='商品名称')
    price = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue(), info='商品价格')
    main_image = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='商品图片')
    summary = db.Column(db.String(10000), nullable=False, server_default=db.FetchedValue(), info='商品描述')
    stock = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='库存数')
    tags = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='tag 标签，用“,”连接')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1:有效，0：无效')
    month_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='月销量')
    total_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='总销量')
    view_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='总浏览次数')
    comment_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='总评论数')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最后一次更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
