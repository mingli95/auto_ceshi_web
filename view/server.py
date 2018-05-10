# -*- coding:utf-8 -*-
#Time:2017-4-27
#
#author:LiMing

from flask import Blueprint,render_template,request,redirect,url_for
import json
from config import db
from module import server
from sqlalchemy import or_,and_

ser = Blueprint('ser',__name__)

@ser.route('/serverList',methods=['POST','GET'])
def serverList():
    if request.method == 'POST':
        s = db.session.query(server).all()
        data = []
        for i in s:
            ser_dict = {}
            ser_dict['id']=i.id
            ser_dict['name']=i.name
            ser_dict['ip']=i.ip
            ser_dict['port']=i.port
            ser_dict['desc']=i.desc
            ser_dict['status']=i.status
            ser_dict['last_update']=i.last_update.strftime('%Y-%m-%d %H:%M:%S')
            data.append(ser_dict)
        if data:
            return json.dumps({"status":200,"message":"success!","data":data})
        else:
            return json.dumps({"status":500,"message":"data Error!"})

@ser.route('/server',methods=['POST','GET'])
def serverL():
    data = db.session.query(server).all()
    return render_template('server.html',data=data)