# -*- coding:utf-8 -*-
#Time:2017-4-27
#
#author:LiMing

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://liming:#123qweasdZ@192.168.1.161:3306/auto_web'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

