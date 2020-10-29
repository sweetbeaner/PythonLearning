#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  22:45
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 练习：定义一个字典类型的变量，比如: my_dict = {"name": "刘德华", "age": 50, "sex": "男"}
my_dict = {"name": "刘德华", "age": 50, "sex": "男"}
# 1. 添加一个键值对数据(address = 香港)
my_dict['address']='香港'
print(my_dict)

# 2. 修改年龄等于54
my_dict['age'] = 54
print(my_dict.get('age'))
# 3. 删除性别键值对
del my_dict['sex']
print(my_dict)
# 4. 根据pop方法删除name这个键值对，并输出删除的value值
value = my_dict.pop('name')
print(my_dict,value)
# 5. 清空字典
my_dict.clear()
print(my_dict)
