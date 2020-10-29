#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  17:43
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

# 练习1: 定义一个字符串类型的变量, 比如:1.txt, 利用partition方法把数据分割成三部分
str = '1.txt'
print(str.partition('.'))
# 练习2: 定义一个字符串类型的变量, 比如:1.txt.png, 利用rpartition方法把数据分割成三部分
str = '1.txt.png'
print(str.rpartition('.'))
# 练习3: 定义一个字符串类型的变量, 使用isdigit 判断字符串中的数据是否都是整型数字

str = '2a13'
print(str.isdigit())

# 练习4: 使用join方法把列表中的每一个数据进行字符串的拼接操作，比如：my_list = ['a', 'b']
# 拼接后的字符串是 'a#b'
s1 = str.join(['a','b'])
print(s1)

