#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  9:26
# !@Author : ChenYuelu
# !@File :.py
# !@Information :
#### 题目1

# 已知代码材料：
#
# ```python
# num = [1,3,5,6,7,8]
# ```
#
# 需求1：使用列表推导式将num 列表中的偶数筛选出来
#
# 需求2：用filter函数处理数字列表，将列表中所有的偶数筛选出来
#
# 需求3：使用匿名函数改写
# num = [1, 3, 5, 6, 7, 8]
# l1 = [x for x in num if x % 2 == 0]
# print(l1)
#
#
# def judgeOushu(x):
#     return x % 2 == 0
#
#
# # 用一个filter将列表中的每一项做函数名判断，返回结果为一个list变量
# result = filter(judgeOushu, num)
# print(list(result))
#
# # 匿名函数：函数变量 = lambda 变量：表达式
# myfunc = lambda x: x % 2 == 0
#
# result = filter(myfunc, num)
# print(list(result))

# 题目2

# 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。

# file = open('题目2.txt', 'a', encoding='utf-8')
# while True:
#     str = input('请输入一个字符:')
#     if str != '#':
#         file.write(str)
#         continue
#     else:
#         print('输入#，终止')
#         break

#  题目1

# 从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件”test”中保存。
# str = input('请输入一个字符串：')
# str = str.upper()
# print(str)
# file = open('text.txt','w',encoding='utf-8')
# file.write(str)
# file.close()

# 题目2

# 将”python是我用过的最好用，最优雅的计算机语言，没有之一！！！“这句话从文件A中读取出来，然后以逗号为分割符分割成三部分，然后依次存入B、C、D文件中。

# def saveTxt(str, filename):
#     file = open(filename, 'w', encoding='utf-8')
#     file.write(str)
#     file.close()
#
#
# file = open('A.txt', 'r', encoding='utf-8')
# str = file.readline()
# list = str.split('，')
# print(list)
# saveTxt(list[0], 'B.txt')
# saveTxt(list[1], 'C.txt')
# saveTxt(list[2], 'D.txt')

# 题目3

# 文件的重命名，文件的删除，创建文件夹，获取当前目录、改变默认目录、获取目录列表、删除文件 完成这七个操作
import os
# os.rename('data.txt','data1.txt')
# os.remove('A.txt')
# print(os.getcwd())
# os.chdir('./AAA')
# print(os.getcwd())
# print(os.listdir())
# os.rmdir('TST')