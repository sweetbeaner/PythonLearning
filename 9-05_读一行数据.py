#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  10:25
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 练习: 准备一个3.txt的文件，里面写入三行数据, 比如: 'abc', 以字符串的方式读取每一行数据


file = open('2.txt','r',encoding='utf-8')
file.readline()
while True:
    result = file.readline()
    if len(result)>0:
        print(result)
    else:
        break
file.close()