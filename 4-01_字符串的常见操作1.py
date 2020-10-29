#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  17:42
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

# 练习1: 定义一个字符串类型的变量，利用find方法获取指定数据对应的下标
str = 'abcdefgg'
print(str.find('e'))
# 练习2: 定义一个字符串类型的变量，利用index方法获取指定数据对应的下标
# index如果找不到该内容，会报异常
print(str.index('e'))
# 练习3: 定义一个字符串类型的变量，利用count方法统计指定数据在字符串中出现的次数
print(str.count('g'))
# 练习4: 定义一个字符串类型的变量，利用replace方法根据指定数据对字符串中的内容进行替换
str = str.replace('gg', 'oo', 1)
print(str)
# 练习5: 定义一个字符串类型的变量，比如: my_str = "苹果#香蕉#鸭梨",利用split方法对数据进行分割
# str.split()分割结果为一个列表
str = '苹果#香蕉#鸭梨'
str = str.split('#')
print(str)
