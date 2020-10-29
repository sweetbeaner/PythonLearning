#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  14:56
# !@Author : SweetBeaner
# !@File :.py
# !@Information :常用数据类型转换

# ==============根据以下注释，完成相关的代码练习==========


# 定义一个字符串类型的变量把字符串转成int类型的数据并进行输出
name="SweetBeaner"
#print(int(name))

# 定义一个int类型的变量把int类型数据转成字符串并进行输出
age = 18
print(str(age))

# 定义一个字符串类型的变量把字符串转成float类型并进行输出
# print(float(name))

# 定义一个float类型变量把float类型的数据转成字符串并进行输出
weight = 80.5
print(str(weight))
# 定义一个字符串类型的变量，使用eval函数表示获取字符串中包裹的内容
age = "18"
print(type(eval(age)))