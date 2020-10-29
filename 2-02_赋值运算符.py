#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  14:48
# !@Author : SweetBeaner
# !@File :.py
# !@Information :测试赋值运算符

# 赋值运算符
# = ，提示：把等号右边的代码执行完，把结果赋值给等号左边的变量


# ==============根据以下注释，完成相关的代码练习==========

# 同时定义三个变量并分别给三个变量赋值，然后输出查看结果

name, age, weight = "SweetBeaner", 18, 71.5
print(name,age,weight)

# 复合赋值运算符

# +=	加法赋值运算符	c += a 等效于 c = c + a  **
# -=	减法赋值运算符	c -= a 等效于 c = c - a  **
# *=	乘法赋值运算符	c *= a 等效于 c = c * a
# /=	除法赋值运算符	c /= a 等效于 c = c / a
# %=	取模赋值运算符	c %= a 等效于 c = c % a
# **=	幂赋值运算符	c **= a 等效于 c = c ** a
# //=	取整除赋值运算符	c //= a 等效于 c = c // a


# ==============根据以下注释，完成相关的代码练习==========


# 定义两个int类型的变量，完成 += 操作并输出结果
num1 = 1
num2 = 2
num1+=num2
print(num1)

# 定义两个int类型的变量，完成 -= 操作并输出结果

num3 = 3
num4 = 4
num3-=num4
print(num3)