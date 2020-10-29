#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  11:12
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

def calc_data(current_func):

    n1 = 3
    n2 = 5

    value = current_func(n1, n2)

    print("结果为:", value)


# 练习1: 调用上面的calc_data函数实现加法计算
fun1 = lambda a,b:a+b
calc_data(fun1)

# 练习2: 调用上面的calc_data函数实现减法计算
fun2 = lambda a,b:a-b
calc_data(fun2)