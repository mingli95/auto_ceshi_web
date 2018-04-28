# -*- coding:utf-8 -*-
#Time:2017-4-27
#
#author:LiMing

from flask import Blueprint,render_template,request,redirect,url_for
import json
from config import db
from module import casesList,apiList,parameters
from sqlalchemy import or_,and_

task = Blueprint('task',__name__)

@task.route('/addTask',methods=['POST','GET'])
def addTask():
    if request.method == 'GET':
        case_id = request.args.get('case_id')
        print(case_id)
        return render_template("add_task.html")



