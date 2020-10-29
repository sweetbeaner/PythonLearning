#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  16:12
# !@Author : SweetBeaner
# !@File :.py
# !@Information :

# if嵌套：在一个if语句里面再次if语句该格式称为if语句嵌套


# ==============根据以下注释，完成相关的代码练习==========

# 接收用户输入的性别，当性别是女则再接收用户输入的年龄，当年龄在20-25输出找到心中女生
# 否则输出对不起，我们不太合适

sex = input("请输入性别：")
if sex == "女":
    age = int(input("请输入年龄："))
    if age > 20 and age <= 25:
        print("你是我的心动女生")
    else:
        print("我们不合适")
else:
    print("我们不合适")
