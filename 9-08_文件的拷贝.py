#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  15:19
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 练习: 根据上课的需求，对test.txt的文件进行拷贝，拷贝的文件名叫做: test[附件].txt
file = open('test.txt','r',encoding='utf-8')
file1 = open('test[附件].txt','a',encoding='utf-8')
content = file.readlines()
for i in content:
    if len(i)>0:
        file1.write(i)
file.close()
file1.close()