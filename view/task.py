# -*- coding:utf-8 -*-
#Time:2017-4-27
#
#author:LiMing

from flask import Blueprint,render_template,request,redirect,url_for
import json
from config import db
from module import taskPlan,taskCase
from sqlalchemy import or_,and_

task = Blueprint('task',__name__)

@task.route('/task',methods=['POST','GET'])
def taskList():
    data = db.session.query(taskPlan).all()
    print(data)
    return render_template("task.html",data=data)

@task.route('/getCaseList',methods=['POST','GET'])
def getCaseList():
    if request.method == 'GET':
        data = request.args.get('caselist')
        data=json.loads(data)
        print(data['caselist'])
        return render_template("add_task.html",caselist=data['caselist'])

@task.route('/addTask',methods=['POST','GET'])
def addTask():
    if request.method == 'POST':
        req = request.get_json()
        print(req)
        taskName= req['task_title']
        startTime= req['start_time']
        endTime= req['end_time']
        interval= req['interval']
        desc= req['task_desc']
        task_plan= taskPlan(name=taskName,start_time=startTime,end_time=endTime,interval=interval,desc=desc)
        db.session.add(task_plan)
        db.session.commit()
        task_id = task_plan.id
        for i in req['caseList']:
            caseName=i['title']
            caseId= i['id']
            order= i['order']
            task_case = taskCase(task_id=task_id,case_id=caseId,case_name=caseName,order=order)
            db.session.add(task_case)
            db.session.commit()
        return json.dumps({"status":200,'message':'success!'})


