#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  10:07
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 练习: 以字节的方式，把字符串数据 '走上人生巅峰，迎娶白富美!' 追加写入到文件 2.txt

file = open('data.txt', 'ab')
str = '走上人生巅峰'
data = str.encode('utf-8')
file.write(data)