#!/usr/bin/env python
#_*_coding:utf-8_*_
import os
import sys
#程序文件主目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#添加环境变量
sys.path.append(BASE_DIR)
#数据库信息
DATABASE = dict(engineer="file",dbpath=os.path.join(BASE_DIR,"database"),tables={"user":"user"})
#日志文件存放路径
LOG_PATH = os.path.join(BASE_DIR,"logs")


