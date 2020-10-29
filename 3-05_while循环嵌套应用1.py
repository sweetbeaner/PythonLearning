#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  12:05
# !@Author : SweetBeaner
# !@File :.py
# !@Information :
# 练习：打印如下图形：
#
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

out = 1
inn = 1
while out <= 5:
    inn=1
    while inn <= 5:
        print(" *",end="")
        inn += 1
    print("")
    out += 1
