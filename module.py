# -*- coding:utf-8 -*-
#Time:2017-4-27
#
#author:LiMing

from config import db
import datetime

# 菜单表
class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    menu_id = db.Column(db.Integer,unique=True)
    name = db.Column(db.String(50))
    last_update = db.Column(db.DATETIME,default=datetime.datetime.now())
    is_deleted = db.Column(db.BOOLEAN,default=False)

# 菜单一级项目
class parentProject(db.Model):
    __tablename__ = 'parent_project'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))
    menu_id = db.Column(db.Integer,db.ForeignKey('menu.menu_id'))
    menu = db.relationship('Menu',backref=db.backref('parent_project', lazy='dynamic'))
    last_update = db.Column(db.DATETIME,default=datetime.datetime.now())
    is_deleted = db.Column(db.BOOLEAN,default=False)

# 菜单二级和多级项目
class subProject(db.Model):
    __tablename__ = 'sub_project'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))
    parent_project_id = db.Column(db.Integer,db.ForeignKey('parent_project.id'))
    parent_project = db.relationship('parentProject',backref=db.backref('sub_project', lazy='dynamic'))
    last_update = db.Column(db.DATETIME,default=datetime.datetime.now())
    is_deleted = db.Column(db.BOOLEAN,default=False)


# Api表
class apiList(db.Model):
    __tablename__ = 'api_list'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(50),unique=True)
    url = db.Column(db.String(50))
    status = db.Column(db.BOOLEAN,default=True)
    desc = db.Column(db.TEXT)
    request_type = db.Column(db.String(20))
    last_update = db.Column(db.DATETIME,default=datetime.datetime.now())
    is_deleted = db.Column(db.BOOLEAN,default=False)
    project_id = db.Column(db.String(50))


# 服务器信息表
class server(db.Model):
    __tablename__ = 'server'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50),unique=True)
    ip = db.Column(db.String(50))
    port = db.Column(db.String(50))
    status = db.Column(db.BOOLEAN,default=True)
    desc = db.Column(db.TEXT)
    last_update = db.Column(db.DATETIME,default=datetime.datetime.now())
    is_deleted = db.Column(db.BOOLEAN,default=False)

# 用例表
class casesList(db.Model):
    __tablename__ = 'cases_list'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(50),unique=True)
    status = db.Column(db.BOOLEAN,default=True)
    desc = db.Column(db.TEXT)
    last_update = db.Column(db.DATETIME,default=datetime.datetime.now())
    is_deleted = db.Column(db.BOOLEAN,default=False)
    server_id = db.Column(db.Integer,db.ForeignKey('server.id'))
    server = db.relationship('server',backref=db.backref('cases_list', lazy='dynamic'))
    project_id = db.Column(db.String(50))
    count = db.Column(db.Integer,default=1)


# 参数表
class parameters(db.Model):
    __tablename__ = 'parameters'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    order = db.Column(db.Integer)
    req = db.Column(db.TEXT)
    ast = db.Column(db.TEXT)
    out_param = db.Column(db.TEXT)
    last_update = db.Column(db.DATETIME,default=datetime.datetime.now())
    is_deleted = db.Column(db.BOOLEAN,default=False)
    case_id = db.Column(db.Integer,db.ForeignKey('cases_list.id'))
    api_id = db.Column(db.Integer,db.ForeignKey('api_list.id'))
    cases_list = db.relationship('casesList',backref=db.backref('parameters', lazy='dynamic'))
    api_list = db.relationship('apiList',backref=db.backref('parameters', lazy='dynamic'))

class taskPlan(db.Model):
    __tablename__ = 'task_plan'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50),unique=True)
    start_time = db.Column(db.DATETIME)
    end_time = db.Column(db.DATETIME)
    interval = db.Column(db.String(50))
    desc = db.Column(db.TEXT)
    last_update = db.Column(db.DATETIME,default=datetime.datetime.now())
    is_deleted = db.Column(db.BOOLEAN,default=False)

class taskCase(db.Model):
    __tablename__ = 'task_case'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    code = db.Column(db.Integer)
    response = db.Column(db.TEXT)
    task_id = db.Column(db.Integer,db.ForeignKey('task_plan.id'))
    case_id = db.Column(db.Integer,db.ForeignKey('cases_list.id'))
    task_plan = db.relationship('taskPlan',backref=db.backref('task_case', lazy='dynamic'))
    cases_list = db.relationship('casesList',backref=db.backref('task_case', lazy='dynamic'))
    last_update = db.Column(db.DATETIME,default=datetime.datetime.now())
    is_deleted = db.Column(db.BOOLEAN,default=False)

class report(db.Model):
    __tablename__ = 'report'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    case_num = db.Column(db.Integer)
    success_num = db.Column(db.Integer)
    fail_num = db.Column(db.Integer)
    success_rate = db.Column(db.String(50))
    task_id = db.Column(db.Integer,db.ForeignKey('task_case.id'))
    task_case = db.relationship('taskCase',backref=db.backref('report', lazy='dynamic'))
    last_update = db.Column(db.DATETIME,default=datetime.datetime.now())
    is_deleted = db.Column(db.BOOLEAN,default=False)


if __name__ == '__main__':
    # 删除旧的表
    db.drop_all()
    db.create_all()
    # 初始化数据
    db.session.add(Menu(menu_id = 10010,name="Api列表"))
    db.session.add(Menu(menu_id = 10020,name="用例列表"))
    db.session.add(Menu(menu_id = 10030,name="服务器列表"))
    db.session.add(parentProject(id = 1,menu_id = 10010,name="智慧地球"))
    db.session.add(parentProject(id = 2,menu_id = 10010,name="中药溯源"))
    db.session.add(parentProject(id = 3,menu_id = 10020,name="智慧地球"))
    db.session.add(parentProject(id = 4,menu_id = 10020,name="中药溯源"))
    db.session.add(parentProject(id = 5,menu_id = 10030,name="智慧地球"))
    db.session.add(parentProject(id = 6,menu_id = 10030,name="中药溯源"))

    db.session.commit()
    # api列表菜单
    db.session.add(subProject(id = 1,name = "采集端",parent_project_id = 2))
    db.session.add(subProject(id = 2,name = "企业端",parent_project_id = 2))
    # 用例列表菜单

    db.session.add(subProject(id = 3,name = "采集端",parent_project_id = 4))
    db.session.add(subProject(id = 4,name = "企业端",parent_project_id = 4))
    # 服务器列表菜单

    db.session.add(subProject(id = 5,name = "采集端",parent_project_id = 6))
    db.session.add(subProject(id = 6,name = "企业端",parent_project_id = 6))
    db.session.commit()
