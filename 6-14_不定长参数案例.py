#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  15:06
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

# 需求: 定义一个函数，实现对不确定个数的参数进行求和操作

def sumTest(*args):
    sum = 0
    for i in args:
        sum = sum +i
    return sum

print(sumTest(1,2,3,4,5))