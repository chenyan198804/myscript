#!/usr/bin/env python
#_*_coding:utf-8_*_
import hashlib
import datetime
import os
import logging
from ChengduLab.conf import settings
def encrypt(string):
    '''
    字符串加密函数
    :param string:待加密的字符串
    :return:返回加密过的字符串
    '''
    ha = hashlib.md5(b'oldboy')
    ha.update(string.encode('utf-8'))
    result = ha.hexdigest()
    return result

def write_error_log(content):
    '''
    写入错误日志
    :param content:日志信息
    :return: 无返回，写入文件error.log
    '''
    _content = "\n{0}:{1}".format(datetime.datetime.now().strftime("%Y-%m-%d %X"), content)
    _filename = os.path.join(settings.LOG_PATH,"errlog.log")
    with open(_filename,"a+") as fa:
        fa.write(_content)
        