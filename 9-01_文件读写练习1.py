#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  9:37
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 练习: 以字节方式读取文本文件1.txt 里面的数据，把数据读取到后进行解密成字符串进行输出

# 1. rb 模式： 表示以字节(二进制)的方式从文件中读取数据
# 2. wb 模式： 表示以字节(二进制)的方式往文件中写入数据
# 3. ab 模式: 表示以字节(二进制)的方式往文件中追加写入数据
# 提示：r表示读取文本文件中的数据，但是不能读取图片、视频、音频
# 为了解决可以读取文本文件和图片和视频等数据，可以使用rb模式，表示以字节或者二进制的方式读取数据

file = open('data.txt', 'w')
file.write('人生苦短，我用python')
file.close()
file = open('data.txt','rb')
content = file.read()
print(content,type(content))
str = content.decode("utf-8")
print(str)