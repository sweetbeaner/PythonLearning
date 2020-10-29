#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  13:43
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

# 集合特点:
# 1. 数据唯一
# 2. 无序
# 3. 可变类型的数据

# 集合的注意点:
# 1. 不能根据下标获取和修改数据
# 2. 创建一个空的集合需要使用set()

# 练习题: 已知集合的注意点及特点，定义一个集合类型的变量，验证集合的特点及注意点
a = set()
a.add('第一')
print(a)
a.add('第二')
print(a)

e = list(a)
print(e)