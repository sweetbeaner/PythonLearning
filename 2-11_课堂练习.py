#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  16:18
# !@Author : SweetBeaner
# !@File :.py
# !@Information :day02课堂练习
# 输入公交卡当前的余额，只要超过2元，就可以上公交车；如果车上有空座位，就可以坐下。

cash = int(input("请输入当前公交卡余额："))

if cash > 2:
    num = int(input("请输入空座位数："))
    if num >= 1:
        print("可以坐下")
    else:
        print("站着")
else:
    print("余额不足，无法上车")
