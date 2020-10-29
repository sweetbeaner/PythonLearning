#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  17:44
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 练习1：定义一个列表，往列表中追加一个数据(李四)  append
list = ['a','b','c']
list.append('d')
print(list)
# 练习2：定义一个列表，在下标0的位置插入一个数据(王五)   insert
list.insert(0,'e')
print(list)
# 练习3: 定义两个列表，把第二个列表中的数据扩展到第一个列表中，输出第一个列表数据    extend
list2 = ['0','1','2']
list.extend(list2)
print(list)


