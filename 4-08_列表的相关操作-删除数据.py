#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  17:45
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 从列表中删除数据有三种方式
# 练习1. 定义一个列表，使用del删除下标1的数据
list = ['a', 'b', 'c', 'd']
del list[1]
print(list)
# 练习2. 定义一个列表，使用pop删除下标0的数据，并把删除的数据进行输出,return
print(list.pop(0))
# 练习3. 定义一个列表，使用remove 删除一个列表中存在的数据
list.remove('d')
print(list)