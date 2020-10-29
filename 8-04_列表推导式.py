#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  11:14
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
import random

# 练习: 使用列表推导式 生成列表，[1, 2, 3]

l1 = [x for x in range(1,4)]
print(l1)
# 练习: 使用列表推导式 生成列表， [1, 3, 5, 9]
l2 = [x for x in range(1,10) if x%2!=0]
print(l2)
# 练习： 使用列表推导式 生成列表 把字符串 my_str = 'abc' 转成 ["aa", "bb", "cc"]
my_str = 'abc'
l3 = [2*x for x in my_str]
print(l3)
# 练习：使用列表推导式 把my_tuple = ("张飞", "刘备", "张郃")中姓张的过滤出来
# 比如:  ["张飞", "张郃"]
my_tuple = ("张飞", "刘备", "张郃")
l4 = [x for x in my_tuple if x[0]=='张']
print(l4)
# 练习: 利用列表推导式，生成5个1-10的随机数字，比如: [1, 3, 2, 4, 10]
l5 = [random.randint(1,10) for _ in range(5)]
print(l5)
# 练习: 已知代码: my_list = [{"name": "李四", "age": 10},{"name": "王五", "age": 20}]
# 把年龄大于18岁的数据过滤出来放到一个列表里面, 比如:[{"name": "王五", "age": 20}]
my_list = [{"name": "李四", "age": 10},{"name": "王五", "age": 20}]
l6 = [x for x in my_list if x.get('age')>18]
print(l6)