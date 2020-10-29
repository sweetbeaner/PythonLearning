#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  14:44
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

### 题目1

# 分别定义一个字符串类型的全局变量、列表类型的全局变量。
# 定义函数func2，在函数中分别添加global关键字修改，和不添加global关键字修改，总结有什么区别。

# g_str = 'abc'
# g_list = ['a','b','c']
#
# def fun2():
#     global g_str
#     g_str = 'efg'
#     global g_list
#     g_list = ['1','2','3']
#
# print(g_str,g_list)
# fun2()
# print(g_str,g_list)


### 题目2

# 完成一个函数，给定三个值。判断你给的值是否可以组成一个三角形
# def judge(a, b, c):
#     if a + b > c and b + c > a and c + a > b:
#         return True
#     return False
#
#
# print(judge(3, 3, 5))

### 题目1

# 斐波那契数列：1，1，2，3，5，8... 即前两个数字是1, 从第三个数字开始，每个数字是前两个数字之和，编写函数，输出sum以内的斐波那契数列
now = 1
pos = 0
pre = 0
i = 1
inp = int(input('请输入一个数字：'))
while i <= inp:
    if i <2:
        now = 1
        pos = 1
        print(now)
    else:
        now = pre+pos
        print(now)
        pre,pos = pos,now
    i+=1