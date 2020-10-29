#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  14:07
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

# 练习: 定义一个变量，查看变量保存的内存地址


num = 1
print(id(num))  # 打印内存地址
num=3
num1 = num # 引用变量的地址
print(id(num1))  # 打印内存地址
num = 3
print(id(num1))  # 打印内存地址