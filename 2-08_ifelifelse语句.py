#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  15:58
# !@Author : SweetBeaner
# !@File :.py
# !@Information :完整的条件判断语句

# 学习if-elif-else语句目的：当需要一次判断多个条件的时候，可以使用该语句，

# ==============根据以下注释，完成相关的代码练习==========

# 接收用户输入的分数，进行评级操作，
# 1.当分数在90-100输出优秀
# 2.当分数在80-89输出良好
# 3.当分数在70-79输出一般
# 4.当分数在60-69输出刚刚及格
# 5.当分数在0-59输出不及格
# 6.以上条件都不满足输出请输入合法分数

score = int(input("请输入您的分数"))
if score >= 0 and score <= 59:
    print("不及格")
elif score >= 60 and score < 70:
    print("刚刚及格")
elif score >= 70 and score < 80:
    print("刚刚一般")
elif score >= 80 and score < 90:
    print("良好")
elif score >= 90 and score < 100:
    print("优秀")
else:
    print("请输入合法分数")
