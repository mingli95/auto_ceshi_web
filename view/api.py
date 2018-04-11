# -*- coding:utf-8 -*-
#Time:2017-4-27
#
#author:LiMing

from flask import Blueprint,render_template,request
import json
from config import db
from module import apiList
from sqlalchemy import or_,and_

api = Blueprint('api',__name__)

@api.route('/apiZhdq',methods=['POST','GET'])
def apiZhdq():
    return render_template("api_zhdq.html")

@api.route('/apiZysyCjd',methods=['POST','GET'])
def apiZysyCjd():
    return render_template("api_zysy_cjd.html")

@api.route('/apiZysyQyd',methods=['POST','GET'])
def apiZysyQyd():
    return render_template("api_zysy_qyd.html")

@api.route('/apiList',methods=['POST'])
def api_list():
    if request.method == 'POST':
        req = request.get_json()
        project_id = req['project_id']
        pp = db.session.query(apiList).filter(apiList.project_id==project_id).all()
        data = []
        for i in pp:
            api_dict = {}
            api_dict['id']=i.id
            api_dict['title']=i.title
            api_dict['url']=i.url
            api_dict['status']=i.status
            api_dict['desc']=i.desc
            api_dict['request_type']=i.request_type
            api_dict['last_update']=i.last_update.strftime('%Y-%m-%d %H:%M:%S')
            api_dict['project_id']=i.project_id
            data.append(api_dict)
        return json.dumps({"status":200,"message":"success!","data":data})

@api.route('/apiAdd',methods=['POST'])
def apiAdd():
    if request.method == 'POST':
        req = request.get_json()
        print(req)
        api_name = req['api_name']
        print(api_name)
        api_project_id = req['api_project_id']
        api_url = req['api_url']
        api_meta = req['api_meta']
        api_status = int(req['api_status'])
        api_desc = req['api_desc']
        try:
            db.session.add(apiList(title=api_name,url=api_url,status=api_status,desc=api_desc,request_type=api_meta,project_id=api_project_id))
            db.session.commit()
            return json.dumps({
                "status":200,
                "message":"success!"
            })
        except :
            return json.dumps({
                "status":500,
                "message":"error!"
            })




