#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  22:58
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

# 练习: 定义一个元组，my_str = ('AA', "BB", "CC")，使用for循环遍历的时候输出数据对应的下标及该数据


my_str = ('AA', "BB", "CC")
enumerate(my_str)
for i,char in enumerate(my_str):
    print(i,char)