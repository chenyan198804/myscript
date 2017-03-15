#!/usr/bin/env python
#_*_coding:utf-8_*_

#初始化用户数据表 user_list.db
from ChengduLab.database.userlist import _user_list
from ChengduLab.conf import settings
from ChengduLab.modules import common
import os
import json
import  sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

def init_db_user():
    _db_file = os.path.join(settings.DATABASE['dbpath'],"user.db")
    with open(_db_file,"w+") as fp:
        for k,v in _user_list.items():
            #对用户设置密码
            tmppassword = _user_list['password']
            #对密码进行加密
            encrypassword = common.encrypt(tmppassword)
            #修改明文密码
            _user_list['password']=encrypassword
        fp.write(json.dumps(_user_list))     
           
def init_database(): 
    tables = list(settings.DATABASE['tables'].values())#数据表名称列表
    database = settings.DATABASE['dbpath'] #数据表存放路径
    for _table in tables:
        #如果表不存在
        if not os.path.exists(os.path.join(database,"{0}.db".format(_table))):
            print("Table {0}.db create successfull".format(_table))
            
        if hasattr(sys.modules[__name__],"init_db_{0}".format(_table)):
            init_func = getattr(sys.modules[__name__],"init_db_{0}".format(_table))
            init_func()

        else:
            common.write_error_log("init table {0} failed, no function init_db_{0} found".format(_table))

if __name__ == "__main__":
    init_database()
