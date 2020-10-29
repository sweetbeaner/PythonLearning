#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  14:37
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 练习: 使用if判断分别结合容器类型、数字类型、None类型使用，判断条件是否成立。
if False:
    print("True 表示条件成立")
else:
    print("False表示条件不成立")

my_str = "aaa"

if my_str:
    print("字符串里面有数据表示成立")
else:
    print("字符串里面没有数据表示失败")

my_list = [1, 4]
if my_list:
    print("列表里面有数据表示成立")
else:
    print("列表里面没有数据表示失败")

my_num = 1
if my_num:
    print("如果是数字，不是0表示条件成立")
else:
    print("如果是数字，是0表示条件失败")

my_data = None

if not my_data:
    print("非空表示成立")
else:
    print("空表示失败")