#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  12:23
# !@Author : SweetBeaner
# !@File :.py
# !@Information :
#  练习: 利用while实现计算1~100的累加和（包含1和100）

i = 1
sum = 0
while i <= 100:
    sum = sum + i
    i += 1
print(sum)
