# -*- coding:utf-8 -*-
#Time:2017-4-27
#
#author:LiMing

from flask import Blueprint,render_template,request,redirect,url_for
import json
from config import db
from module import casesList,apiList,parameters
from sqlalchemy import or_,and_


case = Blueprint('case',__name__)

@case.route('/caseZhdq',methods=['POST','GET'])
def caseZhdq():
    return render_template("case_zhdq.html")

@case.route('/caseZysyCjd',methods=['POST','GET'])
def caseZysyCjd():
    return render_template("case_zysy_cjd.html")

@case.route('/caseZysyQyd',methods=['POST','GET'])
def caseZysyQyd():
    return render_template("case_zysy_qyd.html")

@case.route('/addCase',methods=['POST','GET'])
def addCase():
    if request.method == 'GET':
        pro_id = request.args.get('pro_id')
        pro_name = request.args.get('pro_name')
        case_url = request.args.get('case_url')
        pp = db.session.query(apiList).filter(and_(apiList.is_deleted==0,apiList.status==1)).all()
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
        return render_template("add_case.html",pro_id=pro_id,pro_name=pro_name,data=data,url_path="/%s"%case_url)

@case.route('/caseSubmit',methods=['POST'])
def caseSubmit():
    if request.method == 'POST':
        data = request.get_json()
        if not data['apiList']:
            return json.dumps({'status':500,'message':"请选择用例关联的API接口!"})
        title = data['title']
        project_id = data['project_id']
        server_id = data['server_id']
        status = int(data['status'])
        desc = data['desc']
        cases_list = casesList(title=title,project_id=project_id,server_id=server_id,status=status,desc=desc)
        db.session.add(cases_list)
        db.session.commit()
        case_id = cases_list.id
        for i in data['apiList']:
            print(i)
            api_id=i['api_id']
            order=i['order']
            req=str(i['request'])
            ast=str(i['assert']) or "null"
            out_param=str(i['out_param']) or "null"
            param=parameters(case_id=case_id,api_id=api_id,order=order,req=req,ast=ast,out_param=out_param)
            db.session.add(param)
            db.session.commit()
        return json.dumps({"status":200,'message':'success!'})

@case.route('/caseList',methods=['POST'])
def caseList():
    if request.method == 'POST':
        req = request.get_json()
        try:
            project_id = req['project_id']
            case_title = req['title'] or "null"
        except KeyError:
            return json.dumps({"status":500,"message":"project_id is not exists!"})
        if case_title != "null":
            pp = db.session.query(casesList).filter(and_(casesList.project_id==project_id,casesList.title==case_title)).all()
        else:
            pp = db.session.query(casesList).filter(and_(casesList.project_id==project_id)).all()
        data = []
        for i in pp:
            dict = {}
            dict['id']=i.id
            dict['title']=i.title
            dict['project_id']=i.project_id
            dict['status']=i.status
            dict['desc']=i.desc
            dict['server_id']=i.server_id
            dict['count']=i.count
            dict['last_update']=i.last_update.strftime('%Y-%m-%d %H:%M:%S')
            data.append(dict)
        return json.dumps({"status":200,"message":"success!","data":data})