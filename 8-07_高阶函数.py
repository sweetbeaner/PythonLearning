#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  15:01
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :高阶函数：函数的参数和返回值均为函数

# 练习: 定义一个参数是函数类型的高阶函数
def plus(a, b):
    return a + b


def highLevel1(func):
    a = 3
    b = 5
    c = func(a, b)
    print(c)


highLevel1(plus)

# 练习: 定义一个返回值是函数类型的高阶函数

def highLevel2():
    def show():
        print('我是一个函数')
    return show

test = highLevel2()
print(test,type(test))