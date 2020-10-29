#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  17:44
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 练习1：定义一个列表，根据下标1和下标-1，把列表中的数据分别改成李四和王五
list = ['a', 'b', 'c']

list[1] = '李四'
list[-1] = '王五'
print(list)
# -1为最后一个元素

# 练习2：定义一个列表，根据切片修改列表中的最后两个数据，改完后变成(张三，冯七)

print(list[-2:])
list[-2:] = ['aaa','bbb']
print(list)