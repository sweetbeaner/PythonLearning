#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  14:14
# !@Author : SweetBeaner
# !@File :.py
# !@Information :
# 练习：打印如下图形：
#
# *
# * *
# * * *
# * * * *
# * * * * *


col = 1
while col <= 5:
    i = 1
    while i <= col:
        print(" *",end="")
        i += 1
    col += 1
    print("")
