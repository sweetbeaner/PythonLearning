#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  14:21
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

def modify_value(params):
    print("params修改前:", params, id(params))
    params += params
    print("params修改后:", params, id(params))
a = 1
modify_value(a)

b = [1,2,3]
modify_value(b)