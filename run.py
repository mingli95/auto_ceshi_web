# -*- coding:utf-8 -*-
#Time:2017-4-27
#
#author:LiMing
from flask import Flask
from view.index import web
from view.api import api

##注册蓝图
app = Flask(__name__)
app.register_blueprint(web)
app.register_blueprint(api)



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)