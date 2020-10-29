#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  11:07
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

file = open('test.txt','r',encoding='utf-8')
str = file.readlines()
for i in str:
    if i!='':
        print(i)