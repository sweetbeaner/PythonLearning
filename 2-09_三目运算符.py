#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  16:03
# !@Author : SweetBeaner
# !@File :.py
# !@Information :三目运算符
# 执行流程: 先判断条件是否成立，条件成立会执行if语句左边的代码，否则执行

# 学习三目运算的目的：对if-else语句的代码进行简化，可以一行代码来搞定
# result = a if a > b else b


# ==============根据以下注释，完成相关的代码练习==========

# 定义两个变量，利用三目运算获取两个变量中的最大值并输出显示
num1 = 12
num2 = 14

print(num1 if num1 > num2 else num2)

print(num2 if num1 < num2 else num1)
