#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  14:56
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 练习: 定义一个函数，可以接收不确定个数的位置参数和不确定个数的关键字参数

# 不定长参数:在定义函数时，不确定接收参数的个数(0个或者1个或者多个)，该参数我们可以定义成不定长参数
# 不定长参数的表现形式:
# 1. *args: 专门负责接收不确定个数的位置参数， 称为：不定长位置参数,传递元组
# 2. **kwargs：专门负责接收不确定个数的关键字参数 ，称为：不定长关键字参数，传递字典

# *args：将变量传递成一个元组进函数
def test(*args):
    print(args,type(args))
test(1,2,3)
test()

def test2(**kwargs):
    print(kwargs,type(kwargs))
test2(name='Sweetbeaner',age=12)