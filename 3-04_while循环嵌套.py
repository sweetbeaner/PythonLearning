#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  17:04
# !@Author : SweetBeaner
# !@File :.py
# !@Information :
# 练习：利用while循环实现从第1次循环到第3次，每循环一次 打印 三次走上人生巅峰！

count = 1

while count <= 3:
    print("第%s次循环" % count)
    num = 1
    while num <= 3:
        print("走上人生巅峰")
        num += 1
    count += 1
