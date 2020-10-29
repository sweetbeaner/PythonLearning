#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  15:27
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 拆包: 使用不同变量来保存容器类型(字符串，列表，元组，字典，range)中的每一个数据的操作称为拆包
str = 'ABC'
v1,v2,v3 = str
print(v1,v2,v3)

list = [1,2,3,4]
a,b,c,d = list
print(a,b,c,d)

tur = ('陈',18,140)
x,y,z = tur
print(x,y,z)

dict = {'name':'chen','age':18}
d1,d2 = dict
print(d1,d2)
v1,v2 = dict.values()
print(v1,v2)

ra = range(1,4)
r1,r2,r3 = ra
print(r1,r2,r3)

# 总结:
# 拆包是针对容器类型的一种操作，使用不同变量来保存容器类型中的每一个数据
# 注意点: 变量的个数一对要和容器类型中元素的个数保持一致。