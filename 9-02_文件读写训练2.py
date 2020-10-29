#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  10:03
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 练习: 以字节的方式，把字符串数据 '人生苦短, 我用python' 写入到文件 2.txt

file = open('data2.txt', 'wb')
str = '人生苦短，我用python'
data = str.encode('utf-8')
file.write(data)
file.close()
