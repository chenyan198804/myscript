#!/usr/bin/env python
#_*_coding:utf-8_*_
from ChengduLab.modules.admin import Admin
from ChengduLab.database import init_db 
if __name__ == "__main__":
    init_db.init_database()
    
    admin = Admin()
    login = admin.login()