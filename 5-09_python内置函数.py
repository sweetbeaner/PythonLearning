#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  23:08
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

# 内置函数: 不需要导入包或者模块直接使用的函数称为内置函数
# len(item)	计算容器中元素个数
# max(item)	返回容器中元素最大值
# min(item)	返回容器中元素最小值
# del(item)	删除变量

my_tuple = (1, 2, 3)
result = len(my_tuple)
print(result)

my_list = [1, -1, 3]
# 获取列表中的最大值
max_value = max(my_list)
print(max_value)

# 获取列表中的最小值
min_value = min(my_list)
print(min_value)

name = "李四"
print(name)
# 删除变量
# del(name)
# # 变量被删除以后，不能再次使用
# print(name)

# del关键字也可以删除变量
# del name
# print(name)

# 通过以上代码可以得知，del关键字的功能和del函数函数，可以删除列表或者字典中的数据
# 一般都使用del关键字来完成这样的操作


result = max('123')
print(result)

my_dict = {"a": 1, "b": 2}
result = max(my_dict.values())
print(result)

value = max(('a', "A"))
print(value)
