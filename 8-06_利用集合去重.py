#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  14:40
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 练习: 已知列表 my_list = ['a', 'b' , 'c', 'b'], 利用集合去重

my_list = ['a', 'b' , 'c', 'b']
s = set(my_list)
print(s)
my_list = list(s)
print(my_list)