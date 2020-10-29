#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  17:43
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
#  练习1：定义一个列表，分别使用for循环和while循环对列表进行遍历

list = ['a','b','c','d']
for i in list:
    print(i)
i=0
while i<len(list):
    print(list[i])
    i+=1