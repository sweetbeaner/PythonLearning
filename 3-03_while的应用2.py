#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  12:27
# !@Author : SweetBeaner
# !@File :.py
# !@Information :
# 练习:利用while实现计算1~100之间偶数的累加和（包含1和100）

sum = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        sum = sum + i
    i += 1
print(sum)
