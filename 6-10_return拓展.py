#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  14:40
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 练习: 已知变量 a = 1, b=2 ，使用两种写法完成交换两个变量的值

# 写法1：
def reverse(a,b):
    return (b,a)
print(reverse(1,2))

# 写法2：
a = 1
b = 2
c = a
a = b
b = c
print(a,b)

# def show():
#     for x in range(1, 4):
#         print("外层循环:", x)
#
#         for y in range(2, 6):
#             print("内层循环:", y)
#             if y == 3:
#                 # 利用return的特点，函数执行完return表示函数执行结束，以后再也不会循环啦
#                 return "over"
#
# result = show()
# print(result)
# # 提示：return关键字只能在函数或者方法里面使用，不能单独再外面使用。