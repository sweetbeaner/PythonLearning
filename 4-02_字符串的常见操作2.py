#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  17:43
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

# 练习1: 定义一个字符串类型的变量, 使用startswith判断数据是否是以http开头
str = 'http:www.baidu.com'
print(str.startswith('http'))
# 练习2: 定义一个字符串类型的变量, 使用startswith判断数据是否是以com结尾
print(str.endswith('com'))
# 练习3: 定义一个字符串类型的变量, 使用strip去除两边空格
str1 ='  ojbk  '
str1 = str1.strip()
print(str1)
# 练习4: 定义一个字符串类型的变量, 使用rfind从右往左查找数据对应的下标
print(str1.rfind('j'))