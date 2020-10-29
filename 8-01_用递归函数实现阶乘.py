#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  10:48
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 练习: 利用递归函数实现求n这个数字的阶乘
def digui(num):
    if num >= 1:
        result = num * digui(num - 1)
    else:
        result = 1
    return result


print(digui(10))


def digui2(num):
    while num > 1:
        result = num * digui2(num - 1)
        return result
    result = 1
    return result
print(digui2(10))