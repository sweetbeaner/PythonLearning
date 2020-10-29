#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  23:15
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

# 练习：给下面的代码添加函数的文档说明
import random


def show_random_num():
    '''
    用来生成随机数
    :return:一个随机的数字
    '''
    num = random.randint(1, 10)
    print(num)
