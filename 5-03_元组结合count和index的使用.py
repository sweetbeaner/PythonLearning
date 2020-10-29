#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  22:37
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

name_tuple = ("马忠","张辽",1,True,"张辽","关羽")
# 练习1: 定义一个元组类型的变量, 统计 马忠 在元组中的出现的次数
result = name_tuple.count("马忠")
print(result)
result = name_tuple.count("张辽")
print(result)

# 练习1: 定义一个元组类型的变量, 获取 关羽 在元组中的下标
index = name_tuple.index("关羽")
print(index)