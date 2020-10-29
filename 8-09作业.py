#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  16:24
# !@Author : ChenYuelu
# !@File :.py
# !@Information :
### 题目1

# 编写函数解决鸡兔同笼问题(一个笼子里面有鸡和兔子，总计有24个头，64条腿，问鸡、兔子分别多少只)

# def jitutonglong(a, b):
#     for x in range(1, a):
#         y = a - x
#         if 2 * x + 4 * y == b:
#             print('鸡:%d只，兔：%d只。'%(x,y))
# jitutonglong(24,64)


### 题目2

# 编写函数，计算0到1000内的三个数a、b、c，a+b+c=1000且 a的平方+b的平方=c的平方，求a、b、c可以取的值有哪些
# count = 0
# for a in range(0, 1001):
#     for b in range(0, 1001 - a):
#         c = 1000 - b - a
#         count += 1
#         if a * a + b * b == c * c:
#             print(a, b, c)
# print(count)

# 题目1

# 从键盘获取输入的字符串
# 编写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果

# def strTest(str):
#     str_count = 0
#     kg_count = 0
#     num_count = 0
#     other_count = 0
#     for i in str:
#         if i.isalpha():
#             str_count += 1
#         elif i.isspace():
#             kg_count += 1
#         elif i.isdigit():
#             num_count += 1
#         else:
#             other_count += 1
#     return str_count, kg_count, num_count, other_count
#
# print(strTest(input('请输入一个字符串:')))

# 题目2

# num = [1, 1, 2, 3, 4, 4, 5]
# s_num = set(num)
# num = list(s_num)
# print(num)
# num = [x for x in num if x % 2 != 0]
# print(num)
# 已知列表num， 完成列表num的去重，并使用一行代码完成num列表奇数的筛选


# 题目3

# 新建一个文件，写入“人生苦短，我用Python”，然后将这个文件中的数据读取出来，打印到控制台

# file = open('data.txt', 'w')
# file.write('人生苦短，我用Python')
# file.close()
# file = open('data.txt', 'r')
# print(file.readlines())
# file.close()
