#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  14:33
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

# 函数使用时的注意点


def show():
    print("哈哈哈")


def show(msg):
    print(msg)

# 练习: 已知上面的代码， 调用show函数时会出现什么问题。
#how() missing 1 required positional argument: 'msg'

show()
show('嗨嗨嗨')