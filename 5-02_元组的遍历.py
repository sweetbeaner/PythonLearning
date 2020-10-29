#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  22:33
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 练习1：定义一个元组类型的变量, 分别使用for循环和while循环遍历元组。
tur = (1, 'a', True)
for value in tur:
    print(value)

i=0
while i<len(tur):
    print(tur[i])
    i+=1