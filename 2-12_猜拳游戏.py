#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  15:12
# !@Author : SweetBeaner
# !@File :.py
# !@Information :比较


# ==============根据以下注释，完成相关的代码练习==========

# 根据猜拳游戏的需求，写出猜拳游戏的功能代码
import random

speak = int(input("请输入您出的拳脚，0为包袱，1为剪刀，2为石头"))
battle = random.randint(0, 2)
min = speak - battle

if min == 0:
    print("平手")
else:
    if min < 0:
        if min == -1:
            print("您输了：%d:%d" % (speak, battle))
        elif min == -2:
            print("您赢了：%d:%d" % (speak, battle))
    elif min == 1:
        print("您赢了：%d:%d" % (speak, battle))
    else:
        print("您输了：%d:%d" % (speak, battle))
