# -*- coding:utf-8 -*-
#Time:2017-4-27
#
#author:LiMing

from flask import Blueprint,render_template,redirect,request
import json
from config import db
from module import parentProject,subProject

web = Blueprint('web',__name__)

@web.route('/',methods=['POST','GET'])
def index_root():
    return redirect("/index")

@web.route('/index',methods=['POST','GET'])
def index():
    return render_template('index.html',data=[])

@web.route('/menuList',methods=['POST','GET'])
def menu_list():
    if request.method == 'POST':
        req = request.get_json()
        print(type(req),req['menu_id'])
        pp = db.session.query(parentProject).filter(parentProject.menu_id==req['menu_id']).all()
        data = []
        sub_list = []

        for i in pp:
            pp_dict = {}
            pp_dict['pp_id'] = i.id
            pp_dict['name'] = i.name
            sub = db.session.query(subProject).filter(subProject.parent_project_id==i.id).all()
            if len(sub) == 0:
                pp_dict['sub'] = []
                data.append(pp_dict)
            else:
                for i in sub:
                    sub_dic = {}
                    print(i.id)
                    sub_dic['sub_id'] = i.id
                    sub_dic['sub_name'] = i.name
                    sub_dic['parent_project_id'] = i.parent_project_id
                    sub_list.append(sub_dic)
                pp_dict['sub'] = sub_list
                data.append(pp_dict)
    return json.dumps({"menu_id":req['menu_id'],"data":data})

