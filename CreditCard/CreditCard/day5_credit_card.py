#!/usr/bin/env python
#_*_coding:utf-8_*_
import os,sys

from datetime import date,datetime
from conf import template,errorcode
from conf import settings
from modules import shopping,common
from dbhelper import dbapi
from modules.users import Users
from modules.creditcard import CreditCard
from modules import report


def doshopping(userobj):
    '''
    购物商城模块，进行鼓舞部分的所有处理
    :param userobj:一个用户对象，如果用户未登陆，在支付模块会通过装饰器来登陆
    :return:
    '''
    
    #实例化商城
    shopobj = shopping.Shopping()
    exitflag = False
    while not exitflag:
        #开始菜单
        print(shopobj.welcome_meun)
        shop_classify_id = input('请选择商品分类编号[1-3]:').strip().lower()
        if not shop_classify_id:continue
        if shop_classify_id == '0':
            exitflag = True
            continue
        if int(shop_classify_id) not in range(1,6):
            common.show_message("请选择正确的商品类型编号!","ERROR")
            continue
        elif shop_classify_id == '4':
            #查看购物车
            shopping.Shopping.print_goods_list(shopobj.shopping_cart)
            common.show_message("当前购物车共有{0}件商品，合计{1}元！".format(len(shopobj.shopping_cart), shopobj.shopping_cost))
        