#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  14:10
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

# 练习：验证可变类型的数据在原有内存空间的基础上修改后是否内存地址不变
# 可变类型: 能够原有数据的内存空间的基础上修改数据，【修改后该变量保存的内地地址不变】
# 可变类型有: 列表，字典, 集合

my_list = ["李四"]

print(my_list, id(my_list))

my_list.append("王五")

print(my_list, id(my_list))

my_list[0] = "张三"

print(my_list, id(my_list))

print("==========")

my_dict = {"name": "李四", "age": 20}

print(my_dict, id(my_dict))

del my_dict["age"]
print(my_dict, id(my_dict))



