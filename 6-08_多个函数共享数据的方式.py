#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  14:28
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 练习: 能够写出多个函数之间共享数据的两种方式

# 第一种:全局变量
# num = 100
# def fun1():
#     global num
#     print(num)
# def fun2():
#     global num
#     num = 1
#     print(num)
# fun2()
# fun1()

# 第二种：返回值
def fun3():
    return 101
def fun4():
    num = fun3()
    print(num)
fun4()
