#!/usr/bin/env python
#_*_coding:utf-8_*_

from ChengduLab.modules.common import write_error_log
import json
                
def load_data_from_db(tablename):
    '''
    从指定的数据表中获取所有数据，通过json方式将数据返回
    :param tablename:数据文件名
    :return:返回所有结果
    '''
    try:
        with open(tablename,'r+') as f:
            return json.load(f)
    except Exception as e:
        write_error_log(e)
        
