#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  10:50
# !@Author : SweetBeaner
# !@File :.py
# !@Information :定义变量

# 变量的语法格式
# 变量名 = 数据
name = "SweetBeaner"  # 字符str
age = 18  # 整型int
stature = 1.69  # 浮点型float,Python没有double型
merried = False  # 布尔型True、False
print(name)
print(age)
print(stature)

# 利用type函数查看变量的数据类型
name_type = type(name)  # 获取变量name的数据类型
print(name_type)  # 打印name的变量类型

stature_type = type(stature)  # 获取变量stature的数据类型
print(stature_type)  # 打印stature的变量类型

# 提示：字符串有四种表现形式。
# 注意点：之前所使用的多行注释本质上就是一个字符串