#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  16:57
# !@Author : SweetBeaner
# !@File :.py
# !@Information :
# 练习：接收用户输入的字符串数据并格式化输出字符串数据

inp = input('请输入一个字符串')
format_string = f'用户输入的字符串是{inp}'
print(format_string)
print('用户输入的是%s'%inp)

a=5
b=7
format_string1 = f'a*b={a*b}'
print(format_string1)