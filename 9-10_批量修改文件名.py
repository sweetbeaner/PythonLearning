#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  16:10
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
import os


# 练习: 对指定目录里面的所有文件进行重命名，比如: test目录里面的所有文件，都加上 Sweetbeaner
os.chdir('AAA')
nameList = os.listdir('./')
list
for name in nameList:
    print(name)
    newname = 'Sweetbeaner'+name
    os.rename(name,newname)