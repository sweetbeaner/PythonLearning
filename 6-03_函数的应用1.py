#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  14:20
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :.



# 练习1: 写一个函数打印一条横线

def line():
    print('____________________')

line()
# 练习2: 打印自定义行数的横线
def lines(num):
    i=1
    for i in range(num-1):
        line()
lines(3)