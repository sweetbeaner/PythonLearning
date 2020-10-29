#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  11:07
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
def sum_num(n1, n2):
    return n1 + n2

func = lambda n1,n2:n1+n2


# 练习: 使用匿名函数对以上代码进行简化
def sum(func):
    a = 3
    b = 5
    print(func(a,b))
sum(func)