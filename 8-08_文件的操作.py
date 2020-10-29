#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  16:09
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

# 练习: 从当前工程中创建一个write.txt文件，并写入一下数据，使用r模式读取文件中的数据
# f = open('write.txt','w')
# f.write('测试文件写入')
# f.close()

# f = open('write.txt','r')
# print(f.readlines())
# f.close()

# 练习: write.txt文件中追加写入 我最帅  这个数据。
f = open('write.txt','a',encoding='utf-8')
f.write('追加')
f.close()